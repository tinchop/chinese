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

def create_character_to_tone_dict(chinese_notes):
    character_to_tone_dict = {}
    for pinyin in chinese_notes:
        for character in chinese_notes[pinyin]:
            character_to_tone_dict[character] = get_tone(pinyin)
    return character_to_tone_dict

def get_tone(pinyin):
    for char in pinyin:
        if char in ['ā', 'ē', 'ī', 'ō', 'ū']:
            return 'light_red'
        elif char in ['à', 'è', 'ì', 'ò', 'ù']:
            return 'light_blue'
        elif char in ['ǎ', 'ě', 'ǐ', 'ǒ', 'ǔ']:
            return 'light_green'
        elif char in ['á', 'é', 'í', 'ó', 'ú']:
            return 'light_yellow'
    return 'white'

def is_yes(option):
    return option.lower() == 'y' or option.lower == 'yes'

def save_file(chinese_notes):
    with open(chinese_notes_filename, 'w') as file:
        file.write(json.dumps(chinese_notes, indent=4, ensure_ascii=False, sort_keys=True))