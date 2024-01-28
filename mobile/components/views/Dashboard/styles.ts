import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  page: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  container: {
    height: '80%',
    width: '100%',
  },
  errorText: {
    fontSize: 24,
    color: 'red',
  },
  map: {
    flex: 1,
  },
  searchInput: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    paddingHorizontal: 10,
    margin: 10,
  },
  searchSection: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  searchBottomPanelInput: {
    flex: 1,
    marginRight: 10,
  },
  picker: {
    flex: 1,
  },
  attractionsGrid: {
    flexDirection: 'column',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
  },
  attractionTile: {
    width: '100%', // Każdy kafelek zajmuje 100% szerokości
    padding: 10,
    marginVertical: 5, // Dodaje margines pionowy
    backgroundColor: '#f0f0f0',
    borderRadius: 10,
  },
});
