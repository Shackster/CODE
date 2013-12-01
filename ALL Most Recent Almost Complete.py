# The following is a protoype that needs adjustment for real world application 

import pygame
from pygame import *
import random
import sys

pygame.init()
pygame.mixer.init()
done = False
# set dimensons for screen and define clock 
Clock = pygame.time.Clock()
Screen = pygame.display.set_mode((1280,720),0,32)

# Define all images here
Font_type = pygame.font.SysFont('Nyala',60)
Title_screen_bg = pygame.image.load("images/Thugofwarstartmenu.jpg").convert_alpha()
Title_Screen_start = pygame.image.load("images/Title Screen.png").convert_alpha()
Main_Menu_bg = pygame.image.load("images/Menu 2 thug.jpg").convert_alpha()
Pause_Menu_bg = pygame.image.load("images/Pause Menu 2 thug.jpg").convert_alpha()
Instruction_Screen = pygame.image.load("images/instruction screen.jpg").convert_alpha()
Char_Select_bg = pygame.image.load("images/characterselect.jpg").convert_alpha()
Mash_screen_bg1 = pygame.image.load("images/Alleytry1.jpg").convert_alpha()
Mash_screen_bg2 = pygame.image.load("images/grassbackground1.jpg").convert_alpha()
Mash_screen_bg3 = pygame.image.load("images/Darkbackground1.jpg").convert_alpha()
P1_Win_Scr1 = pygame.image.load("images/win screen 1 P1.jpg").convert_alpha()
P1_Win_Scr2 = pygame.image.load("images/win screen 2 P1.jpg").convert_alpha()
P1_Win_Scr3 = pygame.image.load("images/win screen 3 P1.jpg").convert_alpha()
P2_Win_Scr1 = pygame.image.load("images/win screen 1 P2.jpg").convert_alpha()
P2_Win_Scr2 = pygame.image.load("images/win screen 2 P2.jpg").convert_alpha()
P2_Win_Scr3 = pygame.image.load("images/win screen 3 P2.jpg").convert_alpha()
Tie_Scr1 = pygame.image.load("images/tie 1.gif").convert_alpha()
Tie_Scr2 = pygame.image.load("images/tie 2.gif").convert_alpha()
Tie_Scr3 = pygame.image.load("images/tie 3.gif").convert_alpha()
Tails = pygame.image.load("images/Tail.png").convert_alpha()
Sonic = pygame.image.load("images/Sonic.png").convert_alpha()
Shadow = pygame.image.load("images/Shadow.png").convert_alpha()
Scorpio = pygame.image.load("images/Scorpio.png").convert_alpha()
Tails1 = pygame.image.load("images/Tail1.png").convert_alpha()
Sonic1 = pygame.image.load("images/Sonic1.png").convert_alpha()
Shadow1 = pygame.image.load("images/Shadow1.png").convert_alpha()
Scorpio1 = pygame.image.load("images/Scorpio1.png").convert_alpha()
Tails2 = pygame.image.load("images/Tail2.png").convert_alpha()
Sonic2 = pygame.image.load("images/Sonic2.png").convert_alpha()
Shadow2 = pygame.image.load("images/Shadow2.png").convert_alpha()
Scorpio2 = pygame.image.load("images/Scorpio2.png").convert_alpha()
Tails3 = pygame.image.load("images/Tail3.png").convert_alpha()
Sonic3 = pygame.image.load("images/Sonic3.png").convert_alpha()
Shadow3 = pygame.image.load("images/Shadow3.png").convert_alpha()
Scorpio3 = pygame.image.load("images/Scorpio3.png").convert_alpha()
Space = pygame.image.load("images/space.jpg").convert_alpha()
Water = pygame.image.load("images/water.jpg").convert_alpha()
Up = pygame.image.load("images/Up.png").convert_alpha()
Down = pygame.image.load("images/Down.png").convert_alpha()
Right = pygame.image.load("images/Right.png").convert_alpha()
Left = pygame.image.load("images/Left.png").convert_alpha()
Menu_Arrow1 = pygame.image.load("images/arrow.gif").convert_alpha()
Menu_Arrow2 = pygame.image.load("images/arrow 1.gif").convert_alpha()
Menu_Arrow3 = pygame.image.load("images/arrow 2.gif").convert_alpha()
Go_Message = pygame.image.load("images/go!.png").convert_alpha()
Watch_Message = pygame.image.load("images/watch.png").convert_alpha()

# Miscellaneous and Lists
Menu_Arrow = [Menu_Arrow1,Menu_Arrow2,Menu_Arrow3]
Arrow_rect1 = pygame.Rect((260,156),(83,62))
Arrow_rect2 = pygame.Rect((260,283),(83,62))
Arrow_rect3 = pygame.Rect((260,403),(83,62))
Arrow_Rect = [Arrow_rect1,Arrow_rect2,Arrow_rect3]
Arrows = [Up,Down,Right,Left]
Level_recteasy = pygame.Rect((94,618),(161,103))
Level_rectmed = pygame.Rect((451,618),(140,66))
Level_recthard = pygame.Rect((878,618),(150,70))
Level_Rect = [Level_recteasy,Level_rectmed,Level_recthard]
Mash_Screen_Bg = [Mash_screen_bg1,Mash_screen_bg2,Mash_screen_bg3]
P1_Win_Scr = [P1_Win_Scr1,P1_Win_Scr2,P1_Win_Scr3]
P2_Win_Scr = [P2_Win_Scr1,P2_Win_Scr2,P2_Win_Scr3]
Tie_Scr = [Tie_Scr1,Tie_Scr3,Tie_Scr3]
Fighters = [Tails2,Sonic2,Shadow2,Scorpio2]
Fighters2 = [Tails1,Sonic1,Shadow1,Scorpio1]
CurrentFighterP1 = [Tails,Sonic,Shadow,Scorpio]
CurrentFighterP2 = [Tails3,Sonic3,Shadow3,Scorpio3]
Fighter_names = ["Tails","Sonic","Shadow","Scorpio"]
fps = 2.2
u = 0
y = 0
W = 0
q = 0
#Player1Health = 50
#Player2Health = 50

