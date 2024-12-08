# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import utils

line_number = sum(1 for line in open('birth_dev.tsv'))
predictions = ['London'] * line_number
total, correct = utils.evaluate_places('birth_dev.tsv', predictions)
if total > 0:
    print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
# Correct: 25.0 out of 500.0: 5.0%