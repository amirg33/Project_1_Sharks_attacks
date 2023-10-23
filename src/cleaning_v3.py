import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

def Cleaning_function(df: pd.DataFrame):
    #df = pd.read_csv("../data/attacks.csv",sep=',' ,encoding= 'latin_1')
    
    # Drop all the rows that do not have any information
    df.dropna(axis=0, how="all")
    # Delete a row that does not have any information.
    df[(df["Case Number"] == "0") & (~df["original order"].isnull())] 

    # Clean the case_number Column after seeing that all the 0's and xx's have useless data
    df = df[df["Case Number"]!= "0"]
    df = df[df["Case Number"] != "xx"]
    
    # Clean the type column by correcting some words
    df["Type"] = df["Type"].replace("Boatomg", "Boating")
    df["Type"] = df["Type"].replace("Boating", "Boat")
    df["Type"] = df["Type"].replace("Sea Disaster", "Unprovoked")
    
    # Delete useless columns
    df.drop(columns=["Unnamed: 23", "Unnamed: 22"], inplace=True)

    # Replace information that is in another column and copy it. After seeing that the information can be replaced by another column
    df.loc[df["Case Number"].isna(), "Case Number"] = df["Case Number.1"]
    
    # Delete unnecessary columns
    df.drop(columns=["Case Number.1", "Case Number.2","href","href formula", "pdf", "Investigator or Source"], inplace=True)

    # Clean Filter out all the information of the fatalities
    replacement_dict = {
        ' N': 'N',
        'N ': 'N',
        'M': 'Unknown',
        '2017': 'Unknown',
        'y': 'Y',
        'UNKNOWN': 'Unknown',
        np.nan: 'Unknown'
    }
    df["Fatal (Y/N)"] = df["Fatal (Y/N)"].replace(replacement_dict)
    
    # Convert the pattern of the years ".0" in regular year-patterns
    df["Year"] = df["Year"].astype(str)
    pattern = r'^\d{4}\.\d$'
    matching_rows = df["Year"].str.contains(pattern, na=False)
    df.loc[matching_rows, "Year"] = df["Year"].str.replace('\.0', '', regex=True)
    
    # Convert the same pattern number with the original_order
    df["original order"] = df["original order"].str.replace('\.0', '', regex=True)
    df["original order"] = df["original order"].astype(int)
    df.set_index("original order", inplace=True)
    df.sort_index(inplace=True)
    
    # Make the original_order the index, as it indicates the number of cases in a timeline. 
    # Make it so there are no jumps in between the data as a lot of information has been deleted. 
        # expected_next = df.index[0]
        #index_copy = df.index.tolist()
        #for i, idx in enumerate(index_copy):
        #    if idx != expected_next:
        #        index_copy[i] = expected_next
        #    expected_next += 1
        #df.index = index_copy # type: ignore
        #diff = df.index[0] - 1
        #df.index = df.index - diff
    df.columns = df.columns.str.replace(' ', '_').str.lower().str.strip().str.rstrip('_')
    
    # Convert Years into integers in order to loose the ".0"
    def convert_to_int(value):
        try:
            return int(float(value))
        except ValueError:
            return value
    df['year'] = df['year'].apply(convert_to_int)   
    
    #Convert and format all dates if not specific enough, give NaN
    def convert_date(date_str):
        cleaned_date = ''.join(date_str.split(' ')[-2:])
        if cleaned_date.count('-') == 1:
            cleaned_date = '01-' + cleaned_date
            
        return pd.to_datetime(cleaned_date, format='%d-%b-%Y', errors='coerce')

    df['cleaned_date'] = df['date'].apply(convert_date)

    # 
    date_idx = df.columns.get_loc('date')

    ordered_cols = list(df.columns)
    ordered_cols.insert(date_idx + 1, ordered_cols.pop(ordered_cols.index('cleaned_date')))

    df = df[ordered_cols] # type: ignore

    #reset the index
    df_Data_cleaned_reset = df.reset_index()

    return df_Data_cleaned_reset
