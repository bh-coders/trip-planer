import React, { useState } from 'react';
import { View, TextInput, Button, Keyboard } from 'react-native';
import { styles } from '../styles';
import Config from 'react-native-config';

const Search = ({ setLocation, fetchAttractions, onSearch }: any) => {
  const [searchText, setSearchText] = useState('');

  const handleSearch = async () => {
    try {
      const response = await fetch(
        `https://api.mapbox.com/geocoding/v5/mapbox.places/${searchText}.json?access_token=${Config.MAPBOX_PUBLIC_TOKEN}`
      );
      const data = await response.json();
      if (data.features && data.features.length > 0) {
        const coords = data.features[0].center;
        setLocation({ latitude: coords[1], longitude: coords[0] });
        fetchAttractions({ latitude: coords[1], longitude: coords[0] });
        onSearch(searchText);
        Keyboard.dismiss();
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <View>
      <TextInput
        style={styles.searchInput}
        placeholder="Search for a place"
        value={searchText}
        onChangeText={setSearchText}
      />
      <Button title="Search" onPress={handleSearch} />
    </View>
  );
};

export default Search;
