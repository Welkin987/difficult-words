import read_and_write
import my_split
import base_form
import lookup_rank
import retrive_sentence

import argparse


def parse_parameters():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Process some parameters.')

    # Add command-line arguments
    parser.add_argument('--input', default='./input.txt', help='Input file path, default is ./input.txt')
    parser.add_argument('--output', default='./output.csv', help='Output file path, default is ./output.csv')
    parser.add_argument('--threshold', default=10000, type=int, help='Threshold for word rank, default is 10000')
    parser.add_argument('--sort_by', default='rank', help='Sort by rank, count or index, default is rank')

    # Parse the command-line arguments
    args = parser.parse_args()

    return args.input, args.output, args.threshold, args.sort_by


def main(threshold, input_path='./input.txt', output_path='./output.csv', \
         sort_by='rank'):
    text = read_and_write.read_text(input_path)
    real_words = my_split.my_split(text)
    words = [word.lower() for word in real_words]
    words = [base_form.lemmatize_word(word) for word in words]
    
    unique_dict = {}
    for i, (real_word, word) in enumerate(zip(real_words, words)):
        if word not in unique_dict:
            unique_dict[word] = {
                'word': word,
                'real_word': real_word, 
                'index': i, 
                'count': 1}
        else:
            unique_dict[word]['count'] += 1

    # Extract unique elements
    words = unique_dict.keys()
    ranks = lookup_rank.lookup_freq(words)

    # Filter out words with rank < threshold
    valid_dict = {}
    for i, word in enumerate(words):
        if ranks[i] >= threshold:
            valid_dict[word] = unique_dict[word]
            valid_dict[word]['rank'] = ranks[i]

    # Retrive sentences
    words = valid_dict.keys()
    real_words = [valid_dict[word]['real_word'] for word in words]
    sentences = retrive_sentence.retrive_sentence(text, real_words)
    for word, sentence in zip(words, sentences):
        valid_dict[word]['sentence'] = sentence

    # Sort the dictionary by rank, if if_sort is True, otherwise by index
    if sort_by == 'count':
        sorted_list = sorted(valid_dict.values(), key=lambda x: x['count'], reverse=True)
    elif sort_by in ['rank', 'index']:
        sorted_list = sorted(valid_dict.values(), key=lambda x: x[sort_by])
    else:
        sorted_list = sorted(valid_dict.values(), key=lambda x: x['rank'])

    # Save the result to a file
    read_and_write.write_words(sorted_list, output_path)

if __name__ == "__main__":
    input_path, output_path, threshold, sort_by = parse_parameters()
    main(threshold, input_path, output_path, sort_by)