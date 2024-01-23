import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { View } from 'react-native';
import styles from './Styles';
import Dashboard from './components/views/Dashboard/Dashboard';
import Register from './components/views/Auth/Register/Register';
import SignIn from './components/views/Auth/SignIn/SignIn';
import User from './components/views/User/User';
import Footer from './components/views/common/Footer';
import { AuthProvider } from './contexts/AuthContext';
import ChangePassword from './components/views/User/ChangePassword';
import ChangeEmail from './components/views/User/ChangeEmail';
import DeleteAccount from './components/views/User/DeleteUser';
const Drawer = createDrawerNavigator();

function App(): React.JSX.Element {
  return (
    <AuthProvider>
      <View style={styles.container}>
        <NavigationContainer>
          <Drawer.Navigator initialRouteName="Dashboard">
            <Drawer.Screen name="Dashboard" component={Dashboard} />
            <Drawer.Screen name="Register" component={Register} />
            <Drawer.Screen name="Sign In" component={SignIn} />
            <Drawer.Screen name="User" component={User} />
            <Drawer.Screen
              name="Change Password"
              component={ChangePassword}
              options={{ drawerItemStyle: { display: 'none' } }}
            />
            <Drawer.Screen
              name="Change Email"
              component={ChangeEmail}
              options={{ drawerItemStyle: { display: 'none' } }}
            />
            <Drawer.Screen
              name="Delete Account"
              component={DeleteAccount}
              options={{ drawerItemStyle: { display: 'none' } }}
            />
          </Drawer.Navigator>
        </NavigationContainer>
        <Footer />
      </View>
    </AuthProvider>
  );
}

export default App;
