import React, { useMemo, useRef } from 'react';
import { View, Text } from 'react-native';
import { Picker } from '@react-native-picker/picker';
import BottomSheet, { BottomSheetScrollView } from '@gorhom/bottom-sheet';
import { styles } from '../styles';
import AttractionTile from '../../common/AttractionTile';
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
const getPlaceholderAttractions = () => {
  return Array.from({ length: 8 }, (_, index) => ({
    place_name: `Nazwa Atrakcji ${index + 1}`,
    place_category: `Category ${index + 1}`,
    place_rating: 4.5 + index / 100,
    place_description: `Lorem Ipsum Opis Kwiatuh ${index + 1} Lorem Ipsum Opis Kwiatuh ${
      index + 1
    }Lorem Ipsum Opis Kwiatuh ${index + 1} Lorem Ipsum Opis Kwiatuh ${
      index + 1
    }Lorem Ipsum Opis Kwiatuh ${index + 1}`,
    image_url:
      'https://media.cntraveler.com/photos/58de89946c3567139f9b6cca/16:9/w_1920,c_limit/GettyImages-468366251.jpg',
  }));
};

const BottomPanel: React.FC<BottomPanelProps> = ({
  isVisible,
  searchText,
  onCategoryChange,
  attractions,
  selectedCategory,
}) => {
  const sheetRef = useRef<BottomSheet>(null);
  const snapPoints = useMemo(() => ['5%', '80%'], []);
  const placeholderAttractions = useMemo(() => getPlaceholderAttractions(), []);

  return (
    <BottomSheet ref={sheetRef} index={isVisible ? 1 : 0} snapPoints={snapPoints}>
      <View style={{ padding: 10 }}>
        <View style={styles.searchSection}>
          <Text>{searchText}</Text>

          <Picker
            style={styles.picker}
            selectedValue={selectedCategory}
            onValueChange={(itemValue) => onCategoryChange(itemValue)}>
            <Picker.Item label="Culture" value="culture" />
            <Picker.Item label="Food" value="gastronomy" />
          </Picker>
        </View>
      </View>
      <BottomSheetScrollView>
        <View style={styles.attractionsGrid}>
          {(attractions && attractions.length > 0 ? attractions : placeholderAttractions).map(
            (attraction, index) => (
              <AttractionTile key={index} attraction={attraction} />
            )
          )}
        </View>
      </BottomSheetScrollView>
    </BottomSheet>
  );
};

export default BottomPanel;
