import csv


def read_text(input_path='./input.txt'):
    with open(input_path, 'r', encoding='u8') as f:
        text = f.read()
    return text


def write_words(output_list, output_path='./output.csv'):
    # Define the header for the CSV file
    header = ['word', 'real_word', 'index', 'rank', 'count','sentence']

    # Write the data to the CSV file
    with open(output_path, 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.DictWriter(csvfile, fieldnames=header)

        # Write the header row
        csv_writer.writeheader()

        # Write each item in the output_list as a row in the CSV file
        csv_writer.writerows(output_list)
        
