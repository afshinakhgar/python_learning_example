import random

class Guess :
    difficaulty = [2,10,50,100,500,1000]
    game_limit = 3 #score
    hu_level = {0:'easy',1:'normal',2:'so so',3:'hard',4:'very hard',5:'pro'}
    level = 0
    number =0
    UserNumber = 0
    success = False
    score = 0
    pc_score = 0
    def  __init__(self,level):
        self.number = 0
        self.level = level
        print('you have selected level : '+ str(self.hu_level[level]))
        print('you should choose numbers from 1 to '+ str(self.difficaulty[self.level]))
    def pcNumber (self):
        self.number = random.randint(1,self.difficaulty[self.level])
    
    def getNumber (self):
        self.pcNumber ()
        n = input('Guess a number :')
        while (int(n) > int(self.difficaulty[self.level]) or len(n) == 0):
            n = input('out of range number - Guess a new number :')
        return n
    def reset (self):
        self.pc_score = 0
        self.score = 0
        
   
    def result (self) :
        end = False
        if self.pc_score == self.game_limit or self.score == self.game_limit :
            end = True
            while (end == True):
                userNumber = input('Game is Over, do you want to play again y/yes ?')
                if str(userNumber) == 'yes' or str(userNumber) == 'y' :
                    end = False
                    self.reset()
        if end != True:
            userNumber = self.getNumber ()
        self.success = False
        if int(self.number) == int(userNumber): 
            print('You Are Correct!')
            self.score = int(self.score)+1
        else:
            print('You Are Lose!')
            self.pc_score = int(self.pc_score)+1
        print('##############################')
        print('##############################')
        print('##############################')
        print('##############################')
        print('PC choice : '+ str(self.number))
        print('#============================#')
        print('User choice : '+ str(self.number))
        print('#============================#')
        print('#++++++++++++++++++++++++++++#')
        print('>|-0 your Score : '+ str(self.score))
        print('#============================#')
        print(' 01 Pc Score : '+ str(self.pc_score))
        print('##############################')

        print('------------------------------')
        if self.pc_score == self.game_limit :
            print('PC Won!!!!!!!!!!!!  Game Over !')
        if self.score == self.game_limit:
            print('0000000000000000000000000')
            print('You Won !! Hooray')

        
        return self.pc_score
print ('levels :')
print({0:'easy',1:'normal',2:'so so',3:'hard',4:'very hard',5:'pro'})

level_get = input('select level please : 0 to 5 => 5 is the hardest level : (default : 0 -> easy) ? ')
if  len(level_get) == 0 or level_get == '' :
    level_get=0
guess = Guess(int(level_get))
while (True) :
    guess.result()


input('press enter:')
