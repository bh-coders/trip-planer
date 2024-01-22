import React from 'react';
import { View, Text } from 'react-native';
import { styles } from './styles';

const AddNew = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.errorText}>Adder not ready</Text>
    </View>
  );
};

export default AddNew;