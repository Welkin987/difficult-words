import os
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer


# Specify your custom path here
custom_nltk_path = "./data/nltk"

# Append the custom path to the nltk data path list
nltk.data.path.append(custom_nltk_path)

if not (os.path.exists(os.path.join(custom_nltk_path, 'corpora/wordnet.zip'))
    and os.path.exists(os.path.join(custom_nltk_path, 'taggers/averaged_perceptron_tagger.zip'))
    and os.path.exists(os.path.join(custom_nltk_path, 'tokenizers/punkt.zip'))):
    nltk.download('wordnet', download_dir=custom_nltk_path)
    nltk.download('averaged_perceptron_tagger', download_dir=custom_nltk_path)
    nltk.download('punkt', download_dir=custom_nltk_path)


# Mapping between part-of-speech tags and the format required by WordNetLemmatizer
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun


def lemmatize_word(word):
    lemmatizer = WordNetLemmatizer()
    pos_tagged = pos_tag(word_tokenize(word))
    
    # Since we are passing a single word, we can take the first and only tag
    word, pos = pos_tagged[0]
    wordnet_pos = get_wordnet_pos(pos)  # Get the correct part-of-speech tag
    
    # Lemmatize the word with the appropriate part-of-speech tag
    lemma = lemmatizer.lemmatize(word, pos=wordnet_pos)

    if lemma == 'didn' or lemma =='doesn':
        lemma = 'do'
    elif lemma == 'aren' or lemma =='isn' or lemma =='wasn' or lemma =='weren':
        lemma = 'be'
    elif lemma == 'hasn' or lemma =='haven' or lemma =='hadn':
        lemma = 'have'
    elif lemma == 'wouldn' or lemma =='shouldn' or lemma =='couldn' or lemma =='mustn':
        lemma = 'will'
    return lemma


if __name__ == "__main__":
    # Examples
    print(lemmatize_word("apples"))  # Output: apple
    print(lemmatize_word("went"))    # Output: go
    print(lemmatize_word("Amy's"))    # Output: Amy
