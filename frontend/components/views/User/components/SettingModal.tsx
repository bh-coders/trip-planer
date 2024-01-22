import { Modal, Text, View, TouchableOpacity } from 'react-native';
import { modalStyles } from '../styles';

const SettingsModal = ({ isVisible, setSettingsModalVisible, navigation }: any) => {
  const handleNavigationToModal = (modalName: string) => {
    setSettingsModalVisible(false);
    navigation.navigate(modalName);
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
