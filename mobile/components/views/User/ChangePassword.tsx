import React, { FC } from 'react';
import { View, Alert } from 'react-native';
import ChangePasswordForm from './components/ChangePasswordForm';
import { makeMessageWithBody } from './api/apiService';
import { NavigationProp } from '@react-navigation/native';
type ChangePasswordProps = {
  navigation: NavigationProp<any>;
  userToken: string;
};
const ChangePassword: FC<ChangePasswordProps> = ({ navigation, userToken }) => {
  const onPasswordChange = async (password: string, newPassword: string) => {
    try {
      await makeMessageWithBody({ password, newPassword }, 'change-password', 'PATCH', userToken);

      navigation.navigate('UserDashboard');
    } catch (error) {
      Alert.alert(`Change Password Error: ${error}`);
    }
  };

  return (
    <View>
      <ChangePasswordForm onPasswordChange={onPasswordChange} navigation={navigation} />
    </View>
  );
};

export default ChangePassword;