# Load all the sound files 

        # Background Music
booba_intro = pygame.mixer.Sound('booba/booba intro.wav')
booba_intro_1 = pygame.mixer.Sound('booba/booba intro 1.wav')
booba_loop = pygame.mixer.Sound('booba/booba loop.wav')
booba_loop_1 = pygame.mixer.Sound('booba/booba loop 1.wav')
booba_loop_4 = pygame.mixer.Sound('booba/booba loop 4.wav')
booba_loop_6 = pygame.mixer.Sound('booba/booba loop 6.wav')
booba_loop_7 = pygame.mixer.Sound('booba/booba loop 7.wav')

        # Character Sounds
come_get_some = pygame.mixer.Sound('character sounds/ComeGetSome.wav')
falcon_punch = pygame.mixer.Sound('character sounds/FalconPunch 1.wav')
make_my_day = pygame.mixer.Sound('character sounds/GoAheadMakeMyDay.wav')
hail_the_king = pygame.mixer.Sound('character sounds/HailToTheKingBaby 1.wav')
big_guns = pygame.mixer.Sound('character sounds/ILikeBigGunsAndICannotLie.wav')
equal_kicker = pygame.mixer.Sound('character sounds/ImAnEqualOpportunityAssKicker.wav')
get_medieval = pygame.mixer.Sound('character sounds/ImGonnaGetMedievalOnYourAsses.wav')
its_my_way = pygame.mixer.Sound('character sounds/ItsMyWayOr.wav')
balls_of_steel = pygame.mixer.Sound('character sounds/IveGotBallsOfSteel.wav')
go_postal = pygame.mixer.Sound('character sounds/LooksLikeItsTimeForMeToGoPostal.wav')
my_gun_is_bigger = pygame.mixer.Sound('character sounds/MyGunIsBiggerThanYours.wav')
my_little_friend = pygame.mixer.Sound('character sounds/SayHelloToMyLittleFriend 1.wav')
something_smells = pygame.mixer.Sound('character sounds/SomethingSmellsRottenAroundHere.wav')
who_wants_some = pygame.mixer.Sound('character sounds/WhoWantsSome.wav')
sparta = pygame.mixer.Sound('character sounds/Sparta 2.wav')

# Define all the sound channels
pygame.mixer.set_num_channels(8)
background_music = pygame.mixer.Channel(0)
p1_sounds = pygame.mixer.Channel(1)
p2_sounds = pygame.mixer.Channel(2)
clock_tick_sound = pygame.mixer.Channel(3)
climax_sound = pygame.mixer.Channel(4)
mash_it = pygame.mixer.Channel(5)
saving_roll = pygame.mixer.Channel(6)
stats_screen = pygame.mixer.Channel(7)
SONG_END = pygame.USEREVENT + 1
p1_sounds.set_endevent(SONG_END)
p2_sounds.set_endevent(SONG_END)

def Title_Screen():
    background_music.play(booba_intro_1)
    x = 1
    v = 1
    Screen.blit(Title_screen_bg,(0,0))
    pygame.display.update() 
    while x != 0 :
        background_music.queue(booba_loop_1)
        for event in pygame.event.get():       
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    x = 0
                    background_music.stop()
                    break
                if event.key == K_i:
                    v1 = v - 0.1
                    if v1 < 0.0:
                        v1 = 0.0 
                    v = v1
                    background_music.set_volume(v1)
                if event.key == K_o:
                    v0 = v + 0.1
                    if v0 > 1.0:
                        v0 = 1.0
                    v = v0
                    background_music.set_volume(v0)
        Text_rect = pygame.Rect((365,340),(568,98))      
        Screen.blit(Title_Screen_start,Text_rect)
        time.delay(200)
        pygame.display.update(Text_rect)
        Screen.blit(Title_screen_bg,(0,0))
        time.delay(200)      
        pygame.display.update()
        
