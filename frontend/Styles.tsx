import { StyleSheet, Platform } from 'react-native';

const styles = StyleSheet.create({
  App: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    ...Platform.select({
      ios: {
        //
      },
      android: {
        backgroundColor: 'red',
      },
      web: {
        backgroundColor: 'blue',
      },
    }),
  },
});

export default styles;
