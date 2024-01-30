export interface Attraction {
  id: number;
  name: string;
  country: string;
  city: string;
  region: string;
  category: string;
  description: string;
  rating: number;
}


export const attractionsExamples = [
    {
        id: 1,
        name: 'Royal Castle',
        country: 'Poland',
        city: 'Warsaw',
        region: 'Masovian',
        category: 'Historical',
        description: 'Beautiful castle in the heart of Warsaw.',
        rating: 4
      },
      {
        id: 2,
        name: 'Wawel Castle',
        country: 'Poland',
        city: 'Krakow',
        region: 'Lesser Poland',
        category: 'Historical',
        description: 'Historic castle in Krakow.',
        rating: 4
      },
      {
        id: 3,
        name: 'Malbork Castle',
        country: 'Poland',
        city: 'Malbork',
        region: 'Pomeranian',
        category: 'Historical',
        description: 'World\'s largest brick castle.',
        rating: 5
      },
      {
        id: 4,
        name: 'Berlin Wall',
        country: 'Germany',
        city: 'Berlin',
        region: 'Brandenburg',
        category: 'Historical',
        description: 'Remnant of the Cold War.',
        rating: 3
      },
      {
        id: 5,
        name: 'Neuschwanstein Castle',
        country: 'Germany',
        city: 'Füssen',
        region: 'Bavaria',
        category: 'Historical',
        description: 'Fairytale castle in the Bavarian Alps.',
        rating: 5
      },
      {
        id: 6,
        name: 'Cologne Cathedral',
        country: 'Germany',
        city: 'Cologne',
        region: 'North Rhine-Westphalia',
        category: 'Religious',
        description: 'Gothic cathedral and UNESCO World Heritage Site.',
        rating: 4
      },
      {
        id: 7,
        name: 'Eiffel Tower',
        country: 'France',
        city: 'Paris',
        region: 'Île-de-France',
        category: 'Landmark',
        description: 'Iconic symbol of Paris.',
        rating: 5
      },
      {
        id: 8,
        name: 'Louvre Museum',
        country: 'France',
        city: 'Paris',
        region: 'Île-de-France',
        category: 'Museum',
        description: 'World\'s largest art museum and a historic monument.',
        rating: 4
      },
      {
        id: 9,
        name: 'Mont Saint-Michel',
        country: 'France',
        city: 'Le Mont-Saint-Michel',
        region: 'Normandy',
        category: 'Historical',
        description: 'Island commune with a medieval abbey.',
        rating: 4
      },
    ];
