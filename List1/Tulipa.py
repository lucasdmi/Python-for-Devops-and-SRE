#1st tulipa example



notes = []
weighted_average = 0

for i in range(0, 10, 1):
    note = input('Enter your note:')
    notes.append(note)
    weighted_average += note

weighted_average = sum(notes) / len(notes)

print('The weighted average is:', weighted_average)

