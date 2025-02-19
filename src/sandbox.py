from english_words import get_english_words_set

word_set = list(get_english_words_set(['web2']))
word_set.sort()
word_set_no_caps = [word for word in word_set if not word[0].isupper()]
word_set_min_4 = [word for word in word_set if not word[0].isupper() and len(word) > 3]

print(len(word_set))
print(len(word_set_no_caps))
print(len(word_set_min_4))


print(word_set[10])
print(word_set_no_caps[10])
print(word_set_min_4[10])

test_word = 'test'
letters = ['t','e','s']
possible_words = []
eligible_word = True
for letter in test_word:

    if letter not in letters:
        eligible_word = False
if eligible_word:
    possible_words.append(test_word)

print(possible_words)