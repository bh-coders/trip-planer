import { StackNavigationProp } from "@react-navigation/stack";

export type Attraction = {
    id: number; 
    user_id?: number;
    name: string;
    description: string;
    latitude: number;
    longitude: number;
    open_hours?: OpenHours;
    category: string;
    address: string;
    city?: string;
    country?: string;
    region: string;
    rating: number;
    time_spent?: number;
    price?: number;
    visits?: number;
};

export type NewAttraction = {
    name: string;
    description: string;
    coordinates: string;
    openingHours: OpenHours;
    rating: number;
}

export type Filters = {
    category: string;
    city: string;
    country: string;
    keyword: string;
    radius: string;
    region: string;
};

export type OpenHours = {
    open: number;
    close: number;
};

type StackParamList = {
    AttractionDetailScreen: { id: number }
}

export type NavigationProps = StackNavigationProp<StackParamList>