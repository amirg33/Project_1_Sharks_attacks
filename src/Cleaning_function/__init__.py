import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

def Cleaning_function(df: pd.DataFrame):
    #df = pd.read_csv("../data/attacks.csv",sep=',' ,encoding= 'latin_1')
    # Rename columns
    df.columns = df.columns.str.replace(' ', '_').str.lower().str.strip().str.rstrip('_')
    
    # Drop all the rows that do not have any information
    df.dropna(axis=0, how="all")
    
    # Clean the case_number Column after seeing that all the 0's and xx's have useless data
    df = df[df["case_number"] != "0"]
    df = df[df["case_number"] != "xx"]
    
    # Clean the type column by correcting some words
    df["type"] = df["type"].replace("Boatomg", "Boating")
    
    # Delete useless columns
    df.drop(columns=["unnamed:_23", "unnamed:_22"], inplace=True)
    
    # Replace information that is in another column and copy it. After seeing that the information can be replaced by another column
    df.loc[df["case_number"].isna(), "case_number"] = df["case_number.1"]
    
    # Delete unnecessary columns that are duplicated
    df.drop(columns=["case_number.1", "case_number.2"], inplace=True)
    
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
    df["fatal_(y/n)"] = df["fatal_(y/n)"].replace(replacement_dict)
    
    # Convert the pattern of the years ".0" in regular year-patterns
    df["year"] = df["year"].astype(str)
    pattern = r'^\d{4}\.\d$'
    matching_rows = df["year"].str.contains(pattern, na=False)
    df.loc[matching_rows, "year"] = df["year"].str.replace('\.0', '', regex=True)
    
    # Convert the same pattern number with the original_order
    df["original_order"] = df["original_order"].str.replace('\.0', '', regex=True)
    df["original_order"] = df["original_order"].astype(int)
    df.set_index("original_order", inplace=True)
    df.sort_index(inplace=True)
    
    # Make the original_order the index, as it indicates the number of cases in a timeline. 
    # Make it so there are no jumps in between the data as a lot of information has been deleted. 
    expected_next = df.index[0]
    index_copy = df.index.tolist()
    for i, idx in enumerate(index_copy):
        if idx != expected_next:
            index_copy[i] = expected_next
        expected_next += 1
    df.index = index_copy # type: ignore
    diff = df.index[0] - 1
    df.index = df.index - diff

    return df
