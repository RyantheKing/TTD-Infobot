import re
from collections import Counter

def candid_operations(command):
    command = command.replace('_', ' ')
    command = command.replace('~', ' ')
    command = command.replace('-', ' ')
    command = command.replace('=', ' ')
    command = command.replace('\n', ' ')
    command = command.upper()


    #-----------------------------------7
    alpha_list = command.split(' ')
    spellcheck_list = []
    alpha_char = alpha_list[0][0]
    alpha_list[0] = alpha_list[0][1:]

    if alpha_char == '!' or alpha_char == '.':
        for i in range(len(alpha_list)):
            if i == 0:
                to_append = candidates(alpha_list[i], i)
                new_append = []
                for e in range(len(to_append)):
                    new_append.append(to_append[e])
                spellcheck_list.append(new_append)
            else:
                spellcheck_list.append(candidates(alpha_list[i], i))
    return spellcheck_list

#def words(alpha_string):
    #alpha_string = alpha_string.replace('_', ' ')
    #return re.findall(r'\w+', alpha_string.lower())

def words(enter):
    regex = re.compile('[^!.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\n_-]')
    #First parameter is the replacement, second parameter is your input string
    alpha_string = (regex.sub('_', enter)).upper()
    #Out: 'abdE'
    alpha_list = alpha_string.split()
    
    return alpha_list

derpfile = words(open('commandlist.txt').read())
new_file = []
for e in range(len(derpfile)):
    new_file.append(derpfile[e].replace('_', ' '))

WORDS = list(Counter(set(new_file)))

#def candidates(word, i): 
    #"Generate possible spelling corrections for word."
    #regex = re.compile('[^a-zA-Z _-~=\n]')
    #First parameter is the replacement, second parameter is your input string
    #alpha_string = (regex.sub('', word))
    #word = alpha_string.replace('_', ' ')
    #Out: 'abdE'
    #return set(known([word], i) or known(edits1(word), i) and known(edits2(word), i) or ['None'])

def candidates(word, i): 
    "Generate possible spelling corrections for word."
    if known([word], i) == [word]:
        for i in WORDS:
            if i.startswith(word):        
                prefix_location = i.find('-')
                prefix = i[(prefix_location+1):]
                word = prefix + word
        return list(known([word], i))

    elif (known(edits1(word), i) != None) or (known(edits2(word), i) != None):
        known_list = list(set((known(edits1(word), i)) or (known(edits2(word), i))))
        for e in range(len(known_list)):
            word = known_list[e]
            for i in WORDS:
                if i.startswith(word):        
                    prefix_location = i.find('-')
                    prefix = i[prefix_location+1:]
                    if prefix != '.' and prefix != '!':
                        prefix = ''
                    word = prefix + word

            known_list[e] = word
        return known_list

    else:
        return ['None']

def known(words, i):
    "The subset of `words` that appear in the dictionary of WORDS."
    NEW_WORDS = []
    for n in WORDS:
        line = n.split()
        for i in line:
            if i[-2:].startswith('-'):
                NEW_WORDS.append(i[:-2])
            else:
                NEW_WORDS.append(i)
    return set(w for w in words if w in NEW_WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(e.upper() for e in (deletes + transposes + replaces + inserts))

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

def edits3(word):
    return (e3 for e1 in edits1(word) for e2 in edits1(e1) for e3 in edits1(e2))

def edits4(word):
    return (e4 for e1 in edits1(word) for e2 in edits1(e1) for e3 in edits1(e2) for e4 in edits1(e3))
