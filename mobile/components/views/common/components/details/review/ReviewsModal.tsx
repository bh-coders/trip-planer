import React, { useEffect, useRef, useState } from "react"
import { Alert, FlatList, Modal, Text, TouchableOpacity, View } from "react-native"
import { reviewModal } from "./styles";
import { fetchAttraction, fetchAttractionOpinions } from "../../../../Attractions/api/attractionsApi";
import { Attraction, Opinion } from "../../../../Attractions/types";
import { attractionsExamples, reviewsExamples } from "../../../../Attractions/api/fake/apiMock";
import ReviewTile from "./ReviewTile";
import AttractionReviewTile from "./AtrractionReviewTile";
import SortTile from "./SortTile";
import FilterTile from "./FilterTile";

interface ReviewsModalProps {
    attractionId: number,
    visible: boolean,
    hideMenu: () => void
}


const ReviewsModal: React.FC<ReviewsModalProps> = ({ attractionId, visible, hideMenu: onHide }) => {

    const [attraction, setAttraction] = useState<Attraction>();
    const [attractionOpinions, setAttractionOpinions] = useState<Opinion[]>([]);
    const flatListRef = useRef<FlatList<Opinion>>(null);

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

    const scrollList = (index: number) => {
        flatListRef.current?.scrollToIndex({ index, animated: true });
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
                <AttractionReviewTile
                    attraction={attraction as Attraction}
                    reviews={attractionOpinions}
                />
                <View style={reviewModal.filtersContainer}>
                <SortTile

                />
                <FilterTile

                />
                </View>
                <View style={reviewModal.modalContent}>
                    <FlatList
                        // style={attractionSerchStyles.attractionsList}
                        ref={flatListRef}
                        data={attractionOpinions.sort((a, b) => b.rating - a.rating)}
                        keyExtractor={(item, index) => index.toString()}
                        renderItem={({ index, item: opinion }) => (
                            <View>
                                <ReviewTile
                                    opinion={opinion}
                                    author={{ id: opinion.author, name: 'zenek', avatar: '' }}
                                    loggedInUserId={1} //this needs to be changed to real user id
                                    onPressExtra={() => scrollList(index)}
                                />
                            </View>
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