import React, { useEffect, useState } from "react";
import { Button, Modal, Text, TextInput, View } from "react-native";
import { Picker } from '@react-native-picker/picker';
import { Attraction } from "../types";;

interface FiltersModalProps {
  visible: boolean;
  onSave: (filtersProps: Filters) => void;
  onClose: () => void;
  attractionList: Attraction[];
  radiuses: string[];
}

interface Filters {
  keyword: string;
  country: string;
  city: string;
  region: string;
  category: string;
  radius: string;
}

const FiltersModal: React.FC<FiltersModalProps> = ({ visible, onSave, onClose, attractionList, radiuses }) => {
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

  const countries: string[] = [...new Set(attractionList.map(attraction => attraction?.country as string))];

  const handleSearch = () => {
    onSave({ keyword, country, city, region, category, radius });
  }

  const handleCountrySelected = (selectedCountry: string) => {
    setCountry(selectedCountry);
    if (selectedCountry) {
      setRegionVisible(true);
      const countryRegions = attractionList.filter(attraction => attraction.country === selectedCountry).map(attraction => attraction.region);
      setRegions([...new Set(countryRegions)]);
    } else {
      setRegionVisible(false);
    }
    setRegion('');
    handleRegionSelected('');
  }

  const handleRegionSelected = (selectedRegion: string) => {
    setRegion(selectedRegion);
    if (selectedRegion) {
      setFurtherFiltersVisible(true);
      const regionCities = attractionList.filter(attraction => attraction.region === selectedRegion).map(attraction => attraction.city as string);
      setCities([...new Set(regionCities)]);
      const regionCategories = attractionList.filter(attraction => attraction.region === selectedRegion).map(attraction => attraction.category);
      setCategories([...new Set(regionCategories)]);
    } else {
      setFurtherFiltersVisible(false);
    }
    setCity('');
    setCategory('');
  }


  return (
    <Modal visible={visible} transparent={false} animationType="slide">
      <View style={{ padding: 16 }}>
        <Text>Keyword:</Text>
        <TextInput
          style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 16 }}
          placeholder="Type keyword"
          value={keyword}
          onChangeText={(text) => setKeyword(text)}
        />
      </View>

      <View style={{ flexDirection: 'column', padding: 5 }}>
        <View>
          <Text>Country:</Text>
          <Picker
            selectedValue={country}
            style={{ height: 40, borderColor: 'gray', borderWidth: 1 }}
            onValueChange={(itemValue) => handleCountrySelected(itemValue)}
          >
            <Picker.Item label="All" value="" />
            {countries.map((country, index) => (
              <Picker.Item key={index} label={country} value={country} />
            ))}
          </Picker>
        </View>

        <View>
          <Text>Region:</Text>
          <Picker
            enabled={regionVisible}
            selectedValue={region}
            style={{ height: 40, borderColor: 'gray', borderWidth: 1 }}
            onValueChange={(itemValue) => handleRegionSelected(itemValue)}
          >
            <Picker.Item label="All" value="" />
            {regions.map((region, index) => (
              <Picker.Item key={index} label={region} value={region} />
            ))}
          </Picker>
        </View>

        <View>
          <Text>City:</Text>
          <Picker
            enabled={furtherFiltersVisible}
            selectedValue={city}
            style={{ height: 40, borderColor: 'gray', borderWidth: 1 }}
            onValueChange={(itemValue) => setCity(itemValue)}
          >
            <Picker.Item label="All" value="" />
            {cities.map((city, index) => (
              <Picker.Item key={index} label={city} value={city} />
            ))}
          </Picker>
        </View>

        <View>
          <Text>Category:</Text>
          <Picker
            enabled={furtherFiltersVisible}
            selectedValue={category}
            style={{ height: 40, borderColor: 'gray', borderWidth: 1 }}
            onValueChange={(itemValue) => setCategory(itemValue)}
          >
            <Picker.Item label="All" value="" />
            {categories.map((category, index) => (
              <Picker.Item key={index} label={category} value={category} />
            ))}
          </Picker>
        </View>

        <View>
          <Text>Radius:</Text>
          <Picker
            enabled={furtherFiltersVisible}
            selectedValue={radius}
            style={{ height: 40, borderColor: 'gray', borderWidth: 1 }}
            onValueChange={(itemValue) => setRadius(itemValue)}
          >
            <Picker.Item label="Select Category" value="" />
            {radiuses.map((radius, index) => (
              <Picker.Item key={index} label={radius + " km"} value={radius} />
            ))}
          </Picker>
        </View>
      </View>

      <View style={{ padding: 20, borderRadius: 10, marginTop: 20, alignItems: 'flex-end' }}>
        <Button title="Search Attractions" onPress={handleSearch} />
      </View>
    </Modal>
  );
}

export default FiltersModal;
