from playsound import playsound
from turtle import ontimer

def init(url, repeat = False, time = 0):
    ''' Inicia o áudio '''
    
    def play():
        playsound(url, False)
        
        if repeat: 
            ontimer(play, time * 1000)
    
    play()