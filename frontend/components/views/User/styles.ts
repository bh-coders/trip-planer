import { StyleSheet } from 'react-native';
export const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  userSection: {
    alignItems: 'center',
    padding: 20,
  },
  avatar: {
    width: 100,
    height: 100,
    borderRadius: 50,
    marginBottom: 10,
    borderWidth: 2,
    borderColor: 'black',
  },

  username: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  email: {
    fontSize: 18,
    color: 'gray',
  },
  attractionsSection: {
    marginTop: 20,
  },
  sectionTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    paddingLeft: 20,
    textAlign: 'center',
    marginBottom: 25,
  },
  settingsButton: {
    position: 'absolute',
    top: 10,
    right: 10,
    backgroundColor: '#f0f0f0',
    padding: 8,
    borderRadius: 5,
    zIndex: 1,
  },
  settingsButtonText: {
    color: 'black',
    fontSize: 14,
  },
});

export const modalStyles = StyleSheet.create({
  centeredView: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 22,
  },
  modalView: {
    margin: 20,
    backgroundColor: 'white',
    borderRadius: 20,
    padding: 35,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 4,
    elevation: 5,
  },
  modalText: {
    marginBottom: 15,
    textAlign: 'center',
  },
  buttonClose: {
    backgroundColor: '#2196F3',
    borderRadius: 20,
    padding: 10,
    elevation: 2,
  },
  textStyle: {
    color: 'white',
    fontWeight: 'bold',
    textAlign: 'center',
  },
  settingsButtonText: {
    color: 'black',
    fontSize: 14,
  },
});
