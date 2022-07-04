student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"} #so no nato.to_dict()

nato = pd.read_csv("nato_phonetic_alphabet.csv")
df_nato = pd.DataFrame(nato)

phonetic_dict = {row.letter : row.code for (index,row) in df_nato.iterrows()}
#print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()

#[new_item for item in list]
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)