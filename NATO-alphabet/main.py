import pandas
data=pandas.read_csv(r"C:\Users\ssc\Desktop\100.days.of.code\NATO-alphabet-start\nato_phonetic_alphabet.csv")
new_data={row.letter:row.code for (index,row) in data.iterrows()}
word=input("Enter a word:").upper()
output_list=[new_data[letters] for letters in word]
print(output_list)