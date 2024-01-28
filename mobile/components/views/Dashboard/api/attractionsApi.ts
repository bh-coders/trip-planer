interface Attraction {
  id: number;
  name: string;
  description: string;
}

export const fetchAttractions = (
  city: string,
  category: string = 'food'
): Promise<Attraction[]> => {
  const url = `http://localhost/?city=${encodeURIComponent(city)}?category=${category}`;
  return fetch(url)
    .then((response) => response.json())
    .then((data) => data as Attraction[])
    .catch((error) => {
      console.error('Error fetching attractions:', error);
      throw error;
    });
};
