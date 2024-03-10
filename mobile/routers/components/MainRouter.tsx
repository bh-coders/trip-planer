import { useContext } from 'react';
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
import { AuthContext } from '../../contexts/AuthContext';
import SubMenuDrawerContent from './DrawnerContent';
import SearchAttractions from '../../components/views/Attractions/Search/Search';
import AddNewAttraction from '../../components/views/Attractions/AddNew/AttractionForm';
import AttractionDetailScreen from '../../components/views/common/AttractionDetail.tsx';
import AddNewReview from '../../components/views/Attractions/Review/AddNew.tsx';
import EditReview from '../../components/views/Attractions/Review/Edit.tsx';

const MainRouter = () => {
  const { userToken } = useContext(AuthContext);
  const Drawer = createDrawerNavigator();
  console.log(userToken);
  return (
    <NavigationContainer>
      <Drawer.Navigator
        initialRouteName="Dashboard"
        drawerContent={(props) => <SubMenuDrawerContent {...props} />}>
        <Drawer.Screen name="Dashboard" component={Dashboard} />
        <Drawer.Screen
          name="Search"
          component={SearchAttractions}
          options={{ drawerItemStyle: { display: 'none' } }}
        />
        <Drawer.Screen
          name="AddNew"
          component={AddNewAttraction}
          options={{ drawerItemStyle: { display: 'none' } }}
        />
        {!userToken && <Drawer.Screen name="Register" component={Register} />}
        {!userToken && <Drawer.Screen name="Sign In" component={SignIn} />}
        {userToken && <Drawer.Screen name="My Account" component={UserDashbard} />}
        <Drawer.Screen
          name="AttractionDetailScreen"
          component={AttractionDetailScreen}
          options={{ drawerItemStyle: { display: 'none' } }}
        />
        <Drawer.Screen
          name="NewReviewScreen"
          component={AddNewReview}
          options={{ drawerItemStyle: { display: 'none' } }}
        />
        <Drawer.Screen
          name="EditReviewScreen"
          component={EditReview}
          options={{ drawerItemStyle: { display: 'none' } }}
        />
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