def Main_Menu():
    x = 1
    a = 0   
    v = 1
    background_music.play(booba_loop_1,-1)
    while x != 0 :
        pygame.display.update()
        Screen.blit(Main_Menu_bg,(0,0))
        Screen.blit(Menu_Arrow[a],Arrow_Rect[a])
        pygame.display.update(Arrow_Rect[a])
        for event in pygame.event.get():       
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if a == 0:
                        x = 0
                        background_music.stop()
                        break
                    elif a == 1:
                        a = 1
                        r = 1
                        while r != 0:
                            pygame.display.update()
                            Screen.blit(Instruction_Screen,(0,0))
                            Screen.blit(Menu_Arrow[a],Level_Rect[a])
                            pygame.display.update(Level_Rect[a])
                            for event in pygame.event.get():       
                                if event.type == QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == KEYDOWN:
                                    if (event.key == K_RETURN):
                                        global fps
                                        if a == 0:
                                            fps = 0.8
                                        elif a == 1:
                                            fps = 2.2 
                                        elif a == 2:
                                            fps = 4.5
                                        r = 0
                                        x = 0
                                        pygame.event.clear()
                                        Main_Menu()
                                        break                                        
                                    if (event.key == K_ESCAPE):
                                        r = 0
                                        x = 0
                                        pygame.event.clear()
                                        Main_Menu()
                                        break
                                    if (event.key == K_LEFT) | (event.key == K_a):
                                        a -= 1
                                        if a < 0:
                                            a = 2
                                        b = a + 1
                                        if b > 2:
                                            b = 0
                                        Screen.blit(Menu_Arrow[a],Level_Rect[a])
                                        pygame.display.update(Level_Rect[a])
                                    if (event.key == K_RIGHT) | (event.key == K_d):   
                                        a += 1
                                        if a > 2:
                                            a = 0
                                        b = a - 1
                                        if b < 0:
                                            b = 2
                                        Screen.blit(Menu_Arrow[a],Level_Rect[a])
                                        pygame.display.update(Level_Rect[a])
                                    if event.key == K_i:
                                        v1 = v - 0.1
                                        if v1 < 0.0:
                                            v1 = 0.0 
                                        v = v1
                                        background_music.set_volume(v1)
                                    if event.key == K_o:
                                        v0 = v + 0.1
                                        if v0 > 1.0:
                                            v0 = 1.0
                                        v = v0
                                        background_music.set_volume(v0)
                    elif a == 2:
                        pygame.quit()
                        sys.exit()
                if event.key == K_i:
                    v1 = v - 0.1
                    if v1 < 0.0:
                        v1 = 0.0 
                    v = v1
                    background_music.set_volume(v1)
                if event.key == K_o:
                    v0 = v + 0.1
                    if v0 > 1.0:
                        v0 = 1.0
                    v = v0
                    background_music.set_volume(v0)
                if (event.key == K_UP) | (event.key == K_w):
                    a -= 1
                    if a < 0:
                        a = 2
                    b = a + 1
                    if b > 2:
                        b = 0
                    Screen.blit(Menu_Arrow[a],Arrow_Rect[a])
                    pygame.display.update(Arrow_Rect[a])
                if (event.key == K_DOWN) | (event.key == K_s):   
                    a += 1
                    if a > 2:
                        a = 0
                    b = a - 1
                    if b < 0:
                        b = 2
                    Screen.blit(Menu_Arrow[a],Arrow_Rect[a])
                    pygame.display.update(Arrow_Rect[a])
    return fps       

def Pause_Menu():
    k = 1
    p = 0   
    v = 1
    background_music.play(booba_loop_1,-1)
    while k != 0 :
        pygame.display.update()
        Screen.blit(Pause_Menu_bg,(0,0))
        Screen.blit(Menu_Arrow[p],Arrow_Rect[p])
        pygame.display.update(Arrow_Rect[p])
        for event in pygame.event.get():       
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if p == 0:
                        k = 0
                        pygame.event.clear
                        background_music.stop()
                        Game()
                        break
                    elif p == 1:
                        p = 1
                        r = 1
                        while r != 0:
                            pygame.display.update()
                            Screen.blit(Instruction_Screen,(0,0))
                            Screen.blit(Menu_Arrow[p],Level_Rect[p])
                            pygame.display.update(Level_Rect[p])
                            for event in pygame.event.get():       
                                if event.type == QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == KEYDOWN:
                                    if (event.key == K_RETURN):
                                        global fps
                                        if p == 0:
                                            fps = 0.8
                                        elif p == 1:
                                            fps = 2.2 
                                        elif p == 2:
                                            fps = 4.5
                                        r = 0
                                        k = 0
                                        #pygame.event.clear()
                                        Pause_Menu()
                                        break                                        
                                    if (event.key == K_ESCAPE):
                                        r = 0
                                        k = 0
                                        #pygame.event.clear()
                                        Pause_Menu()
                                        break
                                    if (event.key == K_LEFT) | (event.key == K_a):
                                        p -= 1
                                        if p < 0:
                                            p = 2
                                        b = p + 1
                                        if b > 2:
                                            b = 0
                                        Screen.blit(Menu_Arrow[p],Level_Rect[p])
                                        pygame.display.update(Level_Rect[p])
                                    if (event.key == K_RIGHT) | (event.key == K_d):   
                                        p += 1
                                        if p > 2:
                                            p = 0
                                        b = p - 1
                                        if b < 0:
                                            b = 2
                                        Screen.blit(Menu_Arrow[p],Level_Rect[p])
                                        pygame.display.update(Level_Rect[p])
                                    if event.key == K_i:
                                        v1 = v - 0.1
                                        if v1 < 0.0:
                                            v1 = 0.0 
                                        v = v1
                                        background_music.set_volume(v1)
                                    if event.key == K_o:
                                        v0 = v + 0.1
                                        if v0 > 1.0:
                                            v0 = 1.0
                                        v = v0
                                        background_music.set_volume(v0)
                    elif p == 2:
                        pygame.quit()
                        sys.exit()
                if event.key == K_ESCAPE:
                    k = 0
                    pygame.event.clear()
                    if m == 0:
                        Character_select_screen()
                        Combo_seq_screen_P1(u)
                        Combo_seq_screen_P2(y) 
                        MASH_Screen(u,y,w,q)
                        Game()
                    if m == 1:
                        Combo_seq_screen_P1(u)
                        Combo_seq_screen_P2(y) 
                        MASH_Screen(u,y,w,q)
                        Game()
                    if m == 2:
                        Combo_seq_screen_P2(y) 
                        MASH_Screen(u,y,w,q)
                        Game()
                    if m == 3:
                        MASH_Screen(u,y,w,q)
                        Game()
                    background_music.stop()
                    break                  
                if event.key == K_i:
                    v1 = v - 0.1
                    if v1 < 0.0:
                        v1 = 0.0 
                    v = v1
                    background_music.set_volume(v1)
                if event.key == K_o:
                    v0 = v + 0.1
                    if v0 > 1.0:
                        v0 = 1.0
                    v = v0
                    background_music.set_volume(v0)
                if (event.key == K_UP) | (event.key == K_w):
                    p -= 1
                    if p < 0:
                        p = 2
                    b = p + 1
                    if b > 2:
                        b = 0
                    Screen.blit(Menu_Arrow[p],Arrow_Rect[p])
                    pygame.display.update(Arrow_Rect[p])
                if (event.key == K_DOWN) | (event.key == K_s):   
                    p += 1
                    if p > 2:
                        p = 0
                    b = p - 1
                    if b < 0:
                        b = 2
                    Screen.blit(Menu_Arrow[p],Arrow_Rect[p])
                    pygame.display.update(Arrow_Rect[p])
    return fps       

