import connector
import diccheck

while True:
    dictionary = diccheck.word_check()
    word = input('Enter the word: ')
    if word in ['q', 'Q', 'й', 'Й']:
        break
    if word in dictionary:
        print('This word is already contained in the dictionary!')
        continue
    translation = input('Enter translation: ')
    language = input('Enter the language (1 for English, 2 for German): ')
    if language == '1':
        language = 'English'
    elif language == '2':
        language = 'German'
    connector.dict_insertion(word, translation, language)



