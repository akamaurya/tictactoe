import numpy as np
game_board = np.zeros((3,3),dtype=np.int16)
won=False
def game_comm(player,column,row):
    if player<=3:
        if column == 'A':
            if game_board[row][0] == 0:
                game_board[row][0] = player
            else:
                print('This position has already been selected, Try another\n')
        elif column == 'B':
            if game_board[row][1] == 0:
                game_board[row][1] = player
            else:
                print('This position has already been selected, Try another\n')
        elif column == 'C':
            if game_board[row][2] == 0:
                game_board[row][2] = player
            else:
                print('This position has already been selected, Try another\n')
        print('   A  B  C')
        for a, b in enumerate(game_board):
            print(a,b)

        a0=0; a1=0; a2=0
        b0=0; b1=0; b2=0
        c0=0; c1=0; c3=0

        a0=game_board[0][0];b0=game_board[0][1];c0=game_board[0][2]
        a1=game_board[1][0];b1=game_board[1][1];c1=game_board[1][2]
        a2=game_board[2][0];b2=game_board[2][1];c2=game_board[2][2]
        won=False

        if a0==a1==a2:
            if a0==1:
                print('Player 1 Won!')
                won=True
            elif a0==2:
                print('Player 2 Won!')
                won=True
        elif b0==b1==b2:
            if b0==1:
                print('Player 1 Won!')
                won=True
            elif b0==2:
                print('Player 2 Won!')
                won=True
        elif c0==c1==c2:
            if c0==1:
                print('Player 1 Won!')
                won=True
            elif c0==2:
                print('Player 2 Won!')
                won=True
        
        if a0==b0==c0:
            if a0==1:
                print('Player 1 Won!')
                won=True
            elif a0==2:
                print('Player 2 Won!')
                won=True
        elif a1==b1==c1:
            if a1==1:
                print('Player 1 Won!')
                won=True
            elif a1==2:
                print('Player 2 Won!')
                won=True
        if a2==b2==c2:
            if a2==1:
                print('Player 1 Won!')
                won=True
            elif a2==2:
                print('Player 2 Won!')
                won=True

        if a0==b1==c2:
            if a0==1:
                print('Player 1 Won!')
                won=True
            elif a0==2:
                print('Player 2 Won!')
                won=True
        elif a2==b1==c0:
            if a2==1:
                print('Player 1 Won!')
                won=True
            elif a2==2:
                print('Player 2 Won!')
                won=True
        
    pass

print('   A  B  C')
for a, b in enumerate(game_board):
    print(a,b)

while won!=True:
    j_1=input('Player 1, Play\n')
    j0=j_1[0];j1=j_1[1]
    if j1 is not str:
        j1=int(j1)
    else:
        print('You have entered something other than a int in the row submission column, or somethin other than a str in the Column Submission Column')
        break
    if j0 == 'a' or j0 == 'b' or j0 == 'c':
        j0=j0.capitalize()
    game_comm(1,j0,j1)

    j_2=input('Player 2, Play\n')
    j00=j_2[0];j01=j_2[1]
    if j01 is not str:
        j01=int(j01)
    else:
        print('You have entered something other than a int in the row submission column, or somethin other than a str in the Column Submission Column')
        break
    if j00 == 'a' or j00 == 'b' or j00 == 'c':
        j00=j00.capitalize()
    game_comm(2,j00,j01)
