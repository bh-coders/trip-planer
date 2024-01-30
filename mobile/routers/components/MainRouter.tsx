import Dashboard from '../../components/views/Dashboard/Dashboard';
import Register from '../../components/views/Auth/Register/Register';
import SignIn from '../../components/views/Auth/SignIn/SignIn';
import UserDashbard from '../../components/views/User/UserDashboard';
import ChangePassword from '../../components/views/User/ChangePassword';
import ChangeEmail from '../../components/views/User/ChangeEmail';
import DeleteAccount from '../../components/views/User/DeleteUser';
import ProfileChangeDisplay from '../../components/views/User/ProfileChangeDisplay';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
const Drawer = createDrawerNavigator();
const MainRouter = () => {
  return (
    <NavigationContainer>
      <Drawer.Navigator initialRouteName="Dashboard">
        <Drawer.Screen name="Dashboard" component={Dashboard} />
        <Drawer.Screen name="Register" component={Register} />
        <Drawer.Screen name="Sign In" component={SignIn} />
        <Drawer.Screen name="My Account" component={UserDashbard} />
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
        <Drawer.Screen
          name="Change Profil Informations"
          component={ProfileChangeDisplay}
          options={{ drawerItemStyle: { display: 'none' } }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  );
};
export default MainRouter;
