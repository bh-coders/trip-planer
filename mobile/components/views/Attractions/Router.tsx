import { useState } from "react";
import {DrawerItem} from '@react-navigation/drawer';
import { View } from "react-native";



const AttractionSubMenu: React.FC<any> = (props) => {
    const [nestedMenuOpen, setNestedMenuOpen] = useState(false);

    return(
        <>
        <DrawerItem
        label="Attractions"
        onPress={() => setNestedMenuOpen(!nestedMenuOpen)}
        focused={nestedMenuOpen}
      />
        <View style={{ marginLeft: 16, display: nestedMenuOpen ? 'flex' : 'none'}}>
          <DrawerItem label="Search attraction" onPress={() => {
            props.navigation.navigate('Search');
            setNestedMenuOpen(false);
          }} />
          <DrawerItem label="Add new attrsction" onPress={() => {
            props.navigation.navigate('AddNew');
            setNestedMenuOpen(false);
          }} />
        </View>
    </>
    );
};

export default AttractionSubMenu;