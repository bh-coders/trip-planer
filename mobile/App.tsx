import React from 'react';

import { View } from 'react-native';
import styles from './Styles';
import Router from './routers/Router';
import { AuthProvider } from './contexts/AuthContext';

function App(): React.JSX.Element {
  return (
    <AuthProvider>
      <View style={styles.container}>
        <Router />
      </View>
    </AuthProvider>
  );
}

export default App;