def Character_select_screen():
    x = 1
    a = 0
    global m
    m = 0
    v = 1
    v2 = v - 0.6 
    Color = (0,255,255)
    Color2 = (50,50,50)
    background_music.play(booba_loop_1,-1)
    Screen.blit(Char_Select_bg,(0,0))
    F1 = pygame.Rect((402,381),(126,128))
    F2 = pygame.Rect((532,381),(126,128))
    F3 = pygame.Rect((662,381),(126,128))
    F4 = pygame.Rect((792,381),(126,128))
    NameP1 = pygame.Rect((316,130),(175,70))
    NameP2 = pygame.Rect((750,190),(175,70))
    CurrentCharP1 = pygame.Rect((110,0),(186,311))
    CurrentCharP2 = pygame.Rect((946,71),(220,311))
    label = Font_type.render(str(Fighter_names[a]),True,Color)
    pygame.draw.rect(Screen,(0,0,0),CurrentCharP1,0)
    pygame.draw.rect(Screen,(0,0,0),CurrentCharP2,0)
    Screen.blit(CurrentFighterP1[a],CurrentCharP1)
    Screen.blit(CurrentFighterP2[a],CurrentCharP2)
    pygame.draw.rect(Screen,Color2,NameP1,0)
    pygame.draw.rect(Screen,Color2,NameP2,0)
    Screen.blit(label,NameP1)
    Screen.blit(label,NameP2)
    Screen.blit(Fighters[0],F1)
    Screen.blit(Fighters[1],F2)
    Screen.blit(Fighters[2],F3)
    Screen.blit(Fighters[3],F4)
    pygame.display.update(NameP1)
    pygame.display.update(NameP2)
    pygame.display.update()
    while x != 0:
        for event in pygame.event.get():                   
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SONG_END:
                background_music.set_volume(v)
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    x = 0
                    Player_1 = a
                    global u
                    u = Player_1
                    break
                if event.key == K_ESCAPE:
                    #pygame.event.clear()
                    Pause_Menu()
                if event.key == K_i:
                    v1 = v - 0.1
                    if v1 < 0.0:
                        v1 = 0.0 
                    background_music.set_volume(v1)
                    v = v1
                if event.key == K_o:
                    v0 = v + 0.1
                    if v0 > 1.0:
                        v0 = 1.0
                    background_music.set_volume(v0)
                    v = v0
                if event.key == K_d:
                    a += 1
                    if (v < 0.7) & (v > 0.0):
                        v2 = 0.1
                    if v == 0.0:
                        v2 = 0
                    if a > 3:
                        a = 0
                    background_music.set_volume(v2)
                    p1_sounds.set_volume(v)
                    if a == 0:
                        p1_sounds.play(my_little_friend)
                    elif a == 1:
                        p1_sounds.play(falcon_punch)
                    elif a == 2:
                        p1_sounds.play(sparta)    
                    elif a == 3:
                        p1_sounds.play(hail_the_king)
                    label = Font_type.render(str(Fighter_names[a]),True,Color)
                    pygame.draw.rect(Screen,Color2,NameP1,0)
                    Screen.blit(label,NameP1)
                    pygame.draw.rect(Screen,(0,0,0),CurrentCharP1,0)
                    Screen.blit(CurrentFighterP1[a],CurrentCharP1)
                    pygame.display.update()
                if event.key == K_a:
                    a -= 1
                    if (v < 0.7) & (v > 0.0):
                        v2 = 0.1
                    if v == 0.0:
                        v2 = 0
                    if a < 0:
                        a = 3
                    background_music.set_volume(v2)                  
                    p1_sounds.set_volume(v)
                    if a == 0:
                        p1_sounds.play(my_little_friend)
                    elif a == 1:
                        p1_sounds.play(falcon_punch)
                    elif a == 2:
                        p1_sounds.play(sparta)
                    elif a == 3:
                        p1_sounds.play(hail_the_king)
                    label = Font_type.render(str(Fighter_names[a]),True,Color)
                    pygame.draw.rect(Screen,Color2,NameP1,0)
                    Screen.blit(label,NameP1)
                    pygame.draw.rect(Screen,(0,0,0),CurrentCharP1,0)
                    Screen.blit(CurrentFighterP1[a],CurrentCharP1)
                    pygame.display.update()
    x = 1
    a = 0
    while x != 0:
        for event in pygame.event.get():       
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SONG_END:
                background_music.set_volume(v)
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    x = 0
                    Player_2 = a
                    global y
                    y = Player_2
                    break
                if event.key == K_ESCAPE:
                    #pygame.event.clear()
                    Pause_Menu()
                if event.key == K_i:
                    v1 = v - 0.1
                    if v1 < 0.0:
                        v1 = 0.0 
                    background_music.set_volume(v1)
                    v = v1
                if event.key == K_o:
                    v0 = v + 0.1
                    if v0 > 1.0:
                        v0 = 1.0
                    background_music.set_volume(v0)
                    v = v0
                if event.key == K_RIGHT:
                    a += 1
                    if (v < 0.7) & (v > 0.0):
                        v2 = 0.1
                    if v == 0.0:
                        v2 = 0
                    if a > 3:
                        a = 0
                    background_music.set_volume(v2)
                    p2_sounds.set_volume(v)
                    if a == 0:
                        p2_sounds.play(my_little_friend)
                    elif a == 1:
                        p2_sounds.play(falcon_punch)
                    elif a == 2:
                        p2_sounds.play(sparta)    
                    elif a == 3:
                        p2_sounds.play(hail_the_king)
                    label = Font_type.render(str(Fighter_names[a]),True,Color)
                    pygame.draw.rect(Screen,Color2,NameP2,0)
                    Screen.blit(label,NameP2)
                    pygame.draw.rect(Screen,(0,0,0),CurrentCharP2,0)
                    Screen.blit(CurrentFighterP2[a],CurrentCharP2)
                    pygame.display.update()
                if event.key == K_LEFT:
                    a -= 1
                    if (v < 0.7) & (v > 0.0):
                        v2 = 0.1
                    if v == 0.0:
                        v2 = 0
                    if a < 0:
                        a = 3
                    background_music.set_volume(v2)                  
                    p2_sounds.set_volume(v)
                    if a == 0:
                        p2_sounds.play(my_little_friend)
                    elif a == 1:
                        p2_sounds.play(falcon_punch)
                    elif a == 2:
                        p2_sounds.play(sparta)
                    elif a == 3:
                        p2_sounds.play(hail_the_king)
                    label = Font_type.render(str(Fighter_names[a]),True,Color)
                    pygame.draw.rect(Screen,Color2,NameP2,0)
                    Screen.blit(label,NameP2)
                    pygame.draw.rect(Screen,(0,0,0),CurrentCharP2,0)
                    Screen.blit(CurrentFighterP2[a],CurrentCharP2)
                    pygame.display.update() 
    return u,y

