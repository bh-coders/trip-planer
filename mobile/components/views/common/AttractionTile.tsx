import React from 'react';
import { View, Text, Image } from 'react-native';
import { attractionTileStyles } from './styles';

const AttractionTile = ({ attraction }: any) => {
  const hasImage = attraction.image_url && attraction.image_url.trim() !== '';

  return (
    <View style={attractionTileStyles.attractionTile}>
      <View style={attractionTileStyles.leftContainer}>
        <View style={attractionTileStyles.imageContainer}>
          {hasImage ? (
            <Image source={{ uri: attraction.image_url }} style={attractionTileStyles.image} />
          ) : (
            <View style={attractionTileStyles.emptyImage} />
          )}
        </View>
        <View style={attractionTileStyles.textContainer}>
          <Text style={attractionTileStyles.title}>{attraction.place_name}</Text>
          <Text style={attractionTileStyles.category}>{attraction.place_category}</Text>
          <Text style={attractionTileStyles.description}>{attraction.place_description}</Text>
        </View>
      </View>
      <Text style={attractionTileStyles.rate}>{attraction.place_rating}</Text>
    </View>
  );
};

export default AttractionTile;
