"""Backend for arithmetic kids
Gnerates questions using random integer and random choice and compares answers from GUI to the corresponding answers.
After project 3, I added question generation using the random function insted of the dictionary i started with.
I also used the random library to pick a random operator instead of the simple addition I started with
I also implemented a score system and a Personalized leader board which stores the name and scores of the highest scoring players.

@Author: Carl hiram Yaro
@ID:ch53
@Date: Fall 2021

"""
from random import randint, choice





class Arithmetickids:
    
    def __init__(self):
        """collects answers"""
        #self.answer = ''
        
                
        
    def new_game(self):
        """initializes game"""

        
        self.x = randint(1,9)
        self.y = randint(1,9)
        self.operator = choice("+-*")        
        self.question = str(self.x) + " " + self.operator + " " + str(self.y)
        return self.question
        
    
    def next_question(self):
        """allows user to move to next question"""
        self.x = randint(1,9)
        self.y = randint(1,9)
        self.operator = choice("+-*")
        self.question = str(self.x) + " " + self.operator + " " + str(self.y)
        
        return(self.question)

    
    def new_profile(self,name):
        return "Welcome" + " " + name               
           
    def get_answer(self):
        """gets answer to corresponding question"""        
        
        if self.operator == "+": return self.x + self.y
        elif self.operator == "-": return self.x - self.y
        elif self.operator == "*": return self.x * self.y
        
            
    def check_answer(self,answer):
        """checks answer"""
        self.realanswer = self.get_answer()
        return int(answer) == self.realanswer
    
    def  display_score(self,name,score):
        """Sends score to leaderboard textfile and sorts them. Ethan VanWoerkom Helped with sorting the leaderboard"""
        leaderboard_file = open("leaderboard.txt","r")
        leaderboard = []
        for player_score in leaderboard_file.readlines():
            leaderboard.append(player_score.strip())
        leaderboard_file.close()
            
        leaderboard_file = open("leaderboard.txt","w") 
        leaderboard.append(score + " by " + name + '\n')
        leaderboard.sort()
        leaderboard.reverse()
        
        liststring = ''
        for player_score in leaderboard:
            liststring += player_score + '\n'
        
        leaderboard_file.write(liststring)
        leaderboard_file.close()
        
    def test_method(self,x,y,operator):
        """dummy function to test check answer"""
        self.x = x
        self.y = y
        self.operator = operator
        



        
        
    
    





        
