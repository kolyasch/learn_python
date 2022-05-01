PLACEHOLDER = '[name]'

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()
with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        striped_name = name.strip()
        my_text = letter_contents.replace(PLACEHOLDER, striped_name)
        with open(f'./Output/ReadyToSend/{striped_name}.txt', mode='w') as competed_letter:
            competed_letter.write(my_text)

