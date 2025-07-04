PLACEHOLDER="[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names= name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    start_letter=letter.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=start_letter.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)
