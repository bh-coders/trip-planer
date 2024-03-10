import { StyleSheet } from 'react-native';

export const attractionSearchStyles = StyleSheet.create({
  attractionsList: {
    backgroundColor: '#fff',
    width: '100%',
    padding: 10,
    marginVertical: 1,
  },
  errorText: {
    fontSize: 24,
    color: 'red',
  },
});

export const filterModal = StyleSheet.create({
  keywordContainer: {
    padding: 16,
  },
  keywordInput: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 16,
  },
  pickerContainer: {
    flexDirection: 'column',
    padding: 5,
  },
  picker: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
  },
  button: {
    padding: 20,
    borderRadius: 10,
    marginTop: 20,
    alignItems: 'flex-end',
  },
});
