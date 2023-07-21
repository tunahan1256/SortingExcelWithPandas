import pandas as pd
import numpy as np
import seaborn as sns


pd.set_option("display.max_columns",None)
pd.set_option("display.width", 200)
pd.set_option('display.max_rows', 200)


df = pd.read_excel("kopya.xlsx",sheet_name="tunahan")


Tr2Eng = str.maketrans("çğıöşü", "cgiosu")
df["urunadi"]= df["urunadi"].apply(lambda x: x.lower().translate(Tr2Eng)) #Converting words turkish to english


def set_color(column):
    
    """
    Summary: 
        Checks whether certain colors are in the column
    Args:
        column (str): The string where the colors will be looked at
    Returns:
        color (str): Colors(Black,White,...)
    """
    
    if "siyah" in column or "black" in column:
        return "1_BLACK"
    elif "beyaz" in column or "white" in column:
        return "2_WHITE" 
    elif "kirmizi" in column or "red" in column:
        return "3_RED" 
    elif "turuncu" in column or "orange" in column:
        return "4_ORANGE" 
    elif "sari" in column or "yellow" in column:
        return "5_YELLOW" 
    elif "yesil" in column or "green" in column:
        return "6_GREEN" 
    elif "mavi" in column or "blue" in column:
        return "7_BLUE" 
    elif "mor" in column or "purple" in column:
        return "8_PURPLE" 
    else:
        return "ANYCOLOR"


def set_memory(column):
    
    """
    Summary: 
        Checks whether certain memories are in the column
    Args:
        column (str): The string where the memories will be looked at
    Returns:
        color (str): Memories(16GB,32GB,...)
    """
    
    if "16gb" in column or "16 gb" in column:
        return "1_16GB"
    elif "32gb" in column or "32 gb" in column:
        return "2_32GB" 
    elif "64gb" in column or "64 gb" in column:
        return "3_64GB" 
    elif "128gb" in column or "128 gb" in column:
        return "4_128GB" 
    elif "256gb" in column or "256 gb" in column:
        return "5_256GB" 
    elif "512gb" in column or "512 gb" in column:
        return "6_512GB" 
    elif "1tb" in column or "1 tb" in column:
        return "7_1TB" 
    else:
        return "8_undefined"
    
    #We wrote 1_, 2_ because we want them to come from small to large in the for loop. In this way, we can correctly sort the colors and memories 
   
df["COLOR"] = [set_color(column) for column in df["urunadi"]] #Adding COLOR variable to the dataframe
df["MEMORY"] = [set_memory(column) for column in df["urunadi"]] #Adding MEMORY variable to the dataframe


def memory_color(dataframe, color_column,memory_column,sayac2):
    
    """
    Summary: If the color column of the dataframe is equal to any color, and the memory column is equal to any memory,
    it shows the dataframe in which the color column is equal to that color and the memory column is equal to that memory,
    and synchronizes it to a variable. It then assigns a value to the etmcode and returns the dataframe
    Args:
        dataframe (dataframe): Dataframe
        color_column (str): Values of the color column of the dataframe
        memory_column (str): Values of the memory column of the dataframe
        sayac2 (float): The value that the etmcode column of the data frame will be equal to
    Returns:
        dataframe: Dataframe in which the color column is equal to that color and the memory column is equal to that memory.
    """
    
    a2 = dataframe.loc[(dataframe["COLOR"] == color_column) & (df["MEMORY"]== memory_column),["etmcode","urunadi"]]
    a2.loc[:,"etmcode"] = sayac2
    return a2
      
a1 = pd.DataFrame()
sayac=0


for memory in np.sort(df["MEMORY"].unique()):

    for color in np.sort(df["COLOR"].unique()):
        
        b1 = a1.shape
        a1 = pd.concat([a1,memory_color(df,color,memory,sayac)])
        
        if (b1 == a1.shape):
            sayac=sayac-1

        sayac = sayac + 1
        

df = a1
df.set_index("etmcode",inplace=True)
#df.drop(["COLOR","MEMORY"],axis=1,inplace=True)
print(df)

#file_name = "final_sorted.xlsx"
#df.to_excel(file_name)








































































































