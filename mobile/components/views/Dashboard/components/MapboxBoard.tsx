import React, { useEffect, useState } from 'react';
import { View, PermissionsAndroid, Platform, Alert } from 'react-native';
import { styles } from '../styles';
import Mapbox from '@rnmapbox/maps';
import Config from 'react-native-config';
import Geolocation from 'react-native-geolocation-service';
import Search from './Search';
Mapbox.setAccessToken(Config.MAPBOX_PUBLIC_TOKEN as any);

const MapboxBoard = () => {
  const [location, setLocation] = useState<any>(null);

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
          getCurrentLocation();
        } else {
          Alert.alert('Permission Denied', 'Location permission is required to use this feature.');
        }
      });
    } else {
      getCurrentLocation();
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

  return (
    <View style={styles.container}>
      <Search setLocation={setLocation} />
      {location && (
        <Mapbox.MapView style={styles.map}>
          <Mapbox.Camera
            zoomLevel={10}
            centerCoordinate={[location.longitude, location.latitude]}
          />
        </Mapbox.MapView>
      )}
    </View>
  );
};

export default MapboxBoard;
