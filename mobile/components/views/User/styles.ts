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
    borderWidth: 0.2,
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
  logoutButton: {
    position: 'absolute',
    top: 10,
    left: 10,
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

  textStyle: {
    color: 'white',
    fontWeight: 'bold',
    textAlign: 'center',
  },
  settingsButtonText: {
    color: 'black',
    fontSize: 14,
  },
  settingsButton: {
    backgroundColor: '#20B2AA',
    borderRadius: 20,
    padding: 10,
    elevation: 2,
    marginTop: 10,
    width: 200,
    height: 50,
    justifyContent: 'center',
    alignItems: 'center',
    margin: 10,
  },
  buttonClose: {
    backgroundColor: '#2196F3',
    borderRadius: 20,
    padding: 10,
    elevation: 2,
    marginTop: 10,
    width: 150,
    height: 45,
    justifyContent: 'center',
    alignItems: 'center',
  },
  questionText: {
    fontWeight: 'bold',
    fontSize: 18,
    textAlign: 'center',
  },
});

export const formStyles = StyleSheet.create({
  container: {
    padding: 20,
  },
  input: {
    height: 40,
    marginBottom: 10,
    borderWidth: 1,
    padding: 10,
    borderRadius: 15,
  },
  avatarButton: {
    backgroundColor: '#007bff',
    borderRadius: 15,
    padding: 10,
    alignItems: 'center',
    marginBottom: 10,
  },
  buttonRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 30,
  },
  halfWidthButton: {
    backgroundColor: '#00b35d',
    borderRadius: 15,
    padding: 10,
    alignItems: 'center',
    width: '48%',
  },
  buttonText: {
    color: 'white',
    textAlign: 'center',
  },
  descriptionInput: {
    height: 120,
    textAlignVertical: 'top',
    marginBottom: 10,
    borderWidth: 1,
    padding: 10,
    borderRadius: 15,
  },
});
