import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  footer: {
    height: 50,
    backgroundColor: 'gray',
    alignItems: 'center',
    justifyContent: 'center',
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
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
export const imagePlaceholder = StyleSheet.create({
  imageContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 20,
  },
  placeholder: {
    width: 350,
    height: 300,
    backgroundColor: '#abc',
    marginRight: 10,
  },
});
