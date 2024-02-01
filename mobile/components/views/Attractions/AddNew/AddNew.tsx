import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button, TouchableOpacity } from 'react-native';
import StarRating from 'react-native-star-rating';
import OpeningHoursModal from './OpeningHour';
import mapArrayToJson from '../tools/openingHourMapper';

const AddNewAttraction = () => {
  const [name, setName] = useState('');
  const [coordinates, setCoordinates] = useState('');
  const [description, setDescription] = useState('');
  const [rating, setRating] = useState(0);
  const [modalVisible, setModalVisible] = useState(false);
  const [openingHours, setOpeningHours] = useState(
    [
      { day: 'Mon', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Tue', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Wed', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Thu', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Fri', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Sat', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Sun', openingHour: '09:00', closingHour: '17:00' },
    ]
  );

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
  };

  const handleAddAttractionPress = () => {
    console.log(createAttractionJson());
  };

  return (
    <View style={{ padding: 16 }}>
      <Text>Name:</Text>
      <TextInput
        style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 16 }}
        placeholder="Type name"
        value={name}
        onChangeText={(text) => setName(text)}
      />

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

      <Button title="Set Opening Hours" onPress={() => setModalVisible(true)} />
      <OpeningHoursModal
        initialOpeningHours={openingHours}
        visible={modalVisible}
        onClose={() => setModalVisible(false)}
        onSave={handleSaveOpeningHours}
      />

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
