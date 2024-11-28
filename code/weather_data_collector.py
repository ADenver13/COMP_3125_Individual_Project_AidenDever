# from meteostat import Daily, Point, Hourly
# from datetime import datetime
# point = Point(45.5019, -73.5674)
# start = datetime(2023, 1, 1, 0)
# end = datetime(2023, 12, 31, 0)
# data = Hourly(point, start=start, end=end)
# data = data.fetch()
# data.to_csv('weather_mtl_2023.csv')

import pandas as pd
import numpy as np

df1 = pd.read_csv('C:\\Users\\histo\\individual_project_3125_bixi\\COMP_3125_Individual_Project_AidenDever\\data\\Bixi_2023.csv')
df2 = pd.read_csv('C:\\Users\\histo\\individual_project_3125_bixi\\COMP_3125_Individual_Project_AidenDever\\weather_mtl_2023.csv')

def add_coco_to_trips(df1, df2):
    line_counter = 0

    coco_column = []
    
    # Convert the 'time' column in df2 to milliseconds since the epoch
    df2['time_ms'] = pd.to_datetime(df2['time']).astype(int) // 10**6  # Convert to milliseconds
    
    # Convert the 'STARTTIMEMS' column in df1 to numeric
    df1['STARTTIMEMS'] = pd.to_numeric(df1['STARTTIMEMS'])
    
    # Iterate over each row in df1 (trip data)
    for _, trip_row in df1.iterrows():
        print(line_counter)
        line_counter += 1

        start_timems = trip_row['STARTTIMEMS']
        
        # Calculate the absolute difference between the current trip's STARTTIMEMS and the time in df2
        df2['time_diff'] = np.abs(df2['time_ms'] - start_timems)
        
        # Find the index of the row in df2 with the smallest time difference
        closest_row_index = df2['time_diff'].idxmin()
        
        # Get the 'COCO' value from the closest row
        coco_value = df2.loc[closest_row_index, 'coco']
        
        coco_column.append(coco_value)

    df1['COCO'] = coco_column
    
    df1.to_csv('updated_trip_data_with_coco.csv', index=False)
    
    print("CSV file has been updated with COCO values.")
    return df1

add_coco_to_trips(df1, df2)