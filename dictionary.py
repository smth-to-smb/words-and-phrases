import sqlite3

conn = sqlite3.connect('words.db')

while True:
    word = input('Enter the word: ')
    if word in ['q', 'Q']:
        break
    translation = input('Enter translation: ')
    language = input('Enter the language: ')
    insertion = 'INSERT INTO WORDS (WORD,TRANSLATION,LANGUAGE) VALUES (\'' + word + '\',' + '\'' + translation + '\',' + '\'' + language + '\')'
    conn.execute(insertion)
    conn.commit()


