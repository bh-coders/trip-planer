import React from 'react';
import { Text, TextInput, View } from 'react-native';
import { styles } from '../styles';
import { TouchableOpacity } from 'react-native-gesture-handler';

interface OpenHoursProps {
  label: string;
  value: string;
  onChange: (text: string) => void;
}

export const OpeningHours: React.FC<OpenHoursProps> = ({ label, value, onChange }) => {
  const increment = () => {
    const numericValue = Number(value);
    if (numericValue < 24) {
      onChange((numericValue + 1).toString());
    }
  };

  const decrement = () => {
    const numericValue = Number(value);
    if (numericValue > 0) {
      onChange((numericValue - 1).toString());
    }
  };

  return (
    <View style={styles.openingHours}>
      <Text style={styles.label}>{label}:</Text>
      <View style={styles.inputContainer}>
        <TouchableOpacity onPress={increment}>
          <Text style={styles.arrow}>▲</Text>
        </TouchableOpacity>
        <TextInput
          style={styles.inputHours}
          keyboardType="numeric"
          value={value}
          onChangeText={(text) => onChange(text)}
        />
        <TouchableOpacity onPress={decrement}>
          <Text style={styles.arrow}>▼</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};
