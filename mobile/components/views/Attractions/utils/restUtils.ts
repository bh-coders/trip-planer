import { Attraction, NewAttraction } from "../types";

export const createAttractionJson = (newAttraction: NewAttraction) => {
    const attractionData: Attraction = {
      id: 1,
      name: newAttraction.name,
      description: newAttraction.description,
      category: '',
      address: '',
      region: '',
      latitude: Number(newAttraction.coordinates.substring(0, newAttraction.coordinates.indexOf(','))),
      longitude: Number(newAttraction.coordinates.substring(newAttraction.coordinates.indexOf(',') + 1)),
      open_hours: newAttraction.openingHours,
      rating: newAttraction.rating
    };
    return attractionData;
  };