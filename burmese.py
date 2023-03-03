import string

burmese_characters = {
    "Consonants" : ['က', 'ခ', 'ဂ', 'ဃ', 'င',
                   'စ', 'ဆ', 'ဇ', 'ဈ', 'ဉ', 'ည',
                   'ဋ', 'ဌ', 'ဍ', 'ဎ', 'ဏ',
                   'တ', 'ထ', 'ဒ', 'ဓ', 'န',
                   'ပ', 'ဖ', 'ဗ', 'ဘ', 'မ',
                   'ယ', 'ရ', 'လ', 'ဝ', 'သ',
                   'ဟ', 'ဠ', 'အ'],
    
    "Medials 1" : ['ျ', 'ြ'],
    "Medials 2" : ['ွ', 'ှ'],
    
    "Initial Vowels" : ['ေ'],
    "Mid Vowels 1" : ['ာ', 'ါ'],
    "Mid Vowels 2" : ['ဲ'],
    "Mid Vowels 3" : ['ီ', 'ူ'],
    "Mid Vowels 4" : [ 'ိ'],
    "Mid Vowels 5" : ['ု'],
    "Mid Vowels 6" : ['ံ' ],
    "Final Vowels 1" : ['း'],
    "Final Vowels 2" : ['့'],
    "Independent Vowels 1" : ['ဤ', 'ဥ', 'ဧ', 'ဩ', 'ဪ'],
    "Independent Vowels 2" : ['ဣ'], 
    "Independent Vowels 3" : ['ဦ'],
    
    "Virama" : ['္'],
    "Asat" : ['်'],
    
    "Independent Syllables" : ['၌', '၍', '၏'],
    "Great Tha" : ['ဿ'],
    "Variuous Sign" : ['၎'],
    
    "Digits" : ['၀', '၁', '၂', '၃', '၄', '၅', '၆', '၇', '၈', '၉'],
    "Punctuations" : ['၊', '။', '’'] + list(string.punctuation)
}

START = 0 # ^
CONSONANT = 1 # C
MEDIAl_1 = 2 # M1
MEDIAl_2 = 3 # M2
INITIAL_VOWEL = 4 # V1
MID_VOWEL_1 = 5 # V2
MID_VOWEL_2 = 6 # V3
MID_VOWEL_3 = 7 # V4
MID_VOWEL_4 = 8 # V5
MID_VOWEL_5 = 9 # V6
MID_VOWEL_6 = 10 # V7
FINAL_VOWEL_1 = 11 # V8
FINAL_VOWEL_2 = 12 # V9
INDEPENDENT_VOWEL_1 = 13 # IV1
INDEPENDENT_VOWEL_2 = 14 # IV2
INDEPENDENT_VOWEL_3 = 15 # IV3
VIRAMA = 16 # V
ASAT = 17 # A
INDEPENDENT_SYLLABLE = 18 # IS
GREAT_THA = 19 # T
VARIOUS_SIGN = 20 # VS
DIGIT = 21 # D
PUNCTUATION = 22 # P

writing_order = [  
    #       M  M  V  V  V  V  V  V  V  V  V IV IV IV        I     V
    # ^  C  1  2  1  2	3  4  5  6  7  8  9  1  2  3  V  A  S  T  S  D  P 
    [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1 ], # ^
    [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ], # C
    [ 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # M1
    [ 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # M2
    [ 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # V1
    [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ], # V2
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # V3
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # V4
    [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # V5
    [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # V6
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # V7
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # V8
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # V9
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # IV1
    [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # IV2
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # IV3
    [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # V
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ], # A
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # IS
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # T
    [ 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # VS
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0 ], # D
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] # P
 ]

confusion_writing_set = {
    "ဦ" : "ဦ", # [ ဥ + ီ ](သရ ဥ + လုံးကြီးတင်) Vs [ ဦ ](သရ ဦ)
    "ဥ်" : "ဉ်" # [ ဥ + ် ](သရ ဥ + အသတ်) Vs [ ဉ + ် ](ညကလေး + အသတ်)
}


def category(character):
    char_type = -1
    
    if character >= u'\u1000' and character <= u'\u109f' or character in burmese_characters["Punctuations"]: 
        for k, v in burmese_characters.items():
            if character in v:
                if k == 'Consonants': char_type = CONSONANT
                elif k == 'Medials 1': char_type = MEDIAl_1
                elif k == 'Medials 2': char_type = MEDIAl_2
                elif k == 'Initial Vowels': char_type = INITIAL_VOWEL
                elif k == 'Mid Vowels 1': char_type = MID_VOWEL_1
                elif k == 'Mid Vowels 2': char_type = MID_VOWEL_2
                elif k == 'Mid Vowels 3': char_type = MID_VOWEL_3
                elif k == 'Mid Vowels 4': char_type = MID_VOWEL_4
                elif k == 'Mid Vowels 5': char_type = MID_VOWEL_5
                elif k == 'Mid Vowels 6': char_type = MID_VOWEL_6
                elif k == 'Final Vowels 1': char_type = FINAL_VOWEL_1
                elif k == 'Final Vowels 2': char_type = FINAL_VOWEL_2
                elif k == 'Independent Vowels 1': char_type = INDEPENDENT_VOWEL_1
                elif k == 'Independent Vowels 2': char_type = INDEPENDENT_VOWEL_2
                elif k == 'Independent Vowels 3': char_type = INDEPENDENT_VOWEL_3
                elif k == 'Virama': char_type = VIRAMA
                elif k == 'Asat': char_type = ASAT
                elif k == 'Independent Syllables': char_type = INDEPENDENT_SYLLABLE
                elif k == 'Great Tha': char_type = GREAT_THA
                elif k == 'Various Sign': char_type = VARIOUS_SIGN
                elif k == 'Digits': char_type = DIGIT
                elif k == 'Punctuations': char_type = PUNCTUATION
                 
    return  char_type


def count(syllable, type):
    return len([ch for ch in syllable if ch in burmese_characters[type]])

def is_digit(syllable):
    for s in syllable:
        if s not in burmese_characters["Digits"]: return False
    return True

def is_punctuation(syllable):
    return len(syllable) == 1 and syllable in burmese_characters["Punctuations"]

def valid(syllable):
    if count(syllable, "Consonants") == 0:
        if category(syllable[0]) not in [INDEPENDENT_VOWEL_1, INDEPENDENT_VOWEL_2, INDEPENDENT_VOWEL_3, INDEPENDENT_SYLLABLE, DIGIT, PUNCTUATION]:
            return False
    return True

def asat_structure(syllable):
    stack = []
    for ch in syllable:
        if ch in burmese_characters["Consonants"] or ch == "ေ":
            stack.append(ch)
        elif ch == "်":
            if len(stack) <= 0: return False
            stack.pop()
            if len(stack) <= 0: return False
            stack.pop()
    return True
