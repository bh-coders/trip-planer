import '@testing-library/jest-native/extend-expect';
import React from "react";
import {render} from '@testing-library/react-native';
import App from "../App";

test('render dashboard correctly', () => {
  const { getByText } = render(<App />);
  const textElement = getByText('WAITING FOR MAP');
  expect(textElement).toBeDefined();
});