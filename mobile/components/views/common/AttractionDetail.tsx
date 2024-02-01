import React from 'react';
import { View, Text, ScrollView, Image, TouchableOpacity } from 'react-native';
import { imagePlaceholder } from './styles';

const AttractionDetailScreen = ({route}) => {
    
    const imagePlaceholders = Array.from({ length: 3 }, (_, index) => (
        <View key={index} style={imagePlaceholder.placeholder} />        
    ));

    return (
        <>
        <ScrollView style={{ height: '100%', backgroundColor: '#fff' }}>
            <View style={{ padding: 16, flexDirection: 'row', alignItems: 'center' }}>
                <View style={{ flex: 3 }}>
                    <Text style={{ fontSize: 24, color: 'black', fontWeight: 'bold' }}>{route.params.attraction['name']}</Text>
                </View>
                <View style={{ flex: 1, alignItems: 'center' }}>
                    <View
                        style={{
                            width: 40,
                            height: 40,
                            backgroundColor: '#D9D9D9',
                            borderRadius: 20,
                            justifyContent: 'center',
                            alignItems: 'center',
                        }}
                    >
                        <Text style={{ color: 'black', fontSize: 15, fontWeight: 'bold' }}>{route.params.attraction['rating']}</Text>
                    </View>
                </View>
            </View>

            <View style={{ padding: 16, flexDirection: 'row', justifyContent: 'space-around' }}>
                <Text style={{ fontSize: 16, color: 'gray' }}>{route.params.attraction['category']}</Text>
                <Text style={{ fontSize: 14, color: 'gray' }}>[1000 views]</Text>
            </View>

            <ScrollView horizontal style={{ height: 200 }}>
                <View style={imagePlaceholder.imageContainer}>{imagePlaceholders}</View>
                {/* <Image source={require('path/to/your/image.jpg')} style={{ width: 300, height: 200 }} /> */}
            </ScrollView>

            <View style={{ flexDirection: 'row', justifyContent: 'space-between', padding: 16 }}>
                <View>
                    <Text style={{ fontSize: 16, color: 'gray' }}>[opening hours]</Text>
                </View>
                <View>
                    <Text style={{ fontSize: 16, color: 'gray' }}>[Price]</Text>
                </View>
            </View>

            <View style={{ padding: 16 }}>
                <Text>{route.params.attraction['description']}</Text>
            </View>
        </ScrollView>

    <View style={{
        position: 'absolute',
        bottom: 10,
        left: 0,
        right: 0,
        flexDirection: 'row',
        justifyContent: 'space-around',
        padding: 16
    }}>
        <TouchableOpacity
            style={{
                width: 120,
                height: 40,
                backgroundColor: '#D5D2D2',
                borderRadius: 20,
                justifyContent: 'center',
                alignItems: 'center',
            }}
        >
            <Text style={{ color: 'black' }}>Add to Route</Text>
        </TouchableOpacity>
        <TouchableOpacity
            style={{
                width: 40,
                height: 40,
                backgroundColor: '#D5D2D2',
                borderRadius: 20,
                justifyContent: 'center',
                alignItems: 'center',
            }}
        >
            <Text style={{ color: 'red' }}>❤️</Text>
        </TouchableOpacity>
    </View>
    </>
    );
};

export default AttractionDetailScreen;
