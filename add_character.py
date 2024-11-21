import json
from utils import *


def add_character(new_entry, existing_characters):
    while True:
        print('Which character do you want to add?')
        new_character = input()
        if new_character not in existing_characters:
            new_entry['character'] = new_character
            break
        print('Sorry, the character is already added.')
         
def add_simplified_form(new_entry):
    print('What\'s its simplified form? (if any)')
    new_entry['simplified'] = input()
    
def add_pinyin(new_entry):
    while True:
        print('What\'s the pinyin?')
        new_entry['pinyin'] = input()
        if len(new_entry['pinyin']) > 0:
            break
        print('The pinyin is required.')
         
def add_examples(new_entry):
    print('Do you want to add an example?')
    print('Yes/No?')
    if is_yes(input()):
        print('Add example:')
        new_entry['examples'].append(input())
        
        while True:
            print('Would you like to add another example?')
            print('Yes/No?')
            if is_yes(input()):
                print('Add example:')
                new_entry['examples'].append(input())
            else:
                break
            
def do_add_entry(chinese_notes, new_entry):
    new_entry_value = { "examples" : new_entry['examples'] }
    if new_entry['simplified']:
        new_entry_value['simplified'] = new_entry['simplified']
    if new_entry['pinyin'] in chinese_notes:
        chinese_notes[new_entry['pinyin']][new_entry['character']] = new_entry_value
    else:
        chinese_notes[new_entry['pinyin']] = { new_entry['character'] : new_entry_value}
        
    save_file(chinese_notes)
       
               
chinese_notes = load_chinese_notes()
existing_characters = extract_existing_characters(chinese_notes)
new_entry = {
    "character": None,
    "simplified": None,
    "pinyin": None,
    "examples": []
}

while True:

    add_character(new_entry, existing_characters)
    add_simplified_form(new_entry)
    add_pinyin(new_entry)
    add_examples(new_entry)

    print('Please verify the entry is correct:')
    print(json.dumps(new_entry, indent=4, ensure_ascii=False))
    print('Yes/No?')
    if is_yes(input()):
        do_add_entry(chinese_notes, new_entry)
        print('New character added!')
        break
    print('Let\'s start again then!')