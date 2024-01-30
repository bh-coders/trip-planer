import { useEffect, useState, useContext } from 'react';
import { Text, View, ScrollView, Image, TouchableOpacity, Modal } from 'react-native';
import { makeGetMessage } from './api/apiService';
import { UserCredentials } from './types';
import { AuthContext } from '../../../contexts/AuthContext';
import { styles } from './styles';
import AttractionsSlider from './components/AttractionSlider';
import SettingsModal from './components/SettingModal';
const UserDashboard = ({ navigation }: any) => {
  const [settingsModalVisible, setSettingsModalVisible] = useState(false);
  const [userCredentials, setUserCredentials] = useState<UserCredentials | null>(null);
  const { userToken } = useContext(AuthContext);
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
      <SettingsModal
        isVisible={settingsModalVisible}
        setSettingsModalVisible={setSettingsModalVisible}
        navigation={navigation}
        userToken={userToken}
      />
      <View style={styles.userSection}>
        {/* Avatar */}
        <Image source={{ uri: userCredentials?.avatar }} style={styles.avatar} />
        {''}
        <Text style={styles.username}>Username</Text>
        <Text style={styles.email}>Email@Email</Text>
      </View>

      <View style={styles.attractionsSection}>
        <Text style={styles.sectionTitle}>Recently Added Attractions</Text>
        <AttractionsSlider attractions={userCredentials?.attractions} />
      </View>
    </ScrollView>
  );
};
export default UserDashboard;
