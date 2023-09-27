import random
import time
#import Play_Audio as play


class Characters:   
    def __init__(self, text):
        self.text = text 
        #self.audio = audio

    def get_text(self):        
        return self.text

character_dict = { 
    1:Characters("Mario"),
    2:Characters("Donkey Kong"),
    3:Characters("Link"),
    4:Characters("Samus"),
    5:Characters("Yoshi"),
    6:Characters("Kirby"),
    7:Characters("Fox McCloud"),
    8:Characters("Pikachu"),
    9:Characters("Dark Samus*"),
    10:Characters("Luigi"),
    11:Characters("Ness"),
    12:Characters("Captain Falcon"),
    13:Characters("Jigglypuff"),
    14:Characters("Princess Peach"),
    15:Characters("Princess Daisy*"),
    16:Characters("Bowser"),
    17:Characters("Ice Climbers"),
    18:Characters("Sheik"),
    19:Characters("Princess Zelda"),
    20:Characters("Dr. Mario"),
    21:Characters("Pichu"),
    22:Characters("Falco Lombardi"),
    23:Characters("Marth"),
    24:Characters("Lucina*"),
    25:Characters("Young Link"),
    26:Characters("Ganondorf"),
    27:Characters("Mewtwo"),
    28:Characters("Roy"),
    29:Characters("Chrom*"),
    30:Characters("Mr. Game & Watch"),
    31:Characters("Meta Knight"),
    32:Characters("Pit"),
    33:Characters("Dark Pit*"),
    34:Characters("Zero Suit Samus"),
    35:Characters("Wario"),
    36:Characters("Solid Snake"),
    37:Characters("Ike"),
    38:Characters("Pokemon Trainer"),
    39:Characters("Squirtle"),
    40:Characters("Ivysaur"),
    41:Characters("Charizard"),
    42:Characters("Diddy Kong"),
    43:Characters("Lucas"),
    44:Characters("Sonic"),
    45:Characters("King Dedede"),
    46:Characters("Olimar"),
    47:Characters("Lucario"),
    48:Characters("R.O.B."),
    49:Characters("Toon Link"),
    50:Characters("Wolf O'Donnell"),
    51:Characters("Villager"),
    52:Characters("Mega Man"),
    53:Characters("Wii Fit Trainer"),
    54:Characters("Rosalina & Luma"),
    55:Characters("Little Mac"),
    56:Characters("Greninja"),
    57:Characters("Mii Brawler"),
    58:Characters("Mii Swordfighter"),
    59:Characters("Mii Gunner"),
    60:Characters("Palutena"),
    61:Characters("Pac-Man"),
    62:Characters("Robin"),
    63:Characters("Shulk"),
    64:Characters("Bowser Jr."),
    65:Characters("Duck Hunt Duo"),
    66:Characters("Ryu"),
    67:Characters("Ken Masters*"),
    68:Characters("Cloud Strife"),
    69:Characters("Corrin"),
    70:Characters("Bayonetta"),
    71:Characters("Inkling"),
    72:Characters("Ridley"),
    73:Characters("Simon Belmont"),
    74:Characters("Richter Belmont*"),
    75:Characters("King K. Rool"),
    76:Characters("Isabelle"),
    77:Characters("Incineroar"),
    78:Characters("Piranha Plant"),
    79:Characters("Joker"),
    80:Characters("Hero"),
    81:Characters("Banjo and Kazooie"),
    82:Characters("Terry"),
    83:Characters("Byleth"),
    84:Characters("Min Min"),
    85:Characters("Steve"),
    86:Characters("Sephiroth"),
    87:Characters("Pyra/Mythra"),
    88:Characters("Kazuya Mishima"),
    89:Characters("Sora"),
}

#while True:
#    select = random.randint(1, len(character_dict))
   
#    character = character_dict[select].get_text()
#    print(character)

#    play.play_audio_sd("Change Character.mp3", "Smash/")
#    #filename = character + ".mp3"    
#    #play.play_audio_sd(filename)
    
#    time.sleep(5)

def Randomiser():
    select = random.randint(1, len(character_dict))
   
    character = character_dict[select].get_text()
    print(character)

    #play.play_audio_sd("Change Character.mp3", "Smash/")
    #filename = character + ".mp3"    
    #play.play_audio_sd(filename)
    
    #time.sleep(5)
    return character
