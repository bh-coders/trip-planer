import React, { useState, useEffect } from 'react';
import { View, Text, Button, FlatList, TouchableOpacity } from 'react-native';
import FiltersModal from './FiltersModal';
import { attractionsExamples } from './api/apiMock';
import AttractionModal from './AttractionModal';

const AttractionSearchScreen = () => {
  const [attractions, setAttractions] = useState([]);
  const [attractionDetails, setAttractionDetails] = useState({});
  const [loading, setLoading] = useState(false);
  const [modalVisible, setModalVisible] = useState(false);
  const [attractionModalVisible, setAttractionModalVisible] = useState(false);
  const [filters, setFilters] = useState({});

  const [countries, setCountries] = useState([]);
  const [cities, setCities] = useState([]);
  const [regions, setRegions] = useState([]);
  const [categories, setCategories] = useState([]);
  const attractionData = attractionsExamples;

  useEffect(() => {
   
    const countriesData = ['Poland', 'Germany', 'France'];
    const citiesData = ['Warsaw', 'Berlin', 'Paris'];
    const regionsData = ['Mazovia', 'Brandenburg', 'Île-de-France'];
    const categoriesData = ['Park', 'Museum', 'Historical Site'];

    setCountries(countriesData);
    setCities(citiesData);
    setRegions(regionsData);
    setCategories(categoriesData);

  }, []);

  useEffect(() => {
    console.log(filters);

    if (filters.country != "") {
      const filtredAttractions = attractionData.filter(attraction => {
        return (
          (filters.category === "" || attraction.category === filters.category) &&
          (filters.city === "" || attraction.city === filters.city) &&
          (filters.country === "" || attraction.country === filters.country) &&
          (filters.keyword === "" || attraction.name.toLowerCase().includes(filters.keyword.toLowerCase())) &&
          (filters.region === "" || attraction.region === filters.region)
        );
      });

      setAttractions(filtredAttractions);
    } else {
      setAttractions([]);
    }
  }, [filters])

  const handleSetFilters = (filtersProps: any) => {
    setModalVisible(false);
    setFilters(filtersProps);
  };

  const handleAttractionClick = (attraction) => {
    setAttractionModalVisible(true);
    setAttractionDetails(attraction);

    console.log('Clicked Attraction:', attraction);
  };

  return (
    <>
      <Button title="Filters" onPress={() => setModalVisible(true)} />
      <FiltersModal
        visible={modalVisible}
        onClose={() => setModalVisible(false)}
        onSave={handleSetFilters}
        countries={countries}
        cities={cities}
        regions={regions}
        categories={categories}
      />

      <AttractionModal
        visible={attractionModalVisible}
        attraction={attractionDetails}
        onClose={() => setAttractionModalVisible(false)}
      />

      <View>
        <View style={{ marginTop: 20 }}>
          {loading && <Text>Loading...</Text>}

          {!loading && attractions.length === 0 && <Text>Specify search details</Text>}

          {!loading && attractions.length > 0 && (
            <FlatList
              data={attractions}
              keyExtractor={(item, index) => index.toString()}
              renderItem={({ item }) => (
                <TouchableOpacity onPress={() => handleAttractionClick(item)}>
                  <View style={{ borderBottomWidth: 1, borderColor: 'gray', marginBottom: 10, padding: 10 }}>
                    <Text>{item.name}</Text>
                    <Text>{item.country}, {item.city}, {item.region}</Text>
                    <Text>{item.category}</Text>
                  </View>
                </TouchableOpacity>
              )}
            />
          )}
        </View>
      </View>
    </>
  );
};

export default AttractionSearchScreen;
