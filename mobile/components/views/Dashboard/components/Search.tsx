import React, { useState } from 'react';
import { View, TextInput, TouchableOpacity, Text, Alert, Keyboard } from 'react-native';
import { styles } from '../styles';
import { fetchLocationFromMapbox } from '../api/mapboxApi';
import { fetchAttractions } from '../api/attractionsApi';

const Search = ({ setLocation, setAttractions, setSearchText, searchText }: any) => {
  const handleSearch = () => {
    fetchLocationFromMapbox(searchText)
      .then((location) => {
        setLocation(location);
        return fetchAttractions(searchText);
      })
      .then((attractions) => {
        setAttractions(attractions);
      })
      .catch((error) => {
        Alert.alert('Error', 'Failed to find location');
      });
    Keyboard.dismiss();
  };

  return (
    <View>
      <TextInput
        style={styles.searchInput}
        placeholder="Search for a place"
        value={searchText}
        onChangeText={setSearchText}
      />
      <TouchableOpacity style={styles.searchButton} onPress={handleSearch}>
        <Text>Search</Text>
      </TouchableOpacity>
    </View>
  );
};

export default Search;
