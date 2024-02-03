const mapArrayToJson = (openingHoursArray) => {
    const transformedHours = {};
    
    openingHoursArray.forEach((dayData) => {
      const { day, openingHour, closingHour } = dayData;
      const dayKey = day.toLowerCase(); // Convert day to lowercase for consistency
      transformedHours[dayKey] = {
        openingHour,
        closingHour,
      };
    });
  
    return transformedHours;
  };

export default mapArrayToJson;