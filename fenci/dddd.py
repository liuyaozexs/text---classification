from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

# 词还原
wnl = WordNetLemmatizer()
print(wnl.lemmatize('countries'))
# 词干
stemmer = SnowballStemmer("english") # Choose a language
print(stemmer.stem("watches")) # Stem a word