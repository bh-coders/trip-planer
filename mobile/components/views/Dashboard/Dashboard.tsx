import React from 'react';
import {View} from 'react-native';
import {styles} from './styles';
import Mapbox from '@rnmapbox/maps';
import Config from 'react-native-config';

// public token
Mapbox.setAccessToken(Config.MAPBOX_PUBLIC_TOKEN);
const Dashboard = () => {
  return (
    <View style={styles.page}>
      <View style={styles.container}>
        <Mapbox.MapView style={styles.map} />
      </View>
    </View>
  );
};

export default Dashboard;
