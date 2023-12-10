import csv


def read_word_frequency(file_path='./data/words_list.csv'):
    words_order = [];
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            word, freq = row[0].split()
            words_order.append(word)
    return words_order


words_order = read_word_frequency()


def lookup_freq(words):
    # Create a list of ranks for each word
    ranks = [10000000 if not word in words_order else (words_order.index(word) + 1)
              for word in words]
    return ranks


if __name__ == "__main__":
    # Example usage
    words_to_lookup = ['apple', 'orange', 'is']
    result = lookup_freq(words_to_lookup)
    print(result)

