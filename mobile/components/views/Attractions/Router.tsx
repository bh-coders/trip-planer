import React, { useState } from 'react';
import { DrawerItem, DrawerNavigationProp } from '@react-navigation/drawer';
import { View } from 'react-native';

type DrawerParamList = {
  Search: any;
  AddNew: any;
};

type AttractionSubMenuProps = {
  navigation: DrawerNavigationProp<DrawerParamList>;
};

const AttractionSubMenu: React.FC<AttractionSubMenuProps> = (props) => {
  const [nestedMenuToggle, setNestedMenuToggle] = useState(false);
  const navigation = props.navigation;

  return (
    <>
      <DrawerItem
        label="Attractions"
        onPress={() => setNestedMenuToggle(!nestedMenuToggle)}
        focused={nestedMenuToggle}
      />
      <View style={{ marginLeft: 16, display: nestedMenuToggle ? 'flex' : 'none' }}>
        <DrawerItem
          label="Search attraction"
          onPress={() => {
            navigation.navigate('Search');
            setNestedMenuToggle(false);
          }}
        />
        <DrawerItem
          label="Add new attrsction"
          onPress={() => {
            navigation.navigate('AddNew');
            setNestedMenuToggle(false);
          }}
        />
      </View>
    </>
  );
};

export default AttractionSubMenu;
