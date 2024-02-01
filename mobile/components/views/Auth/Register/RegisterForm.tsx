import React, { useState, FC } from 'react';
import { View, TextInput, Button, Alert } from 'react-native';
import { styles } from '../styles';
import { RegisterProps } from '../types';
type RegisterFormProps = {
  onRegister: (body: RegisterProps) => void;
};
const RegisterForm: FC<RegisterFormProps> = ({ onRegister }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [rePassword, setRePassword] = useState('');

  const [email, setEmail] = useState('');

  const handleSubmit = () => {
    if (password !== rePassword) {
      Alert.alert('Password does not match');
      return;
    }
    onRegister({
      username: username,
      password: password,
      email: email,
      rewrite_password: rePassword,
    });
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput style={styles.input} placeholder="Email" value={email} onChangeText={setEmail} />
      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
      />
      <TextInput
        style={styles.input}
        placeholder="Confirm Password"
        value={rePassword}
        onChangeText={setRePassword}
        secureTextEntry
      />
      <Button title="Register" onPress={handleSubmit} />
    </View>
  );
};

export default RegisterForm;
