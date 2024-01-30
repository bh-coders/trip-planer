import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  page: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  container: {
    height: '100%',
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
  searchButton: {
    height: 40,
    backgroundColor: '#2196F3',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 5,
    margin: 10,
    paddingHorizontal: 20,
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
    width: '100%',
    padding: 10,
    marginVertical: 5,
    backgroundColor: '#f0f0f0',
    borderRadius: 10,
  },
});
export const attractionTileStyles = StyleSheet.create({
  attractionTile: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#fff',
    padding: 20,
    marginVertical: 10,
    borderRadius: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 3,
    elevation: 2,
    width: '100%',
  },
  leftContainer: {
    flexDirection: 'row',
    flex: 1,
    alignItems: 'center',
  },
  imageContainer: {
    marginRight: 15,
  },
  image: {
    width: 70,
    height: 70,
    borderRadius: 15,
  },
  emptyImage: {
    width: 70,
    height: 70,
    borderRadius: 15,
    borderWidth: 1,
    borderColor: '#000',
    backgroundColor: 'transparent',
  },
  textContainer: {
    flexShrink: 1,
  },
  title: {
    fontWeight: 'bold',
    fontSize: 18,
    color: '#000',
  },
  category: {
    fontSize: 14,
    color: 'grey',
    marginBottom: 10,
  },
  description: {
    fontSize: 12,
    color: 'grey',
  },
  rate: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#FFD700',
  },
});
