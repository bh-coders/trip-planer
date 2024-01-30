export type UserCredentials = {
  firstName: string;
  lastName: string;
  username: string;
  email: string;
  attractions: Attraction[];
  avatar?: string;
};

export type Attraction = {
  id: number;
  name: string;
  openingHours?: { [key: string]: { [key: string]: string } };
  photo_uri?: string;
};

export type Token = {
  token: string;
};
