import { Modal, Text, View, TouchableOpacity } from 'react-native';
import { modalStyles } from '../styles';
import React, { FC } from 'react';
import { NavigationProp } from '@react-navigation/native';

type SettingsModalProps = {
  isVisible: boolean;
  setSettingsModalVisible: React.Dispatch<React.SetStateAction<boolean>>;
  navigation: NavigationProp<any>;
  userToken: string | null | undefined;
};

const SettingsModal: FC<SettingsModalProps> = ({
  isVisible,
  setSettingsModalVisible,
  navigation,
  userToken,
}) => {
  const handleNavigationToModal = (modalName: string) => {
    setSettingsModalVisible(false);
    navigation.navigate(modalName, { userToken });
  };

  return (
    <Modal
      visible={isVisible}
      onRequestClose={() => setSettingsModalVisible(false)}
      transparent={true}
      animationType="slide">
      <View style={modalStyles.centeredView}>
        <View style={modalStyles.modalView}>
          <TouchableOpacity
            style={modalStyles.settingsButton}
            onPress={() => handleNavigationToModal('Change Profil Informations')}>
            <Text style={modalStyles.textStyle}>Change Credentials</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={modalStyles.settingsButton}
            onPress={() => handleNavigationToModal('Change Email')}>
            <Text style={modalStyles.textStyle}>Change Email</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={modalStyles.settingsButton}
            onPress={() => handleNavigationToModal('Change Password')}>
            <Text style={modalStyles.textStyle}>Change Password</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={modalStyles.settingsButton}
            onPress={() => handleNavigationToModal('Delete Account')}>
            <Text style={modalStyles.textStyle}>Delete</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={modalStyles.settingsButton}
            onPress={() => setSettingsModalVisible(false)}>
            <Text style={modalStyles.textStyle}>My Attractions</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={modalStyles.buttonClose}
            onPress={() => setSettingsModalVisible(false)}>
            <Text style={modalStyles.textStyle}>Close</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
};
export default SettingsModal;
