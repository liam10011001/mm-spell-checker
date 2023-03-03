import re
import random

import burmese
import dictionary
import my_string


def syllable(sentence):
    syllables = []
    syllable = ''

    for i in range(len(sentence)):
        current_ch = sentence[i]    
        if burmese.category(current_ch) > burmese.START:

            # 1 - find a consonant and assume all the consequennce characters are in the syllable until second or thrid consonant appears
            if burmese.category(current_ch) == burmese.CONSONANT:
                if not syllable: syllable = current_ch # start of new syllable 
                else:
                    post_ch = sentence[i+1]
                    if burmese.category(post_ch) == burmese.VIRAMA or burmese.category(post_ch) == burmese.ASAT:
                        # contian in the syllable
                        syllable += current_ch
                    else:
                        # start of new syllable
                        syllables.append(syllable)
                        syllable = current_ch
                    
            # 2 - syllable ending with Asat and Virama
            elif burmese.category(current_ch) == burmese.VIRAMA:
                syllable += current_ch
                syllables.append(syllable)
                syllable = ''
                
            elif burmese.category(current_ch) == burmese.ASAT:
                syllable += current_ch
                post_ch = sentence[i+1]
                if not burmese.category(post_ch) == burmese.FINAL_VOWEL_1 and not burmese.category(post_ch) == burmese.FINAL_VOWEL_2 and not burmese.category(post_ch) == burmese.VIRAMA:
                    syllables.append(syllable)
                    syllable = ''
                
            # 3 - independent signs and vowels stand alone
            elif burmese.category(current_ch) == burmese.INDEPENDENT_SYLLABLE or burmese.category(current_ch) == burmese.INDEPENDENT_VOWEL_1:
                if syllable: syllables.append(syllable)
                syllables.append(current_ch)
                syllable = ''
                
            # 4 - special independent vowels
            elif burmese.category(current_ch) == burmese.INDEPENDENT_VOWEL_3 or burmese.category(current_ch) == burmese.GREAT_THA:
                if syllable: syllables.append(syllable)
                syllable = current_ch  
                
            # 5 - Digits
            elif burmese.category(current_ch) == burmese.DIGIT:  
                # check if it is a part of squenece of digits or not     
                if not syllable: syllable = current_ch
                else:
                    pre_ch = sentence[i-1]
                    if burmese.category(pre_ch) == burmese.DIGIT: syllable += current_ch
                    else:
                        syllables.append(syllable)
                        syllable = current_ch
                    if not burmese.category(sentence[i+1]) == burmese.DIGIT: 
                        syllables.append(syllable)
                        syllable = ''

            # 6 - Punctuations
            elif burmese.category(current_ch) == burmese.PUNCTUATION:
                if syllable: syllables.append(syllable)
                syllables.append(current_ch)
                syllable = ''
            else:
                syllable += current_ch
        else:
            if syllable:
                syllables.append(syllable)
                syllable = ''
                 
    return syllables


def preprocessing(syllables):
    ''' restructuring the syllables '''
    new_syllables = []
    i = 0
    while i < len(syllables):
        syl = syllables[i]
        if burmese.category(syl[-1]) == burmese.VIRAMA and i < len(syllables)-1:
            new_syllables.append(syl + syllables[i+1])
            i += 2
            continue
        elif "်" in syl and not burmese.asat_structure(syl):
            if len(new_syllables) > 0 and "်" not in new_syllables[-1]:
                pre = new_syllables.pop()
                new_syllables.append(pre + syl)
                i += 1
                continue
        elif "ေ" in syl and burmese.count(syl, "Consonants") == 0:
            if i < len(syllables)-1 and burmese.count(syllables[i+1], "Consonants") > 0:
                new_syllables.append(syl + syllables[i+1])
                i += 2
                continue

        new_syllables.append(syl)
        i += 1

    return new_syllables


def to_sentences(paragraph):
    sents = re.split(r'။|\\n', paragraph)
    return [s.strip()+"။" for s in sents if s]


def remove_punctuations(words):
    return [w for w in words if not burmese.is_punctuation(w)]


def merge(syllables, words):
    #print(syllables)
    if len(syllables) < 1: return False
    tmp_word = "".join(syllables)
    d_words = dictionary.find_exact(tmp_word)
    if d_words:
        #print(d_words)
        return (d_words, len(syllables))
    else:
        if len(syllables) == 1: return (syllables, 1)
        else: return merge(syllables[:-1], words)


def word(syllables):
    postpositions = dictionary.postpositions()
    # split into phrases
    words = []
    break_point = 0
    for i in range(len(syllables)):
        # split and merge into words
        if burmese.is_digit(syllables[i]) or burmese.is_punctuation(syllables[i]):
            phrase = syllables[break_point:i]
            start = 0
            while start < len(phrase):
                (p_words, index) = merge(phrase[start:], [])
                ##print("Possible words :", p_words)
                words.append(random.choice(p_words))
                start += index
            words.append(syllables[i])
            break_point = i+1
    
    return words

def count(words):
    return len(remove_punctuations(words))