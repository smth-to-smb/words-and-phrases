import connector


def word_check():
    words = []
    selection = connector.dict_selection()
    for row in selection:
        words.append(row[0])
    return words

