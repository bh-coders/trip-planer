import React, { useState } from 'react';
import { Button, Modal, Text, TextInput, View } from 'react-native';
import { Picker } from '@react-native-picker/picker';
import { Attraction } from '../../types.ts';
import { filterModal } from '../styles.ts';

interface FiltersModalProps {
  visible: boolean;
  onSave: (filtersProps: Filters) => void;
  attractionList: Attraction[];
  radii: string[];
}

interface Filters {
  keyword: string;
  country: string;
  city: string;
  region: string;
  category: string;
  radius: string;
}

const FiltersModal: React.FC<FiltersModalProps> = ({ visible, onSave, attractionList, radii }) => {
  const [keyword, setKeyword] = useState('');
  const [country, setCountry] = useState('');
  const [cities, setCities] = useState<string[]>([]);
  const [city, setCity] = useState('');
  const [regions, setRegions] = useState<string[]>([]);
  const [region, setRegion] = useState('');
  const [categories, setCategories] = useState<string[]>([]);
  const [category, setCategory] = useState('');
  const [radius, setRadius] = useState('10');
  const [regionVisible, setRegionVisible] = useState(false);
  const [furtherFiltersVisible, setFurtherFiltersVisible] = useState(false);

  const countries: string[] = [
    ...new Set(attractionList.map((attraction) => attraction?.country as string)),
  ];

  const onSearch = () => {
    onSave({ keyword, country, city, region, category, radius });
  };

  const onCountrySelected = (selectedCountry: string) => {
    setCountry(selectedCountry);
    if (selectedCountry) {
      setRegionVisible(true);
      const countryRegions = attractionList
        .filter((attraction) => attraction.country === selectedCountry)
        .map((attraction) => attraction.region);
      setRegions([...new Set(countryRegions)]);
    } else {
      setRegionVisible(false);
    }
    setRegion('');
    onRegionSelected('');
  };

  const onRegionSelected = (selectedRegion: string) => {
    setRegion(selectedRegion);
    if (selectedRegion) {
      setFurtherFiltersVisible(true);
      const regionCities = attractionList
        .filter((attraction) => attraction.region === selectedRegion)
        .map((attraction) => attraction.city as string);
      setCities([...new Set(regionCities)]);
      const regionCategories = attractionList
        .filter((attraction) => attraction.region === selectedRegion)
        .map((attraction) => attraction.category);
      setCategories([...new Set(regionCategories)]);
    } else {
      setFurtherFiltersVisible(false);
    }
    setCity('');
    setCategory('');
  };

  return (
    <Modal visible={visible} transparent={false} animationType="slide">
      <View style={filterModal.keywordContainer}>
        <Text>Keyword:</Text>
        <TextInput
          style={filterModal.keywordInput}
          placeholder="Type keyword"
          value={keyword}
          onChangeText={(text) => setKeyword(text)}
        />
      </View>

      <View style={filterModal.pickerContainer}>
        <View>
          <Text>Country:</Text>
          <Picker
            selectedValue={country}
            style={filterModal.picker}
            onValueChange={(itemValue) => onCountrySelected(itemValue)}>
            <Picker.Item label="All" value="" />
            {countries.map((countryData, index) => (
              <Picker.Item key={index} label={countryData} value={countryData} />
            ))}
          </Picker>
        </View>

        <View>
          <Text>Region:</Text>
          <Picker
            enabled={regionVisible}
            selectedValue={region}
            style={filterModal.picker}
            onValueChange={(itemValue) => onRegionSelected(itemValue)}>
            <Picker.Item label="All" value="" />
            {regions.map((regionData, index) => (
              <Picker.Item key={index} label={regionData} value={regionData} />
            ))}
          </Picker>
        </View>

        <View>
          <Text>City:</Text>
          <Picker
            enabled={furtherFiltersVisible}
            selectedValue={city}
            style={filterModal.picker}
            onValueChange={(itemValue) => setCity(itemValue)}>
            <Picker.Item label="All" value="" />
            {cities.map((cityData, index) => (
              <Picker.Item key={index} label={cityData} value={cityData} />
            ))}
          </Picker>
        </View>

        <View>
          <Text>Category:</Text>
          <Picker
            enabled={furtherFiltersVisible}
            selectedValue={category}
            style={filterModal.picker}
            onValueChange={(itemValue) => setCategory(itemValue)}>
            <Picker.Item label="All" value="" />
            {categories.map((categoryData, index) => (
              <Picker.Item key={index} label={categoryData} value={categoryData} />
            ))}
          </Picker>
        </View>

        <View>
          <Text>Radius:</Text>
          <Picker
            enabled={furtherFiltersVisible}
            selectedValue={radius}
            style={filterModal.picker}
            onValueChange={(itemValue) => setRadius(itemValue)}>
            <Picker.Item label="Select Category" value="" />
            {radii.map((radiusData, index) => (
              <Picker.Item key={index} label={radiusData + ' km'} value={radiusData} />
            ))}
          </Picker>
        </View>
      </View>

      <View style={filterModal.button}>
        <Button title="Search Attractions" onPress={onSearch} />
      </View>
    </Modal>
  );
};

export default FiltersModal;
