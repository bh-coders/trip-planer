import React, { useState } from 'react';
import {
  Button,
  Image,
  Modal,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import Slider from '@react-native-community/slider';
import { launchImageLibrary, MediaType } from 'react-native-image-picker';
import { reviewTile } from '../../common/components/details/review/styles';

interface Review {
  title: string;
  description: string;
  rating: number;
  cost: number;
  timeSpent: number;
  images: string[];
}

interface ReviewFormProps {
  review?: Review;
  onSubmit: (data: Review) => void;
}

const ReviewForm: React.FC<ReviewFormProps> = ({ review, onSubmit }) => {
  const [showImage, setShowImage] = useState(false);
  const [selectedImage, setSelectedImage] = useState('');
  const [formData, setFormData] = useState<Review>(
    review || {
      title: '',
      description: '',
      rating: 0,
      cost: 0,
      timeSpent: 0,
      images: [],
    }
  );

  const handleChange = (field: keyof Review, value: string | number) => {
    setFormData((prevData) => ({ ...prevData, [field]: value }));
  };

  const selectFile = () => {
    const options = {
      mediaType: 'photo' as MediaType,
      saveToPhotos: false,
      includeBase64: true,
    };

    launchImageLibrary(options as any, (response) => {
      if (response.didCancel) {
        console.log('User cancelled image picker');
      } else if (response.errorCode) {
        console.log('ImagePicker Error: ', response.errorMessage);
      } else if (response.assets && response.assets[0].base64) {
        const source = 'data:image/jpeg;base64,' + response.assets[0].base64;
        setFormData((prevData) => ({
          ...prevData,
          images: [...(prevData.images || []), source],
        }));
      } else {
        console.log('Loading image error');
      }
    });
  };

  const removeImage = (index: number) => {
    const newImages = formData.images ? [...formData.images] : [];
    newImages.splice(index, 1);
    setFormData((prevData) => ({ ...prevData, images: newImages }));
  };
  const handleSubmit = () => {
    // Validation, etc.
    onSubmit(formData);
  };

  const toggleImageModal = (image: string) => {
    setSelectedImage(image);
    setShowImage(!showImage);
  };

  return (
    <View style={styles.container}>
      <Text>Title:</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter Title"
        onChangeText={(text) => handleChange('title', text)}
        value={formData.title}
      />

      <Text>Description:</Text>
      <TextInput
        style={[styles.input, styles.multiline]}
        multiline
        placeholder="Type description"
        onChangeText={(text) => handleChange('description', text)}
        value={formData.description}
      />

      <Text>Rating (0-5): {formData.rating}</Text>
      <Slider
        style={styles.slider}
        value={formData.rating}
        minimumValue={0}
        maximumValue={5}
        step={0.5}
        onValueChange={(value) => handleChange('rating', value)}
      />

      <Text>Price (0-5): {formData.cost}</Text>
      <Slider
        style={styles.slider}
        value={formData.cost}
        minimumValue={0}
        maximumValue={5}
        step={0.5}
        onValueChange={(value) => handleChange('cost', value)}
      />

      <Text>Time spent (0-5): {formData.timeSpent}</Text>
      <Slider
        style={styles.slider}
        value={formData.timeSpent}
        minimumValue={0}
        maximumValue={5}
        step={0.5}
        onValueChange={(value) => handleChange('timeSpent', value)}
      />

      <Button title="Add photos" onPress={selectFile} />
      <ScrollView horizontal>
        {formData.images?.map((image, index) => (
          <View key={index} style={reviewTile.imageContainer}>
            <TouchableOpacity onPress={() => toggleImageModal(image)}>
              <Image source={{ uri: image }} style={reviewTile.thumbnail} />
            </TouchableOpacity>
            <TouchableOpacity onPress={() => removeImage(index)} style={reviewTile.closeButton}>
              <Text style={reviewTile.closeText}>Remove</Text>
            </TouchableOpacity>
          </View>
        ))}
      </ScrollView>
      <Modal visible={showImage} transparent={true}>
        <View style={reviewTile.imageModal}>
          <TouchableOpacity style={reviewTile.closeButton} onPress={() => toggleImageModal('')}>
            <Text style={reviewTile.closeText}>Close</Text>
          </TouchableOpacity>
          <Image source={{ uri: selectedImage }} style={reviewTile.modalImage} />
        </View>
      </Modal>
      <Button title="Submit review" onPress={handleSubmit} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    margin: 20,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
  multiline: {
    height: 100,
    textAlignVertical: 'top',
  },
  slider: {
    width: '100%',
    height: 40,
    marginBottom: 10,
  },
});

export const AddNewReview: React.FC = () => {
  return <ReviewForm onSubmit={(data) => console.log('Adding review:', data)} />;
};

export const EditReview: React.FC<{ review: Review }> = ({ review }) => {
  return <ReviewForm review={review} onSubmit={(data) => console.log('Editing review:', data)} />;
};
