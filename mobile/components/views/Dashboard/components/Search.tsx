import { styles } from '../styles';
import { View, TextInput, Button, Alert, Keyboard } from 'react-native';
import { useState } from 'react';
import Config from 'react-native-config';

const Search = ({ setLocation }: any) => {
  const [searchText, setSearchText] = useState('');
  const handleSearch = () => {
    const mapboxGeocodingUrl = `https://api.mapbox.com/geocoding/v5/mapbox.places/${encodeURIComponent(
      searchText
    )}.json?access_token=${Config.MAPBOX_PUBLIC_TOKEN}`;

    fetch(mapboxGeocodingUrl)
      .then((response) => response.json())
      .then((data) => {
        const { coordinates } = data.features[0].geometry;
        setLocation({ latitude: coordinates[1], longitude: coordinates[0] });
        Keyboard.dismiss();
      })
      .catch((error) => {
        console.error('Error during Mapbox geocoding:', error);
        Alert.alert('Error', 'Failed to find location');
      });
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
