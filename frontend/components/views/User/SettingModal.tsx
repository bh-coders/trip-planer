import { Modal, Text, View, TouchableOpacity } from 'react-native';
import { modalStyles } from './styles';

const SettingsModal = ({ isVisible, setSettingsModalVisible }: any) => {
  return (
    <Modal
      visible={isVisible}
      onRequestClose={() => setSettingsModalVisible(false)}
      transparent={true} // Ustawienie tła modala na przezroczyste
      animationType="slide" // Typ animacji pojawienia się modala
    >
      <View style={modalStyles.centeredView}>
        <View style={modalStyles.modalView}>
          {/* Zawartość Modala */}
          <Text style={modalStyles.modalText}>Opcje ustawień</Text>

          {/* Przycisk zamknięcia modala */}
          <TouchableOpacity
            style={modalStyles.buttonClose}
            onPress={() => setSettingsModalVisible(false)}>
            <Text style={modalStyles.textStyle}>Zamknij</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
};
export default SettingsModal;
