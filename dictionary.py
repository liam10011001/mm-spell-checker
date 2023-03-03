import tokenization as t
import my_string
import burmese
import os

POS = ['nouns', 'pronouns', 'adjectives', 'verbs', 'adverbs', 'postpositions', 'conjunctions', 'particles', 'interjections']

def generate_file_name(alphabet):
    vowels = ['ဣ', 'ဤ', 'ဥ', 'ဦ', 'ဧ', 'ဩ', 'ဪ']
    signs = ['၌', '၍', '၎', '၏']
    if burmese.category(alphabet) == burmese.CONSONANT:
        code = ord(alphabet) - ord('က') + 1
        return  "C" + "{:02n}".format(code) + ".txt"
    elif burmese.category(alphabet) == burmese.GREAT_THA:
        return  "C" + "{:02n}".format(35) + ".txt"
    elif burmese.category(alphabet) == burmese.INDEPENDENT_VOWEL_1 or burmese.category(alphabet) == burmese.INDEPENDENT_VOWEL_2 or burmese.category(alphabet) == burmese.INDEPENDENT_VOWEL_3:
        code = vowels.index(alphabet) + 1
        return  "V" + "{:02n}".format(code) + ".txt"
    elif burmese.category(alphabet) == burmese.INDEPENDENT_SYLLABLE or burmese.category(alphabet) == burmese.VARIOUS_SIGN:
        code = signs.index(alphabet) + 1
        return  "S" + "{:02n}".format(code) + ".txt"
    else:
        return False


def find(word, file_path, exact=True, same_initial=False, distance_function=my_string.minimum_edit_distance, distance=2):
    try:
        if os.path.exists(file_path):
            words = []
            with open(file_path, 'r', encoding="utf-8") as f:
                if exact:
                    words = [line.strip() for line in f.readlines() if line.strip() == word]
                else:
                    if same_initial:
                        words = [line.strip() for line in f.readlines() if line.startswith(word)]
                    else:
                        words = [line.strip() for line in f.readlines() if distance_function(word, line.strip()) <= distance]
            return words
        return False
    except:
        return False


def find_similar(word, pos="ALL", distance_function=my_string.minimum_edit_distance, distance=2):
    fname = generate_file_name(word[0])
    if not fname: return False
    
    words = []
    if pos == "ALL":
        for dir in POS:
            file_path = "/".join(["words", dir, fname])
            tmp = find(word, file_path, exact=False, distance_function=distance_function, distance=distance)
            if tmp:
                words.extend(tmp)
    else:
        file_path = "/".join(["words", pos, fname])
        words = find(word, file_path, exact=False, distance_function=distance_function, distance=distance)
    return words


def find_start_with(syllable, pos="ALL"):
    fname = generate_file_name(syllable[0])
    if not fname: return False
    
    words = []
    if pos == "ALL":
        for dir in POS:
            file_path = "/".join(["words", dir, fname])
            tmp = find(syllable, file_path, exact=False, same_initial=True)
            if tmp:
                words.extend(tmp)
    else:
        file_path = "/".join(["words", pos, fname])
        words = find(syllable, file_path, exact=False, same_initial=True)
    return words


def find_exact(word, pos="ALL"):
    fname = generate_file_name(word[0])
    if not fname: return False
    
    words = []
    if pos == "ALL":
        for dir in POS:
            file_path = "/".join(["words", dir, fname])
            tmp = find(word, file_path, exact=True)
            if tmp:
                words.extend(tmp)
    else:
        file_path = "/".join(["words", pos, fname])
        words = find(word, file_path, exact=True)
    return words


def exists(word):
    fname = generate_file_name(word[0])
    if not fname: return False
    for dir in POS:
        file_path = "/".join(["words", dir, fname])
        if find(word, file_path, exact=True): return True
    return False
    

def find_possible(word, pos):
    alp = ''
    for ch in word:
        if ch in burmese.burmese_characters["Consonants"] or ch in burmese.burmese_characters["Independent Vowels 1"] or ch in burmese.burmese_characters["Independent Vowels 2"] or ch in burmese.burmese_characters["Independent Vowels 3"] or ch in burmese.burmese_characters["Independent Syllables"] or ch in burmese.burmese_characters["Variuous Sign"] or ch in burmese.burmese_characters["Great Tha"]:
            alp = ch
    fname = generate_file_name(alp)
    if not fname: return False

    file_path = "/".join(["words", pos, fname])
    try:
        p_words = []
        with open(file_path, 'r', encoding="utf-8") as f:
            p_words = [line.strip() for line in f.readlines() if len(word) == len(line.strip()) and hasSameCharacters(word, line.strip())]
        return p_words
    except:
        return False


def find_pos(pos):
    try:
        words = []
        dir = "words/" + pos + "/"
        files = os.listdir(dir)
        for f_name in files:
            with open(dir + f_name, 'r', encoding='utf-8') as f:
                words += [line.strip() for line in f.readlines()]
        return words
    except:
        return False
    
def conjunctions(): return find_pos("conjunctions")
def interjections(): return find_pos("interjections")
def particles(): return find_pos("particles")
def postpositions(): return find_pos("postpositions")
def pronouns(): return find_pos("pronouns")
