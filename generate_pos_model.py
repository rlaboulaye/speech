import random
 
training_file_name = 'pos_train.txt'
training_data = open(training_file_name).read()

def get_dict_total(dic):
    total = 0
    for key in dic:
        total += dic[key]
    return total

# Transition function from pos to pos
F = {}
F_context = [""]

# Transition function from pos to word observation
H = {}
H_context = ""

for labelled_word in training_data.split():
    labelled_word_arr = labelled_word.split('_')
    word = labelled_word_arr[0]
    pos = labelled_word_arr[1]

    transition_dict = F.setdefault(str(F_context),{})
    transition_dict[pos] = transition_dict.setdefault(pos, 0) + 1
    F_context = (F_context + [pos])[1:]

    H_context = pos
    transition_dict = H.setdefault(H_context, {None: 1})
    transition_dict[word] = transition_dict.setdefault(word, 0) + 1


#print(F)
#print()
#print(H)
#print()

context = [""]

for i in range(0,100):
    transition_dict = F[str(context)]
    num_words = get_dict_total(transition_dict)
    ran = random.random()
    running_prob = 0
    for label in transition_dict:
        running_prob += transition_dict[label] / num_words
        if (ran <= running_prob):
            pos = label
            break
    print(pos, end=' ')
    context = (context + [pos])[1:]
