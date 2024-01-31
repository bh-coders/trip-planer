import { useEffect, useState, useContext } from 'react';
import { Text, View, ScrollView, Image, TouchableOpacity, Modal } from 'react-native';
import { makeGetMessage } from './api/apiService';
import { UserCredentials } from './types';
import { AuthContext } from '../../../contexts/AuthContext';
import { styles } from './styles';
import { removeToken } from '../../utils/tokenUtils';
import AttractionsSlider from './components/AttractionSlider';
import SettingsModal from './components/SettingModal';
const UserDashboard = ({ navigation }: any) => {
  const [settingsModalVisible, setSettingsModalVisible] = useState(false);
  const [userCredentials, setUserCredentials] = useState<UserCredentials | null>(null);
  const { userToken, setUserToken } = useContext(AuthContext);

  const logout = async () => {
    await removeToken();
    setUserToken(null);
  };

  useEffect(() => {
    const fetchUserCredentials = async () => {
      if (userToken) {
        const credentials = await makeGetMessage(userToken);
        setUserCredentials(credentials);
      }
    };
    fetchUserCredentials();
  }, []);
  return (
    <ScrollView style={styles.container}>
      <TouchableOpacity style={styles.settingsButton} onPress={() => setSettingsModalVisible(true)}>
        <Text style={styles.settingsButtonText}>Settings</Text>
      </TouchableOpacity>
      <TouchableOpacity style={styles.logoutButton} onPress={logout}>
        <Text style={styles.settingsButtonText}>Logout</Text>
      </TouchableOpacity>
      <SettingsModal
        isVisible={settingsModalVisible}
        setSettingsModalVisible={setSettingsModalVisible}
        navigation={navigation}
        userToken={userToken}
      />
      <View style={styles.userSection}>
        <Image
          source={{
            uri:
              userCredentials?.avatar ||
              'data:image/jpeg;base64,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',
          }}
          style={styles.avatar}
        />
        {''}
        <Text style={styles.username}>Jan Pawel Ironfist</Text>
        <Text style={styles.email}>kremowka@kremowka.wadowice.pl</Text>
      </View>

      <View style={styles.attractionsSection}>
        <Text style={styles.sectionTitle}>Recently Added Attractions</Text>
        <AttractionsSlider attractions={userCredentials?.attractions} />
      </View>
    </ScrollView>
  );
};
export default UserDashboard;
