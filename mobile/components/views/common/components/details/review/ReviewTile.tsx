import React, { useState } from 'react';
import { Image, Modal, ScrollView, Text, TouchableOpacity, View } from 'react-native';
import { reviewTile } from './styles';
import { Opinion } from '../../../../Attractions/types';
import EditSubMenuModal from '../edit/EditSubMenu';

interface AttractionTileProps {
  opinion: Opinion;
  author: { id: number; name: string; avatar: string | undefined };
  loggedInUserId: number;
  onPressExtra: () => void;
  onEdit: () => void;
}

const AttractionTile: React.FC<AttractionTileProps> = ({
  opinion,
  author,
  loggedInUserId,
  onPressExtra,
  onEdit,
}) => {
  const [shortReview, setShortReview] = useState(true);
  const [showImage, setShowImage] = useState(false);
  const [selectedImage, setSelectedImage] = useState('');
  const [editMenuVisible, setEditMenuVisible] = useState<boolean>(false);
  const hasAuthorAvatar = author.avatar && author.avatar.trim() !== '';

  const toggleReview = () => {
    setShortReview(!shortReview);
    onPressExtra();
  };

  const toggleImageModal = (image: string) => {
    setSelectedImage(image);
    setShowImage(!showImage);
  };

  const editBox = (attractionAuthor: number | undefined) => {
    if (attractionAuthor && attractionAuthor === loggedInUserId) {
      return (
        <TouchableOpacity onPress={() => setEditMenuVisible(true)}>
          <Text style={reviewTile.title}>✎</Text>
        </TouchableOpacity>
      );
    }
  };

  const renderShortReview = () => (
    <TouchableOpacity style={reviewTile.reviewTile} onPress={toggleReview}>
      <View style={reviewTile.tileContainer}>
        {hasAuthorAvatar ? (
          <Image source={{ uri: author.avatar }} style={reviewTile.image} />
        ) : (
          <View style={reviewTile.emptyImage}>
            <Text style={reviewTile.author}>Author: {opinion.author}</Text>
          </View>
        )}
        <Text style={reviewTile.title}>{opinion.title}</Text>
        <Text style={reviewTile.rate}>{opinion.rating.toFixed(1)}</Text>
      </View>
    </TouchableOpacity>
  );

  const renderLongReview = () => (
    <TouchableOpacity style={reviewTile.reviewTile} onPress={toggleReview}>
      <View style={reviewTile.tileContainer}>
        {hasAuthorAvatar ? (
          <Image source={{ uri: author.avatar }} style={reviewTile.image} />
        ) : (
          <View style={reviewTile.emptyImage}>
            <Text style={reviewTile.author}>Author: {opinion.author}</Text>
          </View>
        )}
        <Text style={reviewTile.title}>
          {opinion.title} {editBox(opinion.author)}
        </Text>
        <Text style={reviewTile.rate}>{opinion.rating.toFixed(1)}</Text>
      </View>
      <EditSubMenuModal
        Id={opinion.id}
        visible={editMenuVisible}
        hideMenu={() => setEditMenuVisible(false)}
        edit={() => onEdit()}
      />
      <View
        style={{
          ...reviewTile.tileContainer,
          alignItems: 'flex-end',
          justifyContent: 'flex-end',
          marginTop: -10,
        }}>
        <Text style={reviewTile.price}>Price: {'$'.repeat(opinion.price)}</Text>
        <Text style={reviewTile.timeSpent}>Time: {'⌚'.repeat(opinion.time_spent)}</Text>
      </View>
      <View style={reviewTile.tileContainer}>
        <ScrollView>
          <Text style={reviewTile.description}>{opinion.description}</Text>
          <ScrollView horizontal>
            {opinion.images.map((image, index) => (
              <TouchableOpacity
                style={reviewTile.imageContainer}
                key={index}
                onPress={() => toggleImageModal(image)}>
                <Image source={{ uri: image }} style={reviewTile.thumbnail} />
              </TouchableOpacity>
            ))}
          </ScrollView>
        </ScrollView>
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
