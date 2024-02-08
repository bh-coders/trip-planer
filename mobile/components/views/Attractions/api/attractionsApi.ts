import { Attraction, Opinion } from "../types";

export const fetchUserAttractions = async (
  id: number
): Promise<Attraction[]> => {
  const url = `http://localhost/user/${id}/atrractions`;
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data as Attraction[];
  } catch (error) {
    console.error('Error fetching attractions:', error);
    throw error;
  }
};

export const fetchAttraction = async (
  id: number
): Promise<Attraction> => {
  const url = `http://localhost/atractions/${id}`;
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data as Attraction;
  } catch (error) {
    console.error('Error fetching attraction:', error);
    throw error;
  }
};

export const fetchAttractionImages = async (
  id: number
): Promise<String[]> => {
  const url = ``;
  try {
    await fetch(url);
    return [];
  } catch {
    return [];
  }
};

export const fetchAttractionOpinions = async (
  id: number
): Promise<Opinion[]> => {
  const url = '';
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data as Opinion[];
  } catch (error) {
    console.error('Error fetching opinions:', error);
    throw error;
  }
};

export const createAttraction = async (
  attraction: Attraction
): Promise<String> => {
  const url = '';
  try {
    const response = await fetch(
      url, {
      method: 'POST',
      body: JSON.stringify(attraction)
    });
    const data = await response.json();
    return data as String;
  } catch (error) {
    console.error('Error posting attraction:', error);
    throw error;
  };
};

export const createOpinion = async (
  opinion: Opinion
): Promise<String> => {
  const url = '';
  try {
    const response = await fetch(
      url, {
      method: 'POST',
      body: JSON.stringify(opinion)
    });
    const data = await response.json();
    return data as String;
  } catch (error) {
    console.error('Error posting opinion:', error);
    throw error;
  };
};

export const updateAttraction = async (
  attraction: Attraction
): Promise<Attraction> => {
  const url = '';
  try {
    const response = await fetch(
      url, {
      method: 'PATCH',
      body: JSON.stringify(attraction)
    });
    const data = await response.json();
    return data as Attraction;
  } catch (error) {
    console.error('Error updating attraction:', error);
    throw error;
  }

};

export const updateOpinion = async (
  opinion: Opinion
): Promise<Opinion> => {
  const url = '';
  try {
    const response = await fetch(
      url, {
      method: 'PATCH',
      body: JSON.stringify(opinion)
    });
    const data = await response.json();
    return data as Opinion;
  } catch (error) {
    console.error('Error updating opinion:', error);
    throw error;
  }
};

export const deleteAttraction = async (
  attractionId: number
): Promise<String> => {
  const url = '';
  try {
    const response = await fetch(
      url, {
        method: 'DELETE',
        body: JSON.stringify({attraction_id: attractionId})
      });
    const data = await response.json();
    return data as String;
  } catch (error) {
    console.error('Error deleteing attraction:', error);
    throw error;
  }
};

export const deleteOpinion = async (
  opinionId: number
): Promise<String> => {
  const url = '';
  try {
    const response = await fetch(
      url, {
        method: 'DELETE',
        body: JSON.stringify({opinion_id: opinionId})
      });
    const data = await response.json();
    return data as String;
  } catch (error) {
    console.error('Error deleteing opinion:', error);
    throw error;
  }
};
