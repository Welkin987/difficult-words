def clean_text(text):
    allowed_chars = \
        "abcdefghijklmnopqrstuvwxyz" + \
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cleaned_text = ''.join(char if char in allowed_chars else ' ' for char in text)
    return cleaned_text


def my_split(text):
    # Replace characters not in A-Z or a-z with a space
    cleaned_text = clean_text(text)

    # Split the text into a list of words
    words = cleaned_text.split()

    # Remove words with length <= 2
    filtered_words = [word for word in words if len(word) > 2]
    return filtered_words


if __name__ == "__main__":
    # Example usage:
    text = "This is a test 文本, with some English and 中文 characters 123."
    result = my_split(text)
    print(result)  # Output should be ['This', 'test', 'with', 'some', 'English', 'and', 'characters']
