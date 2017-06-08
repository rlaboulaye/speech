import random
 
def get_dict_total(dic):
    total = 0
    for key in dic:
        total += dic[key]
    return total

def get_pos_model(training_file_name):
    
    training_data = open(training_file_name).read()

    # Transition function from pos to pos
    F = {}
    F_context = ""

    # Transition function from pos to word observation
    H = {}
    H_context = ""

    for labelled_word in training_data.split():
        labelled_word_arr = labelled_word.split('_')
        word = labelled_word_arr[0]
        pos = labelled_word_arr[1]

        transition_dict = F.setdefault(str(F_context),{})
        transition_dict[pos] = transition_dict.setdefault(pos, 0) + 1
        F_context = pos

        H_context = pos
        transition_dict = H.setdefault(H_context, {})
        transition_dict[word] = transition_dict.setdefault(word, 0) + 1

    del F['']

    # Normalizing and Smoothing for F

    for state in F.keys():
        transition_dict = F[state]
        dict_total = get_dict_total(transition_dict)
        for word in transition_dict.keys():
            transition_dict[word] = transition_dict[word] / dict_total

    min_trans_p = 1.
    for state in F.keys():
        transition_dict = F[state]
        for word in transition_dict.keys():
            if transition_dict[word] < min_trans_p:
                min_trans_p = transition_dict[word]
    min_trans_p *= .9

    num_states = len(F.keys())
    for state in F.keys():
        transition_dict = F[state]
        missing_states = num_states - len(transition_dict.keys())
        new_total_prob = 1 + missing_states * min_trans_p
        for word in transition_dict.keys():
            transition_dict[word] = transition_dict[word] / new_total_prob
        for word in F.keys():
            if not word in transition_dict:
                transition_dict[word] = min_trans_p
    #

    # Normalizing and Smoothing for H
    for state in H.keys():
        transition_dict = H[state]
        dict_total = get_dict_total(transition_dict)
        for word in transition_dict.keys():
            transition_dict[word] = transition_dict[word] / dict_total

    min_emit_p = 1.
    for state in H.keys():
        transition_dict = H[state]
        for word in transition_dict.keys():
            if transition_dict[word] < min_emit_p:
                min_emit_p = transition_dict[word]
    min_emit_p *= .9

    num_states = len(H.keys())
    for state in H.keys():
        transition_dict = H[state]
        new_total_prob = 1 + min_emit_p
        for word in transition_dict.keys():
            transition_dict[word] = transition_dict[word] / new_total_prob
        transition_dict[None] = min_trans_p

    #

    return (F, H)

    #context = 'NN'

    #for i in range(0,100):
    #    transition_dict = F[context]
    #    num_words = get_dict_total(transition_dict)
    #    ran = random.random()
    #    running_prob = 0
    #    for label in transition_dict:
    #        running_prob += transition_dict[label] / num_words
    #        if (ran <= running_prob):
    #            pos = label
    #            break
    #    print(pos, end=' ')
    #    context = pos

