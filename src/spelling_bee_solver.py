from english_words import get_english_words_set

word_set = list(get_english_words_set(['web2']))
word_set.sort()
word_set_eligible = [word for word in word_set if not word[0].isupper() and len(word) > 3]

# word_set_eligible = ['coal']
'''A function to give a list of words that can be used in the spelling
bee game'''
def spelling_bee_solver(nl, letters):
    # nl is necessary letter that must be in every word
    # letters is an array of 6 letters that can be used multiple times
    # reduce word list to only those that have nl in them
    word_set_nl = [word for word in word_set_eligible if nl in word]
    possible_words = []
    # print(type(word_set_nl))
    letters.append(nl)
    for word in word_set_nl:
        # print(word)
        eligible_word = True
        for letter in word:
            # print(letter)
            if letter not in letters:
                eligible_word = False
        # print(eligible_word)
        if eligible_word:
            possible_words.append(word)
    return possible_words

print(spelling_bee_solver('a', ['o', 'l', 'k', 'd', 'e', 'c']))
    