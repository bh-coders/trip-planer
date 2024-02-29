import React, { useState } from 'react';
import { Button, Image, StyleSheet, Text, TextInput, View } from 'react-native';
import Slider from '@react-native-community/slider';
import { launchImageLibrary } from 'react-native-image-picker';

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

  // const handleImagePicker = async () => {
  //   const options = {
  //     mediaType: 'photo',
  //     includeBase64: false,
  //   };
  //
  //   try {
  //     const response = await ImagePicker.launchImageLibrary(options);
  //
  //     // if (response && !response.didCancel && !response.errorMessage && response.assets) {
  //     //   const selectedImage = response.assets[0]; // Assuming we want only the first asset
  //     //
  //     //   if (selectedImage && selectedImage.uri) {
  //     //     setFormData((prevData) => ({
  //     //       ...prevData,
  //     //       images: [...(prevData.images || []), selectedImage.uri].filter(
  //     //         (image) => image
  //     //       ) as string[],
  //     //     }));
  //     //   }
  //     // }
  //   } catch (error) {
  //     console.error('ImagePicker Error:', error);
  //   }
  // };

  const selectFile = () => {
    const options = {
      title: 'Select Avatar',
      storageOptions: {
        skipBackup: true,
        path: 'images',
      },
    };

    launchImageLibrary(options as any, (response) => {
      if (response.didCancel) {
        console.log('User cancelled image picker');
      } else if (response.errorCode) {
        console.log('ImagePicker Error: ', response.errorMessage);
      } else if (response.assets && response.assets.length > 0) {
        const source = 'data:image/jpeg;base64,' + response.assets[0].base64;
        setFormData((prevData) => ({
          ...prevData,
          images: [...(prevData.images || []), source],
        }));
      }
    });
  };
  const handleSubmit = () => {
    // Validation, etc.
    onSubmit(formData);
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

      <Text>Opis:</Text>
      <TextInput
        style={[styles.input, styles.multiline]}
        multiline
        placeholder="Wpisz opis"
        onChangeText={(text) => handleChange('description', text)}
        value={formData.description}
      />

      <Text>Ogólna ocena (0-5): {formData.rating}</Text>
      <Slider
        style={styles.slider}
        value={formData.rating}
        minimumValue={0}
        maximumValue={5}
        step={0.5}
        onValueChange={(value) => handleChange('rating', value)}
      />

      <Text>Koszt (0-5): {formData.cost}</Text>
      <Slider
        style={styles.slider}
        value={formData.cost}
        minimumValue={0}
        maximumValue={5}
        step={0.5}
        onValueChange={(value) => handleChange('cost', value)}
      />

      <Text>Czas spędzony (0-5): {formData.timeSpent}</Text>
      <Slider
        style={styles.slider}
        value={formData.timeSpent}
        minimumValue={0}
        maximumValue={5}
        step={0.5}
        onValueChange={(value) => handleChange('timeSpent', value)}
      />

      <Button title="Dodaj zdjęcie" onPress={selectFile} />

      {formData.images?.map((image, index) => (
        <Image key={index} source={{ uri: image }} style={{ width: 200, height: 200, margin: 5 }} />
      ))}

      <Button title="Dodaj recenzję" onPress={handleSubmit} />
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
