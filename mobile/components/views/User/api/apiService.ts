/// We need to consider if we shoudl move makePostMessage to maybe one method
/// And deconstruct props, {...props} in body, we should maybe also add endpoint
/// generic, idk - to consider

export const makeMessageWithBody = async (
  body: any,
  fetchMethod: string,
  address: string,
  token: string
) => {
  try {
    const response = await fetch(`user/${address}`, {
      method: `${fetchMethod}`,
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer: ${token}`,
      },
      body: JSON.stringify(body),
    });

    const data = await response.json();

    return data;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
};

export const makeGetMessage = async (token: string) => {
  try {
    const response = await fetch(`user/me`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer: ${token}`,
      },
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error', error);
    throw error;
  }
};

export const makeDeleteMessage = async (address: string, token: string) => {
  try {
    const response = await fetch(`user/${address}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer: ${token}`,
      },
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error', error);
    throw error;
  }
};
