import React, { useState } from 'react';
import { DrawerContentScrollView, DrawerItem, DrawerItemList } from '@react-navigation/drawer';
import { View } from 'react-native';
import AttractionSubMenu from '../../components/views/Attractions/Router';
import TestSubMenu from '../../components/views/test/Router';

const CustomDrawerContent: React.FC<any> = (props) => {


  return (
    <DrawerContentScrollView {...props}>
      <DrawerItemList {...props} />
      <AttractionSubMenu {...props} />
      <TestSubMenu {...props} />
    </DrawerContentScrollView>
  );
};

export default CustomDrawerContent;
