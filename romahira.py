import csv
from pykakasi import kakasi

# Function to convert Hiragana text to Romaji using pykakasi
def hiragana_to_romaji(hiragana_text):
    kakasi_instance = kakasi()
    kakasi_instance.setMode("H", "a")  # Set conversion mode to convert Hiragana to Romaji
    conv = kakasi_instance.getConverter()
    return conv.do(hiragana_text)

# Function to convert CSV data to JSON format
def convert_csv_to_json(csv_file_path):
    data_list = []

    # Open the CSV file and read its content
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Extract data from the CSV row
            kanji = row['expression']
            original_reading = row['reading']
            meaning = row['meaning']
            
            # Convert the original reading from Hiragana to Romaji
            romaji = hiragana_to_romaji(original_reading)
            
            # Include both original and Romaji readings in the "readings" list
            readings = [original_reading, romaji]

            # Add the extracted data to the list
            data_list.append({
                'kanji': kanji,
                'readings': readings,
                'meaning': meaning,
            })

    return data_list

# Function to write JSON data to a file
def write_json_to_file(data_list, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write("[\n")
        for data in data_list:
            # Write each data entry in JSON format to the file
            jsonfile.write(f'{{ kanji: "{data["kanji"]}", readings: {data["readings"]}, meaning: "{data["meaning"]}" }},\n')
        jsonfile.write("]\n")

# Example usage:
csv_file_path = r'C:\Users\ACER\Downloads\blogpost\n3.csv'
output_file_path = 'N3kan.json'

# Convert CSV data to JSON and write it to a file
converted_data = convert_csv_to_json(csv_file_path)
write_json_to_file(converted_data, output_file_path)
