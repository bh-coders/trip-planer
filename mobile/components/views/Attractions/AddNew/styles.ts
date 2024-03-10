import { StyleSheet } from 'react-native';

export const styles = StyleSheet.create({
  container: {
    padding: 20,
  },
  input: {
    fontSize: 14,
    fontFamily: 'Inter',
    height: 50,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 16,
    borderRadius: 15,
    padding: 10,
  },
  inputDescription: {
    fontSize: 14,
    fontFamily: 'Inter',
    height: 150,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 16,
    borderRadius: 15,
    padding: 10,
  },
  openingHoursContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 16,
  },
  openingHoursInput: {
    fontSize: 10,
    fontFamily: 'Inter',
    height: 50,
    borderColor: 'gray',
    borderWidth: 1,
    flex: 1,
    borderRadius: 15,
    padding: 10,
  },
  label: {
    fontSize: 18,
    fontWeight: 'bold',
    fontFamily: 'Inter',
    marginRight: 10,
  },
  buttonSubmit: {
    backgroundColor: '#20B2AA',
    borderRadius: 20,
    padding: 10,
    elevation: 2,
    marginTop: 10,
    width: '50%',
    position: 'absolute',
    bottom: 20,
    right: 10,
    alignSelf: 'flex-end',
  },
  buttonText: {
    color: 'white',
    fontSize: 14,
    textAlign: 'center',
  },
  errorText: {
    fontSize: 24,
    color: 'red',
    marginBottom: 16,
  },
  openingHours: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  inputHours: {
    fontSize: 18,
    fontFamily: 'Inter',
    marginHorizontal: 10,
    height: 50,
    padding: 10,
  },
  arrow: {
    fontSize: 22,
  },
});
