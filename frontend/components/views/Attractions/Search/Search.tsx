import React from 'react';
import { View, Text } from 'react-native';
import { styles } from './styles';

const Search = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.errorText}>Searcher not ready</Text>
    </View>
  );
};

export default Search;