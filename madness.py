import random

win_prob = [[50.0, 54.1, 62.2, 69.9, 84.6, 68.8, 85.7, 80.2, 89.5, 85.7, 57.1, 100., 100., 0.00, 0.00, 99.3], #1
            [None, 50.0, 61.9, 44.4, 20.0, 72.2, 69.8, 44.4, 50.0, 61.4, 87.5, 100., 0.00, 0.00, 94.1, 0.00], #2
            [None, None, 50.0, 62.5, 50.0, 56.3, 61.1,  100,  100, 69.2, 68.5, 0.00, 0.00, 84.6, 100., 0.00], #3
            [None, None, None, 50.0, 56.4, 33.3, 33.3, 36.4, 50.0, 100., 0.00, 69.2, 80.0, 0.00, 0.00, 0.00], #4
            [None, None, None, None, 50.0, 100., 0.00, 25.0, 25.0, 100., 0.00, 67.9, 82.4, 0.00, 0.00, 0.00], #5
            [None, None, None, None, None, 0.00, 62.5, 25.0, 0.00, 60.0, 63.5, 0.00, 0.00, 87.5, 0.00, 0.00], #6
            [None, None, None, None, None, None, 0.00, 50.0, 0.00, 61.3, 0.00, 0.00, 0.00, 100., 66.7, 0.00], #7
            [None, None, None, None, None, None, None, 0.00, 52.5, 0.00, 100., 0.00, 100., 0.00, 0.00, 0.00], #8
            [None, None, None, None, None, None, None, None, 0.00, 100., 0.00, 0.00, 100., 0.00, 0.00, 100.], #9
            [None, None, None, None, None, None, None, None, None, 0.00, 33.3, 0.00, 0.00, 100., 100., 0.00], #10
            [None, None, None, None, None, None, None, None, None, None, 0.00, 0.00, 0.00, 100., 0.00, 0.00], #11
            [None, None, None, None, None, None, None, None, None, None, None, 0.00, 72.7, 0.00, 0.00, 0.00], #12
            [None, None, None, None, None, None, None, None, None, None, None, None, 0.00, 0.00, 0.00, 0.00], #13
            [None, None, None, None, None, None, None, None, None, None, None, None, None, 0.00, 0.00, 0.00], #14
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0.00, 0.00], #15
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0.00]] #16

round64 =((1, 16),
          (8, 9),
          (5, 12),
          (4, 13),
          (6, 11),
          (3, 14),
          (7, 10),
          (2, 15))

def winner(seed1, seed2):
    # Get win probablility
    if seed2 < seed1:
        temp = seed1
        seed1 = seed2
        seed2 = temp
    prob = win_prob[seed1 - 1][seed2 - 1]
    
    # If there is no data, the higher seed wins
    if prob == 0:
        return seed1
        
    # Create random number
    p = random.randrange(1, 1001)/10
    
    # Return winner
    if p <= prob:
        return seed1
    else:
        return seed2
    
def rounds(matchups, next_round):
    for i, matchup in enumerate(matchups):
        advance = winner(matchup[0], matchup[1])
        next_round[i//2].append(advance)
    
class Region:
    
    def __init__(self):
        self.round32 = [[], [], [], []]
        self.round16 = [[], []]
        self.round8 = [[]]
        
    def play_rounds(self):
        rounds(round64, self.round32)
        rounds(self.round32, self.round16)
        rounds(self.round16, self.round8)
        self.final4 = winner(self.round8[0][0], self.round8[0][1])
    
    


if __name__ =='__main__':
    print('\nEast Regional')
    east = Region()
    east.play_rounds()
    print(east.round32)
    print(east.round16)
    print(east.round8)
    print(east.final4)
    
    print('\nWest Regional')
    west = Region()
    west.play_rounds()
    print(west.round32)
    print(west.round16)
    print(west.round8)
    print(west.final4)
    
    print('\nSouth Regional')
    south = Region()
    south.play_rounds()
    print(south.round32)
    print(south.round16)
    print(south.round8)
    print(south.final4)
    
    print('\nMidwest Regional')
    midwest = Region()
    midwest.play_rounds()
    print(midwest.round32)
    print(midwest.round16)
    print(midwest.round8)
    print(midwest.final4)
    
    print('\nFinal Four')
    print([east.final4, west.final4, south.final4, midwest.final4])
    champ1 = winner(east.final4, west.final4)
    champ2 = winner(south.final4, midwest.final4)
    print([champ1, champ2])
    champ = winner(champ1, champ2)
    print(champ)
    
