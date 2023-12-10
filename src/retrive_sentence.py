import re


def clean_text(text):
    allowed_chars = \
        "abcdefghijklmnopqrstuvwxyz" + \
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
        "\n*.,?!;:—–-()[]{}'\""
    cleaned_text = ''.join(char if char in allowed_chars else ' ' for char in text)
    return cleaned_text


def retrive_sentence(text, words):

    indices = [text.find(word) if word in text else -1 \
               for word in words]

    # Replace all non-English word characters and non-English punctuation with spaces
    cleaned_text = clean_text(text)
    
    sentences = [];
    
    for index in indices:
        
        if index == -1:
            sentences.append('')
            continue

        # Initialize sentence boundaries
        start = index
        end = index
        
        # Search backward for the start of the sentence
        while start > 0 and cleaned_text[start-1] not in '\n.?!':
            start -= 1
        if start > 0 and cleaned_text[start-1] in '.?!':
            if start < len(cleaned_text) and cleaned_text[start] in "\n\"'.,?!;:—–-)]} ":
                start += 1
                while start < len(cleaned_text) and cleaned_text[start] in "\n.,?!;:—–)]} ":
                    start += 1
        
        # Search forward for the end of the sentence
        while end < len(cleaned_text) - 1 and cleaned_text[end] not in '\n.?!':
            end += 1
        if cleaned_text[end] in '.?!':
            while end < len(cleaned_text) - 1 and cleaned_text[end+1] == '.':
                end += 1
            while end < len(cleaned_text) - 1 and cleaned_text[end+1] in ")]}\"'":
                end += 1

        # Extract the sentence and remove duplicate spaces
        sentence = re.sub(' +', ' ', cleaned_text[start:end+1].strip())
        sentences.append(sentence)
    
    return sentences


if __name__ == "__main__":
    # Example usage
    text = "嗨，It's a nice day.你好I have an apple?I have a banana."
    indices = [28, 40, 2]
    sentences = retrive_sentence(text, indices)
    letters = [text[index] for index in indices]
    print(letters)
    print(sentences)