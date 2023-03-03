import random

import burmese
import dictionary
import tokenization
import my_string


def generatePossibleSyllables(syllable):
    possible_syllables = set()
    for pos in dictionary.POS:
        words = dictionary.find_possible(syllable, pos)
        if words: possible_syllables = possible_syllables.union(set(words))
    return possible_syllables


def typo(syllables):
    # Check sequence and typographical errors
    # Return fixed syllables along with observed misspelled syllables
    fixed = []
    errors = []
    for syl in syllables:
        if burmese.is_digit(syl) or burmese.is_punctuation(syl): 
            fixed.append(syl)
            continue
        if not burmese.valid(syl): 
            if "ီ" in syl and syllables.index(syl) > 0 and fixed[-1] == "ဥ":
                syl = "ဦ" + syl
                fixed.pop()
            else: continue

        copy_syl = syl
        for i in range(len(copy_syl)):
            if i == len(copy_syl): break 
            prev = 0
            if i > 0: prev = burmese.category(copy_syl[i-1])
            current = burmese.category(copy_syl[i])
            if burmese.writing_order[prev][current] == 0:
                # check whether previous and current are swapped or not
                if burmese.writing_order[current][prev] == 1:
                    copy_syl = my_string.swap(copy_syl, i-1, i)
                else:
                    # check next and current
                    if i < len(copy_syl) - 1:
                        post = burmese.category(copy_syl[i+1])
                        if burmese.writing_order[prev][post] == 1:
                            if burmese.writing_order[post][current] == 1:
                                copy_syl = my_string.swap(copy_syl, i, i+1)
                            else:
                                copy_syl = my_string.drop(copy_syl, i)
                        else:
                            copy_syl = my_string.drop(copy_syl, i)
                    else:
                        copy_syl = my_string.drop(copy_syl, i)
        if copy_syl is syl: fixed.append(syl)
        else:
            errors.append((syl, [copy_syl]))
            fixed.append(copy_syl)
    return (fixed, errors)


def misspelled(word, errors):
    for (err, p_words) in errors:
        if word in p_words: return True
    return False


def fix_backward(err_word, sim_words, fixed_words, errors, unknown):
    potential_words = []
    for sw in sim_words:
        break_index = 0
        max_word = sw
        tmp = sw
        for i in range(len(fixed_words)-1, -1, -1):
            if burmese.is_digit(fixed_words[i]) or burmese.is_punctuation(fixed_words[i]) or fixed_words[i] in unknown or misspelled(fixed_words[i], errors):
                break
            tmp = fixed_words[i] + tmp
            if dictionary.exists(tmp):
                max_word = tmp
                break_index = len(fixed_words) - i
        if max_word != sw:
            potential_words.append((max_word, break_index))

    return potential_words


def phonetic(words):
    fixed = []
    errors = []
    unknown = []
    for word in words:
        if burmese.is_digit(word) or burmese.is_punctuation(word) or dictionary.exists(word):
            fixed.append(word)
        else:
            sim_words = dictionary.find_similar(word, distance=2)
            if sim_words:
                potential_words = fix_backward(word, sim_words, fixed, errors, unknown)
                if potential_words:
                    (p_word, break_index) = random.choice(potential_words)
                    err_word = word
                    for i in range(break_index):
                        err_word = fixed.pop() + err_word
                    errors.append((err_word, [p_word]))
                    fixed.append(err_word)
                else:
                    errors.append((word, sim_words))
                    fixed.append(word)
            else: 
                fixed.append(word)
                unknown.append(word)
    return (fixed, errors, unknown)


def check(text):
    words = []
    typo_err = []
    phonetic_err = []
    unknown = []
    sentences = tokenization.to_sentences(text)
    for sent in sentences:
        syllables = tokenization.syllable(sent)
        syllables = tokenization.preprocessing(syllables)
        (fixed, l_typo_err) = typo(syllables)
        if l_typo_err:
            syllables = fixed
        l_words = tokenization.word(syllables)
        (fixed, l_phonetic_err, l_unknown) = phonetic(l_words)
        words += fixed
        typo_err += l_typo_err
        phonetic_err += l_phonetic_err
        unknown += l_unknown

    return (tokenization.remove_punctuations(words), typo_err, phonetic_err, unknown)


if __name__ == "__main__":
    print("Myanmar Spell Checker")