def Combo_seq_screen_P1(b):
    background_music.play(booba_loop_4,-1)
    combo_P1 = 1
    index0 = random.randint(0,2)
    Screen.blit(Mash_Screen_Bg[index0],(0,0))
    Area = pygame.Rect((100,100),(600,600))
    Char = pygame.Rect((800,500),(300,300))
    Combo = pygame.Rect((800,250),(50,50))
    UserInput = pygame.Rect((350,350),(853,683))
    Timer = pygame.Rect((800,100),(110,75))
    Player = pygame.Rect((1000,100),(200,200))
    Screen.blit(Fighters[b],Char)
    pygame.draw.rect(Screen,(255,255,255),Combo)
    combo_level = 0
    x = 0 #garbage value
    v = 1
    global m
    m = 1
    index = 0
    timer = pygame.time.Clock()
    #fps = 2.0 #modified later
    player = []
    Comp = []

    ''' P1 TURN '''

    a = 50.0
    Screen.blit(Watch_Message,Area)
    pygame.display.update()
    time.delay(2000)
    random.seed()
    index = random.randint(0,3)
    pygame.draw.rect(Screen,(255,255,255),Area)
    Screen.blit(Arrows[index],(random.randint(100,600),random.randint(100,600)))
    pygame.display.update()
    Comp.append(index)
    x += 1
    timer.tick(fps)
    if x == 4:
        time.delay(1000)
        pygame.display.update(Area)
        Screen.blit(Go_Message,Area)
        pygame.display.update(Area)
        time.delay(2000)
        pygame.draw.rect(Screen, (255,255,255),Area)
    x = 0 #reset garbage variable
    pygame.draw.rect(Screen,(255,255,255),Area)
    pygame.display.update(Area)
    label = Font_type.render(str(int(a)),15,(255,0,0))
    pygame.draw.rect(Screen,(255,255,255),Timer)
    Screen.blit(label, Timer)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                #pygame.event.clear()
                Pause_Menu()
            if event.key == K_d:
                x += 1
                player.append(2)
                Screen.blit(Right,UserInput)
            elif event.key == K_w:
                x += 1
                player.append(0)
                Screen.blit(Up,UserInput)
            elif event.key == K_a:
                x += 1
                player.append(3)
                Screen.blit(Left,UserInput)
            elif event.key == K_s:
                x += 1
                player.append(1)
                Screen.blit(Down,UserInput)
            if event.key == K_i:
                v1 = v - 0.1
                if v1 < 0.0:
                    v1 = 0.0 
                v = v1 
                background_music.set_volume(v1)
            if event.key == K_o:
                v0 = v + 0.1
                if v0 > 1.0:
                    v0 = 1.0
                v = v0 
                background_music.set_volume(v0) 
            pygame.display.update(UserInput)
        a -= float(1.0/40.0)
        timer.tick(800)
        if x == 4:
            time.delay(1000)
            pygame.display.update(Area)
            Screen.blit(Watch_Message,Area)
            pygame.display.update(Area)
            time.delay(1000)
            pygame.draw.rect(Screen, (255,255,255),Area)
            time.delay(1000)
    if Comp == player:
        combo_P1 += 1
        pygame.draw.rect(Screen,(255,255,255),Combo)
        label = Font_type.render(str(combo_P1),15,(255,0,0))
        Screen.blit(label,Combo)
        pygame.display.update()
    else:
        pygame.display.update()
    Comp = []
    player = [] 
    while a >= 0:     
        for event in pygame.event.get():       
            if event.type == QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    #pygame.event.clear()
                    Pause_Menu()
                if event.key == K_i:
                    v1 = v - 0.1
                    if v1 < 0.0:
                        v1 = 0.0 
                    v = v1 
                    background_music.set_volume(v1)
                if event.key == K_o:
                    v0 = v + 0.1
                    if v0 > 1.0:
                        v0 = 1.0
                    v = v0 
                    background_music.set_volume(v0)    
        while x <= 3:
            random.seed()
            index = random.randint(0,3)
            pygame.draw.rect(Screen,(255,255,255),Area)
            Screen.blit(Arrows[index],(random.randint(100,600),random.randint(100,600)))
            pygame.display.update()
            Comp.append(index)
            x += 1
            timer.tick(fps)
            if x == 4:
                time.delay(1000)
                pygame.display.update(Area)
                Screen.blit(Go_Message,Area)
                pygame.display.update(Area)
                time.delay(2000)
                pygame.draw.rect(Screen, (255,255,255),Area)
        x = 0 #reset garbage variable
        pygame.draw.rect(Screen,(255,255,255),Area)
        pygame.display.update(Area)
        while x <= 3:
            if a <= 0:
                break
            label = Font_type.render(str(int(a)),15,(255,0,0))
            pygame.draw.rect(Screen,(255,255,255),Timer)
            Screen.blit(label, Timer)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        #pygame.event.clear()
                        Pause_Menu()
                    if event.key == K_d:
                        x += 1
                        player.append(2)
                        Screen.blit(Right,UserInput)
                    elif event.key == K_w:
                        x += 1
                        player.append(0)
                        Screen.blit(Up,UserInput)
                    elif event.key == K_a:
                        x += 1
                        player.append(3)
                        Screen.blit(Left,UserInput)
                    elif event.key == K_s:
                        x += 1
                        player.append(1)
                        Screen.blit(Down,UserInput)
                    if event.key == K_i:
                        v1 = v - 0.1
                        if v1 < 0.0:
                            v1 = 0.0 
                        v = v1 
                        background_music.set_volume(v1)
                    if event.key == K_o:
                        v0 = v + 0.1
                        if v0 > 1.0:
                            v0 = 1.0
                        v = v0 
                        background_music.set_volume(v0) 
                pygame.display.update(UserInput)
            a -= float(1.0/40.0)
            timer.tick(1000)
            if x == 4:
                time.delay(1000)
                pygame.display.update(Area)
                Screen.blit(Watch_Message,Area)
                pygame.display.update(Area)
                time.delay(1000)
                pygame.draw.rect(Screen, (255,255,255),Area)
                time.delay(1000)
        x = 0
        if Comp == player:
            combo_P1 += 1
            pygame.draw.rect(Screen,(255,255,255),Combo)
            label = Font_type.render(str(combo_P1),15,(255,0,0))
            Screen.blit(label,Combo)
            pygame.display.update()
        else:
            pygame.display.update()
        Comp = []
        player = []
        a -= float(1.0/40.0)
        timer.tick(800)
    global w
    w = combo_P1
    background_music.stop()
    return w

