export type UserCredentials = {
  username: string;
  email: string;
  attractions: Attraction[];
  avatar?: string;
};

export type Attraction = {
  name: string;
  openingHours: { [key: string]: { [key: string]: string } };
};

export type Token = {
  token: string;
};
