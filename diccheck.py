import connector
import enter


def word_check():
    words = []
    selection = connector.dict_selection()
    for row in selection:
        words.append(row[0])
    return words


def list_dictionary():
    counter = 0
    for i in word_check():
        print(i)
        counter += 1
    print('Number of words: ' + str(counter))
    inp = input('Would you like to enter new words?: ')
    if inp in ['Y', 'y', 'Д', 'д']:
        enter.word_enter()
