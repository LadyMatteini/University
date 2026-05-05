score1 = float(input('Enter the first score: '))
score2 = float(input('Enter the second score: '))
score3 = float(input('Enter the third score: '))

scoref = (score1 + score2 + score3) / 3

if scoref >= 6:
    print(f'Approved, your score is {scoref:.1f}')
else:
    print(f'So sad :(, you didn`t do it, your score is {scoref:.1f}')