import sqlite3

conn = sqlite3.connect('words.db')

while True:
    word = input('Enter the word: ')
    if word in ['q', 'Q']:
        break
    translation = input('Enter translation: ')
    language = input('Enter the language (1 for English, 2 for German): ')
    if language == '1':
        language = 'English'
    elif language == '2':
        language = 'German'
    insertion = 'INSERT INTO WORDS (WORD,TRANSLATION,LANGUAGE) VALUES (\'' + word + '\',' + '\'' + translation + '\',' + '\'' + language + '\')'
    conn.execute(insertion)
    conn.commit()


