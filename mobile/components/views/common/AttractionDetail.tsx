import React, { useEffect, useState } from 'react';
import { View, Text, ScrollView, TouchableOpacity, Alert } from 'react-native';
import { imagePlaceholder, attractionDetails } from './styles';
import { Attraction } from '../Attractions/types';
import { fetchAttraction } from '../Attractions/api/attractionsApi';
import { attractionsExamples } from '../Attractions/api/apiMock';

const AttractionDetailScreen: React.FC<{ route: { params: { id: number } } }> = ({ route }) => {

    const [attractionData, setAttractionData] = useState<Attraction>();
    const [attractionImages, setAttractionImages] = useState<any>();


    useEffect(() => {
        const attractionId = route.params.id;
        fetchAttraction(attractionId)
            .then((attraction) => setAttractionData(attraction))
            .catch((error) => {
                setAttractionData(attractionsExamples.find(attraction => attraction.id === attractionId));
                Alert.alert('Error', 'Failed getting attraction. Loading attraction demo data');
            });
        //Add another fetches
        setAttractionImages(Array.from({ length: 3 }, (_, index) => (
            <View key={index} style={imagePlaceholder.placeholder} />
        )));
    }, []);

    return (
        attractionDetails ? (
            <>
                <ScrollView style={attractionDetails.container}>
                    <View style={attractionDetails.header}>
                        <Text style={attractionDetails.name}>{attractionData?.name}</Text>
                        <TouchableOpacity style={attractionDetails.ratingContainer}>
                            <View style={attractionDetails.ratingBox}>
                                <Text style={attractionDetails.ratingText}>
                                    {attractionData?.rating.toFixed(1)}
                                </Text>
                                <View style={attractionDetails.addOpinionIcon}>
                                    <Text style={attractionDetails.addOpinionText}>+</Text>
                                </View>
                            </View>
                        </TouchableOpacity>
                    </View>

                    <View style={attractionDetails.categoryContainer}>
                        <Text style={attractionDetails.category}>{attractionData?.category}</Text>
                        <Text style={attractionDetails.views}>[100 views]</Text>
                    </View>

                    <ScrollView horizontal style={attractionDetails.imageContainer}>
                        <View style={imagePlaceholder.imageContainer}>{attractionImages}</View>
                    </ScrollView>

                    <View style={attractionDetails.openingHoursContainer}>
                        <Text style={attractionDetails.openingHours}>[⌚ opening hours]</Text>
                        <Text style={attractionDetails.price}>[Price]</Text>
                    </View>

                    <Text style={attractionDetails.description}>{attractionData?.description}</Text>
                </ScrollView>

                <View style={attractionDetails.buttonsContainer}>
                    <TouchableOpacity style={attractionDetails.addToRouteButton}>
                        <Text style={attractionDetails.addToRouteText}>Add to route</Text>
                    </TouchableOpacity>
                    <TouchableOpacity style={attractionDetails.favoriteButton}>
                        <Text style={attractionDetails.favoriteText}>❤️</Text>
                    </TouchableOpacity>
                </View>
            </>
        ) : (
            <Text> Loading or something else</Text>
        )
    )
};

export default AttractionDetailScreen;


