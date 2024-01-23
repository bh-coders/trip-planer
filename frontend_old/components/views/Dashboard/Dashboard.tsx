import React from 'react';
import { View, Text } from 'react-native';
import { styles } from './styles';

const Dashboard = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.errorText}>WAITING FOR MAP</Text>
    </View>
  );
};

export default Dashboard;
