import React, { useState, useEffect } from 'react';
import { View, Text, Modal, TextInput, Button, TouchableOpacity } from 'react-native';

const OpeningHoursComponent = ({ label, value, onChangeText }) => (
  <>
    <Text>{label}</Text>
    <TextInput
      style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 10 }}
      keyboardType="numeric"
      value={value.toString()}
      onChangeText={onChangeText}
    />
  </>
);

const OpeningHoursModal = ({ visible, onClose, onSave, initialOpeningHours }) => {
  const [selectedDayIndex, setSelectedDayIndex] = useState(0);
  const getDefaultOpeningHours = () => {
    return [
      { day: 'Mon', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Tue', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Wed', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Thu', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Fri', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Sat', openingHour: '09:00', closingHour: '17:00' },
      { day: 'Sun', openingHour: '09:00', closingHour: '17:00' },
    ];
  };
  const [openingHours, setOpeningHours] = useState(initialOpeningHours || getDefaultOpeningHours());

  const [backupOpeningHours, setBackupOpeningHours] = useState([...openingHours]);

  const daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

  useEffect(() => {
    // Update backupOpeningHours when initialOpeningHours changes
    setBackupOpeningHours(initialOpeningHours || getDefaultOpeningHours());
  }, [initialOpeningHours]);

  const selectedDay = openingHours[selectedDayIndex];

  const handleDayChange = (direction) => {
    const newIndex = (selectedDayIndex + direction + daysOfWeek.length) % daysOfWeek.length;
    setSelectedDayIndex(newIndex);
  };

  const handleSave = () => {
    onSave(openingHours);
  };

  const handleCancel = () => {
    // Restore the backupOpeningHours on cancel
    setOpeningHours([...backupOpeningHours]);
    onClose();
  };

  return (
    <Modal visible={visible} transparent={true} animationType="slide">
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <View style={{ backgroundColor: 'white', padding: 20, borderRadius: 10, width: '90%' }}>
          <TouchableOpacity onPress={handleCancel} style={{ alignSelf: 'flex-end', marginTop: -15, marginRight: -10, marginBottom: 20 }}>
            <Text style={{ fontSize: 20, textDecorationColor: 'red' }}>X</Text>
          </TouchableOpacity>
          <View style={{ flexDirection: 'row', justifyContent: 'space-between', marginBottom: 10 }}>
            <Button title="<" onPress={() => handleDayChange(-1)} />
            <Text style={{ fontSize: 18 }}>{selectedDay.day}</Text>
            <Button title=">" onPress={() => handleDayChange(1)} />
          </View>

          <OpeningHoursComponent
            label="Opening Hour:"
            value={selectedDay.openingHour}
            onChangeText={(text) => setOpeningHours((prev) => updateOpeningHours(prev, selectedDayIndex, 'openingHour', text))}
          />

          <OpeningHoursComponent
            label="Closing Hour:"
            value={selectedDay.closingHour}
            onChangeText={(text) => setOpeningHours((prev) => updateOpeningHours(prev, selectedDayIndex, 'closingHour', text))}
          />
          <View style={{ marginTop: 20 }}>
            <Button title="OK" onPress={handleSave} />
          </View>
        </View>
      </View>
    </Modal>
  );
};

const updateOpeningHours = (prevHours, index, field, value) => {
  return prevHours.map((hour, i) => {
    if (i === index) {
      return { ...hour, [field]: value };
    }
    return hour;
  });
};

export default OpeningHoursModal;
