import { StackNavigationProp } from "@react-navigation/stack";

export type Attraction = {
    id: number;
    name: string;
    country: string;
    city: string;
    region: string;
    category: string;
    description: string;
    rating: number;
};

export type Filters = {
    category: string;
    city: string;
    country: string;
    keyword: string;
    radius: string;
    region: string;
};

type StackParamList = {
    AttractionDetailScreen: { id: number }
}

export type NavigationProps = StackNavigationProp<StackParamList>