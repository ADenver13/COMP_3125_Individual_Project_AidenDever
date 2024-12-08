import pandas as pd
import numpy as np

# Note: COCO is the weather category that meteostat uses. Conversion to a string weather category is done in the analysis notebook

bixi_data_df = pd.read_csv('C:\\Users\\histo\\individual_project_3125_bixi\\COMP_3125_Individual_Project_AidenDever\\data\\Bixi_2023.csv')
weather_df = pd.read_csv('C:\\Users\\histo\\individual_project_3125_bixi\\COMP_3125_Individual_Project_AidenDever\\data\\weather_mtl_2023.csv')

def add_coco_to_trips(bixi_data_df, weather_df):
    line_counter = 0

    coco_column = []
    
    # Convert the 'time' column in weather_df to milliseconds since the epoch for matchup with bixi data
    weather_df['time_ms'] = pd.to_datetime(weather_df['time']).astype(int) // 10**6  # Convert to milliseconds
    
    # Convert the 'STARTTIMEMS' column in bixi_data_df to numeric
    bixi_data_df['STARTTIMEMS'] = pd.to_numeric(bixi_data_df['STARTTIMEMS'])
    
    # Iterate over each row in bixi_data_df
    for _, trip_row in bixi_data_df.iterrows():
        print(line_counter)
        line_counter += 1

        start_timems = trip_row['STARTTIMEMS']
        
        # Calculate the abs dff between the current trip's STARTTIMEMS and the time in weather_df
        weather_df['time_diff'] = np.abs(weather_df['time_ms'] - start_timems)
        
        # Find the index of the row in weather_df with the smallest time difference
        closest_row_index = weather_df['time_diff'].idxmin()
        
        # Get the 'COCO' value from the closest row
        coco_value = weather_df.loc[closest_row_index, 'coco']
        
        coco_column.append(coco_value)

    bixi_data_df['COCO'] = coco_column
    
    bixi_data_df.to_csv('updated_trip_data_with_coco.csv', index=False)
    
    print("CSV file has been updated with COCO values.")
    return bixi_data_df

add_coco_to_trips(bixi_data_df, weather_df)