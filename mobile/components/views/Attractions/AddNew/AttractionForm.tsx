import React, { useState } from 'react';
import { ScrollView, Text, TextInput, TouchableOpacity, View } from 'react-native';
import StarRating from 'react-native-star-rating';
import { OpenHours } from '../types';
import { OpeningHours } from './components/Hours.tsx';
import { styles } from './styles';

const AddNewAttraction = () => {
  const [name, setName] = useState('');
  const [coordinates, setCoordinates] = useState('');
  const [description, setDescription] = useState('');
  const [rating, setRating] = useState(0);
  const [openingHours, setOpeningHours] = useState<OpenHours>({ open: 9, close: 17 });

  const onAddAttraction = () => {
    console.log({ name, description, coordinates, openingHours, rating });
    //ToDo Add your logic here for adding the attraction
  };

  return (
    <>
      <ScrollView style={styles.container}>
        <Text style={styles.label}>Name:</Text>
        <TextInput
          style={styles.input}
          placeholder="Type name"
          value={name}
          onChangeText={(text) => setName(text)}
        />

        <Text style={styles.label}>Coordinates:</Text>
        <TextInput
          style={styles.input}
          placeholder="Type coordinates"
          value={coordinates}
          onChangeText={(text) => setCoordinates(text)}
        />

        <Text style={styles.label}>Description:</Text>
        <TextInput
          style={styles.inputDescription}
          placeholder="Type description"
          value={description}
          onChangeText={(text) => setDescription(text)}
          multiline
        />

        <Text style={styles.label}>Opening hours:</Text>
        <View style={styles.openingHoursContainer}>
          <OpeningHours
            label="Open"
            value={String(openingHours.open)}
            onChange={(text) => setOpeningHours({ open: Number(text), close: openingHours.close })}
          />
          <OpeningHours
            label="Close"
            value={String(openingHours.close)}
            onChange={(text) => setOpeningHours({ open: openingHours.open, close: Number(text) })}
          />
        </View>

        <Text style={styles.label}>Attraction rate:</Text>
        <StarRating
          disabled={false}
          maxStars={5}
          rating={rating}
          selectedStar={(rating) => setRating(rating)}
          fullStarColor={'orange'}
        />
      </ScrollView>
      <TouchableOpacity style={styles.buttonSubmit} onPress={onAddAttraction}>
        <Text style={styles.buttonText}>Add attraction</Text>
      </TouchableOpacity>
    </>
  );
};

export default AddNewAttraction;
