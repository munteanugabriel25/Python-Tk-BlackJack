#! python3

from threading import Thread
import pygame

class Sound:
    sounds= {"chips": "Sounds\\poker-chips.mp3", "card-flip":"Sounds\\Card-flip.mp3", "error":"Sounds\\error.mp3", "dealing-cards":"Sounds\\Dealing-cards.mp3", "gasp": "Sounds\\gasp.mp3"}
    def __init__(self):
        pygame.init()
        self.player = pygame.mixer
        self.player.init()
        self.player.music.set_volume(5)
        
    def sound(self,type):
        self.player.music.load(self.sounds[type])
        self.player.music.play()
    
    def play_sound(self,type):
        thread = Thread(target=self.sound ,daemon=True,args=(type,))
        thread.start()
    
    def get_state(self):
        return self.player.music.get_volume()
        
    def mute_unmute(self,value):
        self.player.music.set_volume(value)
    