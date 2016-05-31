ORG_DATA1 = [
            [' ',' ',' ',' '],
            [' ',' ',' ',' '],
            [' ',' ',' ',' '],
            [' ',' ',' ',' '],
            ]
ORG_DATA = [
            ['16','8','2',' '],
            ['16','8','4',' '],
            ['16','8','4','2'],
            ['16','8','4','2'],
            ]

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
ACTIONS_DICT = dict(zip(letter_codes, actions*2))