import React, { useState, useEffect } from 'react';
import { View, Text, Button, FlatList, TouchableOpacity, Image } from 'react-native';
import FiltersModal from './FiltersModal';
import { attractionsExamples, Attraction } from './api/apiMock';
import AttractionModal from './AttractionModal';
import AttractionTile from '../../common/AttractionTile';
import { styles } from '../../Dashboard/styles';
import { attractionSerchStyles } from './styles';

interface Filters {
  category: string;
  city: string;
  country: string;
  keyword: string;
  radius: string;
  region: string;
}

const AttractionSearchScreen: React.FC = () => {
  const [attractions, setAttractions] = useState<Attraction[]>([]);
  const [attractionDetails, setAttractionDetails] = useState<Attraction | {}>({});
  const [loading, setLoading] = useState(false);
  const [filterModalVisible, setFilterModalVisible] = useState(false);
  const [attractionModalVisible, setAttractionModalVisible] = useState(false);
  const [filters, setFilters] = useState<Filters>({
    category: "",
    city: "",
    country: "",
    keyword: "",
    radius: "10",
    region: ""
  });

  const [radiuses, setRadiuses] = useState<string[]>([]);
  const attractionData = attractionsExamples;

  useEffect(() => {
    const radiusData = ['5', '10', '15'];
    setRadiuses(radiusData);
  }, []);

  useEffect(() => {
    const filteredAttractions = attractionData.filter(attraction => {
      return (
        (filters.category === "" || attraction.category === filters.category) &&
        (filters.city === "" || attraction.city === filters.city) &&
        (filters.country === "" || attraction.country === filters.country) &&
        (filters.keyword === "" || attraction.name.toLowerCase().includes(filters.keyword.toLowerCase())) &&
        (filters.region === "" || attraction.region.toLowerCase().includes(filters.region.toLowerCase()))
      );
    });
    setAttractions(filteredAttractions);
  }, [filters]);

  const handleSetFilters = (filtersProps: Filters) => {
    setFilterModalVisible(false);
    setFilters(filtersProps);
  };

  const handleAttractionClick = (attraction: Attraction) => {
    setAttractionModalVisible(true);
    setAttractionDetails(attraction);

    console.log('Clicked Attraction:', attraction);
  };

  const RightSwipeActions = (item: Attraction) => {
    return (
      <View style={{ alignItems: 'flex-end', flex: 1, marginTop: 40, padding: 10 }} >
        <Button title='Add to favorite' onPress={() => {
          console.log('add to favorite: ', item);
          // swip.close();
          }} />
      </View>
    );
  };

  const LeftSwipeActions = (item: Attraction) => {
    return (
      <View style={{ alignItems: 'flex-start', flex: 1, marginTop: 40, padding: 10 }} >
        <Button title='Add to trip' color='green' onPress={() => console.log('add to trip: ', item)} />
      </View>
    );
  };


  return (
    <>
      <Button title="Filters" onPress={() => setFilterModalVisible(true)} />
      <FiltersModal
        visible={filterModalVisible}
        onClose={() => setFilterModalVisible(false)}
        onSave={handleSetFilters}
        attractionList={attractionData}
        radiuses={radiuses}
      />

      <AttractionModal
        visible={attractionModalVisible}
        attraction={attractionDetails as Attraction}
        onClose={() => setAttractionModalVisible(false)}
      />

      <View style={styles.attractionsGrid}>
        {loading && <Text>Loading...</Text>}

        {!loading && attractions.length === 0 && (
          <View>
            <Image
              source={require('./../../../../resources/images/we_dont_have.png')}
              style={{ width: 200, height: 200, margin: 20, padding: 10 }}
            />
          </View>
        )}

        {!loading && attractions.length > 0 && (
          <FlatList
            style={attractionSerchStyles.attractionsList}
            data={attractions}
            keyExtractor={(item, index) => index.toString()}
            renderItem={({ item: attraction }) => (
              <TouchableOpacity onPress={() => handleAttractionClick(attraction)}>
                <Swipeable
                  renderRightActions={() => RightSwipeActions(attraction)}
                  renderLeftActions={() => LeftSwipeActions(attraction)}
                >
                  <View>
                    <AttractionTile
                      attraction={{
                        place_name: attraction.name,
                        place_description: attraction.description,
                        place_category: attraction.category,
                        place_rating: attraction.rating
                      }}
                    />
                  </View>
                </Swipeable>
              </TouchableOpacity>
            )}
          />
        )}
      </View>
    </>
  );
};

export default AttractionSearchScreen;
