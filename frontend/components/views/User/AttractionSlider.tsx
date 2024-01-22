import React from 'react';
import { View, Text, FlatList, StyleSheet, Dimensions } from 'react-native';

// Szerokość ekranu
const { width } = Dimensions.get('window');

const AttractionsSlider = () => {
  const attractions = [
    { id: '1', title: 'Atrakcja1' },
    { id: '2', title: 'Atrakcja2' },
    { id: '3', title: 'Atrakcja3' },
  ];

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
      showsHorizontalScrollIndicator={false}
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
    justifyContent: 'center',
    alignItems: 'center',
  },
  slideText: {
    fontSize: 24,
    fontWeight: 'bold',
  },
});

export default AttractionsSlider;
