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
        if char in ['ā', 'ē', 'ī', 'ō', 'ū', 'ǖ']:
            return 'light_red'
        elif char in ['à', 'è', 'ì', 'ò', 'ù', 'ǜ']:
            return 'light_blue'
        elif char in ['ǎ', 'ě', 'ǐ', 'ǒ', 'ǔ', 'ǚ']:
            return 'light_green'
        elif char in ['á', 'é', 'í', 'ó', 'ú', 'ǘ']:
            return 'light_yellow'
    return 'white'

def is_yes(option):
    option = option.strip().lower()
    return option == 'y' or option == 'yes' or option == '1' or option == '１'

def save_file(chinese_notes):
    with open(chinese_notes_filename, 'w') as file:
        file.write(json.dumps(chinese_notes, indent=4, ensure_ascii=False, sort_keys=True))