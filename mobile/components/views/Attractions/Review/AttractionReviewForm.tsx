import React, { useEffect, useState } from 'react';
import { Image, Modal, ScrollView, Text, TextInput, TouchableOpacity, View } from 'react-native';
import Slider from '@react-native-community/slider';
import { launchImageLibrary, MediaType } from 'react-native-image-picker';
import { styles } from './styles.ts';

interface Review {
  title: string;
  description: string;
  rating: number;
  price: number;
  time_spent: number;
  images: string[];
}

interface ReviewFormProps {
  review?: Review;
  onSubmit: (data: Review) => void;
}

const ReviewForm: React.FC<ReviewFormProps> = ({ review, onSubmit }) => {
  const emptyReview: Review = {
    title: '',
    description: '',
    rating: 0,
    price: 0,
    time_spent: 0,
    images: [],
  };
  const [showImage, setShowImage] = useState(false);
  const [selectedImage, setSelectedImage] = useState('');
  const [formData, setFormData] = useState<Review>(review || emptyReview);

  useEffect(() => {
    review ? setFormData(review) : setFormData(emptyReview);
  }, [review]);
  const onChangeData = (field: keyof Review, value: string | number) => {
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
    <>
      <View style={styles.container}>
        <ScrollView>
          <Text style={styles.inputTitle}>Title:</Text>
          <TextInput
            style={styles.input}
            placeholder="Enter Title"
            onChangeText={(text) => onChangeData('title', text)}
            value={formData.title}
          />

          <Text style={styles.inputTitle}>Description:</Text>
          <TextInput
            style={[styles.input, styles.multiline]}
            multiline
            placeholder="Type description"
            onChangeText={(text) => onChangeData('description', text)}
            value={formData.description}
          />

          <Text style={styles.sliderTitle}>
            <Text>Rating:</Text>
            {/*<Text style={{ color: 'red' }}>{'❤'.repeat(formData.rating)}</Text>*/}
          </Text>
          <Slider
            style={styles.slider}
            value={formData.rating}
            minimumValue={0}
            maximumValue={5}
            step={1}
            onValueChange={(value) => onChangeData('rating', value)}
          />

          <Text style={styles.sliderTitle}>
            <Text>Price: </Text>
          </Text>
          <Slider
            style={styles.slider}
            value={formData.price}
            minimumValue={0}
            maximumValue={5}
            step={1}
            onValueChange={(value) => onChangeData('price', value)}
          />

          <Text style={styles.sliderTitle}>
            <Text>Time spent:</Text>
          </Text>
          <Slider
            style={styles.slider}
            value={formData.time_spent}
            minimumValue={0}
            maximumValue={5}
            step={1}
            onValueChange={(value) => onChangeData('time_spent', value)}
          />

          <TouchableOpacity onPress={selectFile} style={styles.buttonPhoto}>
            <Text style={styles.buttonText}>Add photos</Text>
          </TouchableOpacity>
          <ScrollView horizontal>
            {formData.images?.map((image, index) => (
              <View key={index} style={styles.imageContainer}>
                <TouchableOpacity onPress={() => toggleImageModal(image)}>
                  <Image source={{ uri: image }} style={styles.thumbnail} />
                </TouchableOpacity>
                <TouchableOpacity onPress={() => removeImage(index)} style={styles.removeButton}>
                  <Text style={styles.removeButtonText}>✘</Text>
                </TouchableOpacity>
              </View>
            ))}
          </ScrollView>
          <Modal visible={showImage} transparent={true}>
            <View style={styles.imageModal}>
              <TouchableOpacity style={styles.closeButton} onPress={() => toggleImageModal('')}>
                <Text style={styles.closeText}>Close</Text>
              </TouchableOpacity>
              <Image source={{ uri: selectedImage }} style={styles.modalImage} />
            </View>
          </Modal>
        </ScrollView>
      </View>
      <TouchableOpacity onPress={handleSubmit} style={styles.buttonSubmit}>
        <Text style={styles.buttonText}>Submit review</Text>
      </TouchableOpacity>
    </>
  );
};

export default ReviewForm;
