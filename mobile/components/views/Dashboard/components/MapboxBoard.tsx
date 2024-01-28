import React, { useEffect, useState } from 'react';
import { View, PermissionsAndroid, Platform, Alert } from 'react-native';
import { styles } from '../styles';
import Mapbox from '@rnmapbox/maps';
import Config from 'react-native-config';
import Search from './Search';
import BottomPanel from './BottomPanel';
import Geolocation from 'react-native-geolocation-service';

Mapbox.setAccessToken(Config.MAPBOX_PUBLIC_TOKEN as any);

const MapboxBoard = () => {
  const [location, setLocation] = useState<any>(null);
  const [attractions, setAttractions] = useState([]);
  const [panelVisible, setPanelVisible] = useState(false);
  const [searchText, setSearchText] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');

  // const handleSearchTextChange = (text: string) => {
  //   setSearchText(text);
  // };
  useEffect(() => {
    if (Platform.OS === 'android') {
      PermissionsAndroid.request(PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION, {
        title: 'Permission to access location',
        message: 'We need your permission to access your location',
        buttonNeutral: 'Ask Me Later',
        buttonNegative: 'Cancel',
        buttonPositive: 'OK',
      }).then((granted) => {
        if (granted === PermissionsAndroid.RESULTS.GRANTED) {
          setLocation(getCurrentLocation());
        } else {
          Alert.alert('Permission Denied', 'Location permission is required to use this feature.');
        }
      });
    } else {
      setLocation(getCurrentLocation());
    }
  }, []);

  const getCurrentLocation = () => {
    Geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude } = position.coords;
        console.log(latitude, longitude);
        setLocation({ latitude, longitude });
      },
      (error) => Alert.alert('Error', error.message),
      { enableHighAccuracy: true, timeout: 15000, maximumAge: 10000 }
    );
  };

  const fetchAttractions = async (coords: { latitude: number; longitude: number }) => {
    try {
      const response = await fetch(
        `https://api.mapbox.com/geocoding/v5/mapbox.places/poi.json?proximity=${coords.longitude},${coords.latitude}&types=poi&categories=food&access_token=${Config.MAPBOX_PUBLIC_TOKEN}`
      );
      const data = await response.json();
      setAttractions(data.features);
    } catch (error) {
      console.error(error);
    }
  };
  const handleSearch = async (text: string) => {
    setSearchText(text);
    setPanelVisible(false);

    try {
      const response = await fetch(
        `https://api.mapbox.com/geocoding/v5/mapbox.places/${text}.json?access_token=${Config.MAPBOX_PUBLIC_TOKEN}`
      );
      const data = await response.json();

      if (data.features && data.features.length > 0) {
        const coords = data.features[0].center;
        setLocation({ latitude: coords[1], longitude: coords[0] });

        fetchAttractions({ latitude: coords[1], longitude: coords[0] });
      }
    } catch (error) {
      console.error(error);
      Alert.alert('Error', 'Failed to fetch location data');
    }
  };
  const handleCategoryChange = async (category: string) => {
    setSelectedCategory(category);

    if (!location) return;

    try {
      const response = await fetch(
        `https://api.mapbox.com/geocoding/v5/mapbox.places/${category}.json?proximity=${location.longitude},${location.latitude}&access_token=${Config.MAPBOX_PUBLIC_TOKEN}`
      );
      const data = await response.json();
      setAttractions(data.features);
    } catch (error) {
      console.error(error);
      Alert.alert('Error', 'Failed to fetch category data');
    }
  };
  return (
    <View style={styles.container}>
      <Search
        setLocation={setLocation}
        fetchAttractions={fetchAttractions}
        onSearch={handleSearch}
      />
      {location && (
        <Mapbox.MapView style={styles.map}>
          <Mapbox.Camera
            zoomLevel={10}
            centerCoordinate={[location.longitude, location.latitude]}
          />
        </Mapbox.MapView>
      )}
      <BottomPanel
        isVisible={panelVisible}
        searchText={searchText}
        selectedCategory={selectedCategory}
        onCategoryChange={handleCategoryChange}
        attractions={attractions}
      />
    </View>
  );
};

export default MapboxBoard;
