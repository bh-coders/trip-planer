import React, { useMemo, useRef } from 'react';
import { View, Text, TextInput } from 'react-native';
import { Picker } from '@react-native-picker/picker';
import BottomSheet, { BottomSheetScrollView } from '@gorhom/bottom-sheet';
import { styles } from '../styles';
interface Attraction {
  place_name: string;
}

interface BottomPanelProps {
  isVisible: boolean;
  searchText: string;
  onCategoryChange: (category: string) => void;
  attractions: Attraction[];
  selectedCategory: any;
}

const BottomPanel: React.FC<BottomPanelProps> = ({
  isVisible,
  searchText,
  onCategoryChange,
  attractions,
  selectedCategory,
}) => {
  const sheetRef = useRef<BottomSheet>(null);
  const snapPoints = useMemo(() => ['5%', '80%'], []);

  return (
    <BottomSheet ref={sheetRef} index={isVisible ? 1 : 0} snapPoints={snapPoints}>
      <View style={{ padding: 10 }}>
        <View style={styles.searchSection}>
          <Text>Search for: {searchText}</Text>

          <Picker
            style={styles.picker}
            selectedValue={selectedCategory}
            onValueChange={(itemValue) => onCategoryChange(itemValue)}>
            <Picker.Item label="Restauracje" value="restauracja" />
            <Picker.Item label="Obiekty sportowe" value="sport" />
          </Picker>
        </View>
      </View>
      <BottomSheetScrollView>
        <View style={styles.attractionsGrid}>
          {attractions.map((attraction, index) => (
            <View key={index} style={styles.attractionTile}>
              <Text>{attraction.place_name}</Text>
            </View>
          ))}
        </View>
      </BottomSheetScrollView>
    </BottomSheet>
  );
};

export default BottomPanel;
