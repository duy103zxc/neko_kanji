import csv
from pykakasi import kakasi

def hiragana_to_romaji(hiragana_text):
    kakasi_instance = kakasi()
    kakasi_instance.setMode("H", "a")  # Set conversion mode to convert Hiragana to Romaji
    conv = kakasi_instance.getConverter()
    return conv.do(hiragana_text)

def convert_csv_to_json(csv_file_path):
    data_list = []

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            kanji = row['expression']
            original_reading = row['reading']
            meaning = row['meaning']
            romaji = hiragana_to_romaji(original_reading)
            
            # Include both original and romaji readings in the "readings" list
            readings = [original_reading, romaji]

            data_list.append({
                'kanji': kanji,
                'readings': readings,
                'meaning': meaning,
            })

    return data_list

def write_json_to_file(data_list, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write("[\n")
        for data in data_list:
            jsonfile.write(f'{{ kanji: "{data["kanji"]}", readings: {data["readings"]}, meaning: "{data["meaning"]}" }},\n')
        jsonfile.write("]\n")

# Example usage:
csv_file_path = r'C:\Users\ACER\Downloads\htm\n4.csv'
output_file_path = 'n4vo.json'

converted_data = convert_csv_to_json(csv_file_path)
write_json_to_file(converted_data, output_file_path)
