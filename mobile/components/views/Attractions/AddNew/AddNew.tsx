import React, { useState } from 'react';
import { View, Text, TextInput, Button, TouchableOpacity } from 'react-native';
import StarRating from 'react-native-star-rating';

const AddNewAttraction = () => {
  const [coordinates, setCoordinates] = useState('');
  const [description, setDescription] = useState('');
  const [rating, setRating] = useState(0);

  const handleOpenHoursPress = () => {
    // Napisz logikę do przeniesienia do ekranu formularza godzin otwarcia
    console.log('Przejdź do formularza godzin otwarcia');
  };

  const handleAddAttractionPress = () => {
    // Napisz logikę do dodania atrakcji (np. wysłanie danych na serwer)
    console.log('Dodaj atrakcję', coordinates, description, rating);
  };

  return (
    <View style={{ padding: 16 }}>
      <Text>Coordinates:</Text>
      <TextInput
        style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 16 }}
        placeholder="Type coordinates"
        value={coordinates}
        onChangeText={(text) => setCoordinates(text)}
      />

      <Text>Description:</Text>
      <TextInput
        style={{ height: 80, borderColor: 'gray', borderWidth: 1, marginBottom: 16 }}
        placeholder="Type description"
        value={description}
        onChangeText={(text) => setDescription(text)}
        multiline
      />

      <TouchableOpacity onPress={handleOpenHoursPress}>
        <Text style={{ color: 'blue', marginBottom: 16 }}>Formularz godzin otwarcia</Text>
      </TouchableOpacity>

      <Text>Attraction rate:</Text>
      <StarRating
        disabled={false}
        maxStars={5}
        rating={rating}
        selectedStar={(rating) => setRating(rating)}
        fullStarColor={'orange'}
      />

      <Button title="Add attraction" onPress={handleAddAttractionPress} />
    </View>
  );
};

export default AddNewAttraction;