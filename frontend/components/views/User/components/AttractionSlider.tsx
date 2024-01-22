import React from 'react';
import { View, Text, FlatList, StyleSheet, Dimensions } from 'react-native';

// Szerokość ekranu
const { width } = Dimensions.get('window');

const AttractionsSlider = () => {
  const attractions = [
    { id: '1', title: 'Placeholder 1' },
    { id: '2', title: 'Placeholder 2' },
    { id: '3', title: 'Placeholder 3' },
  ];
  console.log('WIDTH', width);
  const renderAttraction = ({ item }: any) => (
    <View style={styles.slide}>
      <Text style={styles.slideText}>{item.title}</Text>
    </View>
  );

  return (
    <FlatList
      data={attractions}
      renderItem={renderAttraction}
      keyExtractor={(item) => item.id}
      horizontal
      showsHorizontalScrollIndicator={true}
      pagingEnabled
      style={styles.slider}
    />
  );
};

// Styl dla komponentu
const styles = StyleSheet.create({
  slider: {
    flexGrow: 0,
  },
  slide: {
    width: width,
    height: width * 0.7,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#ccc',
    marginBottom: 25,
    borderRadius: 20,
  },
  slideText: {
    fontSize: 24,
    fontWeight: 'bold',
  },
});

export default AttractionsSlider;
