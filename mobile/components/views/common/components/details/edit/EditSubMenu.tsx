import React from 'react';
import { Modal, Text, TouchableOpacity, View } from 'react-native';
import { attractionDetails } from '../../../styles';

interface EditModalProps {
  Id: number | undefined;
  visible: boolean;
  hideMenu: () => void;
  edit: () => void | undefined;
}

const EditSubMenuModal: React.FC<EditModalProps> = ({
  Id: attractionId,
  visible,
  hideMenu: onMenu,
  edit: edit,
}) => {
  const onEdit = () => {
    console.log(`Edit attraction ${attractionId}`);
    onMenu();
    edit();
  };

  const onDelete = () => {
    console.log(`Delete attraction ${attractionId}`);
    onMenu();
  };

  return (
    <Modal transparent={true} animationType="slide" visible={visible} onRequestClose={onMenu}>
      <View style={attractionDetails.modalContainer}>
        <View style={attractionDetails.modalContent}>
          <TouchableOpacity onPress={onEdit}>
            <Text style={attractionDetails.modalText}>Edit</Text>
          </TouchableOpacity>
          <TouchableOpacity onPress={onDelete}>
            <Text style={attractionDetails.modalText}>Delete</Text>
          </TouchableOpacity>
          <TouchableOpacity onPress={onMenu}>
            <Text style={attractionDetails.modalText}>Cancel</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
};

export default EditSubMenuModal;
