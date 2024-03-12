import React from 'react';
import { DrawerContentScrollView, DrawerItemList } from '@react-navigation/drawer';
import AttractionSubMenu from '../../components/views/Attractions/Router';
import TestSubMenu from '../../components/views/test/Router';

//Here, instead of any, you need to create an interface, but I don't know how yet
const SubMenuDrawerContent: React.FC<any> = (props) => {
  return (
    <DrawerContentScrollView {...props}>
      <DrawerItemList {...props} />
      <AttractionSubMenu {...props} />
      <TestSubMenu {...props} />
    </DrawerContentScrollView>
  );
};

export default SubMenuDrawerContent;
