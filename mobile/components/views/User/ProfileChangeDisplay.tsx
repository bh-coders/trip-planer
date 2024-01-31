import React, { useMemo, useRef } from 'react';
import { View, Text, Alert } from 'react-native';
import ChangeCredentialsProfileForm from './components/ChangeCredentialsProfileForm';
import { makeMessageWithBody } from './api/apiService';
const ProfileChangeDisplay = ({ navigation, userToken }: any) => {
  const onProfileCredentialsChange = async (profile: any) => {
    try {
      await makeMessageWithBody(profile, 'change-profile-credentials', 'PATCH', userToken);
    } catch {
      Alert.alert('Error');
    }
  };
  return (
    <View>
      <ChangeCredentialsProfileForm
        onProfileCredentialsChange={onProfileCredentialsChange}
        navigation={navigation}
      />
    </View>
  );
};

export default ProfileChangeDisplay;
