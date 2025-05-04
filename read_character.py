import json, random, os
from utils import *
from termcolor import colored

chinese_notes = load_chinese_notes()
character_dict = create_character_dict(chinese_notes)

while True:
    
    print('Enter character:')
    character = input()
    os.system('clear')
    
    if (character in character_dict):
        character_entry = character_dict[character]
        show_character(character, character_entry['pinyin'], character_entry.get('simplified', None), character_entry['examples'], character_dict)
    else:
        print('Character not found.')
    
    print('\n')
    print('Read another character?')
    print('1) Yes, 2) No')
    
    if not is_yes(input()):
        break
        
