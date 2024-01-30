import React from 'react';

import { View } from 'react-native';
import styles from './Styles';
import Router from './routers/Router';
import Footer from './components/views/common/Footer';
import { AuthProvider } from './contexts/AuthContext';

function App(): React.JSX.Element {
  return (
    <AuthProvider>
      <View style={styles.container}>
        <Router />
        {/* <Footer /> */}
      </View>
    </AuthProvider>
  );
}

export default App;
