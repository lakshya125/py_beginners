def letter_score(let):
    if let in 'adeinorst':
        return 1
    if let in 'ghl':
        return 2
    if let in 'bcmp':
        return 3
    if let in 'jkuvw':
        return 4
    if let in 'f':
        return 5
    if let in 'z':
        return 6
    if let in 'xy':
        return 8
    if let in 'q':
     return 10
    else:
     return 0

def scrabble_score(S):
     if S == '':
        return 0
     else:
        return letter_score(S[0]) + scrabble_score(S[1:])
assert scrabble_score("testing") == 8