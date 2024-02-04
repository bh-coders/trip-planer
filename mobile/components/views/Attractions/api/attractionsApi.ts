import { Attraction } from "../types";

export const fetchUsersAttractions = (
  id: number
): Promise<Attraction[]> => {
  const url = `http://localhost/user/${id}/atrractions`;
  return fetch(url)
    .then((response) => response.json())
    .then((data) => data as Attraction[])
    .catch((error) => {
      console.error('Error fetching attractions:', error);
      throw error;
    });
};

export const fetchAttraction = (
  id: number
): Promise<Attraction> => {
  const url = `http://localhost/atraction/${id}`;
  return fetch(url)
    .then((response) => response.json())
    .then((data) => data as Attraction)
    .catch((error) => {
      console.error('Error fetching attraction:', error);
      throw error;
    });
};