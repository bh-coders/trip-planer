import { useState } from "react";
import {DrawerItem} from '@react-navigation/drawer';
import { View } from "react-native";



const TestSubMenu: React.FC<any> = (props) => {
    const [nestedMenuOpen, setNestedMenuOpen] = useState(false);

    return(
        <>
        <DrawerItem
        label="test"
        onPress={() => setNestedMenuOpen(!nestedMenuOpen)}
        focused={nestedMenuOpen}
      />
      <View style={{ marginLeft: 16, display: nestedMenuOpen ? 'flex' : 'none'} }>
          <DrawerItem label="nestedTest1" onPress={() => {
            setNestedMenuOpen(false);
          }} />
          <DrawerItem label="nestedTest2" onPress={() => {
            setNestedMenuOpen(false);
          }} />
        </View>
    </>
    );
};

export default TestSubMenu;