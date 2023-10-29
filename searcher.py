import os
import csv

def search_phrase_in_csv_files(directory_path, target_phrase):
    found = False

    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.lower().endswith(".csv"):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        csv_reader = csv.reader(file)
                        for row_number, row in enumerate(csv_reader, 1):
                            for column_number, cell in enumerate(row, 1):
                                if target_phrase in cell:
                                    found = True
                                    print(f"Found '{target_phrase}' in {file_path} at row {row_number}, column {column_number}:")
                                    print(cell.strip())

                except Exception as e:
                    print(f"An error occurred while processing {file_path}: {str(e)}")

    if not found:
        print(f"No occurrences of '{target_phrase}' found in any CSV file.")

def main():
    while True:
        directory_path = input("Enter the directory path: ")
        target_phrase = input("Enter the target phrase: ")
        print("-" * 55)
        search_phrase_in_csv_files(directory_path, target_phrase)
        print("-" * 55)
        response = input("Press Enter to close or type 'search' to search again: ").strip().lower()
        if response != 'search':
            break

if __name__ == "__main__":
    main()