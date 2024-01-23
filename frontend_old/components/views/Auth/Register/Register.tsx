import { View, Text } from 'react-native';
import RegisterForm from './RegisterForm';
import { makePostMessage } from '../api/apiService';
import { storeToken } from '../../../utils/tokenUtils';
const Register = ({ navigation }: any) => {
  const onRegister = async (username: string, password: string, email: string) => {
    try {
      const response = await makePostMessage({ username, password, email }, 'POST', 'register');
      await storeToken(response.token);
      navigation.navigate('Dashboard');
    } catch (error) {
      alert(`Login Error:${error}`);
    }
  };
  return (
    <View>
      <RegisterForm onRegister={onRegister} />
    </View>
  );
};

export default Register;
