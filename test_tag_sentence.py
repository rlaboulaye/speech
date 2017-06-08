from viterbi import viterbi
from generate_pos_model import get_pos_model

training_data = 'pos_train.txt'
test_data = 'pos_test.txt'
text = open(test_data).read()

trans_p, emit_p = get_pos_model(training_data)
states = list(trans_p.keys())
start_p = trans_p['.']

correct = 0
outof = 0
for sentence in text.split('._.'):
    if sentence != '' and sentence != '\n':
        sentence += '._.'
        obs = []
        target = []
        for word_label_pair in sentence.split():
            word_arr = word_label_pair.split('_')
            obs.append(word_arr[0])
            target.append(word_arr[1])
        assignment = viterbi(obs, states, start_p, trans_p, emit_p)
        print(obs)
        print(target)
        print(assignment)
        for i in range(len(target)):
            outof += 1
            if target[i] == assignment[i]:
                correct += 1

print('Test Accuracy: ', correct / outof)
