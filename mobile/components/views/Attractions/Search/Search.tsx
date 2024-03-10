import React, { useEffect, useState } from 'react';
import { Alert, Button, FlatList, Image, Text, TouchableOpacity, View } from 'react-native';
import FiltersModal from './components/FiltersModal.tsx';
import { attractionsExamples } from '../api/fake/apiMock';
import AttractionTile from '../../common/AttractionTile';
import Swipeable from 'react-native-gesture-handler/Swipeable';
import { styles } from '../../Dashboard/styles';
import { attractionSearchStyles } from './styles';
import { Attraction, Filters, NavigationProps } from '../types';
import { fetchUserAttractions } from '../api/attractionsApi';

const AttractionSearchScreen: React.FC<{ navigation: NavigationProps }> = ({ navigation }) => {
  const [loading, setLoading] = useState(true);
  const [userAttractions, setUserAttractions] = useState<Attraction[]>(attractionsExamples);
  const [attractions, setAttractions] = useState<Attraction[]>([]);
  const [filterModalVisible, setFilterModalVisible] = useState(false);
  const [filters, setFilters] = useState<Filters>({
    category: '',
    city: '',
    country: '',
    keyword: '',
    radius: '10',
    region: '',
  });

  const [radii, setRadii] = useState<string[]>([]);

  useEffect(() => {
    const radiusData = ['5', '10', '15'];
    setRadii(radiusData);
    fetchUserAttractions(1)
      .then((fetchAttractions) => setUserAttractions(fetchAttractions))
      .catch(() => {
        if (userAttractions === attractionsExamples) {
          Alert.alert('Error', 'Failed getting user attractions. Loading demo data');
        } else {
          Alert.alert('Error', 'Failed getting user attractions.');
        }
      })
      .then(() => setLoading(false));
  }, [userAttractions]);

  useEffect(() => {
    const filteredAttractions = userAttractions.filter((attraction) => {
      const matchCategory = filters.category === '' || attraction.category === filters.category;
      const matchCity = filters.city === '' || attraction.city === filters.city;
      const matchCountry = filters.country === '' || attraction.country === filters.country;
      const matchKeyword =
        filters.keyword === '' ||
        attraction.name.toLowerCase().includes(filters.keyword.toLowerCase());
      const matchRegion =
        filters.region === '' ||
        (attraction.region && attraction.region.toLowerCase().includes(filters.region.toLowerCase()));

      return matchCategory && matchCity && matchCountry && matchKeyword && matchRegion;
    });

    setAttractions(filteredAttractions);
  }, [filters, userAttractions]);

  const onSetFilters = (filtersProps: Filters) => {
    setFilterModalVisible(false);
    setFilters(filtersProps);
  };

  const onAttractionClick = (attraction: Attraction) => {
    let attractionId = attraction?.id;
    navigation.navigate('AttractionDetailScreen', { id: attractionId });
    console.log('Clicked Attraction:', attraction);
  };

  const RightSwipeActions = (item: Attraction) => {
    return (
      <View style={{ alignItems: 'flex-end', flex: 1, marginTop: 40, padding: 10 }}>
        <Button
          title="Add to favorite"
          onPress={() => {
            console.log('add to favorite: ', item);
          }}
        />
      </View>
    );
  };

  const LeftSwipeActions = (item: Attraction) => {
    return (
      <View style={{ alignItems: 'flex-start', flex: 1, marginTop: 40, padding: 10 }}>
        <Button
          title="Add to trip"
          color="green"
          onPress={() => console.log('add to trip: ', item)}
        />
      </View>
    );
  };

  return (
    <View>
      <Button title="Filters" onPress={() => setFilterModalVisible(true)} />
      <FiltersModal
        visible={filterModalVisible}
        onSave={onSetFilters}
        attractionList={userAttractions}
        radii={radii}
      />

      <View style={styles.attractionsGrid}>
        {loading && <Text>Loading data</Text>}

        {!loading && attractions?.length === 0 && (
          <View>
            <Image
              source={require('./../../../../resources/images/we_dont_have.png')}
              style={{ width: 200, height: 200, margin: 20, padding: 10 }}
            />
          </View>
        )}

        {!loading && attractions?.length > 0 && (
          <FlatList
            style={attractionSearchStyles.attractionsList}
            data={attractions}
            keyExtractor={(item, index) => index.toString()}
            renderItem={({ item: attraction }) => (
              <TouchableOpacity onPress={() => onAttractionClick(attraction)}>
                <Swipeable
                  renderRightActions={() => RightSwipeActions(attraction)}
                  renderLeftActions={() => LeftSwipeActions(attraction)}>
                  <View>
                    <AttractionTile
                      attraction={{
                        place_name: attraction.name,
                        place_description: attraction.description,
                        place_category: attraction.category,
                        place_rating: attraction.rating.toFixed(1),
                      }}
                    />
                  </View>
                </Swipeable>
              </TouchableOpacity>
            )}
          />
        )}
      </View>
    </View>
  );
};

export default AttractionSearchScreen;
