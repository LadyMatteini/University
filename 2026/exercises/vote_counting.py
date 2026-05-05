# Contagem dos votos

whiteVotes = int(input('How many white votes you had?: '))
nullVotes = int(input('How many null votes you had?: '))
validVotes = int(input('How many valids votes you had?: '))

allVotes = ( whiteVotes + nullVotes + validVotes)
whiteVotesPer = (100 * whiteVotes ) / allVotes
nullVotesPer = (100 * nullVotes ) / allVotes
validVotesPer = (100 * validVotes ) / allVotes

print(f'The votes percents were: {whiteVotesPer} white, {nullVotesPer} nulls e {validVotesPer} valids')
