import React, { useState, useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { getToken } from './components/utils/tokenUtils';
import Dashboard from './components/views/Dashboard/Dashboard';
import Auth from './components/views/Auth/Auth';
import User from './components/views/User/User';

const Drawer = createDrawerNavigator();

function App(): React.JSX.Element {
  const [userToken, setUserToken] = useState<string | null>(null);

  useEffect(() => {
    const fetchToken = async () => {
      const token = await getToken();
      setUserToken(token);
    };
    fetchToken();
  }, []);
  return (
    <NavigationContainer>
      <Drawer.Navigator initialRouteName="Dashboard">
        <Drawer.Screen name="Dashboard" component={Dashboard} />
        {!userToken && <Drawer.Screen name="Register" component={Auth} />}
        {!userToken && <Drawer.Screen name="Login" component={Auth} />}
        {userToken && <Drawer.Screen name="User" component={User} />}
      </Drawer.Navigator>
    </NavigationContainer>
  );
}

export default App;
