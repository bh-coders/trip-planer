/// We need to consider if we shoudl move makePostMessage to maybe one method
/// And deconstruct props, {...props} in body, we should maybe also add endpoint
/// generic, idk - to consider

export const makePostMessage = async (body: any, fetchMethod: string, address: string) => {
  console.log('Fetch post ', body, fetchMethod, address);
  try {
    const response = await fetch(`auth/${address}`, {
      method: `${fetchMethod}`,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });

    const data = await response.json();

    console.log('Success:', data);
    return data;
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
};