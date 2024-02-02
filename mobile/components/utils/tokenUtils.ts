import AsyncStorage from '@react-native-async-storage/async-storage';

export const storeToken = async (userToken: string) => {
  try {
    await AsyncStorage.setItem('userToken', userToken);
  } catch (error) {
    console.error(`error: ${error}`);
  }
};

export const getToken = async () => {
  try {
    const userToken = await AsyncStorage.getItem('userToken');
    return userToken;
  } catch (error) {
    console.error(`error: ${error}`);
  }
};

export const removeToken = async () => {
  try {
    await AsyncStorage.removeItem('userToken');
  } catch (error) {
    console.error(`error: ${error}`);
  }
};
