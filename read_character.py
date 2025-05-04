import json, random, os
from utils import *
from termcolor import colored

chinese_notes = load_chinese_notes()
character_dict = create_character_dict(chinese_notes)
existing_characters = list(character_dict.keys())
character_to_tone_dict = create_character_to_tone_dict(chinese_notes)

def print_example(example):
    colored_example = ''
    for letter in example:
        colored_example += get_colored_character(letter)
    print(colored_example)
    
def get_colored_character(character):
    return colored(character, character_to_tone_dict.get(character, 'white'))



while True:
    
    print('Enter character:')
    character = input()
    os.system('clear')
    
    if (character in character_dict):
        character_entry = character_dict[character]
        print('\n')
        print('\n')
        print(get_colored_character(character))
        print(character_entry['pinyin'])
        print('\n')
        
        if 'simplified' in character_entry:
            print('Simplified: ' + character_entry['simplified'])
            print('\n')
        
        for example in character_entry['examples']:
            print_example(example)
    else:
        print('Character not found.')
    
    
    print('\n')
    print('Read another character?')
    print('1) Yes, 2) No')
    
    if not is_yes(input()):
        break
        
