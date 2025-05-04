import json, random, os
from utils import *
from termcolor import colored

chinese_notes = load_chinese_notes()
character_dict = create_character_dict(chinese_notes)
existing_characters = list(character_dict.keys())

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
                
                character_entry = chinese_notes[pinyin][character]
                show_character(character, pinyin, character_entry.get('simplified', None), character_entry['examples'], character_dict)
                
                character_found = True
                break
    
    print('\n')
    print('Show another character?')
    print('1) Yes, 2) No')
    
    if not is_yes(input()):
        break
        
