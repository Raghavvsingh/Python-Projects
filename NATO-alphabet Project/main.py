import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict= {row.letter:row.code for (index,row) in data_frame.iterrows()}

user_input=input("Enter a word: ")
user_input=user_input.upper()

answer=[data_dict[letter] for letter in user_input]

print(answer)