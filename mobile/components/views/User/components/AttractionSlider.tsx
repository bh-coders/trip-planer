import React from 'react';
import { View, Image, FlatList, StyleSheet, Dimensions, Text } from 'react-native';
import { Attraction } from '../types';

const { width } = Dimensions.get('window');

type AttractionsSliderProps = {
  attractions: Attraction[] | undefined;
};

const AttractionsSlider = ({ attractions }: AttractionsSliderProps) => {
  const attractionsPlaceholder: Attraction[] = [
    {
      id: 1,
      name: 'Placeholder 1',
      photo_uri: 'https://piekarniagrzybki.pl/wp-content/uploads/2017/12/kremowka.jpg',
    },
    {
      id: 2,
      name: 'Placeholder 2',
      photo_uri: 'https://pbs.twimg.com/profile_images/1315571099107758081/OVi9vZU5_400x400.jpg',
    },
    {
      id: 3,
      name: 'Placeholder 3',
      photo_uri: 'https://nonsa.pl/images/thumb/7/7d/Testoviron.jpg/300px-Testoviron.jpg',
    },
  ];

  console.log('WIDTH', width);

  const renderAttraction = ({ item }: { item: Attraction }) => (
    <View style={styles.slide}>
      <View style={styles.imageContainer}>
        <Image source={{ uri: item?.photo_uri }} style={styles.attractionPhoto} />
      </View>
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
const styles = StyleSheet.create({
  slider: {
    flexGrow: 0,
  },
  slide: {
    width: width,
    height: width * 0.7,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 25,
    backgroundColor: '#f0f0f0',
    borderRadius: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  imageContainer: {
    width: '95%',
    height: '80%',
    borderRadius: 15,
    overflow: 'hidden',
    backgroundColor: '#ffffff',
    justifyContent: 'center',
  },
  attractionPhoto: {
    width: '100%',
    height: '100%',
    resizeMode: 'contain',
  },
  slideText: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    marginTop: 10,
  },
});

export default AttractionsSlider;
