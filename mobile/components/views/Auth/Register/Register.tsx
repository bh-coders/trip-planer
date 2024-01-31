import { View, Alert } from 'react-native';
import RegisterForm from './RegisterForm';
import { makePostMessage } from '../api/apiService';
import { storeToken } from '../../../utils/tokenUtils';
import { RegisterProps } from '../types';

const Register = ({ navigation }: any) => {
  const onRegister = async (body: RegisterProps) => {
    try {
      const response = await makePostMessage(body, 'POST', 'register');
      await storeToken(response.token);
      navigation.navigate('Dashboard');
    } catch (error) {
      Alert.alert(`Login Error:${error}`);
    }
  };
  return (
    <View>
      <RegisterForm onRegister={onRegister} />
    </View>
  );
};

export default Register;
