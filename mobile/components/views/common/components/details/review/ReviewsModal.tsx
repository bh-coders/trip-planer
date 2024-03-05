import React, { useEffect, useRef, useState } from 'react';
import { Alert, FlatList, Modal, Text, TouchableOpacity, View } from 'react-native';
import { reviewModal } from './styles';
import {
  fetchAttraction,
  fetchAttractionOpinions,
} from '../../../../Attractions/api/attractionsApi';
import { Attraction, Opinion } from '../../../../Attractions/types';
import { attractionsExamples, reviewsExamples } from '../../../../Attractions/api/fake/apiMock';
import ReviewTile from './ReviewTile';
import AttractionReviewTile from './AtrractionReviewTile';
import SortTile from './SortTile';
import FilterTile from './FilterTile';

interface ReviewsModalProps {
  attractionId: number;
  visible: boolean;
  hideMenu: () => void;
  onNewReview: () => void;
  onEditReview: (review: Opinion) => void;
}

const ReviewsModal: React.FC<ReviewsModalProps> = ({
  attractionId,
  visible,
  hideMenu: onHide,
  onNewReview,
  onEditReview,
}) => {
  const [attraction, setAttraction] = useState<Attraction>();
  const [attractionOpinions, setAttractionOpinions] = useState<Opinion[]>([]);
  const flatListRef = useRef<FlatList<Opinion>>(null);

  useEffect(() => {
    fetchAttraction(attractionId)
      .then((attractionData) => setAttraction(attractionData))
      .catch(() => {
        setAttraction(
          attractionsExamples.find((attractionDemo) => attractionDemo.id === attractionId)
        );
      });
    fetchAttractionOpinions(attractionId)
      .then((opinion) => setAttractionOpinions(opinion))
      .catch(() => {
        setAttractionOpinions(reviewsExamples);
        Alert.alert('Error', 'Failed getting reviews. Loading reviews demo data');
      });
  }, [attractionId]);

  const onBack = () => {
    onHide();
  };

  const onAddReviewPress = () => {
    onHide();
    onNewReview();
  };

  const scrollList = (index: number) => {
    flatListRef.current?.scrollToIndex({ index, animated: true });
  };

  return (
    <Modal transparent={false} animationType="slide" visible={visible} onRequestClose={onHide}>
      <View style={reviewModal.modalContainer}>
        <TouchableOpacity onPress={onBack}>
          <Text style={reviewModal.backArrow}>⇦</Text>
        </TouchableOpacity>
        <AttractionReviewTile attraction={attraction as Attraction} reviews={attractionOpinions} />
        <View style={reviewModal.filtersContainer}>
          <SortTile />
          <FilterTile />
        </View>
        <View style={reviewModal.modalContent}>
          <FlatList
            ref={flatListRef}
            data={attractionOpinions.sort((a, b) => b.rating - a.rating)} //ToDo sorting schemes dependent on user selection
            keyExtractor={(item, index) => index.toString()}
            renderItem={({ index, item: opinion }) => (
              <View>
                <ReviewTile
                  opinion={opinion}
                  author={{ id: opinion.author, name: 'zenek', avatar: '' }} //ToDo this needs to be changed to teal user data
                  loggedInUserId={1} //ToDo this needs to be changed to real user id
                  onPressExtra={() => scrollList(index)}
                  onEdit={() => onEditReview(opinion)}
                />
              </View>
            )}
          />
        </View>
      </View>

      <View style={reviewModal.buttonsContainer}>
        <TouchableOpacity style={reviewModal.addOpinionIcon} onPress={onAddReviewPress}>
          <Text style={reviewModal.addOpinionText}>+</Text>
        </TouchableOpacity>
      </View>
    </Modal>
  );
};

export default ReviewsModal;
