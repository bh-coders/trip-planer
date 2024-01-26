import { useState } from "react";
import { Button, Modal, Text, TextInput, View } from "react-native";
import { Picker } from '@react-native-picker/picker';


const FiltersModal = ({ visible, onSave, onClose, countries, cities, regions, categories, radiuses }: any) => {

    const [keyword, setKeyword] = useState('');
    const [country, setCountry] = useState('');
    const [city, setCity] = useState('');
    const [region, setRegion] = useState('');
    const [category, setCategory] = useState('');
    const [radius, setRadius] = useState('10');

    const [regionVisible, setRegionVisible] = useState(false);
    const [furtherFiltersVisible, setFurtherFiltersVisible] = useState(false);

    const handleSearch = () => {
        console.log(keyword, country, city, region, category, radius);

        onSave({ keyword, country, city, region, category, radius });
    }

    const handleCounrtySelected = (country) => {
        setRegionVisible(true);
        setCountry(country)        
    }

    const handleRegionSelected = (region) => {
        setFurtherFiltersVisible(true);
        setRegion(region);
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
                        onValueChange={(itemValue) => handleCounrtySelected(itemValue)}
                    >
                        <Picker.Item label="Select Country" value="" />
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
                        <Picker.Item label="Select Region" value="" />
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
                        <Picker.Item label="Select City" value="" />
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
                        <Picker.Item label="Select Category" value="" />
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