import { StyleSheet, Dimensions } from 'react-native';

export const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },

  openingHoursConteiner: {
    flexDirection: 'row',
    justifyContent: 'space-between'
  },

  openingHours: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  
  label: {
    fontSize: 20,
    fontFamily: 'Inter',
    marginRight: 10,
  },
  
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  
  inputHours: {
    fontSize: 20,
    fontFamily: 'Inter',
    marginHorizontal: 10,
  },

  input: {
    fontSize: 20,
    fontFamily: 'Inter',
    height: 50,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 16
  },

  inputDescription: {
    fontSize: 20,
    fontFamily: 'Inter',
    height: 150,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 16
  },
  
  arrow: {
    fontSize: 20,
  },
  
  errorText: {
    fontSize: 24,
    color: 'red',
  },

});
