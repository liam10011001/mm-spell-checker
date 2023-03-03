import tokenization
import spelling_checker as sc
import dictionary
import my_string

def similarity_test():
    test = [
        ("Cats", "Rats"),
        ("intention", "execution"),
        ("ကျောင်း", "ကြောင်"),
        ("ကြောင်စာ", "ကြောင်"),
        ("ကြောင့်", "ကြောင့်")
    ]
    for (s, t) in test:
        print(s, "->", t)
        print("Minimum Edit Distance :", my_string.minimum_edit_distance(s, t))
        print("Levenshtein Distance :", my_string.lev(s, t))
        print()


def dictionary_test():
    querry = [
        "ကြောင်", "ကြောင်စာ",
        "ကူးသန်း", "ရောင်းဝယ်", "ကူးသန်းရောင်းဝယ်", # ပေါင်းစပ်ကြိယာ
        "သာယာ", "လှပ", "သာယာလှပ", # ပေါင်းစပ်နာမဝိသေသန
        "ပဲ့ကိုင်", "ဝင်ငွေ", # နာမ် + ကြိယာ
        "အခိုင်အမာ", "သစ်ပင်", "ပန်းပင်", "သစ်ပင်ပန်းပင်", "ဥ", "ဦ",
    ]

    for q in ["တဲ့", "ဆင့်", "စိမ့်", "ထည့်", "ကြောင့်", "မယ့်", "ဖြင့်", "အထူးသဖြင့်"]:
        print(q)
        result = dictionary.find_exact(q)
        if result:
            print(len(result), "word(s) found")
            if result:
                for word in result:
                    print(word)
            print()
        else:
            print("Can't find exact word for", q)
            result = dictionary.find_similar(q) + dictionary.find_start_with(q)
            if result:
                print(len(result), "word(s) is/are similar with", q)
                for word in result:
                    if my_string.have_same_characters(word, q):
                        for ch in word: print(ch, end="-")
                        print(end="\n")
                    print(word)
            else:
                print("No similar word(s) with", q)
            print()
        
    
    for q in querry:
        print(q)
        result = dictionary.find_exact(q)
        if result:
            print(len(result), "word(s) found")
            if result:
                for word in result:
                    print(word)
            print()
        else:
            print("Can't find exact word for", q)
            result = dictionary.find_similar(q, distance=1) + dictionary.find_start_with(q)
            if result:
                print(len(result), "word(s) is/are similar with", q)
                for word in result:
                    print(word)
            else:
                print("No similar word(s) with", q)
            print()
    

def file_test():
    for i in range(1, 3):
        fdir = "../text/"
        name = "T" + "{:03n}".format(i) + ".txt"
        file_path = fdir + name

        with open (file_path, 'r', encoding="utf-8") as f:
            text = f.read()
            (words, typo_err, phonetic_err, unknown) = sc.check(text)
            print(tokenization.count(words), "word(s) detected")
            print(tokenization.remove_punctuations(words))
            if typo_err:
                print(len(typo_err), "typo(s) found")
                for err in typo_err:
                    print(err)
            if phonetic_err:
                print(len(phonetic_err), "misspelled word(s) found")
                for err in phonetic_err: print(err)
            if unknown:
                print(len(unknown), "unverifiable word(s) found")
                print(unknown)
            print()
            
        break


def test():
    text = ["ကြောင်စာ ကျွေးနေသည်။ ငါးကြော် ယူလာခဲ့ပါ။",
            "မနက်ဖန် မနက် ကျောင်းသွားမည်",
            "၃ပိဿာ ၂၅ကျပ်သား",
            "၂နာရီ၃၅မိနစ်",
            "ဟနွိုင်း၊ ကမ္ဘောဒီးယား၊ ပခုက္ကူ၊ စက္ကူ၊ သင်္ကြန် ပြဿနာ",
            "နျူကလီးယား", "သူနာပျု",
            "အမိုးနီးယားဓာတ်ငွေ့နဲ့ ထိတွေ့မိခြင်းအတွက် ရှေးဦးသူနာပျုနည်းလမ်း",
            "သဘာဝဟာသဘာဝပါ။",
            "အမိုးနီးယားက ခန္ဓာကိုယ်ထဲကို ပုံစံသုံးမျိုးနဲ့ ဝင်ရောက်နိုင်ပါတယ်။ ဓာတ်ငွေ့ကို ရှူမိတာ၊ မျိုချတာနဲ့ အရေပြားနဲ့ ထိတွေ့မိတာတွေကပါ။"]

    for t in text:
        print(t)
        (words, typo_err, phonetic_err, unknown) = sc.check(t)
        print(tokenization.count(words), "word(s) detected")
        print(tokenization.remove_punctuations(words))
        if typo_err:
            print(len(typo_err), "typo(s) found")
            print(typo_err)
        if phonetic_err:
            print(len(phonetic_err), "misspelled word(s) found")
            print(phonetic_err)
        if unknown:
            print(len(unknown), "unverifiable word(s) found")
            print(unknown)
        print()
        

def typo_error_test():
    test_str = ["စာသင်ကျောင်း","ကြောင့်", "ကြောင့်", "ခုိ၊",
                "ေစ","ချုိး", "ကားး", "ကာ့း", "ကေေ",
                "ကာု", "ကော််", "၁၁ာ", "ခတ္တာာ", "ကာ်",
                "ကေတ်", "မြင့်မိုရ်", "ူေ်ေညန",
                "အမိုးနီးယားဓာတ်ငွေ့နဲ့ ထိတွေ့မိခြင်းအတွက် ရှေးဦးသူနာပြုနည်းလမ်း",
                "ဦး", "ဦး"]
    for t in test_str:
        sentences = tokenization.to_sentences(t)
        syl = []
        for s in sentences:
            syl += tokenization.syllable(s)
        print("Syllables :", syl) 
        syl = tokenization.preprocessing(syl)
        print("Preprocessed :", syl)
        fixed, errors = sc.typo(syl)
        if errors:
            print(len(errors), "typing error(s) found")
            for error, possible in errors:
                print("Error : ", error, "Possible syllable(s) :", possible)
            print("Fixed :", fixed)
        print()


if __name__ == "__main__":
    (words, typo, phonetic, unknown) = sc.check("ကိုယ့်၊ ကြည့်၊ ဖြင့်")

    print(words, typo, phonetic, unknown)
    print("Welcome to Myanmar Spell Checker", 
    "Enter -",
    "1 - to check dictionary",
    "2 - to check string similarity",
    "3 - to test typographic error",
    "4 - to run general spelling check",
    "5 - to check spelling error in files",
    "0 - to terminate",
    sep="\n")
    print(sep=" ")

    choice = input(">>> ").strip()
    while choice:
        if choice.isnumeric():
            if int(choice) == 0: break
            elif int(choice) == 1: dictionary_test()
            elif int(choice) == 2: similarity_test()
            elif int(choice) == 3: typo_error_test()
            elif int(choice) == 4: test()
            elif int(choice) == 5: file_test()
        choice = input(">>> ").strip()

    
