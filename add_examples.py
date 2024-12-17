import json
from utils import *


def add_example(character, chinese_notes):
        print('Enter the example:')
        example = input()
        character_found = False
        for pinyin in chinese_notes:
            if character_found:
                break
            for char in chinese_notes[pinyin]:
                if char == character:
                    chinese_notes[pinyin][char]['examples'].append(example)
                    character_found = True
                    break
                
chinese_notes = load_chinese_notes()
existing_characters = extract_existing_characters(chinese_notes)

while True:
    print('For which character would you like to add an example?')
    character = input()
    examples_added = False

    if character in existing_characters:
        while True:
            add_example(character, chinese_notes)
            print('Would you like to add another example?')
            print('1) Yes, 2) No')
            if not is_yes(input()):
                save_file(chinese_notes)
                examples_added = True
                break
    else:
        print('Sorry, the character is not in the notes file yet. You need to add it using the add_character script.')
    if examples_added:
        break