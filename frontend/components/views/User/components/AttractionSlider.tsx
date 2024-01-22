import React from 'react';
import { View, Text, FlatList, StyleSheet, Dimensions } from 'react-native';
import { Attraction } from '../types';

const { width } = Dimensions.get('window');

type AttractionsSliderProps = {
  attractions: Attraction[] | undefined;
};

const AttractionsSlider = ({ attractions }: AttractionsSliderProps) => {
  const attractionsPlaceholder: Attraction[] = [
    { id: 1, name: 'Placeholder 1' },
    { id: 2, name: 'Placeholder 2' },
    { id: 3, name: 'Placeholder 3' },
  ];

  console.log('WIDTH', width);

  const renderAttraction = ({ item }: { item: Attraction }) => (
    <View style={styles.slide}>
      <Text style={styles.slideText}>{item.name}</Text>
    </View>
  );

  return (
    <FlatList
      data={attractions || attractionsPlaceholder}
      renderItem={renderAttraction}
      keyExtractor={(item) => item.id.toString()}
      horizontal
      showsHorizontalScrollIndicator={true}
      pagingEnabled
      style={styles.slider}
    />
  );
};

// Styl dla

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
