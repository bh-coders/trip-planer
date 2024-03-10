import React from 'react';
import ReviewForm from './AttractionReviewForm.tsx';

const AddNewReview: React.FC = () => {
  return <ReviewForm onSubmit={(data) => console.log('Adding review:', data)} />;
};

export default AddNewReview;
