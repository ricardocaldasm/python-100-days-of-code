import pandas

data = pandas.read_csv(r"day26\nato_phonetic_alphabet.csv")
print(data)

# {new_key:new_value for (index,row) in data.iterrows()}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
# [new_item for item in list]
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
