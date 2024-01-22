// ChangeEmail.tsx
import React, { FC } from 'react';
import { View, Alert } from 'react-native';
import ChangeEmailForm from './components/ChangeEmailForm';
import { makePostMessage } from './api/apiService';
import { NavigationProp } from '@react-navigation/native';

type ChangeEmailProps = {
  navigation: NavigationProp<any>;
  userToken: string;
};
const ChangeEmail: FC<ChangeEmailProps> = ({ navigation, userToken }: any) => {
  const onEmailChange = async (currentEmail: string, newEmail: string, password: string) => {
    try {
      await makePostMessage(
        { currentEmail, newEmail, password },
        'change-email',
        'PATCH',
        userToken,
      );

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
