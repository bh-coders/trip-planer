import React, { useEffect, useState } from "react"
import { Alert, FlatList, Modal, Text, TouchableOpacity, View } from "react-native"
import { reviewModal } from "../../../styles";
import { fetchAttraction, fetchAttractionOpinions } from "../../../../Attractions/api/attractionsApi";
import { Attraction, Opinion } from "../../../../Attractions/types";
import { attractionsExamples, reviewsExamples } from "../../../../Attractions/api/fake/apiMock";
import ReviewTile from "./ReviewTile";
import AttractionTile from "../../../AttractionTile";

interface ReviewsModalProps {
    attractionId: number,
    visible: boolean,
    hideMenu: () => void
}


const ReviewsModal: React.FC<ReviewsModalProps> = ({ attractionId, visible, hideMenu: onHide }) => {

    const [attraction, setAttraction] = useState<Attraction>();
    const [attractionOpinions, setAttractionOpinions] = useState<Opinion[]>([]);

    useEffect(() => {
        fetchAttraction(attractionId)
            .then((attraction) => setAttraction(attraction))
            .catch((error) => {
                setAttraction(attractionsExamples.find(attraction => attraction.id === attractionId));
            });
        fetchAttractionOpinions(attractionId)
            .then((opinion) => setAttractionOpinions(opinion))
            .catch((error) => {
                setAttractionOpinions(reviewsExamples);
                Alert.alert('Error', 'Failed getting reviews. Loading rewievs demo data');
            });
    }, [attractionId]);

    const onBack = () => {
        console.log(`Edit attraction ${attractionId}`);
        onHide();
    };

    return (
        <Modal
            transparent={false}
            animationType='slide'
            visible={visible}
            onRequestClose={onHide}
        >
            <View style={reviewModal.modalContainer}>
                <TouchableOpacity onPress={onBack}>
                    <Text style={reviewModal.backArrow}>⇦</Text>
                </TouchableOpacity>
                <AttractionTile
                    attraction={{
                        place_name: attraction?.name,
                        place_description: attraction?.description,
                        place_category: attraction?.category,
                        place_rating: attraction?.rating.toFixed(1)
                    }}
                />
                <View style={reviewModal.modalContent}>
                    <FlatList
                        // style={attractionSerchStyles.attractionsList}
                        data={attractionOpinions}
                        keyExtractor={(item, index) => index.toString()}
                        renderItem={({ index, item: opinion }) => (
                            <TouchableOpacity>
                                <View>
                                    <ReviewTile
                                        opinion={opinion}
                                    />
                                </View>
                            </TouchableOpacity>
                        )}
                    />
                </View>
            </View>

            <View style={reviewModal.buttonsContainer}>
                <TouchableOpacity style={reviewModal.addOpinionIcon}>
                    <Text style={reviewModal.addOpinionText}>+</Text>
                </TouchableOpacity>
            </View>

        </Modal >
    );
};

export default ReviewsModal;