import React, { useEffect, useState } from 'react';
import { View, PermissionsAndroid, Platform, Alert } from 'react-native';
import { styles } from '../styles';
import Mapbox from '@rnmapbox/maps';
import Search from './Search';
import BottomPanel from './BottomPanel';
import Geolocation from 'react-native-geolocation-service';
import { fetchAttractions } from '../api/attractionsApi';
import { MAPBOX_PUBLIC_TOKEN } from '../../../../consts';
Mapbox.setAccessToken(MAPBOX_PUBLIC_TOKEN as any);

const MapboxBoard = () => {
  const [location, setLocation] = useState<any>(null);
  const [attractions, setAttractions] = useState<any>();
  const [panelVisible, setPanelVisible] = useState(false);
  const [searchText, setSearchText] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');

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
      Geolocation.requestAuthorization('whenInUse').then((status) => {
        if (status === 'granted') {
          setLocation(getCurrentLocation());
        } else {
          Alert.alert('Permission Denied', 'Location permission is required to use this feature.');
        }
      });
    }
  }, []);

  const getCurrentLocation = () => {
    Geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude } = position.coords;
        setLocation({ latitude, longitude });
      },
      (error) => Alert.alert('Error', error.message),
      { enableHighAccuracy: true, timeout: 15000, maximumAge: 10000 }
    );
  };

  const onCategoryChange = async (category: string) => {
    console.log('Zmiana kategorii', category, searchText);
    setSelectedCategory(category);
    try {
      const attractions = await fetchAttractions(searchText, category);
      setAttractions(attractions);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <View style={styles.container}>
      <Search
        setLocation={setLocation}
        fetchAttractions={fetchAttractions}
        setSearchText={setSearchText}
        searchText={searchText}
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
        onCategoryChange={onCategoryChange}
        attractions={attractions}
      />
    </View>
  );
};

export default MapboxBoard;
