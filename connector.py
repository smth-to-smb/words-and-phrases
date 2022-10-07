import sqlite3

conn = sqlite3.connect('words.db')


def dict_selection():
    return conn.execute('SELECT WORD from WORDS WHERE LANGUAGE = \'English\';')


def dict_insertion(word, translation, language):
    insertion = 'INSERT INTO WORDS (WORD,TRANSLATION,LANGUAGE) VALUES (\'' + word + '\',' + '\'' + translation + '\',' + '\'' + language + '\')'
    conn.execute(insertion)
    conn.commit()

