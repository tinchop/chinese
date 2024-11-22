import json, random, os
from utils import *

chinese_notes = load_chinese_notes()
existing_characters = extract_existing_characters(chinese_notes)

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
                print(character)
                print('\n')
                print(pinyin)
                print('\n')
                print(json.dumps(chinese_notes[pinyin][character], indent=4, ensure_ascii=False))
                character_found = True
                break
    
    print('\n')
    print('Show another character?')
    print('Yes/No?')
    
    if not is_yes(input()):
        break
        
