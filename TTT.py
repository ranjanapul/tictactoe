board=[' ']*10
def disp_board():
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('__|___|__')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('__|___|__')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('  |   |  ')
def is_Winner():
    if(board[7]==board[8]==board[9]!=' ' or board[4]==board[5]==board[6]!=' ' or board[1]==board[2]==board[3]!=' ' or board[7]==board[4]==board[1]!=' ' or board[8]==board[5]==board[2]!=' ' or board[9]==board[6]==board[3]!=' ' or board[7]==board[5]==board[3]!=' ' or board[9]==board[5]==board[1]!=' '):
        return True
    return False
print('Welcome to Tic Tac Toe')
pos=0
flag=0
p1=''
p2=''
while((p1.upper()!='X' and p1.upper()!='O')):
    p1=p1+input('Player 1: Do you want to be X or O? ')
if(p1.upper()=='X'):
    p2=p2+'O'
    print('Player 1 will go first ')
else:
    p2='X'
    print('Player 2 will go first ')
ready=input('Are you ready to play? Enter Yes or No ')
if(ready.lower()=='no'):
    print('You have exited the game ')
else:
    while(flag==0):
        board=[' ']*10
        disp_board()
        for i in range(10):
            if(is_Winner()):
                print('Congratulations! You have won the game!')
                inp=input('Do you want to play again? Enter Yes or No ')
                if(inp.lower()=='no'):
                    print('Thank You for playing')
                    flag=1
                    break
                else:
                    p1=''
                    p2=''
                    while((p1.upper()!='X' and p1.upper()!='O')):
                        p1=input('Player 1: Do you want to be X or O? ')
                        if(p1.upper()=='X'):
                            p2='O'
                            print('Player 1 will go first ')
                        else:
                            p2='X'
                            print('Player 2 will go first ')
                    break
            if(i==9):
                print('Game Drawn')
                inp=input('Do you want to play again? Enter Yes or No ')
                if(inp.lower()=='no'):
                    print('Thank You for playing')
                    flag=1
                    break
                else:
                    p1=''
                    p2=''
                    while((p1.upper()!='X' and p1.upper()!='O')):
                        p1=input('Player 1: Do you want to be X or O? ')
                        if(p1.upper()=='X'):
                            p2='O'
                            print('Player 1 will go first ')
                        else:
                            p2='X'
                            print('Player 2 will go first ')
                            break
            pos=int(input('enter position: '))
            if(i%2==0):
                board[pos]='X'
            else:
                board[pos]='O'
            print('\n'*100)
            disp_board()


        





