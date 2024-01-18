import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import { Platform, StyleSheet, Text, View} from 'react-native';

function App() {
  return (
    <>
      <img src={viteLogo} className="logo" alt="Vite logo" />
      <View>
        <Text style={styles.whiteText}>Hello World! Your platform is {Platform.OS}</Text>
      </View>
      <img src={reactLogo} className="logo" alt="React logo" />
    </>
  );
}

const styles = StyleSheet.create({
  whiteText: {
    color: 'white',
  },
});

export default App;
