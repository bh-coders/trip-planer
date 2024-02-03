import React from 'react';
import { View } from 'react-native';
import { styles } from './styles';
import MapboxBoard from './components/MapboxBoard';

const Dashboard = ({ navigation }: any) => {
  return (
    <View style={styles.page}>
      <MapboxBoard navigation={navigation} />
    </View>
  );
};

export default Dashboard;