def Combo_seq_screen_P2(c):
    background_music.play(booba_loop_4,-1) 
    combo_P2 = 1
    index1 = random.randint(0,2)
    Screen.blit(Mash_Screen_Bg[index1],(0,0))
    pygame.display.update()
    pygame.time.delay(1000) # delay b4 P2 start
    Area = pygame.Rect((100,100),(600,600))
    Char = pygame.Rect((800,500),(300,300))
    Combo = pygame.Rect((800,250),(50,50))
    UserInput = pygame.Rect((350,350),(853,683))
    Timer = pygame.Rect((800,100),(110,75))
    Player = pygame.Rect((1000,100),(200,200))
    pygame.draw.rect(Screen,(255,255,255),Area)
    pygame.draw.rect(Screen,(255,255,255),Timer)
    Screen.blit(Fighters[c],Char)
    pygame.draw.rect(Screen,(255,255,255),Combo)
    pygame.display.update()
    pygame.time.delay(2000) #delay before P2 start game
    x = 0 #garbage value
    global m
    m = 2
    index = 0
    timer = pygame.time.Clock()
    #fps = 2.0 #modified later
    player = []
    Comp = []
    a = 51.0
    

   # PUT A LEVEL INDICATOR
   # TIGHTEN UP THE COMBO SEQUENCE
   # PUT UP THE IMAGES THE DESIGN TEAM GAVE YOU


    ''' P2 TURN '''
    while a >= 0: 
        for event in pygame.event.get():       
            if event.type == QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == KEYDOWN:
                if event.key == K_i:
                    v1 = v - 0.1
                    if v1 < 0.0:
                        v1 = 0.0 
                    v = v1 
                    background_music.set_volume(v1)
                if event.key == K_o:
                    v0 = v + 0.1
                    if v0 > 1.0:
                        v0 = 1.0
                    v = v0 
                    background_music.set_volume(v0)  
        while x <= 3:
            random.seed()
            index = random.randint(0,3)
            pygame.draw.rect(Screen,(255,255,255),Area)
            Screen.blit(Arrows[index],(random.randint(100,600),random.randint(100,600)))
            pygame.display.update()
            Comp.append(index)
            x += 1
            timer.tick(fps)
            if x == 4:
                time.delay(1000)
                pygame.display.update(Area)
                Screen.blit(Go_Message,Area)
                pygame.display.update(Area)
                time.delay(2000)
                pygame.draw.rect(Screen, (255,255,255),Area)
        x = 0 #reset garbage variable
        pygame.draw.rect(Screen,(255,255,255),Area)
        pygame.display.update(Area)
        while x <= 3:
            if a <= 0:
                break
            label = Font_type.render(str(int(a)),15,(255,0,0))
            pygame.draw.rect(Screen,(255,255,255),Timer)
            Screen.blit(label, Timer)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        #pygame.event.clear()
                        Pause_Menu()
                    if event.key == K_RIGHT:
                        x += 1
                        player.append(2)
                        Screen.blit(Right,UserInput)
                    elif event.key == K_UP:
                        x += 1
                        player.append(0)
                        Screen.blit(Up,UserInput)
                    elif event.key == K_LEFT:
                        x += 1
                        player.append(3)
                        Screen.blit(Left,UserInput)
                    elif event.key == K_DOWN:
                        x += 1
                        player.append(1)
                        Screen.blit(Down,UserInput)
                    if event.key == K_i:
                        v1 = v - 0.1
                        if v1 < 0.0:
                            v1 = 0.0 
                        v = v1 
                        background_music.set_volume(v1)
                    if event.key == K_o:
                        v0 = v + 0.1
                        if v0 > 1.0:
                            v0 = 1.0
                        v = v0 
                        background_music.set_volume(v0)  
                pygame.display.update(UserInput)
            a -= float(1.0/40.0)
            timer.tick(800)
            if x == 4:
                time.delay(1000)
                pygame.display.update(Area)
                Screen.blit(Watch_Message,Area)
                pygame.display.update(Area)
                time.delay(1000)
                pygame.draw.rect(Screen, (255,255,255),Area)
                time.delay(1000)
        x = 0
        if Comp == player:
            combo_P2 += 1
            pygame.draw.rect(Screen,(255,255,255),Combo)
            label = Font_type.render(str(combo_P2),15,(255,0,0))
            Screen.blit(label,Combo)
            pygame.display.update()
        else:
            pygame.display.update()
        Comp = []
        player = []
        a -= .001
        timer.tick(1000)  
    global q
    q = combo_P2
    background_music.stop()
    return combo_P2

