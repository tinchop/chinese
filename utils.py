import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
chinese_notes_filename = config.get('General', 'notes_filename')

def load_chinese_notes():
    with open(chinese_notes_filename) as data:
	    return json.load(data)
 
def extract_existing_characters(chinese_notes):
    existing_characters = set()
    for pinyin in chinese_notes:
        for character in chinese_notes[pinyin]:
            existing_characters.add(character)
    return list(existing_characters)

def is_yes(option):
    return option.lower() == 'y' or option.lower == 'yes'

def save_file(chinese_notes):
    with open(chinese_notes_filename, 'w') as file:
        file.write(json.dumps(chinese_notes, indent=4, ensure_ascii=False, sort_keys=True))