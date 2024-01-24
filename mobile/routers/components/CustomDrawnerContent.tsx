import React, { useState } from 'react';
import { DrawerContentScrollView, DrawerItem, DrawerItemList } from '@react-navigation/drawer';
import { View } from 'react-native';

const CustomDrawerContent: React.FC<any> = (props) => {
  const [nestedMenuOpen, setNestedMenuOpen] = useState(false);

  return (
    <DrawerContentScrollView {...props}>
      <DrawerItemList {...props} />
      <DrawerItem
        label="Attractions"
        onPress={() => setNestedMenuOpen(!nestedMenuOpen)}
        focused={nestedMenuOpen}
      />
      {nestedMenuOpen && (
        <View style={{ marginLeft: 16 }}>
          <DrawerItem label="Search attraction" onPress={() => {
            props.navigation.navigate('Search');
            setNestedMenuOpen(false);
          }} />
          <DrawerItem label="Add new attrsction" onPress={() => {
            props.navigation.navigate('AddNew');
            setNestedMenuOpen(false);
          }} />
        </View>
      )}
    </DrawerContentScrollView>
  );
};

export default CustomDrawerContent;
