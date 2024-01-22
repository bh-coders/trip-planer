import React, { useState, FC } from 'react';
import { View, TextInput, Button } from 'react-native';
import { styles } from '../styles';
type SignInFormProps = {
  onLogin: (username: string, password: string) => void;
};
const SignInForm: FC<SignInFormProps> = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <Button title="Login" onPress={() => onLogin(username, password)} />
    </View>
  );
};

export default SignInForm;
