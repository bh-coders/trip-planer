import { View, Text } from 'react-native';
import SignInForm from './SignInForm';
import { makePostMessage } from '../api/apiService';
import { storeToken } from '../../../utils/tokenUtils';
const SignIn = ({ navigation }: any) => {
  const onLogin = async (username: string, password: string) => {
    try {
      const response = await makePostMessage({ username, password }, 'login', 'POST');
      await storeToken(response.token);

      navigation.navigate('Dashboard');
    } catch (error) {
      alert(`Login Error:${error}`);
    }
  };
  return (
    <View>
      <SignInForm onLogin={onLogin} />
    </View>
  );
};

export default SignIn;
