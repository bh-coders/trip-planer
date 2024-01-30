import React, { useState } from 'react';
import { View, TouchableOpacity, Text, TextInput } from 'react-native';
import { formStyles } from '../styles';
import { launchImageLibrary } from 'react-native-image-picker';

const ChangeCredentialsProfileForm = ({ onProfileCredentialsChange, navigation }: any) => {
  const [name, setName] = useState<string>('');
  const [surname, setSurname] = useState<string>('');
  const [description, setDescription] = useState<string>('');
  const [avatar, setAvatar] = useState<string>('');

  const selectFile = () => {
    const options = {
      title: 'Select Avatar',
      storageOptions: {
        skipBackup: true,
        path: 'images',
      },
    };

    launchImageLibrary(options as any, (response) => {
      if (response.didCancel) {
        console.log('User cancelled image picker');
      } else if (response.errorCode) {
        console.log('ImagePicker Error: ', response.errorMessage);
      } else if (response.assets && response.assets.length > 0) {
        const source = 'data:image/jpeg;base64,' + response.assets[0].base64;
        setAvatar(source);
      }
    });
  };
  return (
    <View style={formStyles.container}>
      <TouchableOpacity style={formStyles.avatarButton} onPress={selectFile}>
        <Text style={formStyles.buttonText}>Add Avatar</Text>
      </TouchableOpacity>
      <TextInput
        style={formStyles.input}
        placeholder="Name"
        value={name}
        onChangeText={setName}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      <TextInput
        style={formStyles.input}
        placeholder="Surname"
        value={surname}
        onChangeText={setSurname}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      <TextInput
        style={formStyles.descriptionInput}
        placeholder="Description"
        value={description}
        onChangeText={setDescription}
        multiline
        numberOfLines={4} // You can adjust the number of lines
      />
      <View style={formStyles.buttonRow}>
        <TouchableOpacity
          style={formStyles.halfWidthButton}
          onPress={() => onProfileCredentialsChange({ name, surname, description, avatar })}>
          <Text style={formStyles.buttonText}>Confirm</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={formStyles.halfWidthButton}
          onPress={() => navigation.navigate('My Account')}>
          <Text style={formStyles.buttonText}>Back to Profile</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};
export default ChangeCredentialsProfileForm;
