"""Gui for arithmetic kids
@Author: Carl hiram Yaro
@ID : CH53
@Date: Fall 2021

"""
from guizero import App, Box, TextBox, Text, PushButton
from Arithmetickids2 import Arithmetickids
import time


class Arithmetickidsapp:
    
    def __init__(self, app):
        """building app interface"""
        
        # Configure the application GUI.
        app.title = 'Calculator'
        app.width = 400
        app.height = 250
        app.font = 'Helvetica'
        app.text_size = 12
        self.score_value = 0
        self.question_number = 1       
        self.game = Arithmetickids()
        
        #Widgets on top row
        self.top_row = Box(app, width="fill", align="top", border=True)
        self.Q_no = Text(self.top_row, text="Question: {}".format(self.question_number) , align="left")
        self.score = Text(self.top_row, text="Score {}".format(self.score_value), align="right")
        
        #next row
        row2 = Box(app, width="fill", height="fill", align="top", border=True)
        
        self.profile = TextBox(row2, text="Enter name")
                     
        self.player_no = Text(row2, text="Welcome, create new profile")
        
        self.question = Text(row2, text=self.game.new_game())
        
        self.answer = TextBox(row2)
        
        self.instructions = Text(row2, text= "Answer wrong and lose progress")
        
        
        
        #bottom row
        bottom_row = Box(app, width="fill", align="bottom", border=True)
        self.timecheck = Text(bottom_row, text="Timer: ", align="left")
        self.create_profile = PushButton(bottom_row, text="Create profile", align ="right", command = self.new_profile)
        self.submit = PushButton(bottom_row, text="submit", align="right", command = self.trial)
        self.end = PushButton(bottom_row, command = app.destroy, text="Quit", align="right")


            
    def new_profile(self):
        """creates new profile when button is clicked"""        
        self.player_no.value = self.game.new_profile(self.profile.value)
           
    def trial(self):
        """checks to see if answer is correct and gives a score"""
        if self.game.check_answer(self.answer.value):
            self.instructions.value = "Good job, next question"
            self.score_value += 1
            self.score.value = 'Score {}'.format(self.score_value)
            self.n_question()
            
        else:
            self.instructions.value = "Wrong answer, Game over"
            self.savescore()
            app.destroy()
            
            
    def savescore(self):
        self.game.display_score(self.profile.value,self.score.value)

    
    def n_question(self):
        self.question_number += 1
        self.Q_no.value = 'Question {}'.format(self.question_number)
        self.question.value = self.game.next_question()
        self.instructions.value = "Enter the correct anwer"
        self.answer.value = ''

        


        
        
        


       
        
        
        
        







app = App()
Arithmetickidsapp(app)
app.display()
