import React from 'react';
import { View } from 'react-native';
import ChangePasswordForm from './components/ChangePasswordForm';
import { makePostMessage } from './api/apiService';

const ChangePassword = ({ navigation }: any) => {
  const onPasswordChange = async (password: string, newPassword: string) => {
    try {
      await makePostMessage({ password, newPassword }, 'change-password', 'PATCH');

      navigation.navigate('User');
    } catch (error) {
      alert(`Change Password Error: ${error}`);
    }
  };

  return (
    <View>
      <ChangePasswordForm onPasswordChange={onPasswordChange} navigation={navigation} />
    </View>
  );
};

export default ChangePassword;
