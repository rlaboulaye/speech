from viterbi import viterbi
from generate_pos_model import get_pos_model

training_data = 'pos_train.txt'
test_data = 'quick_test.txt'
text = open(test_data).read()
obs = []
target = []
for word_label_pair in text.split():
    word_arr = word_label_pair.split('_')
    obs.append(word_arr[0])
    target.append(word_arr[1])

print(obs)
print(target)

trans_p, emit_p = get_pos_model(training_data)
states = list(trans_p.keys())
start_p = {}
for state in states:
    start_p[state] = 1. / len(states)

viterbi(obs, states, start_p, trans_p, emit_p)