def MASH_Screen(u,y,w,q):
    background_music.play(booba_loop_6,-1)
    index = random.randint(0,2)
    Screen.blit(Mash_Screen_Bg[index],(0,0))
    #global Player1Health
    #global Player2Health
    global m
    a = 101.0
    g = 0
    m = 3
    n = 0
    t = 0
    v = 1
    x = 1 
    while a >= 0 and (-290 < n <290):
        Timer = pygame.Rect((580,0),(90,75))
        Playerbox1 = pygame.Rect((20,20),(50,50))
        Playerbox2 = pygame.Rect((1210,20),(50,50))
        Healthf1 = pygame.Rect((50,900),(150,20))
        Healthf2 = pygame.Rect((1080,900),(150,20))
        Charachter_box1 = pygame.Rect((300,700),(300,300))
        Charachter_box2 = pygame.Rect((680,700),(300,300))
        Sprite_1 = pygame.Rect((80,300),(300,300))
        Sprite_2 = pygame.Rect((960,300),(300,300))
        Screen.blit(Fighters2[u],Sprite_1)#Charachter_box1)
        Screen.blit(Fighters2[y],Sprite_2)#Charachter_box2)
        Screen.blit(Font_type.render(str("P1"),15,(255,0,0)),Playerbox1)
        Screen.blit(Font_type.render(str("P2"),15,(255,0,0)),Playerbox2)
        pygame.draw.rect(Screen,(0,0,0),Healthf1)
        pygame.draw.rect(Screen,(0,0,0),Healthf2)
        #pygame.draw.rect(Screen,(255,255,255),Sprite_1)
        #pygame.draw.rect(Screen,(255,255,255),Sprite_2)
        player1_thug = pygame.Rect((350,450),(290+n,75))
        player2_thug = pygame.Rect((640+n,450),(290-n,75))
        pygame.draw.rect(Screen,(255,0,0),player1_thug)
        pygame.draw.rect(Screen,(255,0,255),player2_thug)

        for event in pygame.event.get():
            if a <= 0 or (-290 >= n) or (n> 290) :
                break
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    #pygame.event.clear()
                    Pause_Menu()
                if event.key == K_RIGHT:
                    t += 1
                    n -= 2 #* w
                elif event.key == K_UP:
                    t += 1 
                    n -= 2 #* w
                elif event.key == K_LEFT:
                    t += 1
                    n -= 2 #* w
                elif event.key == K_DOWN:
                    t += 1
                    n -= 2 #* w
                elif event.key == K_d:
                    g += 1
                    n += 2 #* q
                elif event.key == K_a:
                    g += 1
                    n += 2 ##* q
                elif event.key == K_s:
                    g += 1
                    n += 2 #* q
                elif event.key == K_w:
                    g += 1
                    n += 2 #* q
                if event.key == K_i:
                    v1 = v - 0.1
                    if v1 < 0.0:
                        v1 = 0.0 
                    v = v1 
                    background_music.set_volume(v1)
                if event.key == K_o:
                    v0 = v + 0.1
                    if v0 > 1.0:
                        v0 = 1.0
                    v = v0 
                    background_music.set_volume(v0)  
        a -= float(1.0/35.0)
        pygame.draw.rect(Screen,(255,255,255),Timer)
        label = Font_type.render(str(int(a)),15,(255,0,0))
        Screen.blit(label,Timer)
        player1_thug = pygame.Rect((350,450),(290+n,75))
        player2_thug = pygame.Rect((640+n,450),(290-n,75))
        pygame.draw.rect(Screen,(255,0,0),player1_thug)
        pygame.draw.rect(Screen,(255,0,255),player2_thug)
        pygame.display.update()
        Clock.tick(800)
    P1_Score = w * g
    P2_Score = q * t
    Win_Rect = pygame.Rect((180,109),(897,475))
    P1WinScrBox1 = pygame.Rect((465,353),(50,50))
    P1WinScrBox2 = pygame.Rect((537,393),(99,50))
    P1WinScrBox3 = pygame.Rect((429,480),(179,50))
    P1WinScrBox4 = pygame.Rect((868,348),(50,50))
    P1WinScrBox5 = pygame.Rect((936,391),(99,50))
    P1WinScrBox6 = pygame.Rect((830,480),(179,50))
    P2WinScrBox1 = pygame.Rect((470,351),(50,50))
    P2WinScrBox2 = pygame.Rect((539,403),(99,50))
    P2WinScrBox3 = pygame.Rect((432,487),(179,50))
    P2WinScrBox4 = pygame.Rect((869,351),(50,50))
    P2WinScrBox5 = pygame.Rect((938,401),(99,50))
    P2WinScrBox6 = pygame.Rect((830,487),(179,50))
    TieScrBox1 = pygame.Rect((483,341),(50,50))
    TieScrBox2 = pygame.Rect((551,387),(99,50))
    TieScrBox3 = pygame.Rect((444,474),(179,50))
    TieScrBox4 = pygame.Rect((884,337),(50,50))
    TieScrBox5 = pygame.Rect((953,384),(99,50))
    TieScrBox6 = pygame.Rect((846,467),(179,50))    
    label_ComboP1 = Font_type.render(str(int(w)),15,(255,0,0))
    label_ComboP2 = Font_type.render(str(int(q)),15,(255,0,0))
    label_MashCountP1 = Font_type.render(str(int(g)),15,(255,0,0)) 
    label_MashCountP2 = Font_type.render(str(int(t)),15,(255,0,0)) 
    label_TotalP1 = Font_type.render(str(int(P1_Score)),15,(255,0,0)) 
    label_TotalP2 = Font_type.render(str(int(P2_Score)),15,(255,0,0)) 
    
    while x != 0:
        if P1_Score < P2_Score: #n < 0:
            Screen.blit(P2_Win_Scr[2],Win_Rect)
            Screen.blit(label_ComboP1,P2WinScrBox1)
            Screen.blit(label_MashCountP1,P2WinScrBox2)
            Screen.blit(label_TotalP1,P2WinScrBox3)
            Screen.blit(label_ComboP2,P2WinScrBox4)
            Screen.blit(label_MashCountP2,P2WinScrBox5)
            Screen.blit(label_TotalP2,P2WinScrBox6)
            pygame.display.update()
            #print "P2 won"
            #Player2Health -= n/4
        elif P1_Score > P2_Score: #n > 0:
            Screen.blit(P1_Win_Scr[2],Win_Rect)
            Screen.blit(label_ComboP1,P1WinScrBox1)
            Screen.blit(label_MashCountP1,P1WinScrBox2)
            Screen.blit(label_TotalP1,P1WinScrBox3)
            Screen.blit(label_ComboP2,P1WinScrBox4)
            Screen.blit(label_MashCountP2,P1WinScrBox5)
            Screen.blit(label_TotalP2,P1WinScrBox6)
            pygame.display.update()
            #print "P1 won"
            #Player1Health -= n/4
        else:
            Screen.blit(Tie_Scr[2],Win_Rect) 
            Screen.blit(label_ComboP1,TieScrBox1)
            Screen.blit(label_MashCountP1,TieScrBox2)
            Screen.blit(label_TotalP1,TieScrBox3)
            Screen.blit(label_ComboP2,TieScrBox4)
            Screen.blit(label_MashCountP2,TieScrBox5)
            Screen.blit(label_TotalP2,TieScrBox6)
            pygame.display.update()
        for event in pygame.event.get():       
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if (event.key == K_RETURN) | (event.key == K_ESCAPE) :
                        x = 0
                        background_music.stop()
                    break
        #print "tie"
    #return Player1Health,Player2Health

# SEE HOW TO USE SPRITE MODULE TO PUT SPRITES IN MASH IT SCREEN

def Game():
    while done == False:
        Main_Menu()
        pygame.event.clear()
        u,y = Character_select_screen() # u and y are P1 and P2 characters respectively
        pygame.event.clear()
        w = Combo_seq_screen_P1(u) # P1 combo value
        pygame.event.clear()
        q = Combo_seq_screen_P2(y) # P2 combo value
        pygame.event.clear()
        MASH_Screen(u,y,w,q)

if __name__ == '__main__':
    Title_Screen()
    pygame.event.clear()
    Game()
