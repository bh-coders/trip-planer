import React, { useState } from "react";
import {DrawerItem, DrawerNavigationProp} from '@react-navigation/drawer';
import { View } from "react-native";

type DrawerParamList = {
  Search: any;
  AddNew: undefined;
};

type AttractionSubMenuProps = {
  navigation: DrawerNavigationProp<DrawerParamList>;
};

const AttractionSubMenu: React.FC<AttractionSubMenuProps> = (props) =>{
    const [nestedMenuOpen, setNestedMenuOpen] = useState(false);
    const navigation = props.navigation;

    return(
        <>
        <DrawerItem
        label="Attractions"
        onPress={() => setNestedMenuOpen(!nestedMenuOpen)}
        focused={nestedMenuOpen}
      />
        <View style={{ marginLeft: 16, display: nestedMenuOpen ? 'flex' : 'none'}}>
          <DrawerItem label="Search attraction" onPress={() => {
            navigation.navigate('Search', navigation);
            setNestedMenuOpen(false);
          }} />
          <DrawerItem label="Add new attrsction" onPress={() => {
            navigation.navigate('AddNew');
            setNestedMenuOpen(false);
          }} />
        </View>
    </>
    );
};

export default AttractionSubMenu;