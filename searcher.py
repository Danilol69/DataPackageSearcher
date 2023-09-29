# I created this script so you can search your messages contained in your Discord Data Package to find lost dms for example.
# Don't send your Discord Data Package to others either, because it contains very sensitive information about you.
# Learn more: https://support.discord.com/hc/en-us/articles/360004957991

import os
import json
import csv

def search_phrase_in_files(directory_path, target_phrase):
    found = False
    extensions_to_search = (".txt", ".csv", ".json")

    for root, _, files in os.walk(directory_path):
        for filename in files:
            file_extension = os.path.splitext(filename)[-1].lower()

            if file_extension in extensions_to_search:
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        if file_extension == ".txt":
                            lines = file.readlines()
                            for line_number, line in enumerate(lines, 1):
                                if target_phrase in line:
                                    found = True
                                    print(f"Found '{target_phrase}' in {file_path} at line {line_number}:")
                                    print(line.strip())
                        elif file_extension == ".csv":
                            csv_reader = csv.reader(file)
                            for row_number, row in enumerate(csv_reader, 1):
                                for column_number, cell in enumerate(row, 1):
                                    if target_phrase in cell:
                                        found = True
                                        print(f"Found '{target_phrase}' in {file_path} at row {row_number}, column {column_number}:")
                                        print(cell.strip())
                        elif file_extension == ".json":
                            json_data = json.load(file)
                            if isinstance(json_data, dict):
                                json_data = json_data.values()
                            for item_number, item in enumerate(json_data, 1):
                                if isinstance(item, str) and target_phrase in item:
                                    found = True
                                    print(f"Found '{target_phrase}' in {file_path} at item {item_number}:")
                                    print(item.strip())

                except Exception as e:
                    print(f"An error occurred while processing {file_path}: {str(e)}")

    if not found:
        print(f"No occurrences of '{target_phrase}' found in any text, CSV, or JSON file.")

def main():
    while True:
        directory_path = input("Enter the directory path: ")
        target_phrase = input("Enter the target phrase: ")
        print("-" * 55)
        search_phrase_in_files(directory_path, target_phrase)
        print("-" * 55)
        response = input("Press Enter to close or type 'search' to search again: ").strip().lower()
        if response != 'search':
            break

if __name__ == "__main__":
    main()