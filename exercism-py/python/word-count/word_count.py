def count_words(sentence):
    dt = {}
    
    # converting all punctuation except "'" to ' '
    sentence = "".join(" " if c in list('''!()-[]{};:"\,<>./?@#$%^&*_~''') else c for c in sentence )
    for word in sentence.lower().replace('\n', ' ').replace('\t', ' ').split():
        word=word.strip("'")
        dt[word] = dt[word]+1 if dt.get(word) else 1
    return dt

#print(count_words("That's the password: 'PASSWORD 123'!, cried the Special Agent.\nSo I \tfled."))

