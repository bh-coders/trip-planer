import React from 'react';
import { View, Text, Image } from 'react-native';
import { reviewTile } from '../../../styles';
import { Opinion } from '../../../../Attractions/types';

const AttractionTile = ({ opinion }: any) => {

    return (
        <>
            <View style={reviewTile.reviewTile}>
                <Text style={reviewTile.author}>Author: {opinion.author}</Text>
                <Text style={reviewTile.title}>{opinion.title}</Text>
                <Text style={reviewTile.rate}>{opinion.rating}</Text>
            </View>
        </>
    );
};

export default AttractionTile;