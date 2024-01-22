import React, { useState, FC } from 'react';
import { View, TextInput, Button } from 'react-native';
import { formStyles } from '../styles';

type ChangeEmailFormProps = {
  onEmailChange: (newEmail: string, oldEmail: string, password: string) => void;
  navigation: any;
};

const ChangeEmailForm: FC<ChangeEmailFormProps> = ({ onEmailChange, navigation }) => {
  const [newEmail, setNewEmail] = useState('');
  const [oldEmail, setOldEmail] = useState('');
  const [password, setPassword] = useState('');

  return (
    <View style={formStyles.container}>
      <TextInput
        style={formStyles.input}
        placeholder="New Email"
        value={newEmail}
        onChangeText={setNewEmail}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      <TextInput
        style={formStyles.input}
        placeholder="Old Email"
        value={oldEmail}
        onChangeText={setOldEmail}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      <TextInput
        style={formStyles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <View style={{ marginBottom: 10 }}>
        <Button title="Update Email" onPress={() => onEmailChange(newEmail, oldEmail, password)} />
      </View>
      <View>
        <Button title="Back To User Panel" onPress={() => navigation.navigate('User')} />
      </View>
    </View>
  );
};

export default ChangeEmailForm;
