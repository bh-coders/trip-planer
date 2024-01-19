import { API_TOKEN } from '@env';
import { StatusBar } from 'expo-status-bar';
import { Text, View } from 'react-native';

import styles from './Styles';

export default function App() {
  return (
    <View style={styles.App}>
      <Text>Open up App.tsx to start working on your app! {API_TOKEN}</Text>
      <Text>Some Text</Text>
      <StatusBar style="auto" />
    </View>
  );
}
