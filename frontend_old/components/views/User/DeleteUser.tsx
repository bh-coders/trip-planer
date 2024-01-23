import React, { FC } from 'react';
import { View, TouchableOpacity, Text } from 'react-native';
import { makeDeleteMessage } from './api/apiService';
import { NavigationProp } from '@react-navigation/native';
import { modalStyles } from './styles';
type DeleteAccountProps = {
  navigation: NavigationProp<any>;
  userToken: string;
};
const DeleteAccount: FC<DeleteAccountProps> = ({ navigation, userToken }) => {
  const onDeleteAccount = async () => {
    try {
      await makeDeleteMessage('delete-user', userToken);

      navigation.navigate('Dashboard');
    } catch (error) {
      alert(`Change Password Error: ${error}`);
    }
  };

  return (
    <View>
      <TouchableOpacity style={modalStyles.settingsButton} onPress={onDeleteAccount}>
        <Text style={modalStyles.textStyle}>Yes</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={modalStyles.settingsButton}
        onPress={() => navigation.navigate('Dashboard')}>
        <Text style={modalStyles.textStyle}>No</Text>
      </TouchableOpacity>
    </View>
  );
};

export default DeleteAccount;
