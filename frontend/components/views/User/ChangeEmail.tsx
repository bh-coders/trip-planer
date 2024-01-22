// ChangeEmail.tsx
import React from 'react';
import { View, Alert } from 'react-native';
import ChangeEmailForm from './components/ChangeEmailForm';
import { makePostMessage } from './api/apiService';

const ChangeEmail = ({ navigation }: any) => {
  const onEmailChange = async (currentEmail: string, newEmail: string, password: string) => {
    try {
      await makePostMessage({ currentEmail, newEmail, password }, 'change-email', 'PATCH');

      navigation.navigate('User');
    } catch (error) {
      Alert.alert('Change Email Error');
    }
  };

  return (
    <View>
      <ChangeEmailForm onEmailChange={onEmailChange} navigation={navigation} />
    </View>
  );
};

export default ChangeEmail;
