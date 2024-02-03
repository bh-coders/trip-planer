import React from "react";
import { Button, Modal, Text, View } from "react-native";
import StarRating from 'react-native-star-rating';


const AttractionModal = ({ visible, attraction, onClose }: any) => {
    const handleClose = () => {
        onClose();
    };

    return (
        <Modal visible={visible} transparent={true} animationType="slide">
            <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', paddingHorizontal: 20 }}>
                <View style={{ backgroundColor: 'white', borderRadius: 10, padding: 20, alignItems: 'center' }}>
                    <Text style={{ fontSize: 20, fontWeight: 'bold', marginBottom: 10 }}>{attraction.name}</Text>
                    <Text>{attraction.country}, {attraction.city}, {attraction.region}</Text>
                    <Text style={{ marginTop: 5, marginBottom: 10, fontStyle: 'italic' }}>{attraction.category}</Text>
                    <Text>{attraction.description}</Text>
                    <View style={{ marginVertical: 10 }}>
                        <StarRating
                            disabled={false}
                            maxStars={5}
                            emptyStar={'star-o'}
                            fullStar={'star'}
                            halfStar={'ios-star-half'}
                            rating={attraction.rating}
                            fullStarColor={'orange'}
                        />
                    </View>
                    <View style={{ marginVertical: 20 }}>
                        <Button title="Ok" onPress={handleClose} color={'green'} />
                    </View>
                </View>
            </View>
        </Modal>
    );

};

export default AttractionModal;