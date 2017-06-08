from viterbi import viterbi
from generate_pos_model import get_pos_model

training_data = 'pos_train.txt'
test_data = 'pos_test.txt'
text = open(test_data).read()

trans_p, emit_p = get_pos_model(training_data)
states = list(trans_p.keys())
start_p = trans_p['.']

sentence = 'I like dogs .'
obs = sentence.split()

assignment = viterbi(obs, states, start_p, trans_p, emit_p)
print(obs)
print(assignment)
