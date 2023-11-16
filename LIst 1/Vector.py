#1st vector example




notes = []
weighted_average = 0

notes = [0] * 10
for i in range(0, 10, 1):
    notes[i] = int(input('Enter your note:'))
    weighted_average += notes[i]

weighted_average = sum(notes) / len(notes)

print('The weighted average is:', weighted_average)


