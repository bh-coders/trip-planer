import Config from 'react-native-config';
import { MAPBOX_PUBLIC_TOKEN } from '../../../../consts';
interface Coordinates {
  latitude: number;
  longitude: number;
}

export const fetchLocationFromMapbox = (searchText: string): Promise<Coordinates> => {
  const url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${encodeURIComponent(
    searchText
  )}.json?access_token=${MAPBOX_PUBLIC_TOKEN}`;

  return fetch(url)
    .then((response) => response.json())
    .then((data) => {
      if (data.features && data.features.length > 0) {
        const coordinates = data.features[0].geometry.coordinates;
        return { latitude: coordinates[1], longitude: coordinates[0] } as Coordinates;
      }
      throw new Error('No location found');
    })
    .catch((error) => {
      console.error('Error during Mapbox geocoding:', error);
      throw error;
    });
};
