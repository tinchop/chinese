import json, random, os
from utils import *
from termcolor import colored

chinese_notes = load_chinese_notes()
existing_characters = extract_existing_characters(chinese_notes)
character_to_tone_dict = create_character_to_tone_dict(chinese_notes)

def print_example(example):
    colored_example = ''
    for letter in example:
        colored_example += get_colored_character(letter)
    print(colored_example)
    
def get_colored_character(character):
    return colored(character, character_to_tone_dict.get(character, 'white'))

while True:
    os.system('clear')
    index = random.randint(0, len(existing_characters) - 1)
    character = existing_characters[index]
    
    character_found = False
    for pinyin in chinese_notes:
        if character_found:
            break
        for char in chinese_notes[pinyin]:
            if char == character:
                print('\n')
                print('\n')
                print(get_colored_character(character))
                print(pinyin)
                print('\n')
                
                if 'simplified' in chinese_notes[pinyin][character]:
                    print('Simplified: ' + chinese_notes[pinyin][character]['simplified'])
                    print('\n')
                
                for example in chinese_notes[pinyin][character]['examples']:
                    print_example(example)
                
                character_found = True
                break
    
    print('\n')
    print('Show another character?')
    print('1) Yes, 2) No')
    
    if not is_yes(input()):
        break
        
