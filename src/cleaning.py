import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

def Cleaning_function(df):
    # Rename columns
    df.columns = df.columns.str.replace(' ', '_').str.lower().str.strip().str.rstrip('_')
    
    #Drop all the rows that do not have any information
    df.dropna(axis=0, how="all")
    # Clean the Case Number Column after seeing that all the 0's and xx's have useless data
    df[df["Case Number"]!= "0"]
    df[df["Case Number"] != "xx"]
    #Clean the Type column by correcting some words
    df["Type"] = df["Type"].replace("Boatomg", "Boating")
    #Delete useless columns
    df.drop(columns=["Unnamed: 23", "Unnamed: 22"], inplace=True)
    #Replace information that is in another column and copy it. After seeing that the information can be replaced by another column
    df.loc[df["Case Number"].isna(), "Case Number"] = df["Case Number.1"]
    #Delete unnecesarry columns that are duplicated
    df.drop(columns=["Case Number.1", "Case Number.2"], inplace=True)
    #Clean Filter out all the information of the fatalities
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
    #Convert the pattern of the years ".0" in regular year - patterns
    df["Year"] = df["Year"].astype(str)
    pattern = r'^\d{4}\.\d$'
    matching_rows = df["Year"].str.contains(pattern, na=False)
    df.loc[matching_rows, "Year"] = df["Year"].str.replace('\.0', '', regex=True)
    #Convert the same pattern number with the Original Number
    df["original order"] = df["original order"].str.replace('\.0', '', regex=True)
    df["original order"] = df["original order"].astype(int)
    df.set_index("original order", inplace=True)
    df.sort_index(inplace=True)
    #Make the Original Number the index, as it indicates the number of cases in a timeline. 
    #Make it so the are not jumps in between the data as a lot of information has been deleted. 
    expected_next = df.index[0]
    index_copy = df.index.tolist()
    for i, idx in enumerate(index_copy):
        if idx != expected_next:
            index_copy[i] = expected_next
        expected_next += 1
    df.index = index_copy
    diff = df.index[0] - 1
    df.index = df.index - diff  
