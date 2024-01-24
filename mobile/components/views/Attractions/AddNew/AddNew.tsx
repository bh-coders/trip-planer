import React, { useState } from 'react';
import { View, Text, TextInput, Button, TouchableOpacity } from 'react-native';
import StarRating from 'react-native-star-rating';
<<<<<<< HEAD
import OpeningHoursModal from './OpeningHour';
import mapArrayToJson from '../tools/openingHourMapper';

const AddNewAttraction = () => {
  const [name, setName] = useState('');
  const [coordinates, setCoordinates] = useState('');
  const [description, setDescription] = useState('');
  const [rating, setRating] = useState(0);
  const [modalVisible, setModalVisible] = useState(false);
  const [openingHours, setOpeningHours] = useState();

  const handleSaveOpeningHours = (hours) => {
    setOpeningHours(hours);
    setModalVisible(false);
  };

  const createAttractionJson = () => {
    const attractionData = {
      name: name,
      description: description,
      latitude: coordinates.substring(0, coordinates.indexOf(',')),
      longitude: coordinates.substring(coordinates.indexOf(',') + 1),
      open_hours: mapArrayToJson(openingHours),
      rating: rating
    };
    return attractionData;
=======

const AddNewAttraction = () => {
  const [coordinates, setCoordinates] = useState('');
  const [description, setDescription] = useState('');
  const [rating, setRating] = useState(0);

  const handleOpenHoursPress = () => {
    // Napisz logikę do przeniesienia do ekranu formularza godzin otwarcia
    console.log('Przejdź do formularza godzin otwarcia');
>>>>>>> d7ffab7 (30-frontend-move_attractions_views_to_wo_expo)
  };

  const handleAddAttractionPress = () => {
    // Napisz logikę do dodania atrakcji (np. wysłanie danych na serwer)
<<<<<<< HEAD
    console.log(createAttractionJson());
=======
    console.log('Dodaj atrakcję', coordinates, description, rating);
>>>>>>> d7ffab7 (30-frontend-move_attractions_views_to_wo_expo)
  };

  return (
    <View style={{ padding: 16 }}>
<<<<<<< HEAD
      <Text>Name:</Text>
      <TextInput
        style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 16 }}
        placeholder="Type name"
        value={name}
        onChangeText={(text) => setName(text)}
      />

=======
>>>>>>> d7ffab7 (30-frontend-move_attractions_views_to_wo_expo)
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

<<<<<<< HEAD
      <Button title="Set Opening Hours" onPress={() => setModalVisible(true)} />
      <OpeningHoursModal
        initialOpeningHours={openingHours}
        visible={modalVisible}
        onClose={() => setModalVisible(false)}
        onSave={handleSaveOpeningHours}
      />

      <View style={{ margin: 20 }}>
        <Text style={{marginBottom:10}}>Attraction rate:</Text>
        <StarRating
          disabled={false}
          maxStars={5}
          emptyStar={'star-o'}
          fullStar={'star'}
          halfStar={'ios-star-half'}
          rating={rating}
          selectedStar={(rating) => setRating(rating)}
          fullStarColor={'orange'}
        />
      </View>

      <View style={{ padding: 20, borderRadius: 10, marginTop: 50, alignItems: 'flex-end' }}>
        <Button title="Save" color={'green'} onPress={handleAddAttractionPress} />
      </View>
=======
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
>>>>>>> d7ffab7 (30-frontend-move_attractions_views_to_wo_expo)
    </View>
  );
};

export default AddNewAttraction;