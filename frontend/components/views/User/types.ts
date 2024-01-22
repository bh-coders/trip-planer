export type UserCredentials = {
  username: string;
  email: string;
  attractions: Attraction[];
  avatar?: string;
};

export type Attraction = {
  id: number;
  name: string;
  openingHours?: { [key: string]: { [key: string]: string } };
};

export type Token = {
  token: string;
};
