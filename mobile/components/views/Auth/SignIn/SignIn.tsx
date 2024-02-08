import { View, Alert } from 'react-native';
import SignInForm from './SignInForm';
import { makePostMessage } from '../api/apiService';
import { storeToken } from '../../../utils/tokenUtils';
import { useContext } from 'react';
import { AuthContext } from '../../../../contexts/AuthContext';

const SignIn = ({ navigation }: any) => {
  const { setUserToken } = useContext(AuthContext);

  const onLogin = async (username: string, password: string) => {
    try {
      const response = await makePostMessage({ username, password }, 'POST', 'login');
      const newToken = response?.access_token;
      if (newToken) {
        await storeToken(newToken);
        setUserToken(newToken);
      }
      navigation.navigate('Dashboard');
    } catch (error) {
      Alert.alert(`Login Error:${error}`);
    }
  };
  return (
    <View>
      <SignInForm onLogin={onLogin} />
    </View>
  );
};

export default SignIn;
