import React, { useState } from 'react';
import { View, Text, Image, TouchableOpacity, Modal, ScrollView } from 'react-native';
import { reviewTile } from '../../../styles';
import { Opinion } from '../../../../Attractions/types';

interface AttractionTileProps {
    opinion: Opinion;
}

const AttractionTile: React.FC<AttractionTileProps> = ({ opinion }) => {

    const [shortReview, setShortReview] = useState(true);
    const [showImage, setShowImage] = useState(false);
    const [selectedImage, setSelectedImage] = useState('');

    const toggleReview = () => {
        setShortReview(!shortReview);
    };

    const toggleImageModal = (image: string) => {
        setSelectedImage(image);
        setShowImage(!showImage);
    };

    const renderShortReview = () => (
        <TouchableOpacity style={reviewTile.reviewTile} onPress={toggleReview}>
            <View style={reviewTile.tileContainer}>
                <Text style={reviewTile.author}>Author: {opinion.author}</Text>
                <Text style={reviewTile.title}>{opinion.title}</Text>
                <Text style={reviewTile.rate}>{opinion.rating}</Text>
            </View>
        </TouchableOpacity>
    );

    const renderLongReview = () => (
        <TouchableOpacity style={reviewTile.reviewTile} onPress={toggleReview}>
            <View style={reviewTile.tileContainer}>
                <Text style={reviewTile.author}>Author: {opinion.author}</Text>
                <Text style={reviewTile.title}>{opinion.title}</Text>
                <Text style={reviewTile.rate}>{opinion.rating}</Text>
            </View>
            <View style={reviewTile.tileContainer}>
                <ScrollView>
                    <Text style={reviewTile.description}>{opinion.description}</Text>
                    <View style={reviewTile.imageContainer}>
                        {opinion.images.map((image, index) => (
                            <TouchableOpacity key={index} onPress={() => toggleImageModal(image)}>
                                <Image source={{ uri: image }} style={reviewTile.thumbnail} />
                            </TouchableOpacity>
                        ))}
                    </View>
                </ScrollView>
            </View>
            <View style={reviewTile.tileContainer}>
                <Text style={reviewTile.price}>Price: {opinion.price}</Text>
                <Text style={reviewTile.timeSpent}>Time: {opinion.time_spent}</Text>
            </View>
            <Modal visible={showImage} transparent={true}>
                <View style={reviewTile.imageModal}>
                    <TouchableOpacity style={reviewTile.closeButton} onPress={() => toggleImageModal('')}>
                        <Text style={reviewTile.closeText}>Close</Text>
                    </TouchableOpacity>
                    <Image source={{ uri: selectedImage }} style={reviewTile.modalImage} />
                </View>
            </Modal>
        </TouchableOpacity>
    );

    return shortReview ? renderShortReview() : renderLongReview();
};


export default AttractionTile;