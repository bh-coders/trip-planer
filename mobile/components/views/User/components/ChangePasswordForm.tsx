import React, { useState, FC } from 'react';
import { View, TextInput, Button, Alert } from 'react-native';
import { formStyles } from '../styles';
import { NavigationProp } from '@react-navigation/native';
type ChangePasswordProps = {
  onPasswordChange: (password: string, newPassword: string) => Promise<void>;
  navigation: NavigationProp<any>;
};
const PasswordChangeForm: FC<ChangePasswordProps> = ({ onPasswordChange, navigation }) => {
  const [newPassword, setNewPassword] = useState('');
  const [reNewPassword, setReNewPassword] = useState('');
  const [oldPassword, setOldPassword] = useState('');
  const handleSubmit = () => {
    if (newPassword !== reNewPassword) {
      Alert.alert('New Passwords does not match');
      return;
    }
    onPasswordChange(newPassword, oldPassword);
  };

  return (
    <View style={formStyles.container}>
      <TextInput
        style={formStyles.input}
        placeholder="New Password"
        value={newPassword}
        onChangeText={setNewPassword}
      />
      <TextInput
        style={formStyles.input}
        placeholder="Confirm Password"
        value={reNewPassword}
        onChangeText={setReNewPassword}
        secureTextEntry
      />
      <TextInput
        style={formStyles.input}
        placeholder="Actual Password"
        value={oldPassword}
        onChangeText={setOldPassword}
        secureTextEntry
      />
      <View style={{ marginBottom: 10 }}>
        <Button title="Change Password" onPress={handleSubmit} />
      </View>
      <View>
        <Button title="Back To User Panel" onPress={() => navigation.navigate('My Account')} />
      </View>
    </View>
  );
};

export default PasswordChangeForm;
