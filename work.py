import rupostagger
import re

tagger = rupostagger.RuPosTagger()
tagger.load()
file1 = open("C:\\Users\\Andrey\\Downloads\\rupostagger-master\\test.txt", "r", encoding="UTF-8")

counter_words = 0
counter_nouns = 0
counter_adjs = 0
counter_verbs = 0
counter_prons = 0
counter_advs = 0
counter_preps = 0
counter_nums = 0
counter_parts = 0
counter_conjs = 0
counter_others = 0

while True:
    line = file1.readline()

    if not line:
        break

    opt = re.sub(r'[^\w\s]', '', line)
    print(line)

    for word, label in tagger.tag(opt.split()):
        print(u'{} -> {}'.format(word, label))
        counter_words = counter_words + 1

        if (label.startswith("NOUN")):
            counter_nouns = counter_nouns + 1

        elif (label.startswith("ADJ")):
            counter_adjs = counter_adjs + 1

        elif (label.startswith("VERB")):
            counter_verbs = counter_verbs + 1

        elif (label.startswith("PRON")):
            counter_prons = counter_prons + 1

        elif (label.startswith("ADV")):
            counter_advs = counter_advs + 1

        elif (label.startswith("ADP")):
            counter_preps = counter_preps + 1

        elif (label.startswith("NUM")):
            counter_nums = counter_nums + 1

        elif (label.startswith("PART")):
            counter_parts = counter_parts + 1

        elif (label.startswith("CONJ")):
            counter_conjs = counter_conjs + 1

        else:
            counter_others = counter_others + 1

    print()

print("Частота существительных {:.2f} %".format(counter_nouns / counter_words * 100))
print("Частота прилагательных {:.2f} %".format(counter_adjs / counter_words * 100))
print("Частота глаголов {:.2f} %".format(counter_verbs / counter_words * 100))
print("Частота местоимений {:.2f} %".format(counter_prons / counter_words * 100))
print("Частота наречий {:.2f} %".format(counter_advs / counter_words * 100))
print("Частота предлогов {:.2f} %".format(counter_preps / counter_words * 100))
print("Частота числительных {:.2f} %".format(counter_nums / counter_words * 100))
print("Частота частиц {:.2f} %".format(counter_parts / counter_words * 100))
print("Частота союзов {:.2f} %".format(counter_conjs / counter_words * 100))
print("Частота других частей речи {:.2f} %".format(counter_others / counter_words * 100))