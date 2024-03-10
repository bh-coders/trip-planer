import React from 'react';
import ReviewForm from './AttractionReviewForm.tsx';

const EditReview: React.FC<{ route: any }> = ({ route }) => {
  const { review } = route.params;
  return <ReviewForm review={review} onSubmit={(data) => console.log('Editing review:', data)} />;
};

export default EditReview;
