import { API_TOKEN } from '@env';
import { StatusBar } from 'expo-status-bar';
import { Text, View, Platform } from 'react-native';

import styles from './Styles';

if (Platform.OS === 'ios') {
  console.log('Hello on iOS');
} else if (Platform.OS === 'android') {
  console.log('Hello on Android');
} else {
  console.log('Hello on web');
}

export default function App() {
  if (Platform.OS === 'ios' || Platform.OS === 'android') {
    return (
      <View style={styles.App}>
        <Text>Open up App.tsx to start working on your app! {API_TOKEN}</Text>
        <Text>ZZZZZZ</Text>
        <StatusBar style="auto" />
      </View>
    );
  } else {
    return (
      <div style={styles.App}>
        <p>Open up App.tsx to start working on your app! {API_TOKEN}</p>
        <p>RRRRRRR</p>
      </div>
    );
  }
}
