import random
import os
import time
import pygame
from pygame.locals import (KEYDOWN, QUIT, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_q, K_d, K_z, K_s, K_LSHIFT, K_RSHIFT, MOUSEBUTTONDOWN)
pygame.init()

resolution = pygame.display.Info()

screen = pygame.display.set_mode((resolution.current_w, resolution.current_h))
screen_size = [resolution.current_w, resolution.current_h]
violet = (37, 10, 105)


dossier_script = os.path.dirname(__file__)

digital_7 = os.path.join(dossier_script, "assets", "fonts", "digital-7.ttf")
Technos = os.path.join(dossier_script, "assets", "fonts", "Technos.otf")
Score_Board_St = os.path.join(dossier_script, "assets", "fonts", "Score Board St.ttf")
Arcade = os.path.join(dossier_script, "assets", "fonts", "ARCADE.ttf")






clock = pygame.time.Clock()

running = True



MODE_ACCUEIL = 1
MODE_GAME = 2
MODE_WIN1_LOSE2 = 3
MODE_WIN2_LOSE1 = 4
MODE_LA_PEACE = 5
MODE_SUCCES = 6
MODE_I_MEMES = 7

mode_actuel = MODE_ACCUEIL



grid = pygame.Surface((screen_size[0] - 20, screen_size[1] - 110))
grid.fill("#0B041F")
grid_pos = [10, 100]
grid_size = [screen_size[0] - 20, screen_size[1] - 110]

player = pygame.Surface((25,25))
player.fill("#CF2F11")
player_pos = [grid_pos[0], grid_size[1] / 2 + 100]
player_pos_instant = [player_pos[0], player_pos[1]]
player_size = [25, 25]

player_2 = pygame.Surface((25,25))
player_2.fill("#0000FF")
player_pos_2 = [grid_pos[0] + grid_size[0] - 25, grid_size[1] / 2 + 100]
player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]
player_size_2 = [25, 25]


traînées = {
    "type_x": 5,
    "type_y": 5,
    "color": "#F5FF00",
    "pos_x": player_pos[0],
    "pos_y": player_pos[1],
    "size_x": 5,
    "size_y": 5
}

traînées_finales_q = []
traînées_finales_pos_q = []
traînées_finales_size_q = []

traînées_finales_d = []
traînées_finales_pos_d = []
traînées_finales_size_d = []

traînées_finales_z = []
traînées_finales_pos_z = []
traînées_finales_size_z = []

traînées_finales_s = []
traînées_finales_pos_s = []
traînées_finales_size_s = []


traînées_finales_left = []
traînées_finales_pos_left = []
traînées_finales_size_left = []

traînées_finales_right = []
traînées_finales_pos_right = []
traînées_finales_size_right = []

traînées_finales_up = []
traînées_finales_pos_up = []
traînées_finales_size_up = []

traînées_finales_down = []
traînées_finales_pos_down = []
traînées_finales_size_down = []


executing_lightcycle_movement_q = False
executing_lightcycle_movement_d = True
executing_lightcycle_movement_z = False
executing_lightcycle_movement_s = False

executing_lightcycle_movement_left = True
executing_lightcycle_movement_right = False
executing_lightcycle_movement_up = False
executing_lightcycle_movement_down = False


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------VARIABLES/FONCTIONS I-MEMES-----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------


i_meme_sélectionné_player = 0
i_meme_sélectionné_player_2 = 0
cooldown_i_meme_sélectionné_player = 0
cooldown_i_meme_sélectionné_player_2 = 0
cooldown_i_meme_rare_sélectionné_player = 0
cooldown_i_meme_rare_sélectionné_player_2 = 0
cooldown_i_meme_épique_sélectionné_player = 0
cooldown_i_meme_épique_sélectionné_player_2 = 0
cooldown_i_meme_légendaire_sélectionné_player = 0
cooldown_i_meme_légendaire_sélectionné_player_2 = 0

cooldown_i_meme_red_bull_player = 600
cooldown_i_meme_red_bull_player_2 = 600
executing_i_meme_red_bull_player = False
executing_i_meme_red_bull_player_2 = False
executing_time_i_meme_red_bull_player = 0
executing_time_i_meme_red_bull_player_2 = 0

def i_meme_red_bull(pressed_keys, cooldown_i_meme_red_bull_player, cooldown_i_meme_red_bull_player_2, i_meme_sélectionné_player, i_meme_sélectionné_player_2, executing_i_meme_red_bull_player, executing_i_meme_red_bull_player_2, executing_time_i_meme_red_bull_player, executing_time_i_meme_red_bull_player_2) :
    if i_meme_sélectionné_player == 1 :
        if cooldown_i_meme_red_bull_player > 0 :
            cooldown_i_meme_red_bull_player -= 1

        if cooldown_i_meme_red_bull_player == 0 :
            if pressed_keys[K_LSHIFT] :
                executing_i_meme_red_bull_player == True
                cooldown_i_meme_red_bull_player == 600
        
        if executing_i_meme_red_bull_player :
            executing_time_i_meme_red_bull_player += 1

        if executing_time_i_meme_red_bull_player == 300 :
            executing_time_i_meme_red_bull_player = 0
            executing_i_meme_red_bull_player = False

    if i_meme_sélectionné_player_2 == 1 :
        if cooldown_i_meme_red_bull_player_2 > 0 :
            cooldown_i_meme_red_bull_player_2 -= 1

        if cooldown_i_meme_red_bull_player_2 == 0 :
            if pressed_keys[K_RSHIFT] :
                executing_i_meme_red_bull_player_2 == True
                cooldown_i_meme_red_bull_player_2 == 600

        if executing_i_meme_red_bull_player_2 :
            executing_time_i_meme_red_bull_player_2 += 1

        if executing_time_i_meme_red_bull_player_2 == 300 :
            executing_time_i_meme_red_bull_player_2 = 0
            executing_i_meme_red_bull_player_2 = False

    return cooldown_i_meme_red_bull_player, cooldown_i_meme_red_bull_player_2, executing_i_meme_red_bull_player, executing_i_meme_red_bull_player_2, executing_time_i_meme_red_bull_player, executing_time_i_meme_red_bull_player_2

cooldown_i_meme_disparition_player = 600
cooldown_i_meme_disparition_player_2 = 600
executing_i_meme_disparition_player = False
executing_i_meme_disparition_player_2 = False
executing_time_i_meme_disparition_player = 0
executing_time_i_meme_disparition_player_2 = 0

def i_meme_disparition(pressed_keys, i_meme_sélectionné_player, i_meme_sélectionné_player_2, cooldown_i_meme_disparition_player, cooldown_i_meme_disparition_player_2, executing_i_meme_disparition_player, executing_i_meme_disparition_player_2, executing_time_i_meme_disparition_player, executing_time_i_meme_disparition_player_2) :
    if i_meme_sélectionné_player == 2 :
        if cooldown_i_meme_disparition_player > 0 :
            cooldown_i_meme_disparition_player -= 1

        if cooldown_i_meme_disparition_player == 0 :
            if pressed_keys[K_LSHIFT] :
                executing_i_meme_disparition_player == True
                cooldown_i_meme_disparition_player == 600
        
        if executing_i_meme_disparition_player :
            executing_time_i_meme_disparition_player += 1

        if executing_time_i_meme_disparition_player == 300 :
            executing_time_i_meme_disparition_player = 0
            executing_i_meme_disparition_player = False

    if i_meme_sélectionné_player_2 == 2 :
        if cooldown_i_meme_disparition_player_2 > 0 :
            cooldown_i_meme_disparition_player_2 -= 1

        if cooldown_i_meme_disparition_player_2 == 0 :
            if pressed_keys[K_RSHIFT] :
                executing_i_meme_disparition_player_2 == True
                cooldown_i_meme_disparition_player_2 == 600

        if executing_i_meme_disparition_player_2 :
            executing_time_i_meme_disparition_player_2 += 1

        if executing_time_i_meme_disparition_player_2 == 300 :
            executing_time_i_meme_disparition_player_2 = 0
            executing_i_meme_disparition_player_2 = False

    return cooldown_i_meme_disparition_player, cooldown_i_meme_disparition_player_2, executing_i_meme_disparition_player, executing_i_meme_disparition_player_2, executing_time_i_meme_disparition_player, executing_time_i_meme_disparition_player_2

utilisé_i_meme_jackpot_player = False
utilisé_i_meme_jackpot_player_2 = False

def i_meme_jackpot(i_meme_sélectionné_player, i_meme_sélectionné_player_2, score_player, score_player_2, utilisé_i_meme_jackpot_player, utilisé_i_meme_jackpot_player_2) :
    if i_meme_sélectionné_player == 3 :
        if utilisé_i_meme_jackpot_player == False :
            score_player *= 2
            utilisé_i_meme_jackpot_player = True
    if i_meme_sélectionné_player_2 == 3 :
        if utilisé_i_meme_jackpot_player_2 == False :
            score_player_2 *= 2
            utilisé_i_meme_jackpot_player_2 = True

    return score_player, score_player_2, utilisé_i_meme_jackpot_player, utilisé_i_meme_jackpot_player_2

utilisé_i_meme_devil_never_cry_player = False
utilisé_i_meme_devil_never_cry_player_2 = False
invulnérabilité_temporaire_player = False
invulnérabilité_temporaire_player_2 = False
time_invulnérabilité_temporaire_player = 0
time_invulnérabilité_temporaire_player_2 = 0

def i_meme_devil_never_cry(i_meme_sélectionné_player, i_meme_sélectionné_player_2, mode_actuel, utilisé_i_meme_devil_never_cry_player, utilisé_i_meme_devil_never_cry_player_2,invulnérabilité_temporaire_player, invulnérabilité_temporaire_player_2, time_invulnérabilité_temporaire_player, time_invulnérabilité_temporaire_player_2) :
    if i_meme_sélectionné_player == 4 :
        if mode_actuel == MODE_WIN2_LOSE1 :
            if utilisé_i_meme_devil_never_cry_player == False :
                mode_actuel = MODE_GAME
                utilisé_i_meme_devil_never_cry_player = True
                invulnérabilité_temporaire_player = True
        if invulnérabilité_temporaire_player :
            time_invulnérabilité_temporaire_player += 1
        if time_invulnérabilité_temporaire_player == 300 :
            invulnérabilité_temporaire_player = False
            time_invulnérabilité_temporaire_player = 0

    if i_meme_sélectionné_player_2 == 4 :
        if mode_actuel == MODE_WIN1_LOSE2 :
            if utilisé_i_meme_devil_never_cry_player_2 == False :
                mode_actuel = MODE_GAME
                utilisé_i_meme_devil_never_cry_player_2 = True
                invulnérabilité_temporaire_player_2 = True
        if invulnérabilité_temporaire_player_2 :
            time_invulnérabilité_temporaire_player_2 += 1
        if time_invulnérabilité_temporaire_player_2 == 300 :
            invulnérabilité_temporaire_player_2 = False
            time_invulnérabilité_temporaire_player_2 = 0

    return mode_actuel, utilisé_i_meme_devil_never_cry_player, utilisé_i_meme_devil_never_cry_player_2, invulnérabilité_temporaire_player, invulnérabilité_temporaire_player_2, time_invulnérabilité_temporaire_player, time_invulnérabilité_temporaire_player_2

cooldown_i_meme_hyperdrive_player = 1200
cooldown_i_meme_hyperdrive_player_2 = 1200

def i_meme_hyperdrive(pressed_keys, i_meme_sélectionné_player, i_meme_sélectionné_player_2, cooldown_i_meme_hyperdrive_player, cooldown_i_meme_hyperdrive_player_2, player_pos, player_pos_2, player_size, player_size_2, grid_pos, grid_size, executing_lightcycle_movement_q, executing_lightcycle_movement_d, executing_lightcycle_movement_z, executing_lightcycle_movement_s, executing_lightcycle_movement_left, executing_lightcycle_movement_right, executing_lightcycle_movement_up, executing_lightcycle_movement_down) :
    if i_meme_sélectionné_player == 5 :
        if cooldown_i_meme_hyperdrive_player > 0 :
            cooldown_i_meme_hyperdrive_player -= 1

        if cooldown_i_meme_hyperdrive_player == 0 :
            if pressed_keys[K_LSHIFT] :
                if executing_lightcycle_movement_q :
                    player_pos[0] = grid_pos[0] + 100
                if executing_lightcycle_movement_d :
                    player_pos[0] = grid_pos[0] + grid_size[0] - player_size[0] - 100
                if executing_lightcycle_movement_z :
                    player_pos[1] = grid_pos[1] + 100
                if executing_lightcycle_movement_s :
                    player_pos[1] = grid_pos[1] + grid_size[1] - player_size[1] - 100
                cooldown_i_meme_hyperdrive_player = 1200

    if i_meme_sélectionné_player_2 == 5 :
        if cooldown_i_meme_hyperdrive_player_2 > 0 :
            cooldown_i_meme_hyperdrive_player_2 -= 1

        if cooldown_i_meme_hyperdrive_player_2 == 0 :
            if pressed_keys[K_RSHIFT] :
                if executing_lightcycle_movement_left :
                    player_pos_2[0] = grid_pos[0] + 100
                if executing_lightcycle_movement_right :
                    player_pos_2[0] = grid_pos[0] + grid_size[0] - player_size_2[0] - 100
                if executing_lightcycle_movement_up :
                    player_pos_2[1] = grid_pos[1] + 100
                if executing_lightcycle_movement_down :
                    player_pos_2[1] = grid_pos[1] + grid_size[1] - player_size_2[1] - 100
                cooldown_i_meme_hyperdrive_player_2 = 1200

    return cooldown_i_meme_hyperdrive_player, cooldown_i_meme_hyperdrive_player_2, player_pos, player_pos_2

utilisé_i_meme_nope_player = False
utilisé_i_meme_nope_player_2 = False
cooldown_i_meme_nope_player = 1200
cooldown_i_meme_nope_player_2 = 1200

def i_meme_nope(pressed_keys, i_meme_sélectionné_player, i_meme_sélectionné_player_2, cooldown_i_meme_nope_player, cooldown_i_meme_nope_player_2, utilisé_i_meme_nope_player, utilisé_i_meme_nope_player_2, executing_i_meme_red_bull_player, executing_i_meme_red_bull_player_2, executing_i_meme_disparition_player, executing_i_meme_disparition_player_2, invulnérabilité_temporaire_player, invulnérabilité_temporaire_player_2, executing_i_meme_c_est_quoi_ce_monde_player, executing_i_meme_c_est_quoi_ce_monde_player_2, executing_i_meme_virtual_insanity_player, executing_i_meme_virtual_insanity_player_2) :
    if i_meme_sélectionné_player == 6 :
        if cooldown_i_meme_nope_player > 0 :
            cooldown_i_meme_nope_player -= 1

        if cooldown_i_meme_nope_player == 0 :
            if pressed_keys[K_LSHIFT] :
                if utilisé_i_meme_nope_player == False :
                    if executing_i_meme_red_bull_player_2 :
                        executing_i_meme_red_bull_player_2 = False
                    if executing_i_meme_disparition_player_2 :
                        executing_i_meme_disparition_player_2 = False
                    if invulnérabilité_temporaire_player_2 :
                        invulnérabilité_temporaire_player_2 = False
                    if executing_i_meme_c_est_quoi_ce_monde_player_2 :
                        executing_i_meme_c_est_quoi_ce_monde_player_2 = False
                    if executing_i_meme_virtual_insanity_player_2 :
                        executing_i_meme_virtual_insanity_player_2 = False
                    cooldown_i_meme_nope_player = 1200
                    utilisé_i_meme_nope_player = True

    if i_meme_sélectionné_player_2 == 6 :
        if cooldown_i_meme_nope_player_2 > 0 :
            cooldown_i_meme_nope_player_2 -= 1

        if cooldown_i_meme_nope_player_2 == 0 :
            if pressed_keys[K_RSHIFT] :
                if utilisé_i_meme_nope_player_2 == False :
                    if executing_i_meme_red_bull_player :
                        executing_i_meme_red_bull_player = False
                    if executing_i_meme_disparition_player :
                        executing_i_meme_disparition_player = False
                    if invulnérabilité_temporaire_player :
                        invulnérabilité_temporaire_player = False
                    if executing_i_meme_c_est_quoi_ce_monde_player :
                        executing_i_meme_c_est_quoi_ce_monde_player = False
                    if executing_i_meme_virtual_insanity_player :
                        executing_i_meme_virtual_insanity_player = False
                    cooldown_i_meme_nope_player_2 = 1200
                    utilisé_i_meme_nope_player_2 = True

    return cooldown_i_meme_nope_player, cooldown_i_meme_nope_player_2, utilisé_i_meme_nope_player, utilisé_i_meme_nope_player_2, executing_i_meme_red_bull_player, executing_i_meme_red_bull_player_2, executing_i_meme_disparition_player, executing_i_meme_disparition_player_2, invulnérabilité_temporaire_player, invulnérabilité_temporaire_player_2, executing_i_meme_c_est_quoi_ce_monde_player, executing_i_meme_c_est_quoi_ce_monde_player_2, executing_i_meme_virtual_insanity_player, executing_i_meme_virtual_insanity_player_2

cooldown_i_meme_gandalf_player = 1200
cooldown_i_meme_gandalf_player_2 = 1200

gandalf_murs_petit_1 = {
    "type_x" : 25,
    "type_y" : 50,
    "color" : "#4D3206",
    "pos_x" : player_pos[0] - 50,
    "pos_y" : player_pos[1] - 25,
    "size_x" : 25,
    "size_y" : 50
}

gandalf_murs_grand = {
    "type_x" : 125,
    "type_y" : 20,
    "color" : "#4D3206",
    "pos_x" : player_pos[0] - 50,
    "pos_y" : player_pos[1] - 50,
    "size_x" : 125,
    "size_y" : 20
}

gandalf_murs_petit_2 = {
    "type_x" : 25,
    "type_y" : 50,
    "color" : "#4D3206",
    "pos_x" : player_pos[0] + 50,
    "pos_y" : player_pos[1] - 25,
    "size_x" : 25,
    "size_y" : 50
}

gandalf_murs_finaux_petit_1_q = []
gandalf_murs_finaux_petit_1_q_pos = []
gandalf_murs_finaux_petit_1_q_size = []
gandalf_murs_finaux_grand_q = []
gandalf_murs_finaux_grand_q_pos = []
gandalf_murs_finaux_grand_q_size = []
gandalf_murs_finaux_petit_2_q = []
gandalf_murs_finaux_petit_2_q_pos = []
gandalf_murs_finaux_petit_2_q_size = []

gandalf_murs_finaux_petit_1_d = []
gandalf_murs_finaux_petit_1_d_pos = []
gandalf_murs_finaux_petit_1_d_size = []
gandalf_murs_finaux_grand_d = []
gandalf_murs_finaux_grand_d_pos = []
gandalf_murs_finaux_grand_d_size = []
gandalf_murs_finaux_petit_2_d = []
gandalf_murs_finaux_petit_2_d_pos = []
gandalf_murs_finaux_petit_2_d_size = []

gandalf_murs_finaux_petit_1_z = []
gandalf_murs_finaux_petit_1_z_pos = []
gandalf_murs_finaux_petit_1_z_size = []
gandalf_murs_finaux_grand_z = []
gandalf_murs_finaux_grand_z_pos = []
gandalf_murs_finaux_grand_z_size = []
gandalf_murs_finaux_petit_2_z = []
gandalf_murs_finaux_petit_2_z_pos = []
gandalf_murs_finaux_petit_2_z_size = []

gandalf_murs_finaux_petit_1_s = []
gandalf_murs_finaux_petit_1_s_pos = []
gandalf_murs_finaux_petit_1_s_size = []
gandalf_murs_finaux_grand_s = []
gandalf_murs_finaux_grand_s_pos = []
gandalf_murs_finaux_grand_s_size = []
gandalf_murs_finaux_petit_2_s = []
gandalf_murs_finaux_petit_2_s_pos = []
gandalf_murs_finaux_petit_2_s_size = []


gandalf_murs_finaux_petit_1_left = []
gandalf_murs_finaux_petit_1_left_pos = []
gandalf_murs_finaux_petit_1_left_size = []
gandalf_murs_finaux_grand_left = []
gandalf_murs_finaux_grand_left_pos = []
gandalf_murs_finaux_grand_left_size = []
gandalf_murs_finaux_petit_2_left = []
gandalf_murs_finaux_petit_2_left_pos = []
gandalf_murs_finaux_petit_2_left_size = []

gandalf_murs_finaux_petit_1_right = []
gandalf_murs_finaux_petit_1_right_pos = []
gandalf_murs_finaux_petit_1_right_size = []
gandalf_murs_finaux_grand_right = []
gandalf_murs_finaux_grand_right_pos = []
gandalf_murs_finaux_grand_right_size = []
gandalf_murs_finaux_petit_2_right = []
gandalf_murs_finaux_petit_2_right_pos = []
gandalf_murs_finaux_petit_2_right_size = []

gandalf_murs_finaux_petit_1_up = []
gandalf_murs_finaux_petit_1_up_pos = []
gandalf_murs_finaux_petit_1_up_size = []
gandalf_murs_finaux_grand_up = []
gandalf_murs_finaux_grand_up_pos = []
gandalf_murs_finaux_grand_up_size = []
gandalf_murs_finaux_petit_2_up = []
gandalf_murs_finaux_petit_2_up_pos = []
gandalf_murs_finaux_petit_2_up_size = []

gandalf_murs_finaux_petit_1_down = []
gandalf_murs_finaux_petit_1_down_pos = []
gandalf_murs_finaux_petit_1_down_size = []
gandalf_murs_finaux_grand_down = []
gandalf_murs_finaux_grand_down_pos = []
gandalf_murs_finaux_grand_down_size = []
gandalf_murs_finaux_petit_2_down = []
gandalf_murs_finaux_petit_2_down_pos = []
gandalf_murs_finaux_petit_2_down_size = []

def i_meme_gandalf(pressed_keys, player_pos, player_pos_2, executing_lightcycle_movement_q, executing_lightcycle_movement_d, executing_lightcycle_movement_z, executing_lightcycle_movement_s, executing_lightcycle_movement_left, executing_lightcycle_movement_right, executing_lightcycle_movement_up, executing_lightcycle_movement_down, i_meme_sélectionné_player, i_meme_sélectionné_player_2, gandalf_murs_petit_1, gandalf_murs_grand, gandalf_murs_petit_2, cooldown_i_meme_gandalf_player, cooldown_i_meme_gandalf_player_2, gandalf_murs_finaux_petit_1_q, gandalf_murs_finaux_petit_1_q_pos, gandalf_murs_finaux_petit_1_q_size, gandalf_murs_finaux_grand_q, gandalf_murs_finaux_grand_q_pos, gandalf_murs_finaux_grand_q_size, gandalf_murs_finaux_petit_2_q, gandalf_murs_finaux_petit_2_q_pos, gandalf_murs_finaux_petit_2_q_size, gandalf_murs_finaux_petit_1_d, gandalf_murs_finaux_petit_1_d_pos, gandalf_murs_finaux_petit_1_d_size, gandalf_murs_finaux_grand_d, gandalf_murs_finaux_grand_d_pos, gandalf_murs_finaux_grand_d_size, gandalf_murs_finaux_petit_2_d, gandalf_murs_finaux_petit_2_d_pos, gandalf_murs_finaux_petit_2_d_size, gandalf_murs_finaux_petit_1_z, gandalf_murs_finaux_petit_1_z_pos, gandalf_murs_finaux_petit_1_z_size, gandalf_murs_finaux_grand_z, gandalf_murs_finaux_grand_z_pos, gandalf_murs_finaux_grand_z_size, gandalf_murs_finaux_petit_2_z, gandalf_murs_finaux_petit_2_z_pos, gandalf_murs_finaux_petit_2_z_size, gandalf_murs_finaux_petit_1_s, gandalf_murs_finaux_petit_1_s_pos, gandalf_murs_finaux_petit_1_s_size, gandalf_murs_finaux_grand_s, gandalf_murs_finaux_grand_s_pos, gandalf_murs_finaux_grand_s_size, gandalf_murs_finaux_petit_2_s, gandalf_murs_finaux_petit_2_s_pos, gandalf_murs_finaux_petit_2_s_size, gandalf_murs_finaux_petit_1_left, gandalf_murs_finaux_petit_1_left_pos, gandalf_murs_finaux_petit_1_left_size, gandalf_murs_finaux_grand_left, gandalf_murs_finaux_grand_left_pos, gandalf_murs_finaux_grand_left_size, gandalf_murs_finaux_petit_2_left, gandalf_murs_finaux_petit_2_left_pos, gandalf_murs_finaux_petit_2_left_size, gandalf_murs_finaux_petit_1_right, gandalf_murs_finaux_petit_1_right_pos, gandalf_murs_finaux_petit_1_right_size, gandalf_murs_finaux_grand_right, gandalf_murs_finaux_grand_right_pos, gandalf_murs_finaux_grand_right_size, gandalf_murs_finaux_petit_2_right, gandalf_murs_finaux_petit_2_right_pos, gandalf_murs_finaux_petit_2_right_size, gandalf_murs_finaux_petit_1_up, gandalf_murs_finaux_petit_1_up_pos, gandalf_murs_finaux_petit_1_up_size, gandalf_murs_finaux_grand_up,gandalf_murs_finaux_grand_up_pos, gandalf_murs_finaux_grand_up_size, gandalf_murs_finaux_petit_2_up, gandalf_murs_finaux_petit_2_up_pos, gandalf_murs_finaux_petit_2_up_size, gandalf_murs_finaux_petit_1_down, gandalf_murs_finaux_petit_1_down_pos, gandalf_murs_finaux_petit_1_down_size, gandalf_murs_finaux_grand_down, gandalf_murs_finaux_grand_down_pos, gandalf_murs_finaux_grand_down_size, gandalf_murs_finaux_petit_2_down, gandalf_murs_finaux_petit_2_down_pos, gandalf_murs_finaux_petit_2_down_size) :
    if i_meme_sélectionné_player == 7 :
        if cooldown_i_meme_gandalf_player > 0 :
            cooldown_i_meme_gandalf_player -= 1

        if cooldown_i_meme_gandalf_player == 0 :
            if pressed_keys[K_LSHIFT] :
                if executing_lightcycle_movement_left :
                    m1 = None
                    m1_pos = [5, 5]
                    m1_size = [5, 5]

                    g1 = gandalf_murs_petit_1.copy()
                    g1 = {
                        "type_x" : 50,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0] - 25,
                        "pos_y" : player_pos_2[1] + 50,
                        "size_x" : 50,
                        "size_y" : 25
                    }

                    m1 = pygame.Surface((g1["type_x"], g1["type_y"]))
                    m1_pos = [g1["pos_x"], g1["pos_y"]]
                    m1_size = [g1["size_x"], g1["size_y"]]

                    if m1 is not None :
                        gandalf_murs_finaux_petit_1_left.append(m1)
                        gandalf_murs_finaux_petit_1_left_pos.append(m1_pos)
                        gandalf_murs_finaux_petit_1_left_size.append(m1_size)

                    m2 = None
                    m2_pos = [5, 5]
                    m2_size = [5, 5]

                    g2 = gandalf_murs_grand.copy()
                    g2 = {
                        "type_x" : 25,
                        "type_y" : 125,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0] - 50,
                        "pos_y" : player_pos_2[1] - 50,
                        "size_x" : 25,
                        "size_y" : 125
                    }

                    m2 = pygame.Surface((g2["type_x"], g2["type_y"]))
                    m2_pos = [g2["pos_x"], g2["pos_y"]]
                    m2_size = [g2["size_x"], g2["size_y"]]

                    if m2 is not None :
                        gandalf_murs_finaux_grand_left.append(m2)
                        gandalf_murs_finaux_grand_left_pos.append(m2_pos)
                        gandalf_murs_finaux_grand_left_size.append(m2_size)

                    m3 = None
                    m3_pos = [5, 5]
                    m3_size = [5, 5]

                    g3 = gandalf_murs_petit_2.copy()
                    g3 = {
                        "type_x" : 50,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0] - 25,
                        "pos_y" : player_pos_2[1] - 50,
                        "size_x" : 50,
                        "size_y" : 25
                    }

                    m3 = pygame.Surface((g3["type_x"], g3["type_y"]))
                    m3_pos = [g3["pos_x"], g3["pos_y"]]
                    m3_size = [g3["size_x"], g3["size_y"]]

                    if m3 is not None :
                        gandalf_murs_finaux_petit_2_left.append(m3)
                        gandalf_murs_finaux_petit_2_left_pos.append(m3_pos)
                        gandalf_murs_finaux_petit_2_left_size.append(m3_size)

                if executing_lightcycle_movement_right :
                    m1 = None
                    m1_pos = [5, 5]
                    m1_size = [5, 5]

                    g1 = gandalf_murs_petit_1.copy()
                    g1 = {
                        "type_x" : 50,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0],
                        "pos_y" : player_pos_2[1] - 50,
                        "size_x" : 50,
                        "size_y" : 25
                    }

                    m1 = pygame.Surface((g1["type_x"], g1["type_y"]))
                    m1_pos = [g1["pos_x"], g1["pos_y"]]
                    m1_size = [g1["size_x"], g1["size_y"]]

                    if m1 is not None :
                        gandalf_murs_finaux_petit_1_right.append(m1)
                        gandalf_murs_finaux_petit_1_right_pos.append(m1_pos)
                        gandalf_murs_finaux_petit_1_right_size.append(m1_size)

                    m2 = None
                    m2_pos = [5, 5]
                    m2_size = [5, 5]

                    g2 = gandalf_murs_grand.copy()
                    g2 = {
                        "type_x" : 25,
                        "type_y" : 125,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0] + 50,
                        "pos_y" : player_pos_2[1] - 50,
                        "size_x" : 25,
                        "size_y" : 125
                    }

                    m2 = pygame.Surface((g2["type_x"], g2["type_y"]))
                    m2_pos = [g2["pos_x"], g2["pos_y"]]
                    m2_size = [g2["size_x"], g2["size_y"]]

                    if m2 is not None :
                        gandalf_murs_finaux_grand_right.append(m2)
                        gandalf_murs_finaux_grand_right_pos.append(m2_pos)
                        gandalf_murs_finaux_grand_right_size.append(m2_size)

                    m3 = None
                    m3_pos = [5, 5]
                    m3_size = [5, 5]

                    g3 = gandalf_murs_petit_2.copy()
                    g3 = {
                        "type_x" : 50,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0],
                        "pos_y" : player_pos_2[1] + 50,
                        "size_x" : 50,
                        "size_y" : 25
                    }

                    m3 = pygame.Surface((g3["type_x"], g3["type_y"]))
                    m3_pos = [g3["pos_x"], g3["pos_y"]]
                    m3_size = [g3["size_x"], g3["size_y"]]

                    if m3 is not None :
                        gandalf_murs_finaux_petit_2_right.append(m3)
                        gandalf_murs_finaux_petit_2_right_pos.append(m3_pos)
                        gandalf_murs_finaux_petit_2_right_size.append(m3_size)

                if executing_lightcycle_movement_up :
                    m1 = None
                    m1_pos = [5, 5]
                    m1_size = [5, 5]

                    g1 = gandalf_murs_petit_1.copy()
                    g1 = {
                        "type_x" : 25,
                        "type_y" : 50,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0] - 50,
                        "pos_y" : player_pos_2[1] + 25,
                        "size_x" : 25,
                        "size_y" : 50
                    }

                    m1 = pygame.Surface((g1["type_x"], g1["type_y"]))
                    m1_pos = [g1["pos_x"], g1["pos_y"]]
                    m1_size = [g1["size_x"], g1["size_y"]]

                    if m1 is not None :
                        gandalf_murs_finaux_petit_1_up.append(m1)
                        gandalf_murs_finaux_petit_1_up_pos.append(m1_pos)
                        gandalf_murs_finaux_petit_1_up_size.append(m1_size)

                    m2 = None
                    m2_pos = [5, 5]
                    m2_size = [5, 5]

                    g2 = gandalf_murs_grand.copy()
                    g2 = {
                        "type_x" : 125,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0] - 50,
                        "pos_y" : player_pos_2[1] - 50,
                        "size_x" : 125,
                        "size_y" : 25
                    }

                    m2 = pygame.Surface((g2["type_x"], g2["type_y"]))
                    m2_pos = [g2["pos_x"], g2["pos_y"]]
                    m2_size = [g2["size_x"], g2["size_y"]]

                    if m2 is not None :
                        gandalf_murs_finaux_grand_up.append(m2)
                        gandalf_murs_finaux_grand_up_pos.append(m2_pos)
                        gandalf_murs_finaux_grand_up_size.append(m2_size)

                    m3 = None
                    m3_pos = [5, 5]
                    m3_size = [5, 5]

                    g3 = gandalf_murs_petit_2.copy()
                    g3 = {
                        "type_x" : 25,
                        "type_y" : 50,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0] + 50,
                        "pos_y" : player_pos_2[1] - 25,
                        "size_x" : 25,
                        "size_y" : 50
                    }

                    m3 = pygame.Surface((g3["type_x"], g3["type_y"]))
                    m3_pos = [g3["pos_x"], g3["pos_y"]]
                    m3_size = [g3["size_x"], g3["size_y"]]

                    if m3 is not None :
                        gandalf_murs_finaux_petit_2_up.append(m3)
                        gandalf_murs_finaux_petit_2_up_pos.append(m3_pos)
                        gandalf_murs_finaux_petit_2_up_size.append(m3_size)

                if executing_lightcycle_movement_down :
                    m1 = None
                    m1_pos = [5, 5]
                    m1_size = [5, 5]

                    g1 = gandalf_murs_petit_1.copy()
                    g1 = {
                        "type_x" : 25,
                        "type_y" : 50,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0] - 50,
                        "pos_y" : player_pos_2[1],
                        "size_x" : 25,
                        "size_y" : 50
                    }

                    m1 = pygame.Surface((g1["type_x"], g1["type_y"]))
                    m1_pos = [g1["pos_x"], g1["pos_y"]]
                    m1_size = [g1["size_x"], g1["size_y"]]

                    if m1 is not None :
                        gandalf_murs_finaux_petit_1_down.append(m1)
                        gandalf_murs_finaux_petit_1_down_pos.append(m1_pos)
                        gandalf_murs_finaux_petit_1_down_size.append(m1_size)

                    m2 = None
                    m2_pos = [5, 5]
                    m2_size = [5, 5]

                    g2 = gandalf_murs_grand.copy()
                    g2 = {
                        "type_x" : 125,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0] + 50,
                        "pos_y" : player_pos_2[1] - 50,
                        "size_x" : 125,
                        "size_y" : 25
                    }

                    m2 = pygame.Surface((g2["type_x"], g2["type_y"]))
                    m2_pos = [g2["pos_x"], g2["pos_y"]]
                    m2_size = [g2["size_x"], g2["size_y"]]

                    if m2 is not None :
                        gandalf_murs_finaux_grand_down.append(m2)
                        gandalf_murs_finaux_grand_down_pos.append(m2_pos)
                        gandalf_murs_finaux_grand_down_size.append(m2_size)

                    m3 = None
                    m3_pos = [5, 5]
                    m3_size = [5, 5]

                    g3 = gandalf_murs_petit_2.copy()
                    g3 = {
                        "type_x" : 25,
                        "type_y" : 50,
                        "color" : "#4D3206",
                        "pos_x" : player_pos_2[0] + 50,
                        "pos_y" : player_pos_2[1],
                        "size_x" : 25,
                        "size_y" : 50
                    }

                    m3 = pygame.Surface((g3["type_x"], g3["type_y"]))
                    m3_pos = [g3["pos_x"], g3["pos_y"]]
                    m3_size = [g3["size_x"], g3["size_y"]]

                    if m3 is not None :
                        gandalf_murs_finaux_petit_2_down.append(m3)
                        gandalf_murs_finaux_petit_2_down_pos.append(m3_pos)
                        gandalf_murs_finaux_petit_2_down_size.append(m3_size)

            cooldown_i_meme_gandalf_player = 1200

    if i_meme_sélectionné_player_2 == 7 :
        if cooldown_i_meme_gandalf_player_2 > 0 :
            cooldown_i_meme_gandalf_player_2 -= 1

        if cooldown_i_meme_gandalf_player_2 == 0 :
            if pressed_keys[K_RSHIFT] :
                if executing_lightcycle_movement_q :
                    m1 = None
                    m1_pos = [5, 5]
                    m1_size = [5, 5]

                    g1 = gandalf_murs_petit_1.copy()
                    g1 = {
                        "type_x" : 50,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0] - 25,
                        "pos_y" : player_pos[1] + 50,
                        "size_x" : 50,
                        "size_y" : 25
                    }

                    m1 = pygame.Surface((g1["type_x"], g1["type_y"]))
                    m1_pos = [g1["pos_x"], g1["pos_y"]]
                    m1_size = [g1["size_x"], g1["size_y"]]

                    if m1 is not None :
                        gandalf_murs_finaux_petit_1_q.append(m1)
                        gandalf_murs_finaux_petit_1_q_pos.append(m1_pos)
                        gandalf_murs_finaux_petit_1_q_size.append(m1_size)

                    m2 = None
                    m2_pos = [5, 5]
                    m2_size = [5, 5]

                    g2 = gandalf_murs_grand.copy()
                    g2 = {
                        "type_x" : 25,
                        "type_y" : 125,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0] - 50,
                        "pos_y" : player_pos[1] - 50,
                        "size_x" : 25,
                        "size_y" : 125
                    }

                    m2 = pygame.Surface((g2["type_x"], g2["type_y"]))
                    m2_pos = [g2["pos_x"], g2["pos_y"]]
                    m2_size = [g2["size_x"], g2["size_y"]]

                    if m2 is not None :
                        gandalf_murs_finaux_grand_q.append(m2)
                        gandalf_murs_finaux_grand_q_pos.append(m2_pos)
                        gandalf_murs_finaux_grand_q_size.append(m2_size)

                    m3 = None
                    m3_pos = [5, 5]
                    m3_size = [5, 5]

                    g3 = gandalf_murs_petit_2.copy()
                    g3 = {
                        "type_x" : 50,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0] - 25,
                        "pos_y" : player_pos[1] - 50,
                        "size_x" : 50,
                        "size_y" : 25
                    }

                    m3 = pygame.Surface((g3["type_x"], g3["type_y"]))
                    m3_pos = [g3["pos_x"], g3["pos_y"]]
                    m3_size = [g3["size_x"], g3["size_y"]]

                    if m3 is not None :
                        gandalf_murs_finaux_petit_2_q.append(m3)
                        gandalf_murs_finaux_petit_2_q_pos.append(m3_pos)
                        gandalf_murs_finaux_petit_2_q_size.append(m3_size)

                if executing_lightcycle_movement_d :
                    m1 = None
                    m1_pos = [5, 5]
                    m1_size = [5, 5]

                    g1 = gandalf_murs_petit_1.copy()
                    g1 = {
                        "type_x" : 50,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0],
                        "pos_y" : player_pos[1] - 50,
                        "size_x" : 50,
                        "size_y" : 25
                    }

                    m1 = pygame.Surface((g1["type_x"], g1["type_y"]))
                    m1_pos = [g1["pos_x"], g1["pos_y"]]
                    m1_size = [g1["size_x"], g1["size_y"]]

                    if m1 is not None :
                        gandalf_murs_finaux_petit_1_d.append(m1)
                        gandalf_murs_finaux_petit_1_d_pos.append(m1_pos)
                        gandalf_murs_finaux_petit_1_d_size.append(m1_size)

                    m2 = None
                    m2_pos = [5, 5]
                    m2_size = [5, 5]

                    g2 = gandalf_murs_grand.copy()
                    g2 = {
                        "type_x" : 25,
                        "type_y" : 125,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0] + 50,
                        "pos_y" : player_pos[1] - 50,
                        "size_x" : 25,
                        "size_y" : 125
                    }

                    m2 = pygame.Surface((g2["type_x"], g2["type_y"]))
                    m2_pos = [g2["pos_x"], g2["pos_y"]]
                    m2_size = [g2["size_x"], g2["size_y"]]

                    if m2 is not None :
                        gandalf_murs_finaux_grand_d.append(m2)
                        gandalf_murs_finaux_grand_d_pos.append(m2_pos)
                        gandalf_murs_finaux_grand_d_size.append(m2_size)

                    m3 = None
                    m3_pos = [5, 5]
                    m3_size = [5, 5]

                    g3 = gandalf_murs_petit_2.copy()
                    g3 = {
                        "type_x" : 50,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0],
                        "pos_y" : player_pos[1] + 50,
                        "size_x" : 50,
                        "size_y" : 25
                    }

                    m3 = pygame.Surface((g3["type_x"], g3["type_y"]))
                    m3_pos = [g3["pos_x"], g3["pos_y"]]
                    m3_size = [g3["size_x"], g3["size_y"]]

                    if m3 is not None :
                        gandalf_murs_finaux_petit_2_d.append(m3)
                        gandalf_murs_finaux_petit_2_d_pos.append(m3_pos)
                        gandalf_murs_finaux_petit_2_d_size.append(m3_size)

                if executing_lightcycle_movement_z :
                    m1 = None
                    m1_pos = [5, 5]
                    m1_size = [5, 5]

                    g1 = gandalf_murs_petit_1.copy()
                    g1 = {
                        "type_x" : 25,
                        "type_y" : 50,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0] - 50,
                        "pos_y" : player_pos[1] + 25,
                        "size_x" : 25,
                        "size_y" : 50
                    }

                    m1 = pygame.Surface((g1["type_x"], g1["type_y"]))
                    m1_pos = [g1["pos_x"], g1["pos_y"]]
                    m1_size = [g1["size_x"], g1["size_y"]]

                    if m1 is not None :
                        gandalf_murs_finaux_petit_1_z.append(m1)
                        gandalf_murs_finaux_petit_1_z_pos.append(m1_pos)
                        gandalf_murs_finaux_petit_1_z_size.append(m1_size)

                    m2 = None
                    m2_pos = [5, 5]
                    m2_size = [5, 5]

                    g2 = gandalf_murs_grand.copy()
                    g2 = {
                        "type_x" : 125,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0] - 50,
                        "pos_y" : player_pos[1] - 50,
                        "size_x" : 125,
                        "size_y" : 25
                    }

                    m2 = pygame.Surface((g2["type_x"], g2["type_y"]))
                    m2_pos = [g2["pos_x"], g2["pos_y"]]
                    m2_size = [g2["size_x"], g2["size_y"]]

                    if m2 is not None :
                        gandalf_murs_finaux_grand_z.append(m2)
                        gandalf_murs_finaux_grand_z_pos.append(m2_pos)
                        gandalf_murs_finaux_grand_z_size.append(m2_size)

                    m3 = None
                    m3_pos = [5, 5]
                    m3_size = [5, 5]

                    g3 = gandalf_murs_petit_2.copy()
                    g3 = {
                        "type_x" : 25,
                        "type_y" : 50,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0] + 50,
                        "pos_y" : player_pos[1] - 25,
                        "size_x" : 25,
                        "size_y" : 50
                    }

                    m3 = pygame.Surface((g3["type_x"], g3["type_y"]))
                    m3_pos = [g3["pos_x"], g3["pos_y"]]
                    m3_size = [g3["size_x"], g3["size_y"]]

                    if m3 is not None :
                        gandalf_murs_finaux_petit_2_z.append(m3)
                        gandalf_murs_finaux_petit_2_z_pos.append(m3_pos)
                        gandalf_murs_finaux_petit_2_z_size.append(m3_size)

                if executing_lightcycle_movement_s :
                    m1 = None
                    m1_pos = [5, 5]
                    m1_size = [5, 5]

                    g1 = gandalf_murs_petit_1.copy()
                    g1 = {
                        "type_x" : 25,
                        "type_y" : 50,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0] - 50,
                        "pos_y" : player_pos[1],
                        "size_x" : 25,
                        "size_y" : 50
                    }

                    m1 = pygame.Surface((g1["type_x"], g1["type_y"]))
                    m1_pos = [g1["pos_x"], g1["pos_y"]]
                    m1_size = [g1["size_x"], g1["size_y"]]

                    if m1 is not None :
                        gandalf_murs_finaux_petit_1_s.append(m1)
                        gandalf_murs_finaux_petit_1_s_pos.append(m1_pos)
                        gandalf_murs_finaux_petit_1_s_size.append(m1_size)

                    m2 = None
                    m2_pos = [5, 5]
                    m2_size = [5, 5]

                    g2 = gandalf_murs_grand.copy()
                    g2 = {
                        "type_x" : 125,
                        "type_y" : 25,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0] + 50,
                        "pos_y" : player_pos[1] - 50,
                        "size_x" : 125,
                        "size_y" : 25
                    }

                    m2 = pygame.Surface((g2["type_x"], g2["type_y"]))
                    m2_pos = [g2["pos_x"], g2["pos_y"]]
                    m2_size = [g2["size_x"], g2["size_y"]]

                    if m2 is not None :
                        gandalf_murs_finaux_grand_s.append(m2)
                        gandalf_murs_finaux_grand_s_pos.append(m2_pos)
                        gandalf_murs_finaux_grand_s_size.append(m2_size)

                    m3 = None
                    m3_pos = [5, 5]
                    m3_size = [5, 5]

                    g3 = gandalf_murs_petit_2.copy()
                    g3 = {
                        "type_x" : 25,
                        "type_y" : 50,
                        "color" : "#4D3206",
                        "pos_x" : player_pos[0] + 50,
                        "pos_y" : player_pos[1],
                        "size_x" : 25,
                        "size_y" : 50
                    }

                    m3 = pygame.Surface((g3["type_x"], g3["type_y"]))
                    m3_pos = [g3["pos_x"], g3["pos_y"]]
                    m3_size = [g3["size_x"], g3["size_y"]]

                    if m3 is not None :
                        gandalf_murs_finaux_petit_2_s.append(m3)
                        gandalf_murs_finaux_petit_2_s_pos.append(m3_pos)
                        gandalf_murs_finaux_petit_2_s_size.append(m3_size)

            cooldown_i_meme_gandalf_player_2 = 1200

    return cooldown_i_meme_gandalf_player, cooldown_i_meme_gandalf_player_2, gandalf_murs_finaux_petit_1_q, gandalf_murs_finaux_petit_1_q_pos, gandalf_murs_finaux_petit_1_q_size, gandalf_murs_finaux_grand_q, gandalf_murs_finaux_grand_q_pos, gandalf_murs_finaux_grand_q_size, gandalf_murs_finaux_petit_2_q, gandalf_murs_finaux_petit_2_q_pos, gandalf_murs_finaux_petit_2_q_size, gandalf_murs_finaux_petit_1_d, gandalf_murs_finaux_petit_1_d_pos, gandalf_murs_finaux_petit_1_d_size, gandalf_murs_finaux_grand_d, gandalf_murs_finaux_grand_d_pos, gandalf_murs_finaux_grand_d_size, gandalf_murs_finaux_petit_2_d, gandalf_murs_finaux_petit_2_d_pos, gandalf_murs_finaux_petit_2_d_size, gandalf_murs_finaux_petit_1_z, gandalf_murs_finaux_petit_1_z_pos, gandalf_murs_finaux_petit_1_z_size, gandalf_murs_finaux_grand_z, gandalf_murs_finaux_grand_z_pos, gandalf_murs_finaux_grand_z_size, gandalf_murs_finaux_petit_2_z, gandalf_murs_finaux_petit_2_z_pos, gandalf_murs_finaux_petit_2_z_size, gandalf_murs_finaux_petit_1_s, gandalf_murs_finaux_petit_1_s_pos, gandalf_murs_finaux_petit_1_s_size, gandalf_murs_finaux_grand_s, gandalf_murs_finaux_grand_s_pos, gandalf_murs_finaux_grand_s_size, gandalf_murs_finaux_petit_2_s, gandalf_murs_finaux_petit_2_s_pos, gandalf_murs_finaux_petit_2_s_size, gandalf_murs_finaux_petit_1_left, gandalf_murs_finaux_petit_1_left_pos, gandalf_murs_finaux_petit_1_left_size, gandalf_murs_finaux_grand_left, gandalf_murs_finaux_grand_left_pos, gandalf_murs_finaux_grand_left_size, gandalf_murs_finaux_petit_2_left, gandalf_murs_finaux_petit_2_left_pos, gandalf_murs_finaux_petit_2_left_size, gandalf_murs_finaux_petit_1_right, gandalf_murs_finaux_petit_1_right_pos, gandalf_murs_finaux_petit_1_right_size, gandalf_murs_finaux_grand_right, gandalf_murs_finaux_grand_right_pos, gandalf_murs_finaux_grand_right_size, gandalf_murs_finaux_petit_2_right, gandalf_murs_finaux_petit_2_right_pos, gandalf_murs_finaux_petit_2_right_size, gandalf_murs_finaux_petit_1_up, gandalf_murs_finaux_petit_1_up_pos, gandalf_murs_finaux_petit_1_up_size, gandalf_murs_finaux_grand_up,gandalf_murs_finaux_grand_up_pos, gandalf_murs_finaux_grand_up_size, gandalf_murs_finaux_petit_2_up, gandalf_murs_finaux_petit_2_up_pos, gandalf_murs_finaux_petit_2_up_size, gandalf_murs_finaux_petit_1_down, gandalf_murs_finaux_petit_1_down_pos, gandalf_murs_finaux_petit_1_down_size, gandalf_murs_finaux_grand_down, gandalf_murs_finaux_grand_down_pos, gandalf_murs_finaux_grand_down_size, gandalf_murs_finaux_petit_2_down, gandalf_murs_finaux_petit_2_down_pos, gandalf_murs_finaux_petit_2_down_size

def collision_gandalf_murs() :
    if executing_lightcycle_movement_q :
        for i, j in zip(gandalf_murs_finaux_petit_1_q_pos, gandalf_murs_finaux_petit_1_q_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
        
        for i, j in zip(gandalf_murs_finaux_grand_q_pos, gandalf_murs_finaux_grand_q_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_q_pos, gandalf_murs_finaux_petit_2_q_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_d_pos, gandalf_murs_finaux_grand_d_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_z_pos, gandalf_murs_finaux_petit_1_z_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_z_pos, gandalf_murs_finaux_grand_z_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_z_pos, gandalf_murs_finaux_petit_2_z_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_s_pos, gandalf_murs_finaux_petit_1_s_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_s_pos, gandalf_murs_finaux_grand_s_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_s_pos, gandalf_murs_finaux_petit_2_s_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_left_pos, gandalf_murs_finaux_petit_1_left_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
        
        for i, j in zip(gandalf_murs_finaux_grand_left_pos, gandalf_murs_finaux_grand_left_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_left_pos, gandalf_murs_finaux_petit_2_left_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_right_pos, gandalf_murs_finaux_grand_right_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_up_pos, gandalf_murs_finaux_petit_1_up_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_up_pos, gandalf_murs_finaux_grand_up_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_up_pos, gandalf_murs_finaux_petit_2_up_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_down_pos, gandalf_murs_finaux_petit_1_down_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_down_pos, gandalf_murs_finaux_grand_down_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_down_pos, gandalf_murs_finaux_petit_2_down_size) :
            if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

    if executing_lightcycle_movement_d :
        for i, j in zip(gandalf_murs_finaux_grand_q_pos, gandalf_murs_finaux_grand_q_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_d_pos, gandalf_murs_finaux_petit_1_d_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_d_pos, gandalf_murs_finaux_grand_d_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_d_pos, gandalf_murs_finaux_petit_2_d_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_z_pos, gandalf_murs_finaux_petit_1_z_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_z_pos, gandalf_murs_finaux_grand_z_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_z_pos, gandalf_murs_finaux_petit_2_z_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_s_pos, gandalf_murs_finaux_petit_1_s_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_s_pos, gandalf_murs_finaux_grand_s_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_s_pos, gandalf_murs_finaux_petit_2_s_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_left_pos, gandalf_murs_finaux_grand_left_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_right_pos, gandalf_murs_finaux_petit_1_right_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_right_pos, gandalf_murs_finaux_grand_right_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_right_pos, gandalf_murs_finaux_petit_2_right_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_up_pos, gandalf_murs_finaux_petit_1_up_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_up_pos, gandalf_murs_finaux_grand_up_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_up_pos, gandalf_murs_finaux_petit_2_up_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_down_pos, gandalf_murs_finaux_petit_1_down_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_down_pos, gandalf_murs_finaux_grand_down_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_down_pos, gandalf_murs_finaux_petit_2_down_size) :
            if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

    if executing_lightcycle_movement_z :
        for i, j in zip(gandalf_murs_finaux_petit_1_q_pos, gandalf_murs_finaux_petit_1_q_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_q_pos, gandalf_murs_finaux_grand_q_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_q_pos, gandalf_murs_finaux_petit_2_q_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_d_pos, gandalf_murs_finaux_petit_1_d_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_d_pos, gandalf_murs_finaux_grand_d_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_d_pos, gandalf_murs_finaux_petit_2_d_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_z_pos, gandalf_murs_finaux_petit_1_z_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_z_pos, gandalf_murs_finaux_grand_z_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_z_pos, gandalf_murs_finaux_petit_2_z_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_s_pos, gandalf_murs_finaux_grand_s_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_left_pos, gandalf_murs_finaux_petit_1_left_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_left_pos, gandalf_murs_finaux_grand_left_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_left_pos, gandalf_murs_finaux_petit_2_left_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_right_pos, gandalf_murs_finaux_petit_1_right_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_right_pos, gandalf_murs_finaux_grand_right_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_right_pos, gandalf_murs_finaux_petit_2_right_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_up_pos, gandalf_murs_finaux_petit_1_up_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_up_pos, gandalf_murs_finaux_grand_up_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_up_pos, gandalf_murs_finaux_petit_2_up_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_down_pos, gandalf_murs_finaux_grand_down_size) :
            if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

    if executing_lightcycle_movement_s :
        for i, j in zip(gandalf_murs_finaux_petit_1_q_pos, gandalf_murs_finaux_petit_1_q_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_q_pos, gandalf_murs_finaux_grand_q_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_q_pos, gandalf_murs_finaux_petit_2_q_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_d_pos, gandalf_murs_finaux_petit_1_d_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_d_pos, gandalf_murs_finaux_grand_d_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_d_pos, gandalf_murs_finaux_petit_2_d_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_z_pos, gandalf_murs_finaux_grand_z_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_s_pos, gandalf_murs_finaux_petit_1_s_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_s_pos, gandalf_murs_finaux_grand_s_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_s_pos, gandalf_murs_finaux_petit_2_s_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_left_pos, gandalf_murs_finaux_petit_1_left_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_left_pos, gandalf_murs_finaux_grand_left_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_left_pos, gandalf_murs_finaux_petit_2_left_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_right_pos, gandalf_murs_finaux_petit_1_right_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_right_pos, gandalf_murs_finaux_grand_right_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_right_pos, gandalf_murs_finaux_petit_2_right_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_up_pos, gandalf_murs_finaux_grand_up_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_1_down_pos, gandalf_murs_finaux_petit_1_down_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_grand_down_pos, gandalf_murs_finaux_grand_down_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1

        for i, j in zip(gandalf_murs_finaux_petit_2_down_pos, gandalf_murs_finaux_petit_2_down_size) :
            if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player == False :
                    mode_actuel = MODE_WIN2_LOSE1
                if invulnérabilité_temporaire_player == False :
                    mode_actuel = MODE_WIN2_LOSE1


    if executing_lightcycle_movement_left :
        for i, j in zip(gandalf_murs_finaux_petit_1_q_pos, gandalf_murs_finaux_petit_1_q_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
        
        for i, j in zip(gandalf_murs_finaux_grand_q_pos, gandalf_murs_finaux_grand_q_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_q_pos, gandalf_murs_finaux_petit_2_q_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_d_pos, gandalf_murs_finaux_grand_d_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_z_pos, gandalf_murs_finaux_petit_1_z_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_z_pos, gandalf_murs_finaux_grand_z_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_z_pos, gandalf_murs_finaux_petit_2_z_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_s_pos, gandalf_murs_finaux_petit_1_s_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_s_pos, gandalf_murs_finaux_grand_s_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_s_pos, gandalf_murs_finaux_petit_2_s_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_left_pos, gandalf_murs_finaux_petit_1_left_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
        
        for i, j in zip(gandalf_murs_finaux_grand_left_pos, gandalf_murs_finaux_grand_left_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_left_pos, gandalf_murs_finaux_petit_2_left_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_right_pos, gandalf_murs_finaux_grand_right_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_up_pos, gandalf_murs_finaux_petit_1_up_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_up_pos, gandalf_murs_finaux_grand_up_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_up_pos, gandalf_murs_finaux_petit_2_up_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_down_pos, gandalf_murs_finaux_petit_1_down_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_down_pos, gandalf_murs_finaux_grand_down_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_down_pos, gandalf_murs_finaux_petit_2_down_size) :
            if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

    if executing_lightcycle_movement_right :
        for i, j in zip(gandalf_murs_finaux_grand_q_pos, gandalf_murs_finaux_grand_q_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_d_pos, gandalf_murs_finaux_petit_1_d_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_d_pos, gandalf_murs_finaux_grand_d_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_d_pos, gandalf_murs_finaux_petit_2_d_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_z_pos, gandalf_murs_finaux_petit_1_z_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_z_pos, gandalf_murs_finaux_grand_z_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_z_pos, gandalf_murs_finaux_petit_2_z_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_s_pos, gandalf_murs_finaux_petit_1_s_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_s_pos, gandalf_murs_finaux_grand_s_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_s_pos, gandalf_murs_finaux_petit_2_s_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_left_pos, gandalf_murs_finaux_grand_left_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_right_pos, gandalf_murs_finaux_petit_1_right_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_right_pos, gandalf_murs_finaux_grand_right_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_right_pos, gandalf_murs_finaux_petit_2_right_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_up_pos, gandalf_murs_finaux_petit_1_up_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_up_pos, gandalf_murs_finaux_grand_up_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_up_pos, gandalf_murs_finaux_petit_2_up_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_down_pos, gandalf_murs_finaux_petit_1_down_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_down_pos, gandalf_murs_finaux_grand_down_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_down_pos, gandalf_murs_finaux_petit_2_down_size) :
            if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

    if executing_lightcycle_movement_up :
        for i, j in zip(gandalf_murs_finaux_petit_1_q_pos, gandalf_murs_finaux_petit_1_q_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_q_pos, gandalf_murs_finaux_grand_q_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_q_pos, gandalf_murs_finaux_petit_2_q_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_d_pos, gandalf_murs_finaux_petit_1_d_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_d_pos, gandalf_murs_finaux_grand_d_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_d_pos, gandalf_murs_finaux_petit_2_d_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_z_pos, gandalf_murs_finaux_petit_1_z_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_z_pos, gandalf_murs_finaux_grand_z_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_z_pos, gandalf_murs_finaux_petit_2_z_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_s_pos, gandalf_murs_finaux_grand_s_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_left_pos, gandalf_murs_finaux_petit_1_left_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_left_pos, gandalf_murs_finaux_grand_left_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_left_pos, gandalf_murs_finaux_petit_2_left_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_right_pos, gandalf_murs_finaux_petit_1_right_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_right_pos, gandalf_murs_finaux_grand_right_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_right_pos, gandalf_murs_finaux_petit_2_right_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_up_pos, gandalf_murs_finaux_petit_1_up_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_up_pos, gandalf_murs_finaux_grand_up_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_up_pos, gandalf_murs_finaux_petit_2_up_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_down_pos, gandalf_murs_finaux_grand_down_size) :
            if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

    if executing_lightcycle_movement_down :
        for i, j in zip(gandalf_murs_finaux_petit_1_q_pos, gandalf_murs_finaux_petit_1_q_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_q_pos, gandalf_murs_finaux_grand_q_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_q_pos, gandalf_murs_finaux_petit_2_q_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_d_pos, gandalf_murs_finaux_petit_1_d_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_d_pos, gandalf_murs_finaux_grand_d_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_d_pos, gandalf_murs_finaux_petit_2_d_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_z_pos, gandalf_murs_finaux_grand_z_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_s_pos, gandalf_murs_finaux_petit_1_s_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_s_pos, gandalf_murs_finaux_grand_s_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_s_pos, gandalf_murs_finaux_petit_2_s_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_left_pos, gandalf_murs_finaux_petit_1_left_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_left_pos, gandalf_murs_finaux_grand_left_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_left_pos, gandalf_murs_finaux_petit_2_left_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_right_pos, gandalf_murs_finaux_petit_1_right_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_right_pos, gandalf_murs_finaux_grand_right_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_right_pos, gandalf_murs_finaux_petit_2_right_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_up_pos, gandalf_murs_finaux_grand_up_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_1_down_pos, gandalf_murs_finaux_petit_1_down_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_grand_down_pos, gandalf_murs_finaux_grand_down_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2

        for i, j in zip(gandalf_murs_finaux_petit_2_down_pos, gandalf_murs_finaux_petit_2_down_size) :
            if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                if executing_i_meme_disparition_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2
                if invulnérabilité_temporaire_player_2 == False :
                    mode_actuel = MODE_WIN1_LOSE2






def lightcycle_movement_negative(player_pos, grid_pos, mode_actuel, MODE_FIN_DE_PARTIE, executing_i_meme, invulnérabilité_temporaire_player) :
    if player_pos <= grid_pos :
        if invulnérabilité_temporaire_player == False :
            mode_actuel = MODE_FIN_DE_PARTIE
        else :
            player_pos = grid_pos
    else :
        if executing_i_meme == False :
            player_pos -= 5
        else :
            player_pos -= 10

    return player_pos, mode_actuel

def lightcycle_movement_positive(player_pos, screen_size, grid_size, player_size, mode_actuel, MODE_FIN_DE_PARTIE, executing_i_meme, invulnérabilité_temporaire_player) :
    if player_pos >= (screen_size - grid_size) + (grid_size - player_size - 10) :
        if invulnérabilité_temporaire_player == False :
            mode_actuel = MODE_FIN_DE_PARTIE
        else :
            player_pos = (screen_size - grid_size) + (grid_size - player_size - 10)
    else :
        if executing_i_meme == False :
            player_pos += 5
        else :
            player_pos += 10

    return player_pos, mode_actuel


def création_traînée_GAUCHE(executing, traînées, player_pos_instant_0, player_pos_0, player_pos_1, traînées_finales, traînées_finales_pos, traînées_finales_size) :
    t = None
    t_pos = [5, 5]
    t_size = [5, 5]
    
    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": player_pos_instant_0 - player_pos_0 + 5,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos_0 + 10,
            "pos_y": player_pos_1 + 10,
            "size_x": player_pos_instant_0 - player_pos_0 + 5,
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if t is not None :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)
        traînées_finales_size.append(t_size)

    return traînées_finales, traînées_finales_pos, traînées_finales_size

def création_traînée_DROITE(executing, traînées, player_pos_instant_0, player_pos_instant_1, player_pos_0, traînées_finales, traînées_finales_pos, traînées_finales_size) :
    t = None
    t_pos = [5, 5]
    t_size = [5, 5]

    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": player_pos_0 + 5 - player_pos_instant_0 + 5,
            "type_y": 5,
            "color": "#F5FF00",
            "pos_x": player_pos_instant_0 + 10,
            "pos_y": player_pos_instant_1 + 10,
            "size_x": player_pos_0 + 5 - player_pos_instant_0 + 5,
            "size_y": 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if t is not None :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)
        traînées_finales_size.append(t_size)

    return traînées_finales, traînées_finales_pos, traînées_finales_size

def création_traînées_HAUT(executing, traînées, player_pos_instant_1, player_pos_1, player_pos_0, traînées_finales, traînées_finales_pos, traînées_finales_size) :
    t = None
    t_pos = [5, 5]
    t_size = [5, 5]

    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": 5,
            "type_y": player_pos_instant_1 - player_pos_1 + 5,
            "color": "#F5FF00",
            "pos_x": player_pos_0 + 10,
            "pos_y": player_pos_1 + 10,
            "size_x": 5,
            "size_y": player_pos_instant_1 - player_pos_1 + 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if t is not None :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)
        traînées_finales_size.append(t_size)

    return traînées_finales, traînées_finales_pos, traînées_finales_size

def création_traînées_BAS(executing, traînées, player_pos_1, player_pos_instant_1, player_pos_instant_0, traînées_finales, traînées_finales_pos, traînées_finales_size) :
    t = None
    t_pos = [5, 5]
    t_size = [5, 5]

    if executing :
        traînée = traînées.copy()
        traînée = {
            "type_x": 5,
            "type_y": player_pos_1 - player_pos_instant_1 + 5,
            "color": "#F5FF00",
            "pos_x": player_pos_instant_0 + 10,
            "pos_y": player_pos_instant_1 + 10,
            "size_x": 5,
            "size_y": player_pos_1 - player_pos_instant_1 + 5
        }

        t = pygame.Surface((traînée["type_x"], traînée["type_y"]))
        t_pos = [traînée["pos_x"], traînée["pos_y"]]
        t_size = [traînée["size_x"], traînée["size_y"]]

    if t is not None :
        traînées_finales.append(t)
        traînées_finales_pos.append(t_pos)
        traînées_finales_size.append(t_size)

    return traînées_finales, traînées_finales_pos, traînées_finales_size

def reset_traînées(traînées_finales_q, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_d, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_z, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_s, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_left, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_right, traînées_finales_pos_right, traînées_finales_size_right, traînées_finales_up, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_down, traînées_finales_pos_down, traînées_finales_size_down) :
    traînées_finales_q = []
    traînées_finales_pos_q = []
    traînées_finales_size_q = []

    traînées_finales_d = []
    traînées_finales_pos_d = []
    traînées_finales_size_d = []

    traînées_finales_z = []
    traînées_finales_pos_z = []
    traînées_finales_size_z = []

    traînées_finales_s = []
    traînées_finales_pos_s = []
    traînées_finales_size_s = []


    traînées_finales_left = []
    traînées_finales_pos_left = []
    traînées_finales_size_left = []

    traînées_finales_right = []
    traînées_finales_pos_right = []
    traînées_finales_size_right = []

    traînées_finales_up = []
    traînées_finales_pos_up = []
    traînées_finales_size_up = []

    traînées_finales_down = []
    traînées_finales_pos_down = []
    traînées_finales_size_down = []

    return traînées_finales_q, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_d, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_z, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_s, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_left, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_right, traînées_finales_pos_right, traînées_finales_size_right, traînées_finales_up, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_down, traînées_finales_pos_down, traînées_finales_size_down


heures = 0
minutes = 0
secondes = 0

temps_total = 0

score_player = 0
score_player_2 = 0

score_attribué_player = False
score_attribué_player_2 = False

frôlements_de_la_mort_qui_tue_player = 0
frôlements_player = 0

frôlements_de_la_mort_qui_tue_player_2 = 0
frôlements_player_2 = 0

def frôlement_GAUCHE(executing, traînées_finales_pos, traînées_finales_size, traînées_finales_pos_2, traînées_finales_size_2, traînées_finales_pos_3, traînées_finales_size_3, traînées_finales_pos_4, traînées_finales_size_4, player_pos, score_attribué, score, frôlements, frôlements_de_la_mort_qui_tue) :
    if executing :
        for i, j in zip(traînées_finales_pos, traînées_finales_size) :
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 5 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 10 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_2, traînées_finales_size_2) :
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 5 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 10 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_3, traînées_finales_size_3) :
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 5 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 10 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_4, traînées_finales_size_4) :
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 5 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] <= i[0] + j[0] + 10 and player_pos[0] >= i[0] + j[0] + 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True

    return score, frôlements, frôlements_de_la_mort_qui_tue

def frôlement_DROITE(executing, traînées_finales_pos, traînées_finales_size, traînées_finales_pos_2, traînées_finales_size_2, traînées_finales_pos_3, traînées_finales_size_3, traînées_finales_pos_4, traînées_finales_size_4, player_pos, score_attribué, score, frôlements, frôlements_de_la_mort_qui_tue) :
    if executing :
        for i, j in zip(traînées_finales_pos, traînées_finales_size) :
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 5 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 10 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_2, traînées_finales_size_2) :
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 5 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 10 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_3, traînées_finales_size_3) :
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 5 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 10 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_4, traînées_finales_size_4) :
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 5 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[0] + 25 >= i[0] - 10 and player_pos[0] + 25 <= i[0] - 1 and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    score += 10
                    frôlements += 1
                    score_attribué = True

    return score, frôlements, frôlements_de_la_mort_qui_tue

def frôlement_HAUT(executing, traînées_finales_pos, traînées_finales_size, traînées_finales_pos_2, traînées_finales_size_2, traînées_finales_pos_3, traînées_finales_size_3, traînées_finales_pos_4, traînées_finales_size_4, player_pos, score_attribué, score, frôlements, frôlements_de_la_mort_qui_tue) :
    if executing :
        for i, j in zip(traînées_finales_pos, traînées_finales_size) :
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 5 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 10 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_2, traînées_finales_size_2) :
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 5 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 10 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_3, traînées_finales_size_3) :
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 5 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 10 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_4, traînées_finales_size_4) :
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 5 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] <= i[1] + j[1] + 10 and player_pos[1] >= i[1] + j[1] + 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True

    return score, frôlements, frôlements_de_la_mort_qui_tue

def frôlement_BAS(executing, traînées_finales_pos, traînées_finales_size, traînées_finales_pos_2, traînées_finales_size_2, traînées_finales_pos_3, traînées_finales_size_3, traînées_finales_pos_4, traînées_finales_size_4, player_pos, score_attribué, score, frôlements, frôlements_de_la_mort_qui_tue) :
    if executing :
        for i, j in zip(traînées_finales_pos, traînées_finales_size) :
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 5 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 10 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_2, traînées_finales_size_2) :
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 5 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 10 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_3, traînées_finales_size_3) :
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 5 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 10 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True
        for i, j in zip(traînées_finales_pos_4, traînées_finales_size_4) :
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 5 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 100
                    frôlements_de_la_mort_qui_tue += 1
                    score_attribué = True
            if score_attribué == False :
                if player_pos[1] + 25 >= i[1] - 10 and player_pos[1] + 25 <= i[1] - 1 and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    score += 10
                    frôlements += 1
                    score_attribué = True

    return score, frôlements, frôlements_de_la_mort_qui_tue


collectibles = pygame.Surface((15,15))
collectibles.fill("#346910")
collectibles_pos = [random.randint(grid_pos[0], grid_pos[0] + grid_size[0] - 15), random.randint(grid_pos[1], grid_pos[1] + grid_size[1] - 15)]
collectibles_size = [15, 15]

collectibles_player = 0
collectibles_player_2 = 0

def réapparition_collectibles(executing_GAUCHE, executing_DROITE, executing_HAUT, executing_BAS, grid_pos, grid_size, player_pos, player_size, collectibles_pos, collectibles_size, collectibles, score) :
    if executing_GAUCHE :
        if player_pos[0] <= collectibles_pos[0] + collectibles_size[0] and player_pos[0] >= collectibles_pos[0] and player_pos[1] + 24 >= collectibles_pos[1] and player_pos[1] - 1 <= collectibles_pos[1] + collectibles_size[1] :
            score += 50
            collectibles += 1
            collectibles_pos = [random.randint(grid_pos[0], grid_pos[0] + grid_size[0] - 15), random.randint(grid_pos[1], grid_pos[1] + grid_size[1] - 15)]
    if executing_DROITE :
        if player_pos[0] + player_size[0] >= collectibles_pos[0] and player_pos[0] + player_size[0] <= collectibles_pos[0] + collectibles_size[0] and player_pos[1] + 24 >= collectibles_pos[1] and player_pos[1] - 1 <= collectibles_pos[1] + collectibles_size[1] :
            score += 50
            collectibles += 1
            collectibles_pos = [random.randint(grid_pos[0], grid_pos[0] + grid_size[0] - 15), random.randint(grid_pos[1], grid_pos[1] + grid_size[1] - 15)]
    if executing_HAUT :
        if player_pos[1] <= collectibles_pos[1] + collectibles_size[1] and player_pos[1] >= collectibles_pos[1] and player_pos[0] + 24 >= collectibles_pos[0] and player_pos[0] - 1 <= collectibles_pos[0] + collectibles_size[0] :
            score += 50
            collectibles += 1
            collectibles_pos = [random.randint(grid_pos[0], grid_pos[0] + grid_size[0] - 15), random.randint(grid_pos[1], grid_pos[1] + grid_size[1] - 15)]
    if executing_BAS :
        if player_pos[1] + player_size[1] >= collectibles_pos[1] and player_pos[1] + player_size[1] <= collectibles_pos[1] + collectibles_size[1] and player_pos[0] + 24 >= collectibles_pos[0] and player_pos[0] - 1 <= collectibles_pos[0] + collectibles_size[0] :
            score += 50
            collectibles += 1
            collectibles_pos = [random.randint(grid_pos[0], grid_pos[0] + grid_size[0] - 15), random.randint(grid_pos[1], grid_pos[1] + grid_size[1] - 15)]

    return score, collectibles, collectibles_pos



succès_temps_1_player = False
succès_temps_2_player = False
succès_temps_caché_player = False

succès_score_1_player = False
succès_score_2_player = False
succès_score_caché_player = False

succès_frôlements_1_player = False
succès_frôlements_2_player = False
succès_frôlements_caché_player = False

succès_collectibles_1_player = False
succès_collectibles_2_player = False
succès_collectibles_caché_player = False


succès_temps_1_player_2 = False
succès_temps_2_player_2 = False
succès_temps_caché_player_2 = False

succès_score_1_player_2 = False
succès_score_2_player_2 = False
succès_score_caché_player_2 = False

succès_frôlements_1_player_2 = False
succès_frôlements_2_player_2 = False
succès_frôlements_caché_player_2 = False

succès_collectibles_1_player_2 = False
succès_collectibles_2_player_2 = False
succès_collectibles_caché_player_2 = False

def succès_temps(temps_total, succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_caché_player, succès_temps_caché_player_2) :
    if temps_total >= 30 :
        succès_temps_1_player = True
        succès_temps_1_player_2 = True

    if temps_total >= 60 :
        succès_temps_2_player = True
        succès_temps_2_player_2 = True

    if temps_total >= 150 :
        succès_temps_caché_player = True
        succès_temps_caché_player_2 = True

    return succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_caché_player, succès_temps_caché_player_2

def succès_score(score_player, succès_score_1, succès_score_2, succès_score_caché) :
    if score_player >= 100 :
        succès_score_1 = True
    
    if score_player >= 500 :
        succès_score_2 = True

    if score_player >= 1000 :
        succès_score_caché = True

    return succès_score_1, succès_score_2, succès_score_caché

def succès_frôlements(frôlements_player, succès_frôlements_1, succès_frôlements_2, succès_frôlements_caché) :
    if frôlements_player >= 5 :
        succès_frôlements_1 = True

    if frôlements_player >= 10 :
        succès_frôlements_2 = True

    if frôlements_player >= 25 :
        succès_frôlements_caché = True

    return succès_frôlements_1, succès_frôlements_2, succès_frôlements_caché

def succès_collectibles(collectibles_player, succès_collectibles_1, succès_collectibles_2, succès_collectibles_caché) :
    if collectibles_player >= 1 :
        succès_collectibles_1 = True

    if collectibles_player >= 5 :
        succès_collectibles_2 = True

    if collectibles_player >= 10 :
        succès_collectibles_caché = True

    return succès_collectibles_1, succès_collectibles_2, succès_collectibles_caché



time.sleep(0.1)



while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
                running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                running = False



    if mode_actuel == MODE_ACCUEIL :
        screen.fill("#2746F5")

        font_titre_jeu = pygame.font.Font(Technos, 200)
        titre_jeu_img = font_titre_jeu.render("TRON", True, (255, 255, 255))
        titre_jeu_dimensions = titre_jeu_img.get_size()
        titre_jeu_pos = [screen_size[0] / 2 - titre_jeu_dimensions[0] / 2, 50]
        screen.blit(titre_jeu_img, titre_jeu_pos)

        bt_MODE_GAME = pygame.Surface((600, 100))
        bt_MODE_GAME.fill("#999999")
        bt_MODE_GAME_size = [600, 100]
        bt_MODE_GAME_pos = [screen_size[0] / 2 - bt_MODE_GAME_size[0] / 2, titre_jeu_pos[1] + titre_jeu_dimensions[1] + 10]
        screen.blit(bt_MODE_GAME, bt_MODE_GAME_pos)

        font_titre_bt_MODE_GAME = pygame.font.Font(Technos, 35)
        titre_bt_MODE_GAME_img = font_titre_bt_MODE_GAME.render("Lancer une partie", True, (0, 0, 0))
        titre_bt_MODE_GAME_dimensions = titre_bt_MODE_GAME_img.get_size()
        titre_bt_MODE_GAME_pos = [screen_size[0] / 2 - titre_bt_MODE_GAME_dimensions[0] / 2, bt_MODE_GAME_pos[1] + bt_MODE_GAME_size[1] / 2 - titre_bt_MODE_GAME_dimensions[1] / 2]
        screen.blit(titre_bt_MODE_GAME_img, titre_bt_MODE_GAME_pos)

        bt_MODE_SUCCES = pygame.Surface((600, 100))
        bt_MODE_SUCCES.fill("#999999")
        bt_MODE_SUCCES_size = [600, 100]
        bt_MODE_SUCCES_pos = [screen_size[0] / 2 - bt_MODE_SUCCES_size[0] / 2, bt_MODE_GAME_pos[1] + bt_MODE_GAME_size[1] + 10]
        screen.blit(bt_MODE_SUCCES, bt_MODE_SUCCES_pos)

        font_titre_bt_MODE_SUCCES = pygame.font.Font(Technos, 35)
        titre_bt_MODE_SUCCES_img = font_titre_bt_MODE_SUCCES.render("Liste des succes", True, (0, 0, 0))
        titre_bt_MODE_SUCCES_dimensions = titre_bt_MODE_SUCCES_img.get_size()
        titre_bt_MODE_SUCCES_pos = [screen_size[0] / 2 - titre_bt_MODE_SUCCES_dimensions[0] / 2, bt_MODE_SUCCES_pos[1] + bt_MODE_SUCCES_size[1] / 2 - titre_bt_MODE_SUCCES_dimensions[1] / 2]
        screen.blit(titre_bt_MODE_SUCCES_img, titre_bt_MODE_SUCCES_pos)

        bt_MODE_I_MEMES = pygame.Surface((600, 100))
        bt_MODE_I_MEMES.fill("#999999")
        bt_MODE_I_MEMES_size = [600, 100]
        bt_MODE_I_MEMES_pos = [screen_size[0] / 2 - bt_MODE_I_MEMES_size[0] / 2, bt_MODE_SUCCES_pos[1] + bt_MODE_SUCCES_size[1] + 10]
        screen.blit(bt_MODE_I_MEMES, bt_MODE_I_MEMES_pos)

        font_titre_bt_MODE_I_MEMES = pygame.font.Font(Technos, 35)
        titre_bt_MODE_I_MEMES_img = font_titre_bt_MODE_I_MEMES.render("Menu des I-Memes", True, (0, 0, 0))
        titre_bt_MODE_I_MEMES_dimensions = titre_bt_MODE_I_MEMES_img.get_size()
        titre_bt_MODE_I_MEMES_pos = [screen_size[0] / 2 - titre_bt_MODE_I_MEMES_dimensions[0] / 2, bt_MODE_I_MEMES_pos[1] + bt_MODE_I_MEMES_size[1] / 2 - titre_bt_MODE_I_MEMES_dimensions[1] / 2]
        screen.blit(titre_bt_MODE_I_MEMES_img, titre_bt_MODE_I_MEMES_pos)

        bouton_quitter = pygame.Surface((600, 100))
        bouton_quitter.fill("#999999")
        bouton_quitter_size = [600, 100]
        bouton_quitter_pos = [screen_size[0] / 2 - bouton_quitter_size[0] / 2, bt_MODE_I_MEMES_pos[1] + bt_MODE_I_MEMES_size[1] + 10]
        screen.blit(bouton_quitter, bouton_quitter_pos)

        font_titre_bouton_quitter = pygame.font.Font(Technos, 35)
        titre_bouton_quitter_img = font_titre_bouton_quitter.render("Quitter le jeu", True, (0, 0, 0))
        titre_bouton_quitter_dimensions = titre_bouton_quitter_img.get_size()
        titre_bouton_quitter_pos = [screen_size[0] / 2 - titre_bouton_quitter_dimensions[0] / 2, bouton_quitter_pos[1] + bouton_quitter_size[1] / 2 - titre_bouton_quitter_dimensions[1] / 2]
        screen.blit(titre_bouton_quitter_img, titre_bouton_quitter_pos)

        mouse = pygame.mouse.get_pos()

        clique_gauche = pygame.mouse.get_pressed()[0]

        if clique_gauche :
            if mouse[0] >= bt_MODE_GAME_pos[0] and mouse[0] <= bt_MODE_GAME_pos[0] + bt_MODE_GAME_size[0] and mouse[1] >= bt_MODE_GAME_pos[1] and mouse[1] <= bt_MODE_GAME_pos[1] + bt_MODE_GAME_size[1] :
                mode_actuel = MODE_GAME
            if mouse[0] >= bt_MODE_SUCCES_pos[0] and mouse[0] <= bt_MODE_SUCCES_pos[0] + bt_MODE_SUCCES_size[0] and mouse[1] >= bt_MODE_SUCCES_pos[1] and mouse[1] <= bt_MODE_SUCCES_pos[1] + bt_MODE_SUCCES_size[1] :
                mode_actuel = MODE_SUCCES
            if mouse[0] >= bt_MODE_I_MEMES_pos[0] and mouse[0] <= bt_MODE_I_MEMES_pos[0] + bt_MODE_I_MEMES_size[0] and mouse[1] >= bt_MODE_I_MEMES_pos[1] and mouse[1] <= bt_MODE_I_MEMES_pos[1] + bt_MODE_I_MEMES_size[1] :
                mode_actuel = MODE_I_MEMES
            if mouse[0] >= bouton_quitter_pos[0] and mouse[0] <= bouton_quitter_pos[0] + bouton_quitter_size[0] and mouse[1] >= bouton_quitter_pos[1] and mouse[1] <= bouton_quitter_pos[1] + bouton_quitter_size[1] :
                running = False

        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #--------------------------------------------------------------------------RESET----------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        
        player_pos = [grid_pos[0], grid_size[1] / 2 + 100]
        player_pos_instant = [player_pos[0], player_pos[1]]

        player_pos_2 = [grid_pos[0] + grid_size[0] - 25, grid_size[1] / 2 + 100]
        player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]

        traînées_finales_q, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_d, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_z, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_s, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_left, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_right, traînées_finales_pos_right, traînées_finales_size_right, traînées_finales_up, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_down, traînées_finales_pos_down, traînées_finales_size_down = reset_traînées(traînées_finales_q, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_d, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_z, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_s, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_left, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_right, traînées_finales_pos_right, traînées_finales_size_right, traînées_finales_up, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_down, traînées_finales_pos_down, traînées_finales_size_down)

        heures = 0
        minutes = 0
        secondes = 0
        temps_total = 0

        score_player = 0
        score_player_2 = 0

        score_attribué_player = False
        score_attribué_player_2 = False
        
        frôlements_player = 0
        frôlements_de_la_mort_qui_tue_player = 0
        frôlements_player_2 = 0
        frôlements_de_la_mort_qui_tue_player_2 = 0

        collectibles_pos = [random.randint(grid_pos[0], grid_pos[0] + grid_size[0] - 15), random.randint(grid_pos[1], grid_pos[1] + grid_size[1] - 15)]

        collectibles_player = 0
        collectibles_player_2 = 0

        executing_lightcycle_movement_q = False
        executing_lightcycle_movement_d = True
        executing_lightcycle_movement_z = False
        executing_lightcycle_movement_s = False

        executing_lightcycle_movement_left = True
        executing_lightcycle_movement_right = False
        executing_lightcycle_movement_up = False
        executing_lightcycle_movement_down = False

        utilisé_i_meme_jackpot_player = False
        utilisé_i_meme_jackpot_player_2 = False

        utilisé_i_meme_devil_never_cry_player = False
        utilisé_i_meme_devil_never_cry_player_2 = False



    if mode_actuel == MODE_GAME :
        screen.fill(violet)
        screen.blit(grid, grid_pos)


        pressed_keys = pygame.key.get_pressed()

        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------Joueur 1------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        #-------------------------------------------------------------------------------Q---------------------------------------------------------------------------
        
        if pressed_keys[K_q] and not pressed_keys[K_d] and not pressed_keys[K_z] and not pressed_keys[K_s] :
            if executing_lightcycle_movement_q == False or executing_lightcycle_movement_d == False :            
                score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_HAUT(executing_lightcycle_movement_z, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
                score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_BAS(executing_lightcycle_movement_s, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
                
                executing_lightcycle_movement_z = False
                executing_lightcycle_movement_s = False

                executing_lightcycle_movement_q = True

                player_pos_instant = [player_pos[0], player_pos[1]]
            else :
                mode_actuel = MODE_WIN2_LOSE1
        if executing_lightcycle_movement_q :
            player_pos[0], mode_actuel = lightcycle_movement_negative(player_pos[0], grid_pos[0], mode_actuel, MODE_WIN2_LOSE1, executing_i_meme_red_bull_player, invulnérabilité_temporaire_player)
            
        #-------------------------------------------------------------------------------D---------------------------------------------------------------------------
        
        if pressed_keys[K_d] and not pressed_keys[K_q] and not pressed_keys[K_z] and not pressed_keys[K_s] :
            if executing_lightcycle_movement_q == False or executing_lightcycle_movement_d == False :
                score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_HAUT(executing_lightcycle_movement_z, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
                score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_BAS(executing_lightcycle_movement_s, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
                
                executing_lightcycle_movement_z = False
                executing_lightcycle_movement_s = False

                executing_lightcycle_movement_d = True

                player_pos_instant = [player_pos[0], player_pos[1]]
            else :
                mode_actuel = MODE_WIN2_LOSE1
        if executing_lightcycle_movement_d :
            player_pos[0], mode_actuel = lightcycle_movement_positive(player_pos[0], screen_size[0], grid_size[0], player_size[0], mode_actuel, MODE_WIN2_LOSE1, executing_i_meme_red_bull_player, invulnérabilité_temporaire_player)

        #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

        if pressed_keys[K_z] and not pressed_keys[K_q] and not pressed_keys[K_d] and not pressed_keys[K_s] :
            if executing_lightcycle_movement_z == False or executing_lightcycle_movement_s == False :
                score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_GAUCHE(executing_lightcycle_movement_q, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
                score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_DROITE(executing_lightcycle_movement_d, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
                
                executing_lightcycle_movement_q = False
                executing_lightcycle_movement_d = False

                executing_lightcycle_movement_z = True

                player_pos_instant = [player_pos[0], player_pos[1]]
            else :
                mode_actuel = MODE_WIN2_LOSE1
        if executing_lightcycle_movement_z :
            player_pos[1], mode_actuel = lightcycle_movement_negative(player_pos[1], grid_pos[1], mode_actuel, MODE_WIN2_LOSE1, executing_i_meme_red_bull_player, invulnérabilité_temporaire_player)

        #-------------------------------------------------------------------------------S---------------------------------------------------------------------------
        
        if pressed_keys[K_s] and not pressed_keys[K_q] and not pressed_keys[K_d] and not pressed_keys[K_z] :
            if executing_lightcycle_movement_z == False or executing_lightcycle_movement_s == False :
                score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_GAUCHE(executing_lightcycle_movement_q, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)
                score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player = frôlement_DROITE(executing_lightcycle_movement_d, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos, score_attribué_player, score_player, frôlements_player, frôlements_de_la_mort_qui_tue_player)

                executing_lightcycle_movement_q = False
                executing_lightcycle_movement_d = False

                executing_lightcycle_movement_s = True

                player_pos_instant = [player_pos[0], player_pos[1]]
            else :
                mode_actuel = MODE_WIN2_LOSE1
        if executing_lightcycle_movement_s :
            player_pos[1], mode_actuel = lightcycle_movement_positive(player_pos[1], screen_size[1], grid_size[1], player_size[1], mode_actuel, MODE_WIN2_LOSE1, executing_i_meme_red_bull_player, invulnérabilité_temporaire_player)


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------
        
        if pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT] and not pressed_keys[K_UP] and not pressed_keys[K_DOWN] :
            if executing_lightcycle_movement_left == False or executing_lightcycle_movement_right == False :
                score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_HAUT(executing_lightcycle_movement_up, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)
                score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_BAS(executing_lightcycle_movement_down, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)

                executing_lightcycle_movement_up = False
                executing_lightcycle_movement_down = False

                executing_lightcycle_movement_left = True

                player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]
            else :
                mode_actuel = MODE_WIN1_LOSE2
        if executing_lightcycle_movement_left :
            player_pos_2[0], mode_actuel = lightcycle_movement_negative(player_pos_2[0], grid_pos[0], mode_actuel, MODE_WIN1_LOSE2, executing_i_meme_red_bull_player_2, invulnérabilité_temporaire_player_2)

        #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------
        
        if pressed_keys[K_RIGHT] and not pressed_keys[K_LEFT] and not pressed_keys[K_UP] and not pressed_keys[K_DOWN] :
            if executing_lightcycle_movement_left == False or executing_lightcycle_movement_right == False :
                score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_HAUT(executing_lightcycle_movement_up, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)
                score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_BAS(executing_lightcycle_movement_down, traînées_finales_pos_q, traînées_finales_size_q, traînées_finales_pos_d, traînées_finales_size_d, traînées_finales_pos_left, traînées_finales_size_left, traînées_finales_pos_right, traînées_finales_size_right, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)

                executing_lightcycle_movement_up = False
                executing_lightcycle_movement_down = False

                executing_lightcycle_movement_right = True

                player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]
            else :
                mode_actuel = MODE_WIN1_LOSE2
        if executing_lightcycle_movement_right :
            player_pos_2[0], mode_actuel = lightcycle_movement_positive(player_pos_2[0], screen_size[0], grid_size[0], player_size_2[0], mode_actuel, MODE_WIN1_LOSE2, executing_i_meme_red_bull_player_2, invulnérabilité_temporaire_player_2)

        #------------------------------------------------------------------------------UP---------------------------------------------------------------------------
        
        if pressed_keys[K_UP] and not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT] and not pressed_keys[K_DOWN] :
            if executing_lightcycle_movement_up == False or executing_lightcycle_movement_down == False :
                score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_GAUCHE(executing_lightcycle_movement_left, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)
                score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_DROITE(executing_lightcycle_movement_right, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)

                executing_lightcycle_movement_left = False
                executing_lightcycle_movement_right = False

                executing_lightcycle_movement_up = True

                player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]
            else :
                mode_actuel = MODE_WIN1_LOSE2
        if executing_lightcycle_movement_up :
            player_pos_2[1], mode_actuel = lightcycle_movement_negative(player_pos_2[1], grid_pos[1], mode_actuel, MODE_WIN1_LOSE2, executing_i_meme_red_bull_player_2, invulnérabilité_temporaire_player_2)

        #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
        
        if pressed_keys[K_DOWN] and not pressed_keys[K_LEFT] and not pressed_keys[K_RIGHT] and not pressed_keys[K_UP] :
            if executing_lightcycle_movement_up == False or executing_lightcycle_movement_down == False :
                score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_GAUCHE(executing_lightcycle_movement_left, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)
                score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2 = frôlement_DROITE(executing_lightcycle_movement_right, traînées_finales_pos_z, traînées_finales_size_z, traînées_finales_pos_s, traînées_finales_size_s, traînées_finales_pos_up, traînées_finales_size_up, traînées_finales_pos_down, traînées_finales_size_down, player_pos_2, score_attribué_player_2, score_player_2, frôlements_player_2, frôlements_de_la_mort_qui_tue_player_2)

                executing_lightcycle_movement_left = False
                executing_lightcycle_movement_right = False

                executing_lightcycle_movement_down = True

                player_pos_2_instant = [player_pos_2[0], player_pos_2[1]]
            else :
                mode_actuel = MODE_WIN1_LOSE2
        if executing_lightcycle_movement_down :
            player_pos_2[1], mode_actuel = lightcycle_movement_positive(player_pos_2[1], screen_size[1], grid_size[1], player_size_2[1], mode_actuel, MODE_WIN1_LOSE2, executing_i_meme_red_bull_player_2, invulnérabilité_temporaire_player_2)


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #--------------------------------------------------------------------COLLISIONS JOUEURS---------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        if executing_lightcycle_movement_d and executing_lightcycle_movement_left :
            if player_pos[0] >= player_pos_2[0] - player_size_2[0] and player_pos[1] >= player_pos_2[1] and player_pos[1] <= player_pos_2[1] + player_size_2[1] :
                mode_actuel = MODE_LA_PEACE
        
        if executing_lightcycle_movement_q and executing_lightcycle_movement_right :
            if player_pos_2[0] >= player_pos[0] + player_size[0] and player_pos_2[1] >= player_pos[1] and player_pos_2[1] <= player_pos[1] + player_size[1] :
                mode_actuel = MODE_LA_PEACE
        
        if executing_lightcycle_movement_s and executing_lightcycle_movement_up :
            if player_pos[1] >= player_pos_2[1] + player_size_2[1] and player_pos[0] >= player_pos_2[0] and player_pos[0] <= player_pos_2[0] + player_size_2[0] :
                mode_actuel = MODE_LA_PEACE
        
        if executing_lightcycle_movement_z and executing_lightcycle_movement_down :
            if player_pos_2[1] >= player_pos[1] + player_size[1] and player_pos_2[0] >= player_pos[0] and player_pos_2[0] <= player_pos[0] + player_size[0] :
                mode_actuel = MODE_LA_PEACE


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------------------------TRAÎNEES---------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        #---------------------------------------------------------------------------Joueur 1------------------------------------------------------------------------

        #-------------------------------------------------------------------------------Q---------------------------------------------------------------------------
        
        traînées_finales_q, traînées_finales_pos_q, traînées_finales_size_q = création_traînée_GAUCHE(executing_lightcycle_movement_q , traînées, player_pos_instant[0], player_pos[0], player_pos[1], traînées_finales_q, traînées_finales_pos_q, traînées_finales_size_q)
        
        #-------------------------------------------------------------------------------D---------------------------------------------------------------------------
        
        traînées_finales_d, traînées_finales_pos_d, traînées_finales_size_d = création_traînée_DROITE(executing_lightcycle_movement_d, traînées, player_pos_instant[0], player_pos_instant[1], player_pos[0], traînées_finales_d, traînées_finales_pos_d, traînées_finales_size_d)

        #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

        traînées_finales_z, traînées_finales_pos_z, traînées_finales_size_z = création_traînées_HAUT(executing_lightcycle_movement_z , traînées, player_pos_instant[1], player_pos[1], player_pos[0], traînées_finales_z, traînées_finales_pos_z, traînées_finales_size_z)

        #-------------------------------------------------------------------------------S---------------------------------------------------------------------------
        
        traînées_finales_s, traînées_finales_pos_s, traînées_finales_size_s = création_traînées_BAS(executing_lightcycle_movement_s, traînées, player_pos[1], player_pos_instant[1], player_pos_instant[0], traînées_finales_s, traînées_finales_pos_s, traînées_finales_size_s)


        #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------

        #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------
        
        traînées_finales_left, traînées_finales_pos_left, traînées_finales_size_left = création_traînée_GAUCHE(executing_lightcycle_movement_left , traînées, player_pos_2_instant[0], player_pos_2[0], player_pos_2[1], traînées_finales_left, traînées_finales_pos_left, traînées_finales_size_left)

        #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------
        
        traînées_finales_right, traînées_finales_pos_right, traînées_finales_size_right = création_traînée_DROITE(executing_lightcycle_movement_right, traînées, player_pos_2_instant[0], player_pos_2_instant[1], player_pos_2[0], traînées_finales_right, traînées_finales_pos_right, traînées_finales_size_right)

        #------------------------------------------------------------------------------UP---------------------------------------------------------------------------
        
        traînées_finales_up, traînées_finales_pos_up, traînées_finales_size_up = création_traînées_HAUT(executing_lightcycle_movement_up , traînées, player_pos_2_instant[1], player_pos_2[1], player_pos_2[0], traînées_finales_up, traînées_finales_pos_up, traînées_finales_size_up)

        #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
        
        traînées_finales_down, traînées_finales_pos_down, traînées_finales_size_down = création_traînées_BAS(executing_lightcycle_movement_down, traînées, player_pos_2[1], player_pos_2_instant[1], player_pos_2_instant[0], traînées_finales_down, traînées_finales_pos_down, traînées_finales_size_down)


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------COLLISIONS TRAÎNEES-------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        #---------------------------------------------------------------------------Joueur 1------------------------------------------------------------------------
        
        #-------------------------------------------------------------------------------Q---------------------------------------------------------------------------

        if executing_lightcycle_movement_q :
            for i, j in zip(traînées_finales_pos_z, traînées_finales_size_z) :
                if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
            
            for i, j in zip(traînées_finales_pos_s, traînées_finales_size_s) :
                if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

            for i, j in zip(traînées_finales_pos_up, traînées_finales_size_up) :
                if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

            for i, j in zip(traînées_finales_pos_down, traînées_finales_size_down) :
                if player_pos[0] <= i[0] + 5 and player_pos[0] >= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

        #-------------------------------------------------------------------------------D---------------------------------------------------------------------------

        if executing_lightcycle_movement_d :
            for i, j in zip(traînées_finales_pos_z, traînées_finales_size_z) :
                if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

            for i, j in zip(traînées_finales_pos_s, traînées_finales_size_s) :
                if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

            for i, j in zip(traînées_finales_pos_up, traînées_finales_size_up) :
                if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

            for i, j in zip(traînées_finales_pos_down, traînées_finales_size_down) :
                if player_pos[0] + 25 >= i[0] and player_pos[0] + 20 <= i[0] and player_pos[1] + 24 >= i[1] and player_pos[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

        #-------------------------------------------------------------------------------Z---------------------------------------------------------------------------

        if executing_lightcycle_movement_z :
            for i, j in zip(traînées_finales_pos_q, traînées_finales_size_q) :
                if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

            for i, j in zip(traînées_finales_pos_d, traînées_finales_size_d) :
                if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

            for i, j in zip(traînées_finales_pos_left, traînées_finales_size_left) :
                if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

            for i, j in zip(traînées_finales_pos_right, traînées_finales_size_right) :
                if player_pos[1] <= i[1] + 5 and player_pos[1] >= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

        #-------------------------------------------------------------------------------S---------------------------------------------------------------------------

        if executing_lightcycle_movement_s :
            for i, j in zip(traînées_finales_pos_q, traînées_finales_size_q) :
                if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

            for i, j in zip(traînées_finales_pos_d, traînées_finales_size_d) :
                if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

            for i, j in zip(traînées_finales_pos_left, traînées_finales_size_left) :
                if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1

            for i, j in zip(traînées_finales_pos_right, traînées_finales_size_right) :
                if player_pos[1] + 25 >= i[1] and player_pos[1] + 20 <= i[1] and player_pos[0] + 24 >= i[0] and player_pos[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player == False :
                        mode_actuel = MODE_WIN2_LOSE1
                    if invulnérabilité_temporaire_player == False :
                        mode_actuel = MODE_WIN2_LOSE1


        #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------

        #-----------------------------------------------------------------------------LEFT--------------------------------------------------------------------------

        if executing_lightcycle_movement_left :
            for i, j in zip(traînées_finales_pos_z, traînées_finales_size_z) :
                if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_s, traînées_finales_size_s) :
                if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_up, traînées_finales_size_up) :
                if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_down, traînées_finales_size_down) :
                if player_pos_2[0] <= i[0] + 5 and player_pos_2[0] >= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

        #-----------------------------------------------------------------------------RIGHT-------------------------------------------------------------------------

        if executing_lightcycle_movement_right :
            for i, j in zip(traînées_finales_pos_z, traînées_finales_size_z) :
                if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_s, traînées_finales_size_s) :
                if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_up, traînées_finales_size_up) :
                if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_down, traînées_finales_size_down) :
                if player_pos_2[0] + 25 >= i[0] and player_pos_2[0] + 20 <= i[0] and player_pos_2[1] + 24 >= i[1] and player_pos_2[1] - 1 <= i[1] + j[1] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

        #------------------------------------------------------------------------------UP---------------------------------------------------------------------------

        if executing_lightcycle_movement_up :
            for i, j in zip(traînées_finales_pos_q, traînées_finales_size_q) :
                if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_d, traînées_finales_size_d) :
                if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_left, traînées_finales_size_left) :
                if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_right, traînées_finales_size_right) :
                if player_pos_2[1] <= i[1] + 5 and player_pos_2[1] >= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

        #-----------------------------------------------------------------------------DOWN--------------------------------------------------------------------------
        
        if executing_lightcycle_movement_down :
            for i, j in zip(traînées_finales_pos_q, traînées_finales_size_q) :
                if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_d, traînées_finales_size_d) :
                if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_left, traînées_finales_size_left) :
                if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

            for i, j in zip(traînées_finales_pos_right, traînées_finales_size_right) :
                if player_pos_2[1] + 25 >= i[1] and player_pos_2[1] + 20 <= i[1] and player_pos_2[0] + 24 >= i[0] and player_pos_2[0] - 1 <= i[0] + j[0] :
                    if executing_i_meme_disparition_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2
                    if invulnérabilité_temporaire_player_2 == False :
                        mode_actuel = MODE_WIN1_LOSE2

        
        for i, j in zip(traînées_finales_q, traînées_finales_pos_q) :
            i.fill(traînées["color"])
            screen.blit(i, j)

        for i, j in zip(traînées_finales_d, traînées_finales_pos_d) :
            i.fill(traînées["color"])
            screen.blit(i, j)

        for i, j in zip(traînées_finales_z, traînées_finales_pos_z) :
            i.fill(traînées["color"])
            screen.blit(i, j)

        for i, j in zip(traînées_finales_s, traînées_finales_pos_s) :
            i.fill(traînées["color"])
            screen.blit(i, j)


        for i, j in zip(traînées_finales_left, traînées_finales_pos_left) :
            i.fill(traînées["color"])
            screen.blit(i, j)

        for i, j in zip(traînées_finales_right, traînées_finales_pos_right) :
            i.fill(traînées["color"])
            screen.blit(i, j)

        for i, j in zip(traînées_finales_up, traînées_finales_pos_up) :
            i.fill(traînées["color"])
            screen.blit(i, j)

        for i, j in zip(traînées_finales_down, traînées_finales_pos_down) :
            i.fill(traînées["color"])
            screen.blit(i, j)


        if executing_i_meme_disparition_player == False :
            screen.blit(player, player_pos)
        if executing_i_meme_disparition_player_2 == False :
            screen.blit(player_2, player_pos_2)


        cooldown_i_meme_red_bull_player, cooldown_i_meme_red_bull_player_2, executing_i_meme_red_bull_player, executing_i_meme_red_bull_player_2, executing_time_i_meme_red_bull_player, executing_time_i_meme_red_bull_player_2 = i_meme_red_bull(pressed_keys, cooldown_i_meme_red_bull_player, cooldown_i_meme_red_bull_player_2, i_meme_sélectionné_player, i_meme_sélectionné_player_2, executing_i_meme_red_bull_player, executing_i_meme_red_bull_player_2, executing_time_i_meme_red_bull_player, executing_time_i_meme_red_bull_player_2)
        cooldown_i_meme_disparition_player, cooldown_i_meme_disparition_player_2, executing_i_meme_disparition_player, executing_i_meme_disparition_player_2, executing_time_i_meme_disparition_player, executing_time_i_meme_disparition_player_2 = i_meme_disparition(pressed_keys, i_meme_sélectionné_player, i_meme_sélectionné_player_2, cooldown_i_meme_disparition_player, cooldown_i_meme_disparition_player_2, executing_i_meme_disparition_player, executing_i_meme_disparition_player_2, executing_time_i_meme_disparition_player, executing_time_i_meme_disparition_player_2)

        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------------------------STATISTIQUES-----------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        secondes += 1/60
        
        if secondes == 60 :
            secondes = 0
            minutes += 1
            score_player += 100
            score_player_2 += 100
        
        if minutes == 60 :
            minutes = 0
            heures += 1
            score_player += 10000
            score_player_2 += 10000

        #--------------------------------------------------------------------------AFFICHAGE------------------------------------------------------------------------

        Temps = f"{heures} : {minutes} : {round(secondes)}"
        font_Temps = pygame.font.Font(digital_7, 30)
        Temps_img = font_Temps.render(Temps, True, (255, 255, 255))
        Temps_dimensions = Temps_img.get_size()
        Temps_pos = [screen_size[0] / 2 - Temps_dimensions[0] / 2, grid_pos[1] / 2 - Temps_dimensions[1] / 2]

        screen.blit(Temps_img, Temps_pos)

        titre_Temps = "TEMPS"
        font_titre_Temps = pygame.font.Font(Score_Board_St, 15)
        titre_Temps_img = font_titre_Temps.render(titre_Temps, True, (255, 255, 255))
        titre_Temps_dimensions = titre_Temps_img.get_size()
        titre_Temps_pos = [screen_size[0] / 2 - titre_Temps_dimensions[0] / 2, Temps_pos[1] + Temps_dimensions[1]]

        screen.blit(titre_Temps_img, titre_Temps_pos)


        Score_player = f"{score_player}"
        font_Score_player = pygame.font.Font(Technos, 20)
        Score_player_img = font_Score_player.render(Score_player, True, (207, 47, 17))
        Score_player_dimensions = Score_player_img.get_size()
        Score_player_pos = [screen_size[0] / 2 - Score_player_dimensions[0] / 2 - 100, grid_pos[1] / 2 - Score_player_dimensions[1] / 2]

        screen.blit(Score_player_img, Score_player_pos)

        titre_Score_player = "SCORE J1"
        font_titre_Score_player = pygame.font.Font(Score_Board_St, 15)
        titre_Score_player_img = font_titre_Score_player.render(titre_Score_player, True, (207, 47, 17))
        titre_Score_player_dimensions = titre_Score_player_img.get_size()
        titre_Score_player_pos = [screen_size[0] / 2 - titre_Score_player_dimensions[0] / 2 - 100, Score_player_pos[1] / 2 - 5]

        screen.blit(titre_Score_player_img, titre_Score_player_pos)    

        Score_player_2 = f"{score_player_2}"
        font_Score_player_2 = pygame.font.Font(Technos, 20)
        Score_player_2_img = font_Score_player_2.render(Score_player_2, True, (0, 0, 255))
        Score_player_2_dimensions = Score_player_2_img.get_size()
        Score_player_2_pos = [screen_size[0] / 2 - Score_player_2_dimensions[0] / 2 + 100, grid_pos[1] / 2 - Score_player_2_dimensions[1] / 2]

        screen.blit(Score_player_2_img, Score_player_2_pos)

        titre_Score_player_2 = "SCORE J2"
        font_titre_Score_player_2 = pygame.font.Font(Score_Board_St, 15)
        titre_Score_player_2_img = font_titre_Score_player_2.render(titre_Score_player_2, True, (0, 0, 255))
        titre_Score_player_2_dimensions = titre_Score_player_2_img.get_size()
        titre_Score_player_2_pos = [screen_size[0] / 2 - titre_Score_player_2_dimensions[0] / 2 + 100, Score_player_2_pos[1] / 2 - 5]

        screen.blit(titre_Score_player_2_img, titre_Score_player_2_pos)


        cooldown_i_meme_player_fond = pygame.Surface ((104, 19))
        cooldown_i_meme_player_fond.fill("#000000")
        cooldown_i_meme_player_fond_size = [104, 19]
        cooldown_i_meme_player_fond_pos = [grid_pos[0] + (Score_player_pos[0] - grid_pos[0]) / 2 - cooldown_i_meme_player_fond_size[0] / 2, grid_pos[1] / 2]

        screen.blit(cooldown_i_meme_player_fond, cooldown_i_meme_player_fond_pos)

        if cooldown_i_meme_sélectionné_player == cooldown_i_meme_rare_sélectionné_player :
            avancement_cooldown_player = (100 - (cooldown_i_meme_sélectionné_player * 0.16666))
        if cooldown_i_meme_sélectionné_player == cooldown_i_meme_épique_sélectionné_player :
            avancement_cooldown_player = (100 - (cooldown_i_meme_sélectionné_player * 0.08333))
        if cooldown_i_meme_sélectionné_player == cooldown_i_meme_légendaire_sélectionné_player :
            avancement_cooldown_player = (100 - (cooldown_i_meme_sélectionné_player * 0.05555))
        cooldown_i_meme_player = pygame.Surface((round(avancement_cooldown_player), 15))
        cooldown_i_meme_player.fill("#F54927")
        cooldown_i_meme_player_size = [round(avancement_cooldown_player), 15]
        cooldown_i_meme_player_pos = [cooldown_i_meme_player_fond_pos[0] + 2, cooldown_i_meme_player_fond_pos[1] + 2]

        screen.blit(cooldown_i_meme_player, cooldown_i_meme_player_pos)


        cooldown_i_meme_player_2_fond = pygame.Surface ((104, 19))
        cooldown_i_meme_player_2_fond.fill("#000000")
        cooldown_i_meme_player_2_fond_size = [104, 19]
        cooldown_i_meme_player_2_fond_pos = [((grid_pos[0] + grid_size[0]) - (((grid_pos[0] + grid_size[0]) - (Score_player_2_pos[0] + Score_player_2_dimensions[0])) / 2)) - cooldown_i_meme_player_fond_size[0] / 2, grid_pos[1] / 2]

        screen.blit(cooldown_i_meme_player_2_fond, cooldown_i_meme_player_2_fond_pos)

        if cooldown_i_meme_sélectionné_player_2 == cooldown_i_meme_rare_sélectionné_player_2 :
            avancement_cooldown_player_2 = (100 - (cooldown_i_meme_sélectionné_player_2 * 0.16666))
        if cooldown_i_meme_sélectionné_player_2 == cooldown_i_meme_épique_sélectionné_player_2 :
            avancement_cooldown_player_2 = (100 - (cooldown_i_meme_sélectionné_player_2 * 0.08333))
        if cooldown_i_meme_sélectionné_player_2 == cooldown_i_meme_légendaire_sélectionné_player_2 :
            avancement_cooldown_player_2 = (100 - (cooldown_i_meme_sélectionné_player_2 * 0.05555))
        cooldown_i_meme_player_2 = pygame.Surface((round(avancement_cooldown_player_2), 15))
        cooldown_i_meme_player_2.fill("#0000FF")
        cooldown_i_meme_player_2_size = [round(avancement_cooldown_player_2), 15]
        cooldown_i_meme_player_2_pos = [cooldown_i_meme_player_2_fond_pos[0] + 2, cooldown_i_meme_player_2_fond_pos[1] + 2]

        screen.blit(cooldown_i_meme_player_2, cooldown_i_meme_player_2_pos)
        
        score_player, collectibles_player, collectibles_pos = réapparition_collectibles(executing_lightcycle_movement_q, executing_lightcycle_movement_d , executing_lightcycle_movement_z, executing_lightcycle_movement_s, grid_pos, grid_size, player_pos, player_size, collectibles_pos, collectibles_size, collectibles_player, score_player)
        score_player_2, collectibles_player_2, collectibles_pos = réapparition_collectibles(executing_lightcycle_movement_left, executing_lightcycle_movement_right, executing_lightcycle_movement_up, executing_lightcycle_movement_down, grid_pos, grid_size, player_pos_2, player_size_2, collectibles_pos, collectibles_size, collectibles_player_2, score_player_2)

        screen.blit(collectibles, collectibles_pos)



    if mode_actuel == MODE_WIN1_LOSE2 :
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------------------CALCULS DE FIN DE PARTIE-----------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        mode_actuel, utilisé_i_meme_devil_never_cry_player, utilisé_i_meme_devil_never_cry_player_2, invulnérabilité_temporaire_player, invulnérabilité_temporaire_player_2, time_invulnérabilité_temporaire_player, time_invulnérabilité_temporaire_player_2 = i_meme_devil_never_cry(i_meme_sélectionné_player, i_meme_sélectionné_player_2, mode_actuel, utilisé_i_meme_devil_never_cry_player, utilisé_i_meme_devil_never_cry_player_2,invulnérabilité_temporaire_player, invulnérabilité_temporaire_player_2, time_invulnérabilité_temporaire_player, time_invulnérabilité_temporaire_player_2)
        score_player, score_player_2, utilisé_i_meme_jackpot_player, utilisé_i_meme_jackpot_player_2 = i_meme_jackpot(i_meme_sélectionné_player, i_meme_sélectionné_player_2, score_player, score_player_2, utilisé_i_meme_jackpot_player, utilisé_i_meme_jackpot_player_2)

        temps_total = heures * 3600 + minutes * 60 + secondes

        frôlements_player += frôlements_de_la_mort_qui_tue_player
        frôlements_player_2 += frôlements_de_la_mort_qui_tue_player_2

        succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_caché_player, succès_temps_caché_player_2 = succès_temps(temps_total, succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_caché_player, succès_temps_caché_player_2)

        succès_score_1_player, succès_score_2_player, succès_score_caché_player = succès_score(score_player, succès_score_1_player, succès_score_2_player, succès_score_caché_player)
        succès_score_1_player_2, succès_score_2_player_2, succès_score_caché_player_2 = succès_score(score_player_2, succès_score_1_player_2, succès_score_2_player_2, succès_score_caché_player_2)

        succès_frôlements_1_player, succès_frôlements_2_player, succès_frôlements_caché_player = succès_frôlements(frôlements_player, succès_frôlements_1_player, succès_frôlements_2_player, succès_frôlements_caché_player)
        succès_frôlements_1_player_2, succès_frôlements_2_player_2, succès_frôlements_caché_player_2 = succès_frôlements(frôlements_player_2, succès_frôlements_1_player_2, succès_frôlements_2_player_2, succès_frôlements_caché_player_2)

        succès_collectibles_1_player, succès_collectibles_2_player, succès_collectibles_caché_player = succès_collectibles(collectibles_player, succès_collectibles_1_player, succès_collectibles_2_player, succès_collectibles_caché_player)
        succès_collectibles_1_player_2, succès_collectibles_2_player_2, succès_collectibles_caché_player_2 = succès_collectibles(collectibles_player_2, succès_collectibles_1_player_2, succès_collectibles_2_player_2, succès_collectibles_caché_player_2)


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------AFFICHAGE-------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        screen.fill("#F54927")

        #---------------------------------------------------------------------------TITRE---------------------------------------------------------------------------
        
        font_titre_WIN1_LOSE2 = pygame.font.Font(Technos, 75)
        titre_WIN1_LOSE2_img = font_titre_WIN1_LOSE2.render("Victoire du Joueur 1 !", True, (255, 255, 255))
        titre_WIN1_LOSE2_dimensions = titre_WIN1_LOSE2_img.get_size()
        titre_WIN1_LOSE2_pos = [screen_size[0] / 2 - titre_WIN1_LOSE2_dimensions[0] / 2, 50]
        screen.blit(titre_WIN1_LOSE2_img, titre_WIN1_LOSE2_pos)

        #-------------------------------------------------------------------------STAT TEMPS------------------------------------------------------------------------

        if heures > 1 :
            stats_temps = f"Cette partie a dure {heures} heures, {minutes} minute(s) et {round(secondes)} seconde(s)."
        elif heures > 0 :
            stats_temps = f"Cette partie a dure {heures} heure, {minutes} minute(s) et {round(secondes)} seconde(s)."
        elif minutes > 1 :
            stats_temps = f"Cette partie a dure {minutes} minutes et {round(secondes)} seconde(s)."
        elif minutes > 0 :
            stats_temps = f"Cette partie a dure {minutes} minute et {round(secondes)} seconde(s)."
        elif round(secondes) > 1 :
            stats_temps = f"Cette partie a dure {round(secondes)} secondes."
        else :
            stats_temps = f"Cette partie a dure {round(secondes)} seconde."

        font_stats_temps = pygame.font.Font(Arcade, 50)
        stats_temps_img = font_stats_temps.render(stats_temps, True, (255, 255, 255))
        stats_temps_dimensions = stats_temps_img.get_size()
        stats_temps_pos = [screen_size[0] / 2 - stats_temps_dimensions[0] / 2, titre_WIN1_LOSE2_pos[1] + titre_WIN1_LOSE2_dimensions[1] + 50]
        screen.blit(stats_temps_img, stats_temps_pos)

        #-------------------------------------------------------------------------SEPARATION------------------------------------------------------------------------

        separation = pygame.Surface((2, 400))
        separation.fill("#FFFFFF")
        separation_size = [2, 400]
        separation_pos = [screen_size[0] / 2 - separation_size[0] / 2, stats_temps_pos[1] + stats_temps_dimensions[1] + 50]
        screen.blit(separation, separation_pos)

        #--------------------------------------------------------------------------STATS J1-------------------------------------------------------------------------

        font_titre_stats_player = pygame.font.Font(Technos, 30)
        titre_stats_player_img = font_titre_stats_player.render("Joueur 1", True, (255, 255, 255))
        titre_stats_player_dimenions = titre_stats_player_img.get_size()
        titre_stats_player_pos = [separation_pos[0] / 2 - titre_stats_player_dimenions[0] / 2, separation_pos[1]]
        screen.blit(titre_stats_player_img, titre_stats_player_pos)


        stat_frôlements_player = f"Trainees frolees : {frôlements_player}"
        font_stat_frôlements_player = pygame.font.Font(Arcade, 25)
        stat_frôlements_player_img = font_stat_frôlements_player.render(stat_frôlements_player, True, (255, 255, 255))
        stat_frôlements_player_dimensions = stat_frôlements_player_img.get_size()
        stat_frôlements_player_pos = [separation_pos[0] / 2 - stat_frôlements_player_dimensions[0] / 2, titre_stats_player_pos[1] + titre_stats_player_dimenions[1] + 50]
        screen.blit(stat_frôlements_player_img, stat_frôlements_player_pos)

        stat_frôlements_de_la_mort_qui_tue_player = f"Traines frolees (frolements de la mort qui tue) : {frôlements_de_la_mort_qui_tue_player}"
        font_stat_frôlements_de_la_mort_qui_tue_player = pygame.font.Font(Arcade, 25)
        stat_frôlements_de_la_mort_qui_tue_player_img = font_stat_frôlements_de_la_mort_qui_tue_player.render(stat_frôlements_de_la_mort_qui_tue_player, True, (255, 255, 255))
        stat_frôlements_de_la_mort_qui_tue_player_dimensions = stat_frôlements_de_la_mort_qui_tue_player_img.get_size()
        stat_frôlements_de_la_mort_qui_tue_player_pos = [separation_pos[0] / 2 - stat_frôlements_de_la_mort_qui_tue_player_dimensions[0] / 2, stat_frôlements_player_pos[1] + stat_frôlements_player_dimensions[1] + 50]
        screen.blit(stat_frôlements_de_la_mort_qui_tue_player_img, stat_frôlements_de_la_mort_qui_tue_player_pos)

        stat_collectibles_player = f"Collectibles recuperes : {collectibles_player}"
        font_stat_collectibles_player = pygame.font.Font(Arcade, 25)
        stat_collectibles_player_img = font_stat_collectibles_player.render(stat_collectibles_player, True, (255, 255, 255))
        stat_collectibles_player_dimensions = stat_collectibles_player_img.get_size()
        stat_collectibles_player_pos = [separation_pos[0] / 2 - stat_collectibles_player_dimensions[0] / 2, stat_frôlements_de_la_mort_qui_tue_player_pos[1] + stat_frôlements_de_la_mort_qui_tue_player_dimensions[1] + 50]
        screen.blit(stat_collectibles_player_img, stat_collectibles_player_pos)

        stat_score_player = f"Score total : {score_player}"
        font_stat_score_player = pygame.font.Font(Arcade, 25)
        stat_score_player_img = font_stat_score_player.render(stat_score_player, True, (255, 255, 255))
        stat_score_player_dimensions = stat_score_player_img.get_size()
        stat_score_player_pos = [separation_pos[0] / 2 - stat_score_player_dimensions[0] / 2, stat_collectibles_player_pos[1] + stat_collectibles_player_dimensions[1] + 50]
        screen.blit(stat_score_player_img, stat_score_player_pos)

        #--------------------------------------------------------------------------STATS J2-------------------------------------------------------------------------

        font_titre_stats_player_2 = pygame.font.Font(Technos, 30)
        titre_stats_player_2_img = font_titre_stats_player_2.render("Joueur 2", True, (255, 255, 255))
        titre_stats_player_2_dimenions = titre_stats_player_2_img.get_size()
        titre_stats_player_2_pos = [3 * (separation_pos[0] / 2) - titre_stats_player_2_dimenions[0] / 2, separation_pos[1]]
        screen.blit(titre_stats_player_2_img, titre_stats_player_2_pos)


        stat_frôlements_player_2 = f"Trainees frolees : {frôlements_player_2}"
        font_stat_frôlements_player_2 = pygame.font.Font(Arcade, 25)
        stat_frôlements_player_2_img = font_stat_frôlements_player_2.render(stat_frôlements_player_2, True, (255, 255, 255))
        stat_frôlements_player_2_dimensions = stat_frôlements_player_2_img.get_size()
        stat_frôlements_player_2_pos = [3 * (separation_pos[0] / 2) - stat_frôlements_player_2_dimensions[0] / 2, titre_stats_player_2_pos[1] + titre_stats_player_2_dimenions[1] + 50]
        screen.blit(stat_frôlements_player_2_img, stat_frôlements_player_2_pos)

        stat_frôlements_de_la_mort_qui_tue_player_2 = f"Traines frolees (frolements de la mort qui tue) : {frôlements_de_la_mort_qui_tue_player_2}"
        font_stat_frôlements_de_la_mort_qui_tue_player_2 = pygame.font.Font(Arcade, 25)
        stat_frôlements_de_la_mort_qui_tue_player_2_img = font_stat_frôlements_de_la_mort_qui_tue_player_2.render(stat_frôlements_de_la_mort_qui_tue_player_2, True, (255, 255, 255))
        stat_frôlements_de_la_mort_qui_tue_player_2_dimensions = stat_frôlements_de_la_mort_qui_tue_player_2_img.get_size()
        stat_frôlements_de_la_mort_qui_tue_player_2_pos = [3 * (separation_pos[0] / 2) - stat_frôlements_de_la_mort_qui_tue_player_2_dimensions[0] / 2, stat_frôlements_player_2_pos[1] + stat_frôlements_player_2_dimensions[1] + 50]
        screen.blit(stat_frôlements_de_la_mort_qui_tue_player_2_img, stat_frôlements_de_la_mort_qui_tue_player_2_pos)

        stat_collectibles_player_2 = f"Collectibles recuperes : {collectibles_player_2}"
        font_stat_collectibles_player_2 = pygame.font.Font(Arcade, 25)
        stat_collectibles_player_2_img = font_stat_collectibles_player_2.render(stat_collectibles_player_2, True, (255, 255, 255))
        stat_collectibles_player_2_dimensions = stat_collectibles_player_2_img.get_size()
        stat_collectibles_player_2_pos = [ 3 * (separation_pos[0] / 2) - stat_collectibles_player_2_dimensions[0] / 2, stat_frôlements_de_la_mort_qui_tue_player_2_pos[1] + stat_frôlements_de_la_mort_qui_tue_player_2_dimensions[1] + 50]
        screen.blit(stat_collectibles_player_2_img, stat_collectibles_player_2_pos)

        stat_score_player_2 = f"Score total : {score_player_2}"
        font_stat_score_player_2 = pygame.font.Font(Arcade, 25)
        stat_score_player_2_img = font_stat_score_player_2.render(stat_score_player_2, True, (255, 255, 255))
        stat_score_player_2_dimensions = stat_score_player_2_img.get_size()
        stat_score_player_2_pos = [3 * (separation_pos[0] / 2) - stat_score_player_2_dimensions[0] / 2, stat_collectibles_player_2_pos[1] + stat_collectibles_player_2_dimensions[1] + 50]
        screen.blit(stat_score_player_2_img, stat_score_player_2_pos)

        #-------------------------------------------------------------------------BT QUITTER------------------------------------------------------------------------

        bt_retour_au_menu = pygame.Surface((800, 125))
        bt_retour_au_menu.fill("#999999")
        bt_retour_au_menu_size = [800, 125]
        bt_retour_au_menu_pos = [screen_size[0] / 2 - bt_retour_au_menu_size[0] / 2, separation_pos[1] + separation_size[1] + 25]
        screen.blit(bt_retour_au_menu, bt_retour_au_menu_pos)

        font_titre_bt_retour_au_menu = pygame.font.Font(Technos, 50)
        titre_bt_retour_au_menu_img = font_titre_bt_retour_au_menu.render("Retour au menu", True, (255, 255, 255))
        titre_bt_retour_au_menu_dimensions = titre_bt_retour_au_menu_img.get_size()
        titre_bt_retour_au_menu_pos = [screen_size[0] / 2 - titre_bt_retour_au_menu_dimensions[0] / 2, bt_retour_au_menu_pos[1] + bt_retour_au_menu_size[1] / 2 - titre_bt_retour_au_menu_dimensions[1] / 2]
        screen.blit(titre_bt_retour_au_menu_img, titre_bt_retour_au_menu_pos)

        mouse = pygame.mouse.get_pos()

        clique_gauche = pygame.mouse.get_pressed()[0]

        if clique_gauche :
            if mouse[0] >= bt_retour_au_menu_pos[0] and mouse[0] <= bt_retour_au_menu_pos[0] + bt_retour_au_menu_size[0] and mouse[1] >= bt_retour_au_menu_pos[1] and mouse[1] <= bt_retour_au_menu_pos[1] + bt_retour_au_menu_size[1] :
                mode_actuel = MODE_ACCUEIL



    if mode_actuel == MODE_WIN2_LOSE1 :
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------------------CALCULS DE FIN DE PARTIE-----------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        mode_actuel, utilisé_i_meme_devil_never_cry_player, utilisé_i_meme_devil_never_cry_player_2, invulnérabilité_temporaire_player, invulnérabilité_temporaire_player_2, time_invulnérabilité_temporaire_player, time_invulnérabilité_temporaire_player_2 = i_meme_devil_never_cry(i_meme_sélectionné_player, i_meme_sélectionné_player_2, mode_actuel, utilisé_i_meme_devil_never_cry_player, utilisé_i_meme_devil_never_cry_player_2,invulnérabilité_temporaire_player, invulnérabilité_temporaire_player_2, time_invulnérabilité_temporaire_player, time_invulnérabilité_temporaire_player_2)
        score_player, score_player_2, utilisé_i_meme_jackpot_player, utilisé_i_meme_jackpot_player_2 = i_meme_jackpot(i_meme_sélectionné_player, i_meme_sélectionné_player_2, score_player, score_player_2, utilisé_i_meme_jackpot_player, utilisé_i_meme_jackpot_player_2)

        temps_total = heures * 3600 + minutes * 60 + secondes

        frôlements_player += frôlements_de_la_mort_qui_tue_player
        frôlements_player_2 += frôlements_de_la_mort_qui_tue_player_2

        succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_caché_player, succès_temps_caché_player_2 = succès_temps(temps_total, succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_caché_player, succès_temps_caché_player_2)

        succès_score_1_player, succès_score_2_player, succès_score_caché_player = succès_score(score_player, succès_score_1_player, succès_score_2_player, succès_score_caché_player)
        succès_score_1_player_2, succès_score_2_player_2, succès_score_caché_player_2 = succès_score(score_player_2, succès_score_1_player_2, succès_score_2_player_2, succès_score_caché_player_2)

        succès_frôlements_1_player, succès_frôlements_2_player, succès_frôlements_caché_player = succès_frôlements(frôlements_player, succès_frôlements_1_player, succès_frôlements_2_player, succès_frôlements_caché_player)
        succès_frôlements_1_player_2, succès_frôlements_2_player_2, succès_frôlements_caché_player_2 = succès_frôlements(frôlements_player_2, succès_frôlements_1_player_2, succès_frôlements_2_player_2, succès_frôlements_caché_player_2)

        succès_collectibles_1_player, succès_collectibles_2_player, succès_collectibles_caché_player = succès_collectibles(collectibles_player, succès_collectibles_1_player, succès_collectibles_2_player, succès_collectibles_caché_player)
        succès_collectibles_1_player_2, succès_collectibles_2_player_2, succès_collectibles_caché_player_2 = succès_collectibles(collectibles_player_2, succès_collectibles_1_player_2, succès_collectibles_2_player_2, succès_collectibles_caché_player_2)


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------AFFICHAGE-------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        screen.fill("#2360FA")

        #---------------------------------------------------------------------------TITRE---------------------------------------------------------------------------
        
        font_titre_WIN2_LOSE1 = pygame.font.Font(Technos, 75)
        titre_WIN2_LOSE1_img = font_titre_WIN2_LOSE1.render("Victoire du Joueur 2 !", True, (0, 0, 0))
        titre_WIN2_LOSE1_dimensions = titre_WIN2_LOSE1_img.get_size()
        titre_WIN2_LOSE1_pos = [screen_size[0] / 2 - titre_WIN2_LOSE1_dimensions[0] / 2, 50]
        screen.blit(titre_WIN2_LOSE1_img, titre_WIN2_LOSE1_pos)

        #-------------------------------------------------------------------------STAT TEMPS------------------------------------------------------------------------

        if heures > 1 :
            stats_temps = f"Cette partie a dure {heures} heures, {minutes} minute(s) et {round(secondes)} seconde(s)."
        elif heures > 0 :
            stats_temps = f"Cette partie a dure {heures} heure, {minutes} minute(s) et {round(secondes)} seconde(s)."
        elif minutes > 1 :
            stats_temps = f"Cette partie a dure {minutes} minutes et {round(secondes)} seconde(s)."
        elif minutes > 0 :
            stats_temps = f"Cette partie a dure {minutes} minute et {round(secondes)} seconde(s)."
        elif round(secondes) > 1 :
            stats_temps = f"Cette partie a dure {round(secondes)} secondes."
        else :
            stats_temps = f"Cette partie a dure {round(secondes)} seconde."

        font_stats_temps = pygame.font.Font(Arcade, 50)
        stats_temps_img = font_stats_temps.render(stats_temps, True, (0, 0, 0))
        stats_temps_dimensions = stats_temps_img.get_size()
        stats_temps_pos = [screen_size[0] / 2 - stats_temps_dimensions[0] / 2, titre_WIN2_LOSE1_pos[1] + titre_WIN2_LOSE1_dimensions[1] + 50]
        screen.blit(stats_temps_img, stats_temps_pos)

        #-------------------------------------------------------------------------SEPARATION------------------------------------------------------------------------

        separation = pygame.Surface((2, 400))
        separation.fill("#FFFFFF")
        separation_size = [2, 400]
        separation_pos = [screen_size[0] / 2 - separation_size[0] / 2, stats_temps_pos[1] + stats_temps_dimensions[1] + 50]
        screen.blit(separation, separation_pos)

        #--------------------------------------------------------------------------STATS J1-------------------------------------------------------------------------

        font_titre_stats_player = pygame.font.Font(Technos, 30)
        titre_stats_player_img = font_titre_stats_player.render("Joueur 1", True, (0, 0, 0))
        titre_stats_player_dimenions = titre_stats_player_img.get_size()
        titre_stats_player_pos = [separation_pos[0] / 2 - titre_stats_player_dimenions[0] / 2, separation_pos[1]]
        screen.blit(titre_stats_player_img, titre_stats_player_pos)


        stat_frôlements_player = f"Trainees frolees : {frôlements_player}"
        font_stat_frôlements_player = pygame.font.Font(Arcade, 25)
        stat_frôlements_player_img = font_stat_frôlements_player.render(stat_frôlements_player, True, (0, 0, 0))
        stat_frôlements_player_dimensions = stat_frôlements_player_img.get_size()
        stat_frôlements_player_pos = [separation_pos[0] / 2 - stat_frôlements_player_dimensions[0] / 2, titre_stats_player_pos[1] + titre_stats_player_dimenions[1] + 50]
        screen.blit(stat_frôlements_player_img, stat_frôlements_player_pos)

        stat_frôlements_de_la_mort_qui_tue_player = f"Traines frolees (frolements de la mort qui tue) : {frôlements_de_la_mort_qui_tue_player}"
        font_stat_frôlements_de_la_mort_qui_tue_player = pygame.font.Font(Arcade, 25)
        stat_frôlements_de_la_mort_qui_tue_player_img = font_stat_frôlements_de_la_mort_qui_tue_player.render(stat_frôlements_de_la_mort_qui_tue_player, True, (0, 0, 0))
        stat_frôlements_de_la_mort_qui_tue_player_dimensions = stat_frôlements_de_la_mort_qui_tue_player_img.get_size()
        stat_frôlements_de_la_mort_qui_tue_player_pos = [separation_pos[0] / 2 - stat_frôlements_de_la_mort_qui_tue_player_dimensions[0] / 2, stat_frôlements_player_pos[1] + stat_frôlements_player_dimensions[1] + 50]
        screen.blit(stat_frôlements_de_la_mort_qui_tue_player_img, stat_frôlements_de_la_mort_qui_tue_player_pos)

        stat_collectibles_player = f"Collectibles recuperes : {collectibles_player}"
        font_stat_collectibles_player = pygame.font.Font(Arcade, 25)
        stat_collectibles_player_img = font_stat_collectibles_player.render(stat_collectibles_player, True, (0, 0, 0))
        stat_collectibles_player_dimensions = stat_collectibles_player_img.get_size()
        stat_collectibles_player_pos = [separation_pos[0] / 2 - stat_collectibles_player_dimensions[0] / 2, stat_frôlements_de_la_mort_qui_tue_player_pos[1] + stat_frôlements_de_la_mort_qui_tue_player_dimensions[1] + 50]
        screen.blit(stat_collectibles_player_img, stat_collectibles_player_pos)

        stat_score_player = f"Score total : {score_player}"
        font_stat_score_player = pygame.font.Font(Arcade, 25)
        stat_score_player_img = font_stat_score_player.render(stat_score_player, True, (0, 0, 0))
        stat_score_player_dimensions = stat_score_player_img.get_size()
        stat_score_player_pos = [separation_pos[0] / 2 - stat_score_player_dimensions[0] / 2, stat_collectibles_player_pos[1] + stat_collectibles_player_dimensions[1] + 50]
        screen.blit(stat_score_player_img, stat_score_player_pos)

        #--------------------------------------------------------------------------STATS J2-------------------------------------------------------------------------

        font_titre_stats_player_2 = pygame.font.Font(Technos, 30)
        titre_stats_player_2_img = font_titre_stats_player_2.render("Joueur 2", True, (0, 0, 0))
        titre_stats_player_2_dimenions = titre_stats_player_2_img.get_size()
        titre_stats_player_2_pos = [3 * (separation_pos[0] / 2) - titre_stats_player_2_dimenions[0] / 2, separation_pos[1]]
        screen.blit(titre_stats_player_2_img, titre_stats_player_2_pos)


        stat_frôlements_player_2 = f"Trainees frolees : {frôlements_player_2}"
        font_stat_frôlements_player_2 = pygame.font.Font(Arcade, 25)
        stat_frôlements_player_2_img = font_stat_frôlements_player_2.render(stat_frôlements_player_2, True, (0, 0, 0))
        stat_frôlements_player_2_dimensions = stat_frôlements_player_2_img.get_size()
        stat_frôlements_player_2_pos = [3 * (separation_pos[0] / 2) - stat_frôlements_player_2_dimensions[0] / 2, titre_stats_player_2_pos[1] + titre_stats_player_2_dimenions[1] + 50]
        screen.blit(stat_frôlements_player_2_img, stat_frôlements_player_2_pos)

        stat_frôlements_de_la_mort_qui_tue_player_2 = f"Traines frolees (frolements de la mort qui tue) : {frôlements_de_la_mort_qui_tue_player_2}"
        font_stat_frôlements_de_la_mort_qui_tue_player_2 = pygame.font.Font(Arcade, 25)
        stat_frôlements_de_la_mort_qui_tue_player_2_img = font_stat_frôlements_de_la_mort_qui_tue_player_2.render(stat_frôlements_de_la_mort_qui_tue_player_2, True, (0, 0, 0))
        stat_frôlements_de_la_mort_qui_tue_player_2_dimensions = stat_frôlements_de_la_mort_qui_tue_player_2_img.get_size()
        stat_frôlements_de_la_mort_qui_tue_player_2_pos = [3 * (separation_pos[0] / 2) - stat_frôlements_de_la_mort_qui_tue_player_2_dimensions[0] / 2, stat_frôlements_player_2_pos[1] + stat_frôlements_player_2_dimensions[1] + 50]
        screen.blit(stat_frôlements_de_la_mort_qui_tue_player_2_img, stat_frôlements_de_la_mort_qui_tue_player_2_pos)

        stat_collectibles_player_2 = f"Collectibles recuperes : {collectibles_player_2}"
        font_stat_collectibles_player_2 = pygame.font.Font(Arcade, 25)
        stat_collectibles_player_2_img = font_stat_collectibles_player_2.render(stat_collectibles_player_2, True, (0, 0, 0))
        stat_collectibles_player_2_dimensions = stat_collectibles_player_2_img.get_size()
        stat_collectibles_player_2_pos = [ 3 * (separation_pos[0] / 2) - stat_collectibles_player_2_dimensions[0] / 2, stat_frôlements_de_la_mort_qui_tue_player_2_pos[1] + stat_frôlements_de_la_mort_qui_tue_player_2_dimensions[1] + 50]
        screen.blit(stat_collectibles_player_2_img, stat_collectibles_player_2_pos)

        stat_score_player_2 = f"Score total : {score_player_2}"
        font_stat_score_player_2 = pygame.font.Font(Arcade, 25)
        stat_score_player_2_img = font_stat_score_player_2.render(stat_score_player_2, True, (0, 0, 0))
        stat_score_player_2_dimensions = stat_score_player_2_img.get_size()
        stat_score_player_2_pos = [3 * (separation_pos[0] / 2) - stat_score_player_2_dimensions[0] / 2, stat_collectibles_player_2_pos[1] + stat_collectibles_player_2_dimensions[1] + 50]
        screen.blit(stat_score_player_2_img, stat_score_player_2_pos)

        #-------------------------------------------------------------------------BT QUITTER------------------------------------------------------------------------

        bt_retour_au_menu = pygame.Surface((800, 125))
        bt_retour_au_menu.fill("#999999")
        bt_retour_au_menu_size = [800, 125]
        bt_retour_au_menu_pos = [screen_size[0] / 2 - bt_retour_au_menu_size[0] / 2, separation_pos[1] + separation_size[1] + 25]
        screen.blit(bt_retour_au_menu, bt_retour_au_menu_pos)

        font_titre_bt_retour_au_menu = pygame.font.Font(Technos, 50)
        titre_bt_retour_au_menu_img = font_titre_bt_retour_au_menu.render("Retour au menu", True, (255, 255, 255))
        titre_bt_retour_au_menu_dimensions = titre_bt_retour_au_menu_img.get_size()
        titre_bt_retour_au_menu_pos = [screen_size[0] / 2 - titre_bt_retour_au_menu_dimensions[0] / 2, bt_retour_au_menu_pos[1] + bt_retour_au_menu_size[1] / 2 - titre_bt_retour_au_menu_dimensions[1] / 2]
        screen.blit(titre_bt_retour_au_menu_img, titre_bt_retour_au_menu_pos)

        mouse = pygame.mouse.get_pos()

        clique_gauche = pygame.mouse.get_pressed()[0]

        if clique_gauche :
            if mouse[0] >= bt_retour_au_menu_pos[0] and mouse[0] <= bt_retour_au_menu_pos[0] + bt_retour_au_menu_size[0] and mouse[1] >= bt_retour_au_menu_pos[1] and mouse[1] <= bt_retour_au_menu_pos[1] + bt_retour_au_menu_size[1] :
                mode_actuel = MODE_ACCUEIL



    if mode_actuel == MODE_LA_PEACE :
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------------------CALCULS DE FIN DE PARTIE-----------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        mode_actuel, utilisé_i_meme_devil_never_cry_player, utilisé_i_meme_devil_never_cry_player_2, invulnérabilité_temporaire_player, invulnérabilité_temporaire_player_2, time_invulnérabilité_temporaire_player, time_invulnérabilité_temporaire_player_2 = i_meme_devil_never_cry(i_meme_sélectionné_player, i_meme_sélectionné_player_2, mode_actuel, utilisé_i_meme_devil_never_cry_player, utilisé_i_meme_devil_never_cry_player_2,invulnérabilité_temporaire_player, invulnérabilité_temporaire_player_2, time_invulnérabilité_temporaire_player, time_invulnérabilité_temporaire_player_2)
        score_player, score_player_2, utilisé_i_meme_jackpot_player, utilisé_i_meme_jackpot_player_2 = i_meme_jackpot(i_meme_sélectionné_player, i_meme_sélectionné_player_2, score_player, score_player_2, utilisé_i_meme_jackpot_player, utilisé_i_meme_jackpot_player_2)

        temps_total = heures * 3600 + minutes * 60 + secondes

        frôlements_player += frôlements_de_la_mort_qui_tue_player
        frôlements_player_2 += frôlements_de_la_mort_qui_tue_player_2

        succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_caché_player, succès_temps_caché_player_2 = succès_temps(temps_total, succès_temps_1_player, succès_temps_1_player_2, succès_temps_2_player, succès_temps_2_player_2, succès_temps_caché_player, succès_temps_caché_player_2)

        succès_score_1_player, succès_score_2_player, succès_score_caché_player = succès_score(score_player, succès_score_1_player, succès_score_2_player, succès_score_caché_player)
        succès_score_1_player_2, succès_score_2_player_2, succès_score_caché_player_2 = succès_score(score_player_2, succès_score_1_player_2, succès_score_2_player_2, succès_score_caché_player_2)

        succès_frôlements_1_player, succès_frôlements_2_player, succès_frôlements_caché_player = succès_frôlements(frôlements_player, succès_frôlements_1_player, succès_frôlements_2_player, succès_frôlements_caché_player)
        succès_frôlements_1_player_2, succès_frôlements_2_player_2, succès_frôlements_caché_player_2 = succès_frôlements(frôlements_player_2, succès_frôlements_1_player_2, succès_frôlements_2_player_2, succès_frôlements_caché_player_2)

        succès_collectibles_1_player, succès_collectibles_2_player, succès_collectibles_caché_player = succès_collectibles(collectibles_player, succès_collectibles_1_player, succès_collectibles_2_player, succès_collectibles_caché_player)
        succès_collectibles_1_player_2, succès_collectibles_2_player_2, succès_collectibles_caché_player_2 = succès_collectibles(collectibles_player_2, succès_collectibles_1_player_2, succès_collectibles_2_player_2, succès_collectibles_caché_player_2)


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------AFFICHAGE-------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        screen.fill("#0B041F")

        #---------------------------------------------------------------------------TITRE---------------------------------------------------------------------------
        
        font_titre_LA_PEACE = pygame.font.Font(Technos, 50)
        titre_LA_PEACE_img = font_titre_LA_PEACE.render("Vous avez trouve La Peace", True, (255, 255, 255))
        titre_LA_PEACE_dimensions = titre_LA_PEACE_img.get_size()
        titre_LA_PEACE_pos = [screen_size[0] / 2 - titre_LA_PEACE_dimensions[0] / 2, 50]
        screen.blit(titre_LA_PEACE_img, titre_LA_PEACE_pos)

        #-------------------------------------------------------------------------STAT TEMPS------------------------------------------------------------------------

        if heures > 1 :
            stats_temps = f"Cette partie a dure {heures} heures, {minutes} minute(s) et {round(secondes)} seconde(s)."
        elif heures > 0 :
            stats_temps = f"Cette partie a dure {heures} heure, {minutes} minute(s) et {round(secondes)} seconde(s)."
        elif minutes > 1 :
            stats_temps = f"Cette partie a dure {minutes} minutes et {round(secondes)} seconde(s)."
        elif minutes > 0 :
            stats_temps = f"Cette partie a dure {minutes} minute et {round(secondes)} seconde(s)."
        elif round(secondes) > 1 :
            stats_temps = f"Cette partie a dure {round(secondes)} secondes."
        else :
            stats_temps = f"Cette partie a dure {round(secondes)} seconde."

        font_stats_temps = pygame.font.Font(Arcade, 50)
        stats_temps_img = font_stats_temps.render(stats_temps, True, (255, 255, 255))
        stats_temps_dimensions = stats_temps_img.get_size()
        stats_temps_pos = [screen_size[0] / 2 - stats_temps_dimensions[0] / 2, titre_LA_PEACE_pos[1] + titre_LA_PEACE_dimensions[1] + 50]
        screen.blit(stats_temps_img, stats_temps_pos)

        #-------------------------------------------------------------------------SEPARATION------------------------------------------------------------------------

        separation = pygame.Surface((2, 400))
        separation.fill("#FFFFFF")
        separation_size = [2, 400]
        separation_pos = [screen_size[0] / 2 - separation_size[0] / 2, stats_temps_pos[1] + stats_temps_dimensions[1] + 50]
        screen.blit(separation, separation_pos)

        #--------------------------------------------------------------------------STATS J1-------------------------------------------------------------------------

        font_titre_stats_player = pygame.font.Font(Technos, 30)
        titre_stats_player_img = font_titre_stats_player.render("Joueur 1", True, (255, 255, 255))
        titre_stats_player_dimenions = titre_stats_player_img.get_size()
        titre_stats_player_pos = [separation_pos[0] / 2 - titre_stats_player_dimenions[0] / 2, separation_pos[1]]
        screen.blit(titre_stats_player_img, titre_stats_player_pos)


        stat_frôlements_player = f"Trainees frolees : {frôlements_player}"
        font_stat_frôlements_player = pygame.font.Font(Arcade, 25)
        stat_frôlements_player_img = font_stat_frôlements_player.render(stat_frôlements_player, True, (255, 255, 255))
        stat_frôlements_player_dimensions = stat_frôlements_player_img.get_size()
        stat_frôlements_player_pos = [separation_pos[0] / 2 - stat_frôlements_player_dimensions[0] / 2, titre_stats_player_pos[1] + titre_stats_player_dimenions[1] + 50]
        screen.blit(stat_frôlements_player_img, stat_frôlements_player_pos)

        stat_frôlements_de_la_mort_qui_tue_player = f"Traines frolees (frolements de la mort qui tue) : {frôlements_de_la_mort_qui_tue_player}"
        font_stat_frôlements_de_la_mort_qui_tue_player = pygame.font.Font(Arcade, 25)
        stat_frôlements_de_la_mort_qui_tue_player_img = font_stat_frôlements_de_la_mort_qui_tue_player.render(stat_frôlements_de_la_mort_qui_tue_player, True, (255, 255, 255))
        stat_frôlements_de_la_mort_qui_tue_player_dimensions = stat_frôlements_de_la_mort_qui_tue_player_img.get_size()
        stat_frôlements_de_la_mort_qui_tue_player_pos = [separation_pos[0] / 2 - stat_frôlements_de_la_mort_qui_tue_player_dimensions[0] / 2, stat_frôlements_player_pos[1] + stat_frôlements_player_dimensions[1] + 50]
        screen.blit(stat_frôlements_de_la_mort_qui_tue_player_img, stat_frôlements_de_la_mort_qui_tue_player_pos)

        stat_collectibles_player = f"Collectibles recuperes : {collectibles_player}"
        font_stat_collectibles_player = pygame.font.Font(Arcade, 25)
        stat_collectibles_player_img = font_stat_collectibles_player.render(stat_collectibles_player, True, (255, 255, 255))
        stat_collectibles_player_dimensions = stat_collectibles_player_img.get_size()
        stat_collectibles_player_pos = [separation_pos[0] / 2 - stat_collectibles_player_dimensions[0] / 2, stat_frôlements_de_la_mort_qui_tue_player_pos[1] + stat_frôlements_de_la_mort_qui_tue_player_dimensions[1] + 50]
        screen.blit(stat_collectibles_player_img, stat_collectibles_player_pos)

        stat_score_player = f"Score total : {score_player}"
        font_stat_score_player = pygame.font.Font(Arcade, 25)
        stat_score_player_img = font_stat_score_player.render(stat_score_player, True, (255, 255, 255))
        stat_score_player_dimensions = stat_score_player_img.get_size()
        stat_score_player_pos = [separation_pos[0] / 2 - stat_score_player_dimensions[0] / 2, stat_collectibles_player_pos[1] + stat_collectibles_player_dimensions[1] + 50]
        screen.blit(stat_score_player_img, stat_score_player_pos)

        #--------------------------------------------------------------------------STATS J2-------------------------------------------------------------------------

        font_titre_stats_player_2 = pygame.font.Font(Technos, 30)
        titre_stats_player_2_img = font_titre_stats_player_2.render("Joueur 2", True, (255, 255, 255))
        titre_stats_player_2_dimenions = titre_stats_player_2_img.get_size()
        titre_stats_player_2_pos = [3 * (separation_pos[0] / 2) - titre_stats_player_2_dimenions[0] / 2, separation_pos[1]]
        screen.blit(titre_stats_player_2_img, titre_stats_player_2_pos)


        stat_frôlements_player_2 = f"Trainees frolees : {frôlements_player_2}"
        font_stat_frôlements_player_2 = pygame.font.Font(Arcade, 25)
        stat_frôlements_player_2_img = font_stat_frôlements_player_2.render(stat_frôlements_player_2, True, (255, 255, 255))
        stat_frôlements_player_2_dimensions = stat_frôlements_player_2_img.get_size()
        stat_frôlements_player_2_pos = [3 * (separation_pos[0] / 2) - stat_frôlements_player_2_dimensions[0] / 2, titre_stats_player_2_pos[1] + titre_stats_player_2_dimenions[1] + 50]
        screen.blit(stat_frôlements_player_2_img, stat_frôlements_player_2_pos)

        stat_frôlements_de_la_mort_qui_tue_player_2 = f"Traines frolees (frolements de la mort qui tue) : {frôlements_de_la_mort_qui_tue_player_2}"
        font_stat_frôlements_de_la_mort_qui_tue_player_2 = pygame.font.Font(Arcade, 25)
        stat_frôlements_de_la_mort_qui_tue_player_2_img = font_stat_frôlements_de_la_mort_qui_tue_player_2.render(stat_frôlements_de_la_mort_qui_tue_player_2, True, (255, 255, 255))
        stat_frôlements_de_la_mort_qui_tue_player_2_dimensions = stat_frôlements_de_la_mort_qui_tue_player_2_img.get_size()
        stat_frôlements_de_la_mort_qui_tue_player_2_pos = [3 * (separation_pos[0] / 2) - stat_frôlements_de_la_mort_qui_tue_player_2_dimensions[0] / 2, stat_frôlements_player_2_pos[1] + stat_frôlements_player_2_dimensions[1] + 50]
        screen.blit(stat_frôlements_de_la_mort_qui_tue_player_2_img, stat_frôlements_de_la_mort_qui_tue_player_2_pos)

        stat_collectibles_player_2 = f"Collectibles recuperes : {collectibles_player_2}"
        font_stat_collectibles_player_2 = pygame.font.Font(Arcade, 25)
        stat_collectibles_player_2_img = font_stat_collectibles_player_2.render(stat_collectibles_player_2, True, (255, 255, 255))
        stat_collectibles_player_2_dimensions = stat_collectibles_player_2_img.get_size()
        stat_collectibles_player_2_pos = [ 3 * (separation_pos[0] / 2) - stat_collectibles_player_2_dimensions[0] / 2, stat_frôlements_de_la_mort_qui_tue_player_2_pos[1] + stat_frôlements_de_la_mort_qui_tue_player_2_dimensions[1] + 50]
        screen.blit(stat_collectibles_player_2_img, stat_collectibles_player_2_pos)

        stat_score_player_2 = f"Score total : {score_player_2}"
        font_stat_score_player_2 = pygame.font.Font(Arcade, 25)
        stat_score_player_2_img = font_stat_score_player_2.render(stat_score_player_2, True, (255, 255, 255))
        stat_score_player_2_dimensions = stat_score_player_2_img.get_size()
        stat_score_player_2_pos = [3 * (separation_pos[0] / 2) - stat_score_player_2_dimensions[0] / 2, stat_collectibles_player_2_pos[1] + stat_collectibles_player_2_dimensions[1] + 50]
        screen.blit(stat_score_player_2_img, stat_score_player_2_pos)

        #-------------------------------------------------------------------------BT QUITTER------------------------------------------------------------------------

        bt_retour_au_menu = pygame.Surface((800, 125))
        bt_retour_au_menu.fill("#999999")
        bt_retour_au_menu_size = [800, 125]
        bt_retour_au_menu_pos = [screen_size[0] / 2 - bt_retour_au_menu_size[0] / 2, separation_pos[1] + separation_size[1] + 25]
        screen.blit(bt_retour_au_menu, bt_retour_au_menu_pos)

        font_titre_bt_retour_au_menu = pygame.font.Font(Technos, 50)
        titre_bt_retour_au_menu_img = font_titre_bt_retour_au_menu.render("Retour au menu", True, (255, 255, 255))
        titre_bt_retour_au_menu_dimensions = titre_bt_retour_au_menu_img.get_size()
        titre_bt_retour_au_menu_pos = [screen_size[0] / 2 - titre_bt_retour_au_menu_dimensions[0] / 2, bt_retour_au_menu_pos[1] + bt_retour_au_menu_size[1] / 2 - titre_bt_retour_au_menu_dimensions[1] / 2]
        screen.blit(titre_bt_retour_au_menu_img, titre_bt_retour_au_menu_pos)

        mouse = pygame.mouse.get_pos()

        clique_gauche = pygame.mouse.get_pressed()[0]

        if clique_gauche :
            if mouse[0] >= bt_retour_au_menu_pos[0] and mouse[0] <= bt_retour_au_menu_pos[0] + bt_retour_au_menu_size[0] and mouse[1] >= bt_retour_au_menu_pos[1] and mouse[1] <= bt_retour_au_menu_pos[1] + bt_retour_au_menu_size[1] :
                mode_actuel = MODE_ACCUEIL



    if mode_actuel == MODE_SUCCES :
        #---------------------------------------------------------------------------TITRE---------------------------------------------------------------------------

        font_titre_menu_succès = pygame.font.Font(Technos, 75)
        titre_menu_succès_img = font_titre_menu_succès.render("Liste des succes", True, (255, 255, 255))
        titre_menu_succès_dimensions = titre_menu_succès_img.get_size()
        titre_menu_succès_pos = [screen_size[0] / 2 - titre_menu_succès_dimensions[0] / 2, 50]

        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------Joueur 1------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        bt_joueur_1 = pygame.Surface((550, 200))
        bt_joueur_1.fill("#999999")
        bt_joueur_1_size = [550, 200]
        bt_joueur_1_pos = [screen_size[0] / 4 - bt_joueur_1_size[0] / 2, screen_size[1] / 2 - bt_joueur_1_size[1] / 2]
 
        font_titre_bt_joueur_1 = pygame.font.Font(Technos, 60)
        titre_bt_joueur_1_img = font_titre_bt_joueur_1.render("Joueur 1", True, (255, 255, 255))
        titre_bt_joueur_1_dimensions = titre_bt_joueur_1_img.get_size()
        titre_bt_joueur_1_pos = [bt_joueur_1_pos[0] + bt_joueur_1_size[0] / 2 - titre_bt_joueur_1_dimensions[0] / 2, bt_joueur_1_pos[1] + bt_joueur_1_size[1] / 2 - titre_bt_joueur_1_dimensions[1] / 2]

        #---------------------------------------------------------------------------TEMPS---------------------------------------------------------------------------

        font__titre_bt_joueur_1 = pygame.font.Font(Technos, 45)
        _titre_bt_joueur_1_img = font__titre_bt_joueur_1.render("Joueur 1", True, (255, 255, 255))
        _titre_bt_joueur_1_dimensions = _titre_bt_joueur_1_img.get_size()
        _titre_bt_joueur_1_pos = [screen_size[0] / 2 - _titre_bt_joueur_1_dimensions[0] / 2, titre_menu_succès_pos[1] + titre_menu_succès_dimensions[1] + 10]


        bt_catégorie_temps = pygame.Surface((300, 50))
        bt_catégorie_temps.fill("#999999")
        bt_catégorie_temps_size = [300, 50]
        bt_catégorie_temps_pos = [screen_size[0] / 2 - 300 - bt_catégorie_temps_size[0] - 30, titre_menu_succès_pos[1] + titre_menu_succès_dimensions[1] + 75]
  
        font_titre_bt_catégorie_temps = pygame.font.Font(Technos, 25)
        titre_bt_catégorie_temps_img = font_titre_bt_catégorie_temps.render("Temps", True, (255, 255, 255))
        titre_bt_catégorie_temps_dimensions = titre_bt_catégorie_temps_img.get_size()
        titre_bt_catégorie_temps_pos = [bt_catégorie_temps_pos[0] + bt_catégorie_temps_size[0] / 2 - titre_bt_catégorie_temps_dimensions[0] / 2, bt_catégorie_temps_pos[1] + bt_catégorie_temps_size[1] / 2 - titre_bt_catégorie_temps_dimensions[1] / 2]


        font_succès_temps_1_player = pygame.font.Font(Arcade, 50)
        succès_temps_1_player_img = font_succès_temps_1_player.render("Survivre 30 secondes", True, (255, 255, 255))
        succès_temps_1_player_dimensions = succès_temps_1_player_img.get_size()
        succès_temps_1_player_pos = [20, bt_catégorie_temps_pos[1] + bt_catégorie_temps_size[1] + 50]

        if succès_temps_1_player :
            Statut_succès_temps_1_player = "Statut : Accompli"
        else :
            Statut_succès_temps_1_player = "Statut : Non accompli"
        font_statut_succès_temps_1_player = pygame.font.Font(Arcade, 35)
        statut_succès_temps_1_player_img = font_statut_succès_temps_1_player.render(Statut_succès_temps_1_player, True, (255, 255, 255))
        statut_succès_temps_1_player_dimensions = statut_succès_temps_1_player_img.get_size()
        statut_succès_temps_1_player_pos = [20, succès_temps_1_player_pos[1] + succès_temps_1_player_dimensions[1] + 20]

        font_succès_temps_2_player = pygame.font.Font(Arcade, 50)
        succès_temps_2_player_img = font_succès_temps_2_player.render("Survivre 1 minute", True, (255, 255, 255))
        succès_temps_2_player_dimensions = succès_temps_2_player_img.get_size()
        succès_temps_2_player_pos = [20, statut_succès_temps_1_player_pos[1] + statut_succès_temps_1_player_dimensions[1] + 50]

        if succès_temps_2_player :
            Statut_succès_temps_2_player = "Statut : Accompli"
        else :
            Statut_succès_temps_2_player = "Statut : Non accompli"
        font_statut_succès_temps_2_player = pygame.font.Font(Arcade, 35)
        statut_succès_temps_2_player_img = font_statut_succès_temps_2_player.render(Statut_succès_temps_2_player, True, (255, 255, 255))
        statut_succès_temps_2_player_dimensions = statut_succès_temps_2_player_img.get_size()
        statut_succès_temps_2_player_pos = [20, succès_temps_2_player_pos[1] + succès_temps_2_player_dimensions[1] + 20]

        font_succès_temps_caché_player = pygame.font.Font(Arcade, 50)
        succès_temps_caché_player_img = font_succès_temps_caché_player.render("Succes cache : Survivre 2 minutes et 30 secondes", True, (255, 255, 255))
        succès_temps_caché_player_dimensions = succès_temps_caché_player_img.get_size()
        succès_temps_caché_player_pos = [20, statut_succès_temps_2_player_pos[1] + statut_succès_temps_2_player_dimensions[1] + 50]

        if succès_temps_caché_player :
            Statut_succès_temps_caché_player = "Statut : Accompli"
        else :
            Statut_succès_temps_caché_player = "Statut : Non accompli"
        font_statut_succès_temps_caché_player = pygame.font.Font(Arcade, 35)
        statut_succès_temps_caché_player_img = font_statut_succès_temps_caché_player.render(Statut_succès_temps_caché_player, True, (255, 255, 255))
        statut_succès_temps_caché_player_dimensions = statut_succès_temps_caché_player_img.get_size()
        statut_succès_temps_caché_player_pos = [20, succès_temps_caché_player_pos[1] + succès_temps_caché_player_dimensions[1] + 20]

        #---------------------------------------------------------------------------SCORE---------------------------------------------------------------------------

        bt_catégorie_score = pygame.Surface((300, 50))
        bt_catégorie_score.fill("#999999")
        bt_catégorie_score_size = [300, 50]
        bt_catégorie_score_pos = [screen_size[0] / 2 - bt_catégorie_score_size[0] - 10, titre_menu_succès_pos[1] + titre_menu_succès_dimensions[1] + 75]

        font_titre_bt_catégorie_score = pygame.font.Font(Technos, 25)
        titre_bt_catégorie_score_img = font_titre_bt_catégorie_score.render("Score", True, (255, 255, 255))
        titre_bt_catégorie_score_dimensions = titre_bt_catégorie_score_img.get_size()
        titre_bt_catégorie_score_pos = [bt_catégorie_score_pos[0] + bt_catégorie_score_size[0] / 2 - titre_bt_catégorie_score_dimensions[0] / 2, bt_catégorie_score_pos[1] + bt_catégorie_score_size[1] / 2 - titre_bt_catégorie_score_dimensions[1] / 2]


        font_succès_score_1_player = pygame.font.Font(Arcade, 50)
        succès_score_1_player_img = font_succès_score_1_player.render("Marquer 100 points en une partie", True, (255, 255, 255))
        succès_score_1_player_dimensions = succès_score_1_player_img.get_size()
        succès_score_1_player_pos = [20, bt_catégorie_score_pos[1] + bt_catégorie_score_size[1] + 50]

        if succès_score_1_player :
            Statut_succès_score_1_player = "Statut : Accompli"
        else :
            Statut_succès_score_1_player = "Statut : Non accompli"
        font_statut_succès_score_1_player = pygame.font.Font(Arcade, 35)
        statut_succès_score_1_player_img = font_statut_succès_score_1_player.render(Statut_succès_score_1_player, True, (255, 255, 255))
        statut_succès_score_1_player_dimensions = statut_succès_score_1_player_img.get_size()
        statut_succès_score_1_player_pos = [20, succès_score_1_player_pos[1] + succès_score_1_player_dimensions[1] + 20]

        font_succès_score_2_player = pygame.font.Font(Arcade, 50)
        succès_score_2_player_img = font_succès_score_2_player.render("Marquer 500 points en une partie", True, (255, 255, 255))
        succès_score_2_player_dimensions = succès_score_2_player_img.get_size()
        succès_score_2_player_pos = [20, statut_succès_score_1_player_pos[1] + statut_succès_score_1_player_dimensions[1] + 50]

        if succès_score_2_player :
            Statut_succès_score_2_player = "Statut : Accompli"
        else :
            Statut_succès_score_2_player = "Statut : Non accompli"
        font_statut_succès_score_2_player = pygame.font.Font(Arcade, 35)
        statut_succès_score_2_player_img = font_statut_succès_score_2_player.render(Statut_succès_score_2_player, True, (255, 255, 255))
        statut_succès_score_2_player_dimensions = statut_succès_score_2_player_img.get_size()
        statut_succès_score_2_player_pos = [20, succès_score_2_player_pos[1] + succès_score_2_player_dimensions[1] + 20]

        font_succès_score_caché_player = pygame.font.Font(Arcade, 50)
        succès_score_caché_player_img = font_succès_score_caché_player.render("Succes cache : Marquer 1000 points en une partie", True, (255, 255, 255))
        succès_score_caché_player_dimensions = succès_score_caché_player_img.get_size()
        succès_score_caché_player_pos = [20, statut_succès_score_2_player_pos[1] + statut_succès_score_2_player_dimensions[1] + 50]

        if succès_score_caché_player :
            Statut_succès_score_caché_player = "Statut : Accompli"
        else :
            Statut_succès_score_caché_player = "Statut : Non accompli"
        font_statut_succès_score_caché_player = pygame.font.Font(Arcade, 35)
        statut_succès_score_caché_player_img = font_statut_succès_score_caché_player.render(Statut_succès_score_caché_player, True, (255, 255, 255))
        statut_succès_score_caché_player_dimensions = statut_succès_score_caché_player_img.get_size()
        statut_succès_score_caché_player_pos = [20, succès_score_caché_player_pos[1] + succès_score_caché_player_dimensions[1] + 20]

        #----------------------------------------------------------------------FRÔLEMENTS---------------------------------------------------------------------------

        bt_catégorie_frôlements = pygame.Surface((300, 50))
        bt_catégorie_frôlements.fill("#999999")
        bt_catégorie_frôlements_size = [300, 50]
        bt_catégorie_frôlements_pos = [bt_catégorie_score_pos[0] + bt_catégorie_score_size[0] + 20, titre_menu_succès_pos[1] + titre_menu_succès_dimensions[1] + 75]

        font_titre_bt_catégorie_frôlements = pygame.font.Font(Technos, 25)
        titre_bt_catégorie_frôlements_img = font_titre_bt_catégorie_frôlements.render("Frolements", True, (255, 255, 255))
        titre_bt_catégorie_frôlements_dimensions = titre_bt_catégorie_frôlements_img.get_size()
        titre_bt_catégorie_frôlements_pos = [bt_catégorie_frôlements_pos[0] + bt_catégorie_frôlements_size[0] / 2 - titre_bt_catégorie_frôlements_dimensions[0] / 2, bt_catégorie_frôlements_pos[1] + bt_catégorie_frôlements_size[1] / 2 - titre_bt_catégorie_frôlements_dimensions[1] / 2]


        font_succès_frôlements_1_player = pygame.font.Font(Arcade, 50)
        succès_frôlements_1_player_img = font_succès_frôlements_1_player.render("Froler 5 trainees en une partie", True, (255, 255, 255))
        succès_frôlements_1_player_dimensions = succès_frôlements_1_player_img.get_size()
        succès_frôlements_1_player_pos = [20, bt_catégorie_frôlements_pos[1] + bt_catégorie_frôlements_size[1] + 50]

        if succès_frôlements_1_player :
            Statut_succès_frôlements_1_player = "Statut : Accompli"
        else :
            Statut_succès_frôlements_1_player = "Statut : Non accompli"
        font_statut_succès_frôlements_1_player = pygame.font.Font(Arcade, 35)
        statut_succès_frôlements_1_player_img = font_statut_succès_frôlements_1_player.render(Statut_succès_frôlements_1_player, True, (255, 255, 255))
        statut_succès_frôlements_1_player_dimensions = statut_succès_frôlements_1_player_img.get_size()
        statut_succès_frôlements_1_player_pos = [20, succès_frôlements_1_player_pos[1] + succès_frôlements_1_player_dimensions[1] + 20]

        font_succès_frôlements_2_player = pygame.font.Font(Arcade, 50)
        succès_frôlements_2_player_img = font_succès_frôlements_2_player.render("Froler 10 trainees en une partie", True, (255, 255, 255))
        succès_frôlements_2_player_dimensions = succès_frôlements_2_player_img.get_size()
        succès_frôlements_2_player_pos = [20, statut_succès_frôlements_1_player_pos[1] + statut_succès_frôlements_1_player_dimensions[1] + 50]

        if succès_frôlements_2_player :
            Statut_succès_frôlements_2_player = "Statut : Accompli"
        else :
            Statut_succès_frôlements_2_player = "Statut : Non accompli"
        font_statut_succès_frôlements_2_player = pygame.font.Font(Arcade, 35)
        statut_succès_frôlements_2_player_img = font_statut_succès_frôlements_2_player.render(Statut_succès_frôlements_2_player, True, (255, 255, 255))
        statut_succès_frôlements_2_player_dimensions = statut_succès_frôlements_2_player_img.get_size()
        statut_succès_frôlements_2_player_pos = [20, succès_frôlements_2_player_pos[1] + succès_frôlements_2_player_dimensions[1] + 20]

        font_succès_frôlements_caché_player = pygame.font.Font(Arcade, 50)
        succès_frôlements_caché_player_img = font_succès_frôlements_caché_player.render("Succes cache : Froler 25 trainees en une partie", True, (255, 255, 255))
        succès_frôlements_caché_player_dimensions = succès_frôlements_caché_player_img.get_size()
        succès_frôlements_caché_player_pos = [20, statut_succès_frôlements_2_player_pos[1] + statut_succès_frôlements_2_player_dimensions[1] + 50]

        if succès_frôlements_caché_player :
            Statut_succès_frôlements_caché_player = "Statut : Accompli"
        else :
            Statut_succès_frôlements_caché_player = "Statut : Non accompli"
        font_statut_succès_frôlements_caché_player = pygame.font.Font(Arcade, 35)
        statut_succès_frôlements_caché_player_img = font_statut_succès_frôlements_caché_player.render(Statut_succès_frôlements_caché_player, True, (255, 255, 255))
        statut_succès_frôlements_caché_player_dimensions = statut_succès_frôlements_caché_player_img.get_size()
        statut_succès_frôlements_caché_player_pos = [20, succès_frôlements_caché_player_pos[1] + succès_frôlements_caché_player_dimensions[1] + 20]

        #----------------------------------------------------------------------COLLECTIBLES---------------------------------------------------------------------------

        bt_catégorie_collectibles = pygame.Surface((300, 50))
        bt_catégorie_collectibles.fill("#999999")
        bt_catégorie_collectibles_size = [300, 50]
        bt_catégorie_collectibles_pos = [bt_catégorie_frôlements_pos[0] + bt_catégorie_frôlements_size[0] + 20, titre_menu_succès_pos[1] + titre_menu_succès_dimensions[1] + 75]

        font_titre_bt_catégorie_collectibles = pygame.font.Font(Technos, 25)
        titre_bt_catégorie_collectibles_img = font_titre_bt_catégorie_collectibles.render("Collectibles", True, (255, 255, 255))
        titre_bt_catégorie_collectibles_dimensions = titre_bt_catégorie_collectibles_img.get_size()
        titre_bt_catégorie_collectibles_pos = [bt_catégorie_collectibles_pos[0] + bt_catégorie_collectibles_size[0] / 2 - titre_bt_catégorie_collectibles_dimensions[0] / 2, bt_catégorie_collectibles_pos[1] + bt_catégorie_collectibles_size[1] / 2 - titre_bt_catégorie_collectibles_dimensions[1] / 2]


        font_succès_collectibles_1_player = pygame.font.Font(Arcade, 50)
        succès_collectibles_1_player_img = font_succès_collectibles_1_player.render("Recuperer 1 collectible en une partie", True, (255, 255, 255))
        succès_collectibles_1_player_dimensions = succès_collectibles_1_player_img.get_size()
        succès_collectibles_1_player_pos = [20, bt_catégorie_collectibles_pos[1] + bt_catégorie_collectibles_size[1] + 50]

        if succès_collectibles_1_player :
            Statut_succès_collectibles_1_player = "Statut : Accompli"
        else :
            Statut_succès_collectibles_1_player = "Statut : Non accompli"
        font_statut_succès_collectibles_1_player = pygame.font.Font(Arcade, 35)
        statut_succès_collectibles_1_player_img = font_statut_succès_collectibles_1_player.render(Statut_succès_collectibles_1_player, True, (255, 255, 255))
        statut_succès_collectibles_1_player_dimensions = statut_succès_collectibles_1_player_img.get_size()
        statut_succès_collectibles_1_player_pos = [20, succès_collectibles_1_player_pos[1] + succès_collectibles_1_player_dimensions[1] + 20]

        font_succès_collectibles_2_player = pygame.font.Font(Arcade, 50)
        succès_collectibles_2_player_img = font_succès_collectibles_2_player.render("Recuperer 5 collectibles en une partie", True, (255, 255, 255))
        succès_collectibles_2_player_dimensions = succès_collectibles_2_player_img.get_size()
        succès_collectibles_2_player_pos = [20, statut_succès_collectibles_1_player_pos[1] + statut_succès_collectibles_1_player_dimensions[1] + 50]

        if succès_collectibles_2_player :
            Statut_succès_collectibles_2_player = "Statut : Accompli"
        else :
            Statut_succès_collectibles_2_player = "Statut : Non accompli"
        font_statut_succès_collectibles_2_player = pygame.font.Font(Arcade, 35)
        statut_succès_collectibles_2_player_img = font_statut_succès_collectibles_2_player.render(Statut_succès_collectibles_2_player, True, (255, 255, 255))
        statut_succès_collectibles_2_player_dimensions = statut_succès_collectibles_2_player_img.get_size()
        statut_succès_collectibles_2_player_pos = [20, succès_collectibles_2_player_pos[1] + succès_collectibles_2_player_dimensions[1] + 20]

        font_succès_collectibles_caché_player = pygame.font.Font(Arcade, 50)
        succès_collectibles_caché_player_img = font_succès_collectibles_caché_player.render("Succes cache : Recuperer 10 collectibles en une partie", True, (255, 255, 255))
        succès_collectibles_caché_player_dimensions = succès_collectibles_caché_player_img.get_size()
        succès_collectibles_caché_player_pos = [20, statut_succès_collectibles_2_player_pos[1] + statut_succès_collectibles_2_player_dimensions[1] + 50]

        if succès_collectibles_caché_player :
            Statut_succès_collectibles_caché_player = "Statut : Accompli"
        else :
            Statut_succès_collectibles_caché_player = "Statut : Non accompli"
        font_statut_succès_collectibles_caché_player = pygame.font.Font(Arcade, 35)
        statut_succès_collectibles_caché_player_img = font_statut_succès_collectibles_caché_player.render(Statut_succès_collectibles_caché_player, True, (255, 255, 255))
        statut_succès_collectibles_caché_player_dimensions = statut_succès_collectibles_caché_player_img.get_size()
        statut_succès_collectibles_caché_player_pos = [20, succès_collectibles_caché_player_pos[1] + succès_collectibles_caché_player_dimensions[1] + 20]


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        bt_joueur_2 = pygame.Surface((550, 200))
        bt_joueur_2.fill("#999999")
        bt_joueur_2_size = [550, 200]
        bt_joueur_2_pos = [3 * (screen_size[0] / 4) - bt_joueur_2_size[0] / 2, screen_size[1] / 2 - bt_joueur_2_size[1] / 2]

        font_titre_bt_joueur_2 = pygame.font.Font(Technos, 60)
        titre_bt_joueur_2_img = font_titre_bt_joueur_2.render("Joueur 2", True, (255, 255, 255))
        titre_bt_joueur_2_dimensions = titre_bt_joueur_2_img.get_size()
        titre_bt_joueur_2_pos = [bt_joueur_2_pos[0] + bt_joueur_2_size[0] / 2 - titre_bt_joueur_2_dimensions[0] / 2, bt_joueur_2_pos[1] + bt_joueur_2_size[1] / 2 - titre_bt_joueur_2_dimensions[1] / 2]

        #---------------------------------------------------------------------------TEMPS---------------------------------------------------------------------------

        font__titre_bt_joueur_2 = pygame.font.Font(Technos, 45)
        _titre_bt_joueur_2_img = font__titre_bt_joueur_2.render("Joueur 2", True, (255, 255, 255))
        _titre_bt_joueur_2_dimensions = _titre_bt_joueur_2_img.get_size()
        _titre_bt_joueur_2_pos = [screen_size[0] / 2 - _titre_bt_joueur_2_dimensions[0] / 2, titre_menu_succès_pos[1] + titre_menu_succès_dimensions[1] + 10]


        bt_catégorie_temps2 = pygame.Surface((300, 50))
        bt_catégorie_temps2.fill("#999999")
        bt_catégorie_temps2_size = [300, 50]
        bt_catégorie_temps2_pos = [screen_size[0] / 2 - 300 - bt_catégorie_temps2_size[0] - 30, titre_menu_succès_pos[1] + titre_menu_succès_dimensions[1] + 75 + bt_catégorie_temps2_size[1]]

        font_titre_bt_catégorie_temps2 = pygame.font.Font(Technos, 25)
        titre_bt_catégorie_temps2_img = font_titre_bt_catégorie_temps2.render("Temps", True, (255, 255, 255))
        titre_bt_catégorie_temps2_dimensions = titre_bt_catégorie_temps2_img.get_size()
        titre_bt_catégorie_temps2_pos = [bt_catégorie_temps2_pos[0] + bt_catégorie_temps2_size[0] / 2 - titre_bt_catégorie_temps2_dimensions[0] / 2, bt_catégorie_temps2_pos[1] + bt_catégorie_temps2_size[1] / 2 - titre_bt_catégorie_temps2_dimensions[1] / 2]


        font_succès_temps_1_player2 = pygame.font.Font(Arcade, 50)
        succès_temps_1_player2_img = font_succès_temps_1_player2.render("Survivre 30 secondes", True, (255, 255, 255))
        succès_temps_1_player2_dimensions = succès_temps_1_player2_img.get_size()
        succès_temps_1_player2_pos = [20, bt_catégorie_temps2_pos[1] + bt_catégorie_temps2_size[1] + 50]

        if succès_temps_1_player_2 :
            Statut_succès_temps_1_player2 = "Statut : Accompli"
        else :
            Statut_succès_temps_1_player2 = "Statut : Non accompli"
        font_statut_succès_temps_1_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_temps_1_player2_img = font_statut_succès_temps_1_player2.render(Statut_succès_temps_1_player2, True, (255, 255, 255))
        statut_succès_temps_1_player2_dimensions = statut_succès_temps_1_player2_img.get_size()
        statut_succès_temps_1_player2_pos = [20, succès_temps_1_player2_pos[1] + succès_temps_1_player2_dimensions[1] + 20]


        font_succès_temps_2_player2 = pygame.font.Font(Arcade, 50)
        succès_temps_2_player2_img = font_succès_temps_2_player2.render("Survivre 1 minute", True, (255, 255, 255))
        succès_temps_2_player2_dimensions = succès_temps_2_player2_img.get_size()
        succès_temps_2_player2_pos = [20, statut_succès_temps_1_player2_pos[1] + statut_succès_temps_1_player2_dimensions[1] + 50]

        if succès_temps_2_player_2 :
            Statut_succès_temps_2_player2 = "Statut : Accompli"
        else :
            Statut_succès_temps_2_player2 = "Statut : Non accompli"
        font_statut_succès_temps_2_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_temps_2_player2_img = font_statut_succès_temps_2_player2.render(Statut_succès_temps_2_player2, True, (255, 255, 255))
        statut_succès_temps_2_player2_dimensions = statut_succès_temps_2_player2_img.get_size()
        statut_succès_temps_2_player2_pos = [20, succès_temps_2_player2_pos[1] + succès_temps_2_player2_dimensions[1] + 20]

        font_succès_temps_caché_player2 = pygame.font.Font(Arcade, 50)
        succès_temps_caché_player2_img = font_succès_temps_caché_player2.render("Succes cache : Survivre 2 minutes et 30 secondes", True, (255, 255, 255))
        succès_temps_caché_player2_dimensions = succès_temps_caché_player2_img.get_size()
        succès_temps_caché_player2_pos = [20, statut_succès_temps_2_player2_pos[1] + statut_succès_temps_2_player2_dimensions[1] + 50]

        if succès_temps_caché_player_2 :
            Statut_succès_temps_caché_player2 = "Statut : Accompli"
        else :
            Statut_succès_temps_caché_player2 = "Statut : Non accompli"
        font_statut_succès_temps_caché_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_temps_caché_player2_img = font_statut_succès_temps_caché_player2.render(Statut_succès_temps_caché_player2, True, (255, 255, 255))
        statut_succès_temps_caché_player2_dimensions = statut_succès_temps_caché_player2_img.get_size()
        statut_succès_temps_caché_player2_pos = [20, succès_temps_caché_player2_pos[1] + succès_temps_caché_player2_dimensions[1] + 20]

        #---------------------------------------------------------------------------SCORE---------------------------------------------------------------------------

        bt_catégorie_score2 = pygame.Surface((300, 50))
        bt_catégorie_score2.fill("#999999")
        bt_catégorie_score2_size = [300, 50]
        bt_catégorie_score2_pos = [screen_size[0] / 2 - bt_catégorie_score2_size[0] - 10, titre_menu_succès_pos[1] + titre_menu_succès_dimensions[1] + 75 + bt_catégorie_score2_size[1]]

        font_titre_bt_catégorie_score2 = pygame.font.Font(Technos, 25)
        titre_bt_catégorie_score2_img = font_titre_bt_catégorie_score2.render("Score", True, (255, 255, 255))
        titre_bt_catégorie_score2_dimensions = titre_bt_catégorie_score2_img.get_size()
        titre_bt_catégorie_score2_pos = [bt_catégorie_score2_pos[0] + bt_catégorie_score2_size[0] / 2 - titre_bt_catégorie_score2_dimensions[0] / 2, bt_catégorie_score2_pos[1] + bt_catégorie_score2_size[1] / 2 - titre_bt_catégorie_score2_dimensions[1] / 2]


        font_succès_score_1_player2 = pygame.font.Font(Arcade, 50)
        succès_score_1_player2_img = font_succès_score_1_player2.render("Marquer 100 points en une partie", True, (255, 255, 255))
        succès_score_1_player2_dimensions = succès_score_1_player2_img.get_size()
        succès_score_1_player2_pos = [20, bt_catégorie_score2_pos[1] + bt_catégorie_score2_size[1] + 50]

        if succès_score_1_player_2 :
            Statut_succès_score_1_player2 = "Statut : Accompli"
        else :
            Statut_succès_score_1_player2 = "Statut : Non accompli"
        font_statut_succès_score_1_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_score_1_player2_img = font_statut_succès_score_1_player2.render(Statut_succès_score_1_player2, True, (255, 255, 255))
        statut_succès_score_1_player2_dimensions = statut_succès_score_1_player2_img.get_size()
        statut_succès_score_1_player2_pos = [20, succès_score_1_player2_pos[1] + succès_score_1_player2_dimensions[1] + 20]

        font_succès_score_2_player2 = pygame.font.Font(Arcade, 50)
        succès_score_2_player2_img = font_succès_score_2_player2.render("Marquer 500 points en une partie", True, (255, 255, 255))
        succès_score_2_player2_dimensions = succès_score_2_player2_img.get_size()
        succès_score_2_player2_pos = [20, statut_succès_score_1_player2_pos[1] + statut_succès_score_1_player2_dimensions[1] + 50]

        if succès_score_2_player_2 :
            Statut_succès_score_2_player2 = "Statut : Accompli"
        else :
            Statut_succès_score_2_player2 = "Statut : Non accompli"
        font_statut_succès_score_2_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_score_2_player2_img = font_statut_succès_score_2_player2.render(Statut_succès_score_2_player2, True, (255, 255, 255))
        statut_succès_score_2_player2_dimensions = statut_succès_score_2_player2_img.get_size()
        statut_succès_score_2_player2_pos = [20, succès_score_2_player2_pos[1] + succès_score_2_player2_dimensions[1] + 20]

        font_succès_score_caché_player2 = pygame.font.Font(Arcade, 50)
        succès_score_caché_player2_img = font_succès_score_caché_player2.render("Succes cache : Marquer 1000 points en une partie", True, (255, 255, 255))
        succès_score_caché_player2_dimensions = succès_score_caché_player2_img.get_size()
        succès_score_caché_player2_pos = [20, statut_succès_score_2_player2_pos[1] + statut_succès_score_2_player2_dimensions[1] + 50]

        if succès_score_caché_player_2 :
            Statut_succès_score_caché_player2 = "Statut : Accompli"
        else :
            Statut_succès_score_caché_player2 = "Statut : Non accompli"
        font_statut_succès_score_caché_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_score_caché_player2_img = font_statut_succès_score_caché_player2.render(Statut_succès_score_caché_player2, True, (255, 255, 255))
        statut_succès_score_caché_player2_dimensions = statut_succès_score_caché_player2_img.get_size()
        statut_succès_score_caché_player2_pos = [20, succès_score_caché_player2_pos[1] + succès_score_caché_player2_dimensions[1] + 20]

        #----------------------------------------------------------------------FRÔLEMENTS---------------------------------------------------------------------------

        bt_catégorie_frôlements2 = pygame.Surface((300, 50))
        bt_catégorie_frôlements2.fill("#999999")
        bt_catégorie_frôlements2_size = [300, 50]
        bt_catégorie_frôlements2_pos = [bt_catégorie_score2_pos[0] + bt_catégorie_score2_size[0] + 20, titre_menu_succès_pos[1] + titre_menu_succès_dimensions[1] + 75 + bt_catégorie_frôlements2_size[1]]

        font_titre_bt_catégorie_frôlements2 = pygame.font.Font(Technos, 25)
        titre_bt_catégorie_frôlements2_img = font_titre_bt_catégorie_frôlements2.render("Frolements", True, (255, 255, 255))
        titre_bt_catégorie_frôlements2_dimensions = titre_bt_catégorie_frôlements2_img.get_size()
        titre_bt_catégorie_frôlements2_pos = [bt_catégorie_frôlements_pos[0] + bt_catégorie_frôlements2_size[0] / 2 - titre_bt_catégorie_frôlements2_dimensions[0] / 2, bt_catégorie_frôlements2_pos[1] + bt_catégorie_frôlements2_size[1] / 2 - titre_bt_catégorie_frôlements2_dimensions[1] / 2]


        font_succès_frôlements_1_player2 = pygame.font.Font(Arcade, 50)
        succès_frôlements_1_player2_img = font_succès_frôlements_1_player2.render("Froler 5 trainees en une partie", True, (255, 255, 255))
        succès_frôlements_1_player2_dimensions = succès_frôlements_1_player2_img.get_size()
        succès_frôlements_1_player2_pos = [20, bt_catégorie_frôlements2_pos[1] + bt_catégorie_frôlements2_size[1] + 50]

        if succès_frôlements_1_player_2 :
            Statut_succès_frôlements_1_player2 = "Statut : Accompli"
        else :
            Statut_succès_frôlements_1_player2 = "Statut : Non accompli"
        font_statut_succès_frôlements_1_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_frôlements_1_player2_img = font_statut_succès_frôlements_1_player2.render(Statut_succès_frôlements_1_player2, True, (255, 255, 255))
        statut_succès_frôlements_1_player2_dimensions = statut_succès_frôlements_1_player2_img.get_size()
        statut_succès_frôlements_1_player2_pos = [20, succès_frôlements_1_player2_pos[1] + succès_frôlements_1_player2_dimensions[1] + 20]

        font_succès_frôlements_2_player2 = pygame.font.Font(Arcade, 50)
        succès_frôlements_2_player2_img = font_succès_frôlements_2_player2.render("Froler 10 trainees en une partie", True, (255, 255, 255))
        succès_frôlements_2_player2_dimensions = succès_frôlements_2_player2_img.get_size()
        succès_frôlements_2_player2_pos = [20, statut_succès_frôlements_1_player2_pos[1] + statut_succès_frôlements_1_player2_dimensions[1] + 50]

        if succès_frôlements_2_player_2 :
            Statut_succès_frôlements_2_player2 = "Statut : Accompli"
        else :
            Statut_succès_frôlements_2_player2 = "Statut : Non accompli"
        font_statut_succès_frôlements_2_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_frôlements_2_player2_img = font_statut_succès_frôlements_2_player2.render(Statut_succès_frôlements_2_player2, True, (255, 255, 255))
        statut_succès_frôlements_2_player2_dimensions = statut_succès_frôlements_2_player2_img.get_size()
        statut_succès_frôlements_2_player2_pos = [20, succès_frôlements_2_player2_pos[1] + succès_frôlements_2_player2_dimensions[1] + 20]

        font_succès_frôlements_caché_player2 = pygame.font.Font(Arcade, 50)
        succès_frôlements_caché_player2_img = font_succès_frôlements_caché_player2.render("Succes cache : Froler 25 trainees en une partie", True, (255, 255, 255))
        succès_frôlements_caché_player2_dimensions = succès_frôlements_caché_player2_img.get_size()
        succès_frôlements_caché_player2_pos = [20, statut_succès_frôlements_2_player2_pos[1] + statut_succès_frôlements_2_player2_dimensions[1] + 50]

        if succès_frôlements_caché_player_2 :
            Statut_succès_frôlements_caché_player2 = "Statut : Accompli"
        else :
            Statut_succès_frôlements_caché_player2 = "Statut : Non accompli"
        font_statut_succès_frôlements_caché_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_frôlements_caché_player2_img = font_statut_succès_frôlements_caché_player2.render(Statut_succès_frôlements_caché_player2, True, (255, 255, 255))
        statut_succès_frôlements_caché_player2_dimensions = statut_succès_frôlements_caché_player2_img.get_size()
        statut_succès_frôlements_caché_player2_pos = [20, succès_frôlements_caché_player2_pos[1] + succès_frôlements_caché_player2_dimensions[1] + 20]

        #----------------------------------------------------------------------COLLECTIBLES---------------------------------------------------------------------------

        bt_catégorie_collectibles2 = pygame.Surface((300, 50))
        bt_catégorie_collectibles2.fill("#999999")
        bt_catégorie_collectibles2_size = [300, 50]
        bt_catégorie_collectibles2_pos = [bt_catégorie_frôlements2_pos[0] + bt_catégorie_frôlements2_size[0] + 20, titre_menu_succès_pos[1] + titre_menu_succès_dimensions[1] + 75 + bt_catégorie_collectibles2_size[1]]

        font_titre_bt_catégorie_collectibles2 = pygame.font.Font(Technos, 25)
        titre_bt_catégorie_collectibles2_img = font_titre_bt_catégorie_collectibles2.render("Collectibles", True, (255, 255, 255))
        titre_bt_catégorie_collectibles2_dimensions = titre_bt_catégorie_collectibles2_img.get_size()
        titre_bt_catégorie_collectibles2_pos = [bt_catégorie_collectibles2_pos[0] + bt_catégorie_collectibles2_size[0] / 2 - titre_bt_catégorie_collectibles2_dimensions[0] / 2, bt_catégorie_collectibles2_pos[1] + bt_catégorie_collectibles2_size[1] / 2 - titre_bt_catégorie_collectibles2_dimensions[1] / 2]


        font_succès_collectibles_1_player2 = pygame.font.Font(Arcade, 50)
        succès_collectibles_1_player2_img = font_succès_collectibles_1_player2.render("Recuperer 1 collectible en une partie", True, (255, 255, 255))
        succès_collectibles_1_player2_dimensions = succès_collectibles_1_player2_img.get_size()
        succès_collectibles_1_player2_pos = [20, bt_catégorie_collectibles2_pos[1] + bt_catégorie_collectibles2_size[1] + 50]

        if succès_collectibles_1_player_2 :
            Statut_succès_collectibles_1_player2 = "Statut : Accompli"
        else :
            Statut_succès_collectibles_1_player2 = "Statut : Non accompli"
        font_statut_succès_collectibles_1_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_collectibles_1_player2_img = font_statut_succès_collectibles_1_player2.render(Statut_succès_collectibles_1_player2, True, (255, 255, 255))
        statut_succès_collectibles_1_player2_dimensions = statut_succès_collectibles_1_player2_img.get_size()
        statut_succès_collectibles_1_player2_pos = [20, succès_collectibles_1_player2_pos[1] + succès_collectibles_1_player2_dimensions[1] + 20]

        font_succès_collectibles_2_player2 = pygame.font.Font(Arcade, 50)
        succès_collectibles_2_player2_img = font_succès_collectibles_2_player2.render("Recuperer 5 collectibles en une partie", True, (255, 255, 255))
        succès_collectibles_2_player2_dimensions = succès_collectibles_2_player2_img.get_size()
        succès_collectibles_2_player2_pos = [20, statut_succès_collectibles_1_player2_pos[1] + statut_succès_collectibles_1_player2_dimensions[1] + 50]

        if succès_collectibles_2_player_2 :
            Statut_succès_collectibles_2_player2 = "Statut : Accompli"
        else :
            Statut_succès_collectibles_2_player2 = "Statut : Non accompli"
        font_statut_succès_collectibles_2_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_collectibles_2_player2_img = font_statut_succès_collectibles_2_player2.render(Statut_succès_collectibles_2_player2, True, (255, 255, 255))
        statut_succès_collectibles_2_player2_dimensions = statut_succès_collectibles_2_player2_img.get_size()
        statut_succès_collectibles_2_player2_pos = [20, succès_collectibles_2_player2_pos[1] + succès_collectibles_2_player2_dimensions[1] + 20]

        font_succès_collectibles_caché_player2 = pygame.font.Font(Arcade, 50)
        succès_collectibles_caché_player2_img = font_succès_collectibles_caché_player2.render("Succes cache : Recuperer 10 collectibles en une partie", True, (255, 255, 255))
        succès_collectibles_caché_player2_dimensions = succès_collectibles_caché_player2_img.get_size()
        succès_collectibles_caché_player2_pos = [20, statut_succès_collectibles_2_player2_pos[1] + statut_succès_collectibles_2_player2_dimensions[1] + 50]

        if succès_collectibles_caché_player_2 :
            Statut_succès_collectibles_caché_player2 = "Statut : Accompli"
        else :
            Statut_succès_collectibles_caché_player2 = "Statut : Non accompli"
        font_statut_succès_collectibles_caché_player2 = pygame.font.Font(Arcade, 35)
        statut_succès_collectibles_caché_player2_img = font_statut_succès_collectibles_caché_player2.render(Statut_succès_collectibles_caché_player2, True, (255, 255, 255))
        statut_succès_collectibles_caché_player2_dimensions = statut_succès_collectibles_caché_player2_img.get_size()
        statut_succès_collectibles_caché_player2_pos = [20, succès_collectibles_caché_player2_pos[1] + succès_collectibles_caché_player2_dimensions[1] + 20]


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------------BT RETOUR---------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        bt_retour = pygame.Surface((600, 100))
        bt_retour.fill("#999999")
        bt_retour_size = [600, 100]
        bt_retour_pos = [screen_size[0] / 2 - bt_retour_size[0] / 2, screen_size[1] - bt_retour_size[1] - 25]

        font_titre_bt_retour = pygame.font.Font(Technos, 50)
        titre_bt_retour_img = font_titre_bt_retour.render("Retour", True, (255, 255, 255))
        titre_bt_retour_dimensions = titre_bt_retour_img.get_size()
        titre_bt_retour_pos = [screen_size[0] / 2 - titre_bt_retour_dimensions[0] / 2, bt_retour_pos[1] + bt_retour_size[1] / 2 - titre_bt_retour_dimensions[1] / 2]


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------------BT QUITTER---------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        bt_retour2 = pygame.Surface((600, 100))
        bt_retour2.fill("#999999")
        bt_retour2_size = [600, 100]
        bt_retour2_pos = [screen_size[0] / 2 - bt_retour2_size[0] / 2, screen_size[1] - bt_retour2_size[1] - bt_retour_size[1] - 25]

        font_titre_bt_retour2 = pygame.font.Font(Technos, 35)
        titre_bt_retour2_img = font_titre_bt_retour2.render("Retour au menu", True, (255, 255, 255))
        titre_bt_retour2_dimensions = titre_bt_retour2_img.get_size()
        titre_bt_retour2_pos = [screen_size[0] / 2 - titre_bt_retour2_dimensions[0] / 2, bt_retour2_pos[1] + bt_retour2_size[1] / 2 - titre_bt_retour2_dimensions[1] / 2]


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------ORGANISATION--------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------


        sélection_joueurs = 1
        sélection_catégorie_joueur_1 = 2
        catégorie_temps_joueur_1 = 3
        catégorie_score_joueur_1 = 4
        catégorie_frôlements_joueur_1 = 5
        catégorie_collectibles_joueur_1 = 6
        sélection_catégorie_joueur_2 = 7
        catégorie_temps_joueur_2 = 8
        catégorie_score_joueur_2 = 9
        catégorie_frôlements_joueur_2 = 10
        catégorie_collectibles_joueur_2 = 11


        fenêtre_actuelle = sélection_joueurs

        mouse = pygame.mouse.get_pos()

        clique_gauche = pygame.mouse.get_pressed()[0]

        if clique_gauche :
            if mouse[0] >= bt_joueur_1_pos[0] and mouse[0] <= bt_joueur_1_pos[0] + bt_joueur_1_size[0] and mouse[1] >= bt_joueur_1_pos[1] and mouse[1] <= bt_joueur_1_pos[1] + bt_joueur_1_size[1] :
                fenêtre_actuelle = sélection_catégorie_joueur_1

            if mouse[0] >= bt_catégorie_temps_pos[0] and mouse[0] <= bt_catégorie_temps_pos[0] + bt_catégorie_temps_size[0] and mouse[1] >= bt_catégorie_temps_pos[1] and mouse[1] <= bt_catégorie_temps_pos[1] + bt_catégorie_temps_size[1] :
                fenêtre_actuelle = catégorie_temps_joueur_1

            if mouse[0] >= bt_catégorie_score_pos[0] and mouse[0] <= bt_catégorie_score_pos[0] + bt_catégorie_score_size[0] and mouse[1] >= bt_catégorie_score_pos[1] and mouse[1] <= bt_catégorie_score_pos[1] + bt_catégorie_score_size[1] :
                fenêtre_actuelle = catégorie_score_joueur_1

            if mouse[0] >= bt_catégorie_frôlements_pos[0] and mouse[0] <= bt_catégorie_frôlements_pos[0] + bt_catégorie_frôlements_size[0] and mouse[1] >= bt_catégorie_frôlements_pos[1] and mouse[1] <= bt_catégorie_frôlements_pos[1] + bt_catégorie_frôlements_size[1] :
                fenêtre_actuelle = catégorie_frôlements_joueur_1

            if mouse[0] >= bt_catégorie_collectibles_pos[0] and mouse[0] <= bt_catégorie_collectibles_pos[0] + bt_catégorie_collectibles_size[0] and mouse[1] >= bt_catégorie_collectibles_pos[1] and mouse[1] <= bt_catégorie_collectibles_pos[1] + bt_catégorie_collectibles_size[1] :
                fenêtre_actuelle = catégorie_collectibles_joueur_1


            if mouse[0] >= bt_joueur_2_pos[0] and mouse[0] <= bt_joueur_2_pos[0] + bt_joueur_2_size[0] and mouse[1] >= bt_joueur_2_pos[1] and mouse[1] <= bt_joueur_2_pos[1] + bt_joueur_2_size[1] :
                fenêtre_actuelle = sélection_catégorie_joueur_2

            if mouse[0] >= bt_catégorie_temps2_pos[0] and mouse[0] <= bt_catégorie_temps2_pos[0] + bt_catégorie_temps2_size[0] and mouse[1] >= bt_catégorie_temps2_pos[1] and mouse[1] <= bt_catégorie_temps2_pos[1] + bt_catégorie_temps2_size[1] :
                fenêtre_actuelle = catégorie_temps_joueur_2

            if mouse[0] >= bt_catégorie_score2_pos[0] and mouse[0] <= bt_catégorie_score2_pos[0] + bt_catégorie_score2_size[0] and mouse[1] >= bt_catégorie_score2_pos[1] and mouse[1] <= bt_catégorie_score2_pos[1] + bt_catégorie_score2_size[1] :
                fenêtre_actuelle = catégorie_score_joueur_2

            if mouse[0] >= bt_catégorie_frôlements2_pos[0] and mouse[0] <= bt_catégorie_frôlements2_pos[0] + bt_catégorie_frôlements2_size[0] and mouse[1] >= bt_catégorie_frôlements2_pos[1] and mouse[1] <= bt_catégorie_frôlements2_pos[1] + bt_catégorie_frôlements2_size[1] :
                fenêtre_actuelle = catégorie_frôlements_joueur_2

            if mouse[0] >= bt_catégorie_collectibles2_pos[0] and mouse[0] <= bt_catégorie_collectibles2_pos[0] + bt_catégorie_collectibles2_size[0] and mouse[1] >= bt_catégorie_collectibles2_pos[1] and mouse[1] <= bt_catégorie_collectibles2_pos[1] + bt_catégorie_collectibles2_size[1] :
                fenêtre_actuelle = catégorie_collectibles_joueur_2

            if mouse[0] >= bt_retour_pos[0] and mouse[0] <= bt_retour_pos[0] + bt_retour_size[0] and mouse[1] >= bt_retour_pos[1] and mouse[1] <= bt_retour_pos[1] + bt_retour_size[1] :
                fenêtre_actuelle = sélection_joueurs


            if mouse[0] >= bt_retour2_pos[0] and mouse[0] <= bt_retour2_pos[0] + bt_retour2_size[0] and mouse[1] >= bt_retour2_pos[1] and mouse[1] <= bt_retour2_pos[1] + bt_retour2_size[1] :
                mode_actuel = MODE_ACCUEIL

            if fenêtre_actuelle == sélection_joueurs :
                screen.fill("#0B041F")
                screen.blit(titre_menu_succès_img, titre_menu_succès_pos)
                screen.blit(bt_joueur_1, bt_joueur_1_pos)
                screen.blit(titre_bt_joueur_1_img, titre_bt_joueur_1_pos)
                screen.blit(bt_joueur_2, bt_joueur_2_pos)
                screen.blit(titre_bt_joueur_2_img, titre_bt_joueur_2_pos)
                screen.blit(bt_retour2, bt_retour2_pos)
                screen.blit(titre_bt_retour2_img, titre_bt_retour2_pos)

            if fenêtre_actuelle == sélection_catégorie_joueur_1 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_succès_img, titre_menu_succès_pos)
                screen.blit(_titre_bt_joueur_1_img, _titre_bt_joueur_1_pos)
                screen.blit(bt_catégorie_temps, bt_catégorie_temps_pos)
                screen.blit(titre_bt_catégorie_temps_img, titre_bt_catégorie_temps_pos)
                screen.blit(bt_catégorie_score, bt_catégorie_score_pos)
                screen.blit(titre_bt_catégorie_score_img, titre_bt_catégorie_score_pos)
                screen.blit(bt_catégorie_frôlements, bt_catégorie_frôlements_pos)
                screen.blit(titre_bt_catégorie_frôlements_img, titre_bt_catégorie_frôlements_pos)
                screen.blit(bt_catégorie_collectibles, bt_catégorie_collectibles_pos)
                screen.blit(titre_bt_catégorie_collectibles_img, titre_bt_catégorie_collectibles_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == catégorie_temps_joueur_1 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_succès_img, titre_menu_succès_pos)
                screen.blit(_titre_bt_joueur_1_img, _titre_bt_joueur_1_pos)
                screen.blit(bt_catégorie_temps, bt_catégorie_temps_pos)
                screen.blit(titre_bt_catégorie_temps_img, titre_bt_catégorie_temps_pos)
                screen.blit(bt_catégorie_score, bt_catégorie_score_pos)
                screen.blit(titre_bt_catégorie_score_img, titre_bt_catégorie_score_pos)
                screen.blit(bt_catégorie_frôlements, bt_catégorie_frôlements_pos)
                screen.blit(titre_bt_catégorie_frôlements_img, titre_bt_catégorie_frôlements_pos)
                screen.blit(bt_catégorie_collectibles, bt_catégorie_collectibles_pos)
                screen.blit(titre_bt_catégorie_collectibles_img, titre_bt_catégorie_collectibles_pos)
                screen.blit(succès_temps_1_player_img, succès_temps_1_player_pos)
                screen.blit(statut_succès_temps_1_player_img, statut_succès_temps_1_player_pos)
                screen.blit(succès_temps_2_player_img, succès_temps_2_player_pos)
                screen.blit(statut_succès_temps_2_player_img, statut_succès_temps_2_player_pos)
                if succès_temps_caché_player :
                    screen.blit(succès_temps_caché_player_img, succès_temps_caché_player_pos)
                    screen.blit(statut_succès_temps_caché_player_img, statut_succès_temps_caché_player_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == catégorie_score_joueur_1 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_succès_img, titre_menu_succès_pos)
                screen.blit(_titre_bt_joueur_1_img, _titre_bt_joueur_1_pos)
                screen.blit(bt_catégorie_temps, bt_catégorie_temps_pos)
                screen.blit(titre_bt_catégorie_temps_img, titre_bt_catégorie_temps_pos)
                screen.blit(bt_catégorie_score, bt_catégorie_score_pos)
                screen.blit(titre_bt_catégorie_score_img, titre_bt_catégorie_score_pos)
                screen.blit(bt_catégorie_frôlements, bt_catégorie_frôlements_pos)
                screen.blit(titre_bt_catégorie_frôlements_img, titre_bt_catégorie_frôlements_pos)
                screen.blit(bt_catégorie_collectibles, bt_catégorie_collectibles_pos)
                screen.blit(titre_bt_catégorie_collectibles_img, titre_bt_catégorie_collectibles_pos)
                screen.blit(succès_score_1_player_img, succès_score_1_player_pos)
                screen.blit(statut_succès_score_1_player_img, statut_succès_score_1_player_pos)
                screen.blit(succès_score_2_player_img, succès_score_2_player_pos)
                screen.blit(statut_succès_score_2_player_img, statut_succès_score_2_player_pos)
                if succès_score_caché_player :
                    screen.blit(succès_score_caché_player_img, succès_score_caché_player_pos)
                    screen.blit(statut_succès_score_caché_player_img, statut_succès_score_caché_player_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == catégorie_frôlements_joueur_1 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_succès_img, titre_menu_succès_pos)
                screen.blit(_titre_bt_joueur_1_img, _titre_bt_joueur_1_pos)
                screen.blit(bt_catégorie_temps, bt_catégorie_temps_pos)
                screen.blit(titre_bt_catégorie_temps_img, titre_bt_catégorie_temps_pos)
                screen.blit(bt_catégorie_score, bt_catégorie_score_pos)
                screen.blit(titre_bt_catégorie_score_img, titre_bt_catégorie_score_pos)
                screen.blit(bt_catégorie_frôlements, bt_catégorie_frôlements_pos)
                screen.blit(titre_bt_catégorie_frôlements_img, titre_bt_catégorie_frôlements_pos)
                screen.blit(bt_catégorie_collectibles, bt_catégorie_collectibles_pos)
                screen.blit(titre_bt_catégorie_collectibles_img, titre_bt_catégorie_collectibles_pos)
                screen.blit(succès_frôlements_1_player_img, succès_frôlements_1_player_pos)
                screen.blit(statut_succès_frôlements_1_player_img, statut_succès_frôlements_1_player_pos)
                screen.blit(succès_frôlements_2_player_img, succès_frôlements_2_player_pos)
                screen.blit(statut_succès_frôlements_2_player_img, statut_succès_frôlements_2_player_pos)
                if succès_frôlements_caché_player :
                    screen.blit(succès_frôlements_caché_player_img, succès_frôlements_caché_player_pos)
                    screen.blit(statut_succès_frôlements_caché_player_img, statut_succès_frôlements_caché_player_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == catégorie_collectibles_joueur_1 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_succès_img, titre_menu_succès_pos)
                screen.blit(_titre_bt_joueur_1_img, _titre_bt_joueur_1_pos)
                screen.blit(bt_catégorie_temps, bt_catégorie_temps_pos)
                screen.blit(titre_bt_catégorie_temps_img, titre_bt_catégorie_temps_pos)
                screen.blit(bt_catégorie_score, bt_catégorie_score_pos)
                screen.blit(titre_bt_catégorie_score_img, titre_bt_catégorie_score_pos)
                screen.blit(bt_catégorie_frôlements, bt_catégorie_frôlements_pos)
                screen.blit(titre_bt_catégorie_frôlements_img, titre_bt_catégorie_frôlements_pos)
                screen.blit(bt_catégorie_collectibles, bt_catégorie_collectibles_pos)
                screen.blit(titre_bt_catégorie_collectibles_img, titre_bt_catégorie_collectibles_pos)
                screen.blit(succès_collectibles_1_player_img, succès_collectibles_1_player_pos)
                screen.blit(statut_succès_collectibles_1_player_img, statut_succès_collectibles_1_player_pos)
                screen.blit(succès_collectibles_2_player_img, succès_collectibles_2_player_pos)
                screen.blit(statut_succès_collectibles_2_player_img, statut_succès_collectibles_2_player_pos)
                if succès_collectibles_caché_player :
                    screen.blit(succès_collectibles_caché_player_img, succès_collectibles_caché_player_pos)
                    screen.blit(statut_succès_collectibles_caché_player_img, statut_succès_collectibles_caché_player_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == sélection_catégorie_joueur_2 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_succès_img, titre_menu_succès_pos)
                screen.blit(_titre_bt_joueur_2_img, _titre_bt_joueur_2_pos)
                screen.blit(bt_catégorie_temps2, bt_catégorie_temps2_pos)
                screen.blit(titre_bt_catégorie_temps2_img, titre_bt_catégorie_temps2_pos)
                screen.blit(bt_catégorie_score2, bt_catégorie_score2_pos)
                screen.blit(titre_bt_catégorie_score2_img, titre_bt_catégorie_score2_pos)
                screen.blit(bt_catégorie_frôlements2, bt_catégorie_frôlements2_pos)
                screen.blit(titre_bt_catégorie_frôlements2_img, titre_bt_catégorie_frôlements2_pos)
                screen.blit(bt_catégorie_collectibles2, bt_catégorie_collectibles2_pos)
                screen.blit(titre_bt_catégorie_collectibles2_img, titre_bt_catégorie_collectibles2_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == catégorie_temps_joueur_2 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_succès_img, titre_menu_succès_pos)
                screen.blit(_titre_bt_joueur_2_img, _titre_bt_joueur_2_pos)
                screen.blit(bt_catégorie_temps2, bt_catégorie_temps2_pos)
                screen.blit(titre_bt_catégorie_temps2_img, titre_bt_catégorie_temps2_pos)
                screen.blit(bt_catégorie_score2, bt_catégorie_score2_pos)
                screen.blit(titre_bt_catégorie_score2_img, titre_bt_catégorie_score2_pos)
                screen.blit(bt_catégorie_frôlements2, bt_catégorie_frôlements2_pos)
                screen.blit(titre_bt_catégorie_frôlements2_img, titre_bt_catégorie_frôlements2_pos)
                screen.blit(bt_catégorie_collectibles2, bt_catégorie_collectibles2_pos)
                screen.blit(titre_bt_catégorie_collectibles2_img, titre_bt_catégorie_collectibles2_pos)
                screen.blit(succès_temps_1_player2_img, succès_temps_1_player2_pos)
                screen.blit(statut_succès_temps_1_player2_img, statut_succès_temps_1_player2_pos)
                screen.blit(succès_temps_2_player2_img, succès_temps_2_player2_pos)
                screen.blit(statut_succès_temps_2_player2_img, statut_succès_temps_2_player2_pos)
                if succès_temps_caché_player_2 :
                    screen.blit(succès_temps_caché_player2_img, succès_temps_caché_player2_pos)
                    screen.blit(statut_succès_temps_caché_player2_img, statut_succès_temps_caché_player2_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == catégorie_score_joueur_2 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_succès_img, titre_menu_succès_pos)
                screen.blit(_titre_bt_joueur_2_img, _titre_bt_joueur_2_pos)
                screen.blit(bt_catégorie_temps2, bt_catégorie_temps2_pos)
                screen.blit(titre_bt_catégorie_temps2_img, titre_bt_catégorie_temps2_pos)
                screen.blit(bt_catégorie_score2, bt_catégorie_score2_pos)
                screen.blit(titre_bt_catégorie_score2_img, titre_bt_catégorie_score2_pos)
                screen.blit(bt_catégorie_frôlements2, bt_catégorie_frôlements2_pos)
                screen.blit(titre_bt_catégorie_frôlements2_img, titre_bt_catégorie_frôlements2_pos)
                screen.blit(bt_catégorie_collectibles2, bt_catégorie_collectibles2_pos)
                screen.blit(titre_bt_catégorie_collectibles2_img, titre_bt_catégorie_collectibles2_pos)
                screen.blit(succès_score_1_player2_img, succès_score_1_player2_pos)
                screen.blit(statut_succès_score_1_player2_img, statut_succès_score_1_player2_pos)
                screen.blit(succès_score_2_player2_img, succès_score_2_player2_pos)
                screen.blit(statut_succès_score_2_player2_img, statut_succès_score_2_player2_pos)
                if succès_score_caché_player_2 :
                    screen.blit(succès_score_caché_player2_img, succès_score_caché_player2_pos)
                    screen.blit(statut_succès_score_caché_player2_img, statut_succès_score_caché_player2_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == catégorie_frôlements_joueur_2 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_succès_img, titre_menu_succès_pos)
                screen.blit(_titre_bt_joueur_2_img, _titre_bt_joueur_2_pos)
                screen.blit(bt_catégorie_temps2, bt_catégorie_temps2_pos)
                screen.blit(titre_bt_catégorie_temps2_img, titre_bt_catégorie_temps2_pos)
                screen.blit(bt_catégorie_score2, bt_catégorie_score2_pos)
                screen.blit(titre_bt_catégorie_score2_img, titre_bt_catégorie_score2_pos)
                screen.blit(bt_catégorie_frôlements2, bt_catégorie_frôlements2_pos)
                screen.blit(titre_bt_catégorie_frôlements2_img, titre_bt_catégorie_frôlements2_pos)
                screen.blit(bt_catégorie_collectibles2, bt_catégorie_collectibles2_pos)
                screen.blit(titre_bt_catégorie_collectibles2_img, titre_bt_catégorie_collectibles2_pos)
                screen.blit(succès_frôlements_1_player2_img, succès_frôlements_1_player2_pos)
                screen.blit(statut_succès_frôlements_1_player2_img, statut_succès_frôlements_1_player2_pos)
                screen.blit(succès_frôlements_2_player2_img, succès_frôlements_2_player2_pos)
                screen.blit(statut_succès_frôlements_2_player2_img, statut_succès_frôlements_2_player2_pos)
                if succès_frôlements_caché_player_2 :
                    screen.blit(succès_frôlements_caché_player2_img, succès_frôlements_caché_player2_pos)
                    screen.blit(statut_succès_frôlements_caché_player2_img, statut_succès_frôlements_caché_player2_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == catégorie_collectibles_joueur_2 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_succès_img, titre_menu_succès_pos)
                screen.blit(_titre_bt_joueur_2_img, _titre_bt_joueur_2_pos)
                screen.blit(bt_catégorie_temps2, bt_catégorie_temps2_pos)
                screen.blit(titre_bt_catégorie_temps2_img, titre_bt_catégorie_temps2_pos)
                screen.blit(bt_catégorie_score2, bt_catégorie_score2_pos)
                screen.blit(titre_bt_catégorie_score2_img, titre_bt_catégorie_score2_pos)
                screen.blit(bt_catégorie_frôlements2, bt_catégorie_frôlements2_pos)
                screen.blit(titre_bt_catégorie_frôlements2_img, titre_bt_catégorie_frôlements2_pos)
                screen.blit(bt_catégorie_collectibles2, bt_catégorie_collectibles2_pos)
                screen.blit(titre_bt_catégorie_collectibles2_img, titre_bt_catégorie_collectibles2_pos)
                screen.blit(succès_collectibles_1_player2_img, succès_collectibles_1_player2_pos)
                screen.blit(statut_succès_collectibles_1_player2_img, statut_succès_collectibles_1_player2_pos)
                screen.blit(succès_collectibles_2_player2_img, succès_collectibles_2_player2_pos)
                screen.blit(statut_succès_collectibles_2_player2_img, statut_succès_collectibles_2_player2_pos)
                if succès_collectibles_caché_player_2 :
                    screen.blit(succès_collectibles_caché_player2_img, succès_collectibles_caché_player2_pos)
                    screen.blit(statut_succès_collectibles_caché_player2_img, statut_succès_collectibles_caché_player2_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)



    if mode_actuel == MODE_I_MEMES :
        #---------------------------------------------------------------------------TITRE---------------------------------------------------------------------------

        font_titre_menu_i_memes = pygame.font.Font(Technos, 75)
        titre_menu_i_memes_img = font_titre_menu_i_memes.render("Menu des I-Memes", True, (255, 255, 255))
        titre_menu_i_memes_dimensions = titre_menu_i_memes_img.get_size()
        titre_menu_i_memes_pos = [screen_size[0] / 2 - titre_menu_i_memes_dimensions[0] / 2, 50]

        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------Joueur 1------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        bt_joueur_1 = pygame.Surface((550, 200))
        bt_joueur_1.fill("#999999")
        bt_joueur_1_size = [550, 200]
        bt_joueur_1_pos = [screen_size[0] / 4 - bt_joueur_1_size[0] / 2, screen_size[1] / 2 - bt_joueur_1_size[1] / 2]
 
        font_titre_bt_joueur_1 = pygame.font.Font(Technos, 60)
        titre_bt_joueur_1_img = font_titre_bt_joueur_1.render("Joueur 1", True, (255, 255, 255))
        titre_bt_joueur_1_dimensions = titre_bt_joueur_1_img.get_size()
        titre_bt_joueur_1_pos = [bt_joueur_1_pos[0] + bt_joueur_1_size[0] / 2 - titre_bt_joueur_1_dimensions[0] / 2, bt_joueur_1_pos[1] + bt_joueur_1_size[1] / 2 - titre_bt_joueur_1_dimensions[1] / 2]

        #--------------------------------------------------------------------------RARE----------------------------------------------------------------------------

        font__titre_bt_joueur_1 = pygame.font.Font(Technos, 45)
        _titre_bt_joueur_1_img = font__titre_bt_joueur_1.render("Joueur 1", True, (255, 255, 255))
        _titre_bt_joueur_1_dimensions = _titre_bt_joueur_1_img.get_size()
        _titre_bt_joueur_1_pos = [screen_size[0] / 2 - _titre_bt_joueur_1_dimensions[0] / 2, titre_menu_i_memes_pos[1] + titre_menu_i_memes_dimensions[1] + 10]


        bt_rareté_rare = pygame.Surface((300, 50))
        bt_rareté_rare.fill("#999999")
        bt_rareté_rare_size = [300, 50]
        bt_rareté_rare_pos = [screen_size[0] / 2 - 470, titre_menu_i_memes_pos[1] + titre_menu_i_memes_dimensions[1] + 75]
  
        font_titre_bt_rareté_rare = pygame.font.Font(Technos, 25)
        titre_bt_rareté_rare_img = font_titre_bt_rareté_rare.render("Rare", True, (255, 255, 255))
        titre_bt_rareté_rare_dimensions = titre_bt_rareté_rare_img.get_size()
        titre_bt_rareté_rare_pos = [bt_rareté_rare_pos[0] + bt_rareté_rare_size[0] / 2 - titre_bt_rareté_rare_dimensions[0] / 2, bt_rareté_rare_pos[1] + bt_rareté_rare_size[1] / 2 - titre_bt_rareté_rare_dimensions[1] / 2]


        font_red_bull_player = pygame.font.Font(Arcade, 35)
        red_bull_player_img = font_red_bull_player.render("Red Bull : Confere une acceleration temporaire de 5 secondes", True, (255, 255, 255))
        red_bull_player_dimensions = red_bull_player_img.get_size()
        red_bull_player_pos = [20, bt_rareté_rare_pos[1] + bt_rareté_rare_size[1] + 35]

        statut_red_bull_player = pygame.Surface((175, 25))
        statut_red_bull_player.fill("#999999")
        statut_red_bull_player_size = [175, 25]
        statut_red_bull_player_pos = [20, red_bull_player_pos[1] + red_bull_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 1 :
            titre_Statut_red_bull_player = "Statut : Equipe"
        elif succès_temps_1_player :
            titre_Statut_red_bull_player = "Statut : Possede"
        else :
            titre_Statut_red_bull_player = "Statut : Non possede"
        font_titre_statut_red_bull_player = pygame.font.Font(Arcade, 15)
        titre_statut_red_bull_player_img = font_titre_statut_red_bull_player.render(titre_Statut_red_bull_player, True, (255, 255, 255))
        titre_statut_red_bull_player_dimensions = titre_statut_red_bull_player_img.get_size()
        titre_statut_red_bull_player_pos = [statut_red_bull_player_pos[0] + statut_red_bull_player_size[0] / 2 - titre_statut_red_bull_player_dimensions[0] / 2, statut_red_bull_player_pos[1] + statut_red_bull_player_size[1] / 2 - titre_statut_red_bull_player_dimensions[1] / 2]

        font_disparition_player = pygame.font.Font(Arcade, 35)
        disparition_player_img = font_disparition_player.render("Disparition : Rend invisible et intangible pendant 5 secondes", True, (255, 255, 255))
        disparition_player_dimensions = disparition_player_img.get_size()
        disparition_player_pos = [20, statut_red_bull_player_pos[1] + statut_red_bull_player_size[1] + 35]

        statut_disparition_player = pygame.Surface((175, 25))
        statut_disparition_player.fill("#999999")
        statut_disparition_player_size = [175, 25]
        statut_disparition_player_pos = [20, disparition_player_pos[1] + disparition_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 2 :
            titre_Statut_disparition_player = "Statut : Equipe"
        elif succès_score_1_player :
            titre_Statut_disparition_player = "Statut : Possede"
        else :
            titre_Statut_disparition_player = "Statut : Non possede"
        font_titre_statut_disparition_player = pygame.font.Font(Arcade, 15)
        titre_statut_disparition_player_img = font_titre_statut_disparition_player.render(titre_Statut_disparition_player, True, (255, 255, 255))
        titre_statut_disparition_player_dimensions = titre_statut_disparition_player_img.get_size()
        titre_statut_disparition_player_pos = [statut_disparition_player_pos[0] + statut_disparition_player_size[0] / 2 - titre_statut_disparition_player_dimensions[0] / 2, statut_disparition_player_pos[1] + statut_disparition_player_size[1] / 2 - titre_statut_disparition_player_dimensions[1] / 2]

        font_jackpot_player = pygame.font.Font(Arcade, 35)
        jackpot_player_img = font_jackpot_player.render("Jackpot (Passif) : Double votre score final en fin de partie", True, (255, 255, 255))
        jackpot_player_dimensions = jackpot_player_img.get_size()
        jackpot_player_pos = [20, statut_disparition_player_pos[1] + statut_disparition_player_size[1] + 35]

        statut_jackpot_player = pygame.Surface((175, 25))
        statut_jackpot_player.fill("#999999")
        statut_jackpot_player_size = [175, 25]
        statut_jackpot_player_pos = [20, jackpot_player_pos[1] + jackpot_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 3 :
            titre_Statut_jackpot_player = "Statut : Equipe"
        elif succès_frôlements_1_player :
            titre_Statut_jackpot_player = "Statut : Possede"
        else :
            titre_Statut_jackpot_player = "Statut : Non possede"
        font_titre_statut_jackpot_player = pygame.font.Font(Arcade, 15)
        titre_statut_jackpot_player_img = font_titre_statut_jackpot_player.render(titre_Statut_jackpot_player, True, (255, 255, 255))
        titre_statut_jackpot_player_dimensions = titre_statut_jackpot_player_img.get_size()
        titre_statut_jackpot_player_pos = [statut_jackpot_player_pos[0] + statut_jackpot_player_size[0] / 2 - titre_statut_jackpot_player_dimensions[0] / 2, statut_jackpot_player_pos[1] + statut_jackpot_player_size[1] / 2 - titre_statut_jackpot_player_dimensions[1] / 2]

        font_devil_never_cry_player = pygame.font.Font(Arcade, 35)
        devil_never_cry_player_img = font_devil_never_cry_player.render("Devil Never Cry (Passif) : Ressuscite 1 fois", True, (255, 255, 255))
        devil_never_cry_player_dimensions = devil_never_cry_player_img.get_size()
        devil_never_cry_player_pos = [20, statut_jackpot_player_pos[1] + statut_jackpot_player_size[1] + 35]

        statut_devil_never_cry_player = pygame.Surface((175, 25))
        statut_devil_never_cry_player.fill("#999999")
        statut_devil_never_cry_player_size = [175, 25]
        statut_devil_never_cry_player_pos = [20, devil_never_cry_player_pos[1] + devil_never_cry_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 4 :
            titre_Statut_devil_never_cry_player = "Statut : Equipe"
        elif succès_collectibles_1_player :
            titre_Statut_devil_never_cry_player = "Statut : Possede"
        else :
            titre_Statut_devil_never_cry_player = "Statut : Non possede"
        font_titre_statut_devil_never_cry_player = pygame.font.Font(Arcade, 15)
        titre_statut_devil_never_cry_player_img = font_titre_statut_devil_never_cry_player.render(titre_Statut_devil_never_cry_player, True, (255, 255, 255))
        titre_statut_devil_never_cry_player_dimensions = titre_statut_devil_never_cry_player_img.get_size()
        titre_statut_devil_never_cry_player_pos = [statut_devil_never_cry_player_pos[0] + statut_devil_never_cry_player_size[0] / 2 - titre_statut_devil_never_cry_player_dimensions[0] / 2, statut_devil_never_cry_player_pos[1] + statut_devil_never_cry_player_size[1] / 2 - titre_statut_devil_never_cry_player_dimensions[1] / 2]

        #-------------------------------------------------------------------------EPIQUE-----------------------------------------------------------------------------

        bt_rareté_épique = pygame.Surface((300, 50))
        bt_rareté_épique.fill("#999999")
        bt_rareté_épique_size = [300, 50]
        bt_rareté_épique_pos = [screen_size[0] / 2 - bt_rareté_épique_size[0] / 2, titre_menu_i_memes_pos[1] + titre_menu_i_memes_dimensions[1] + 75]

        font_titre_bt_rareté_épique = pygame.font.Font(Technos, 25)
        titre_bt_rareté_épique_img = font_titre_bt_rareté_épique.render("Epique", True, (255, 255, 255))
        titre_bt_rareté_épique_dimensions = titre_bt_rareté_épique_img.get_size()
        titre_bt_rareté_épique_pos = [bt_rareté_épique_pos[0] + bt_rareté_épique_size[0] / 2 - titre_bt_rareté_épique_dimensions[0] / 2, bt_rareté_épique_pos[1] + bt_rareté_épique_size[1] / 2 - titre_bt_rareté_épique_dimensions[1] / 2]


        font_hyperdrive_player = pygame.font.Font(Arcade, 35)
        hyperdrive_player_img = font_hyperdrive_player.render("Hyperdrive : Propulse a l'autre bout de la grille dans la direction actuelle", True, (255, 255, 255))
        hyperdrive_player_dimensions = hyperdrive_player_img.get_size()
        hyperdrive_player_pos = [20, bt_rareté_épique_pos[1] + bt_rareté_épique_size[1] + 35]

        statut_hyperdrive_player = pygame.Surface((175, 25))
        statut_hyperdrive_player.fill("#999999")
        statut_hyperdrive_player_size = [175, 25]
        statut_hyperdrive_player_pos = [20, hyperdrive_player_pos[1] + hyperdrive_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 5 :
            titre_Statut_hyperdrive_player = "Statut : Equipe"
        elif succès_temps_2_player :
            titre_Statut_hyperdrive_player = "Statut : Possede"
        else :
            titre_Statut_hyperdrive_player = "Statut : Non possede"
        font_titre_statut_hyperdrive_player = pygame.font.Font(Arcade, 15)
        titre_statut_hyperdrive_player_img = font_titre_statut_hyperdrive_player.render(titre_Statut_hyperdrive_player, True, (255, 255, 255))
        titre_statut_hyperdrive_player_dimensions = titre_statut_hyperdrive_player_img.get_size()
        titre_statut_hyperdrive_player_pos = [statut_hyperdrive_player_pos[0] + statut_hyperdrive_player_size[0] / 2 - titre_statut_hyperdrive_player_dimensions[0] / 2, statut_hyperdrive_player_pos[1] + statut_hyperdrive_player_size[1] / 2 - titre_statut_hyperdrive_player_dimensions[1] / 2]

        font_nope_player = pygame.font.Font(Arcade, 35)
        nope_player_img = font_nope_player.render("Nope (usage unique) : Contre l'effet nefaste d'un I-Meme adverse", True, (255, 255, 255))
        nope_player_dimensions = nope_player_img.get_size()
        nope_player_pos = [20, statut_hyperdrive_player_pos[1] + statut_hyperdrive_player_size[1] + 35]

        statut_nope_player = pygame.Surface((175, 25))
        statut_nope_player.fill("#999999")
        statut_nope_player_size = [175, 25]
        statut_nope_player_pos = [20, nope_player_pos[1] + nope_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 6 :
            titre_Statut_nope_player = "Statut : Equipe"
        elif succès_score_2_player :
            titre_Statut_nope_player = "Statut : Possede"
        else :
            titre_Statut_nope_player = "Statut : Non possede"
        font_titre_statut_nope_player = pygame.font.Font(Arcade, 15)
        titre_statut_nope_player_img = font_titre_statut_nope_player.render(titre_Statut_nope_player, True, (255, 255, 255))
        titre_statut_nope_player_dimensions = titre_statut_nope_player_img.get_size()
        titre_statut_nope_player_pos = [statut_nope_player_pos[0] + statut_nope_player_size[0] / 2 - titre_statut_nope_player_dimensions[0] / 2, statut_nope_player_pos[1] + statut_nope_player_size[1] / 2 - titre_statut_nope_player_dimensions[1] / 2]

        font_gandalf_player = pygame.font.Font(Arcade, 35)
        gandalf_player_img = font_gandalf_player.render("Gandalf : Erige un mur en face de l'adversaire", True, (255, 255, 255))
        gandalf_player_dimensions = gandalf_player_img.get_size()
        gandalf_player_pos = [20, statut_nope_player_pos[1] + statut_nope_player_size[1] + 35]

        statut_gandalf_player = pygame.Surface((175, 25))
        statut_gandalf_player.fill("#999999")
        statut_gandalf_player_size = [175, 25]
        statut_gandalf_player_pos = [20, gandalf_player_pos[1] + gandalf_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 7 :
            titre_Statut_gandalf_player = "Statut : Equipe"
        elif succès_frôlements_2_player :
            titre_Statut_gandalf_player = "Statut : Possede"
        else :
            titre_Statut_gandalf_player = "Statut : Non possede"
        font_titre_statut_gandalf_player = pygame.font.Font(Arcade, 15)
        titre_statut_gandalf_player_img = font_titre_statut_gandalf_player.render(titre_Statut_gandalf_player, True, (255, 255, 255))
        titre_statut_gandalf_player_dimensions = titre_statut_gandalf_player_img.get_size()
        titre_statut_gandalf_player_pos = [statut_gandalf_player_pos[0] + statut_gandalf_player_size[0] / 2 - titre_statut_gandalf_player_dimensions[0] / 2, statut_gandalf_player_pos[1] + statut_gandalf_player_size[1] / 2 - titre_statut_gandalf_player_dimensions[1] / 2]

        font_death_star_player = pygame.font.Font(Arcade, 35)
        death_star_player_img = font_death_star_player.render("Death Star : Tire un rayon laser dans la direction actuelle", True, (255, 255, 255))
        death_star_player_dimensions = death_star_player_img.get_size()
        death_star_player_pos = [20, statut_gandalf_player_pos[1] + statut_gandalf_player_size[1] + 35]

        statut_death_star_player = pygame.Surface((175, 25))
        statut_death_star_player.fill("#999999")
        statut_death_star_player_size = [175, 25]
        statut_death_star_player_pos = [20, death_star_player_pos[1] + death_star_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 8 :
            titre_Statut_death_star_player = "Statut : Equipe"
        elif succès_collectibles_2_player :
            titre_Statut_death_star_player = "Statut : Possede"
        else :
            titre_Statut_death_star_player = "Statut : Non possede"
        font_titre_statut_death_star_player = pygame.font.Font(Arcade, 15)
        titre_statut_death_star_player_img = font_titre_statut_death_star_player.render(titre_Statut_death_star_player, True, (255, 255, 255))
        titre_statut_death_star_player_dimensions = titre_statut_death_star_player_img.get_size()
        titre_statut_death_star_player_pos = [statut_death_star_player_pos[0] + statut_death_star_player_size[0] / 2 - titre_statut_death_star_player_dimensions[0] / 2, statut_death_star_player_pos[1] + statut_death_star_player_size[1] / 2 - titre_statut_death_star_player_dimensions[1] / 2]

        #----------------------------------------------------------------------LEGENDAIRE---------------------------------------------------------------------------

        bt_rareté_légendaire = pygame.Surface((300, 50))
        bt_rareté_légendaire.fill("#999999")
        bt_rareté_légendaire_size = [300, 50]
        bt_rareté_légendaire_pos = [bt_rareté_épique_pos[0] + bt_rareté_épique_size[0] + 20, titre_menu_i_memes_pos[1] + titre_menu_i_memes_dimensions[1] + 75]

        font_titre_bt_rareté_légendaire = pygame.font.Font(Technos, 25)
        titre_bt_rareté_légendaire_img = font_titre_bt_rareté_légendaire.render("Legendaire", True, (255, 255, 255))
        titre_bt_rareté_légendaire_dimensions = titre_bt_rareté_légendaire_img.get_size()
        titre_bt_rareté_légendaire_pos = [bt_rareté_légendaire_pos[0] + bt_rareté_légendaire_size[0] / 2 - titre_bt_rareté_légendaire_dimensions[0] / 2, bt_rareté_légendaire_pos[1] + bt_rareté_légendaire_size[1] / 2 - titre_bt_rareté_légendaire_dimensions[1] / 2]


        font_thanos_player = pygame.font.Font(Arcade, 35)
        thanos_player_img = font_thanos_player.render("Thanos : Fais disparaitre toutes les trainees de la grille", True, (255, 255, 255))
        thanos_player_dimensions = thanos_player_img.get_size()
        thanos_player_pos = [20, bt_rareté_légendaire_pos[1] + bt_rareté_légendaire_size[1] + 35]

        statut_thanos_player = pygame.Surface((175, 25))
        statut_thanos_player.fill("#999999")
        statut_thanos_player_size = [175, 25]
        statut_thanos_player_pos = [20, thanos_player_pos[1] + thanos_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 9 :
            titre_Statut_thanos_player = "Statut : Equipe"
        elif succès_temps_caché_player :
            titre_Statut_thanos_player = "Statut : Possede"
        else :
            titre_Statut_thanos_player = "Statut : Non possede"
        font_titre_statut_thanos_player = pygame.font.Font(Arcade, 15)
        titre_statut_thanos_player_img = font_titre_statut_thanos_player.render(titre_Statut_thanos_player, True, (255, 255, 255))
        titre_statut_thanos_player_dimensions = titre_statut_thanos_player_img.get_size()
        titre_statut_thanos_player_pos = [statut_thanos_player_pos[0] + statut_thanos_player_size[0] / 2 - titre_statut_thanos_player_dimensions[0] / 2, statut_thanos_player_pos[1] + statut_thanos_player_size[1] / 2 - titre_statut_thanos_player_dimensions[1] / 2]

        font_c_est_quoi_ce_monde_player = pygame.font.Font(Arcade, 35)
        c_est_quoi_ce_monde_player_img = font_c_est_quoi_ce_monde_player.render("C'est quoi ce monde ? : Inverse les touches de l'adversaire pendant 5 secondes", True, (255, 255, 255))
        c_est_quoi_ce_monde_player_dimensions = c_est_quoi_ce_monde_player_img.get_size()
        c_est_quoi_ce_monde_player_pos = [20, statut_thanos_player_pos[1] + statut_thanos_player_size[1] + 35]

        statut_c_est_quoi_ce_monde_player = pygame.Surface((175, 25))
        statut_c_est_quoi_ce_monde_player.fill("#999999")
        statut_c_est_quoi_ce_monde_player_size = [175, 25]
        statut_c_est_quoi_ce_monde_player_pos = [20, c_est_quoi_ce_monde_player_pos[1] + c_est_quoi_ce_monde_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 10 :
            titre_Statut_c_est_quoi_ce_monde_player = "Statut : Equipe"
        elif succès_score_caché_player :
            titre_Statut_c_est_quoi_ce_monde_player = "Statut : Possede"
        else :
            titre_Statut_c_est_quoi_ce_monde_player = "Statut : Non possede"
        font_titre_statut_c_est_quoi_ce_monde_player = pygame.font.Font(Arcade, 15)
        titre_statut_c_est_quoi_ce_monde_player_img = font_titre_statut_c_est_quoi_ce_monde_player.render(titre_Statut_c_est_quoi_ce_monde_player, True, (255, 255, 255))
        titre_statut_c_est_quoi_ce_monde_player_dimensions = titre_statut_c_est_quoi_ce_monde_player_img.get_size()
        titre_statut_c_est_quoi_ce_monde_player_pos = [statut_c_est_quoi_ce_monde_player_pos[0] + statut_c_est_quoi_ce_monde_player_size[0] / 2 - titre_statut_c_est_quoi_ce_monde_player_dimensions[0] / 2, statut_c_est_quoi_ce_monde_player_pos[1] + statut_c_est_quoi_ce_monde_player_size[1] / 2 - titre_statut_c_est_quoi_ce_monde_player_dimensions[1] / 2]

        font_virtual_insanity_player = pygame.font.Font(Arcade, 35)
        virtual_insanity_player_img = font_virtual_insanity_player.render("Virtual Insanity : L'adversaire ne peut plus se diriger et est ralentit pendant 5 secondes", True, (255, 255, 255))
        virtual_insanity_player_dimensions = virtual_insanity_player_img.get_size()
        virtual_insanity_player_pos = [20, statut_c_est_quoi_ce_monde_player_pos[1] + statut_c_est_quoi_ce_monde_player_size[1] + 35]

        statut_virtual_insanity_player = pygame.Surface((175, 25))
        statut_virtual_insanity_player.fill("#999999")
        statut_virtual_insanity_player_size = [175, 25]
        statut_virtual_insanity_player_pos = [20, virtual_insanity_player_pos[1] + virtual_insanity_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 11 :
            titre_Statut_virtual_insanity_player = "Statut : Equipe"
        elif succès_frôlements_caché_player :
            titre_Statut_virtual_insanity_player = "Statut : Possede"
        else :
            titre_Statut_virtual_insanity_player = "Statut : Non possede"
        font_titre_statut_virtual_insanity_player = pygame.font.Font(Arcade, 15)
        titre_statut_virtual_insanity_player_img = font_titre_statut_virtual_insanity_player.render(titre_Statut_virtual_insanity_player, True, (255, 255, 255))
        titre_statut_virtual_insanity_player_dimensions = titre_statut_virtual_insanity_player_img.get_size()
        titre_statut_virtual_insanity_player_pos = [statut_virtual_insanity_player_pos[0] + statut_virtual_insanity_player_size[0] / 2 - titre_statut_virtual_insanity_player_dimensions[0] / 2, statut_virtual_insanity_player_pos[1] + statut_virtual_insanity_player_size[1] / 2 - titre_statut_virtual_insanity_player_dimensions[1] / 2]

        font_la_peace_player = pygame.font.Font(Arcade, 35)
        la_peace_player_img = font_la_peace_player.render("La Peace : Vous et votre adversaire cessez de vous battre et trouvez La Peace", True, (255, 255, 255))
        la_peace_player_dimensions = la_peace_player_img.get_size()
        la_peace_player_pos = [20, statut_virtual_insanity_player_pos[1] + statut_virtual_insanity_player_size[1] + 35]

        statut_la_peace_player = pygame.Surface((175, 25))
        statut_la_peace_player.fill("#999999")
        statut_la_peace_player_size = [175, 25]
        statut_la_peace_player_pos = [20, la_peace_player_pos[1] + la_peace_player_dimensions[1] + 10]

        if i_meme_sélectionné_player == 12 :
            titre_Statut_la_peace_player = "Statut : Equipe"
        elif succès_collectibles_caché_player :
            titre_Statut_la_peace_player = "Statut : Possede"
        else :
            titre_Statut_la_peace_player = "Statut : Non possede"
        font_titre_statut_la_peace_player = pygame.font.Font(Arcade, 15)
        titre_statut_la_peace_player_img = font_titre_statut_la_peace_player.render(titre_Statut_la_peace_player, True, (255, 255, 255))
        titre_statut_la_peace_player_dimensions = titre_statut_la_peace_player_img.get_size()
        titre_statut_la_peace_player_pos = [statut_la_peace_player_pos[0] + statut_la_peace_player_size[0] / 2 - titre_statut_la_peace_player_dimensions[0] / 2, statut_la_peace_player_pos[1] + statut_la_peace_player_size[1] / 2 - titre_statut_la_peace_player_dimensions[1] / 2]


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------------Joueur 2------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        bt_joueur_2 = pygame.Surface((550, 200))
        bt_joueur_2.fill("#999999")
        bt_joueur_2_size = [550, 200]
        bt_joueur_2_pos = [3 * (screen_size[0] / 4) - bt_joueur_2_size[0] / 2, screen_size[1] / 2 - bt_joueur_2_size[1] / 2]

        font_titre_bt_joueur_2 = pygame.font.Font(Technos, 60)
        titre_bt_joueur_2_img = font_titre_bt_joueur_2.render("Joueur 2", True, (255, 255, 255))
        titre_bt_joueur_2_dimensions = titre_bt_joueur_2_img.get_size()
        titre_bt_joueur_2_pos = [bt_joueur_2_pos[0] + bt_joueur_2_size[0] / 2 - titre_bt_joueur_2_dimensions[0] / 2, bt_joueur_2_pos[1] + bt_joueur_2_size[1] / 2 - titre_bt_joueur_2_dimensions[1] / 2]

        #---------------------------------------------------------------------------RARE----------------------------------------------------------------------------

        font__titre_bt_joueur_2 = pygame.font.Font(Technos, 45)
        _titre_bt_joueur_2_img = font__titre_bt_joueur_2.render("Joueur 2", True, (255, 255, 255))
        _titre_bt_joueur_2_dimensions = _titre_bt_joueur_2_img.get_size()
        _titre_bt_joueur_2_pos = [screen_size[0] / 2 - _titre_bt_joueur_2_dimensions[0] / 2, titre_menu_i_memes_pos[1] + titre_menu_i_memes_dimensions[1] + 10]


        bt_rareté_rare2 = pygame.Surface((300, 50))
        bt_rareté_rare2.fill("#999999")
        bt_rareté_rare2_size = [300, 50]
        bt_rareté_rare2_pos = [screen_size[0] / 2 - 470, titre_menu_i_memes_pos[1] + titre_menu_i_memes_dimensions[1] + 75 + bt_rareté_rare_size[1]]
  
        font_titre_bt_rareté_rare2 = pygame.font.Font(Technos, 25)
        titre_bt_rareté_rare2_img = font_titre_bt_rareté_rare.render("Rare", True, (255, 255, 255))
        titre_bt_rareté_rare2_dimensions = titre_bt_rareté_rare_img.get_size()
        titre_bt_rareté_rare2_pos = [bt_rareté_rare2_pos[0] + bt_rareté_rare2_size[0] / 2 - titre_bt_rareté_rare2_dimensions[0] / 2, bt_rareté_rare2_pos[1] + bt_rareté_rare2_size[1] / 2 - titre_bt_rareté_rare2_dimensions[1] / 2]


        font_red_bull_player2 = pygame.font.Font(Arcade, 35)
        red_bull_player2_img = font_red_bull_player2.render("Red Bull : Confere une acceleration temporaire de 5 secondes", True, (255, 255, 255))
        red_bull_player2_dimensions = red_bull_player2_img.get_size()
        red_bull_player2_pos = [20, bt_rareté_rare2_pos[1] + bt_rareté_rare2_size[1] + 35]

        statut_red_bull_player2 = pygame.Surface((175, 25))
        statut_red_bull_player2.fill("#999999")
        statut_red_bull_player2_size = [175, 25]
        statut_red_bull_player2_pos = [20, red_bull_player2_pos[1] + red_bull_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 1 :
            titre_Statut_red_bull_player2 = "Statut : Equipe"
        elif succès_temps_1_player_2 :
            titre_Statut_red_bull_player2 = "Statut : Possede"
        else :
            titre_Statut_red_bull_player2 = "Statut : Non possede"
        font_titre_statut_red_bull_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_red_bull_player2_img = font_titre_statut_red_bull_player2.render(titre_Statut_red_bull_player2, True, (255, 255, 255))
        titre_statut_red_bull_player2_dimensions = titre_statut_red_bull_player2_img.get_size()
        titre_statut_red_bull_player2_pos = [statut_red_bull_player2_pos[0] + statut_red_bull_player2_size[0] / 2 - titre_statut_red_bull_player2_dimensions[0] / 2, statut_red_bull_player2_pos[1] + statut_red_bull_player2_size[1] / 2 - titre_statut_red_bull_player2_dimensions[1] / 2]

        font_disparition_player2 = pygame.font.Font(Arcade, 35)
        disparition_player2_img = font_disparition_player2.render("Disparition : Rend invisible et intangible pendant 5 secondes", True, (255, 255, 255))
        disparition_player2_dimensions = disparition_player2_img.get_size()
        disparition_player2_pos = [20, statut_red_bull_player2_pos[1] + statut_red_bull_player2_size[1] + 35]

        statut_disparition_player2 = pygame.Surface((175, 25))
        statut_disparition_player2.fill("#999999")
        statut_disparition_player2_size = [175, 25]
        statut_disparition_player2_pos = [20, disparition_player2_pos[1] + disparition_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 2 :
            titre_Statut_disparition_player2 = "Statut : Equipe"
        elif succès_score_1_player_2 :
            titre_Statut_disparition_player2 = "Statut : Possede"
        else :
            titre_Statut_disparition_player2 = "Statut : Non possede"
        font_titre_statut_disparition_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_disparition_player2_img = font_titre_statut_disparition_player2.render(titre_Statut_disparition_player2, True, (255, 255, 255))
        titre_statut_disparition_player2_dimensions = titre_statut_disparition_player2_img.get_size()
        titre_statut_disparition_player2_pos = [statut_disparition_player2_pos[0] + statut_disparition_player2_size[0] / 2 - titre_statut_disparition_player2_dimensions[0] / 2, statut_disparition_player2_pos[1] + statut_disparition_player2_size[1] / 2 - titre_statut_disparition_player2_dimensions[1] / 2]

        font_jackpot_player2 = pygame.font.Font(Arcade, 35)
        jackpot_player2_img = font_jackpot_player2.render("Jackpot (Passif) : Double votre score final en fin de partie", True, (255, 255, 255))
        jackpot_player2_dimensions = jackpot_player2_img.get_size()
        jackpot_player2_pos = [20, statut_disparition_player2_pos[1] + statut_disparition_player2_size[1] + 35]

        statut_jackpot_player2 = pygame.Surface((175, 25))
        statut_jackpot_player2.fill("#999999")
        statut_jackpot_player2_size = [175, 25]
        statut_jackpot_player2_pos = [20, jackpot_player2_pos[1] + jackpot_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 3 :
            titre_Statut_jackpot_player2 = "Statut : Equipe"
        elif succès_frôlements_1_player_2 :
            titre_Statut_jackpot_player2 = "Statut : Possede"
        else :
            titre_Statut_jackpot_player2 = "Statut : Non possede"
        font_titre_statut_jackpot_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_jackpot_player2_img = font_titre_statut_jackpot_player2.render(titre_Statut_jackpot_player2, True, (255, 255, 255))
        titre_statut_jackpot_player2_dimensions = titre_statut_jackpot_player2_img.get_size()
        titre_statut_jackpot_player2_pos = [statut_jackpot_player2_pos[0] + statut_jackpot_player2_size[0] / 2 - titre_statut_jackpot_player2_dimensions[0] / 2, statut_jackpot_player2_pos[1] + statut_jackpot_player2_size[1] / 2 - titre_statut_jackpot_player2_dimensions[1] / 2]

        font_devil_never_cry_player2 = pygame.font.Font(Arcade, 35)
        devil_never_cry_player2_img = font_devil_never_cry_player2.render("Devil Never Cry (Passif) : Ressuscite 1 fois", True, (255, 255, 255))
        devil_never_cry_player2_dimensions = devil_never_cry_player2_img.get_size()
        devil_never_cry_player2_pos = [20, statut_jackpot_player2_pos[1] + statut_jackpot_player2_size[1] + 35]

        statut_devil_never_cry_player2 = pygame.Surface((175, 25))
        statut_devil_never_cry_player2.fill("#999999")
        statut_devil_never_cry_player2_size = [175, 25]
        statut_devil_never_cry_player2_pos = [20, devil_never_cry_player2_pos[1] + devil_never_cry_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 4 :
            titre_Statut_devil_never_cry_player2 = "Statut : Equipe"
        elif succès_collectibles_1_player_2 :
            titre_Statut_devil_never_cry_player2 = "Statut : Possede"
        else :
            titre_Statut_devil_never_cry_player2 = "Statut : Non possede"
        font_titre_statut_devil_never_cry_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_devil_never_cry_player2_img = font_titre_statut_devil_never_cry_player2.render(titre_Statut_devil_never_cry_player2, True, (255, 255, 255))
        titre_statut_devil_never_cry_player2_dimensions = titre_statut_devil_never_cry_player2_img.get_size()
        titre_statut_devil_never_cry_player2_pos = [statut_devil_never_cry_player2_pos[0] + statut_devil_never_cry_player2_size[0] / 2 - titre_statut_devil_never_cry_player2_dimensions[0] / 2, statut_devil_never_cry_player2_pos[1] + statut_devil_never_cry_player2_size[1] / 2 - titre_statut_devil_never_cry_player2_dimensions[1] / 2]

        #-------------------------------------------------------------------------EPIQUE-----------------------------------------------------------------------------

        bt_rareté_épique2 = pygame.Surface((300, 50))
        bt_rareté_épique2.fill("#999999")
        bt_rareté_épique2_size = [300, 50]
        bt_rareté_épique2_pos = [screen_size[0] / 2 - bt_rareté_épique2_size[0] / 2, titre_menu_i_memes_pos[1] + titre_menu_i_memes_dimensions[1] + 75 + bt_rareté_épique2_size[1]]

        font_titre_bt_rareté_épique2 = pygame.font.Font(Technos, 25)
        titre_bt_rareté_épique2_img = font_titre_bt_rareté_épique2.render("Epique", True, (255, 255, 255))
        titre_bt_rareté_épique2_dimensions = titre_bt_rareté_épique2_img.get_size()
        titre_bt_rareté_épique2_pos = [bt_rareté_épique2_pos[0] + bt_rareté_épique2_size[0] / 2 - titre_bt_rareté_épique2_dimensions[0] / 2, bt_rareté_épique2_pos[1] + bt_rareté_épique2_size[1] / 2 - titre_bt_rareté_épique2_dimensions[1] / 2]


        font_hyperdrive_player2 = pygame.font.Font(Arcade, 35)
        hyperdrive_player2_img = font_hyperdrive_player2.render("Hyperdrive : Propulse a l'autre bout de la grille dans la direction actuelle", True, (255, 255, 255))
        hyperdrive_player2_dimensions = hyperdrive_player2_img.get_size()
        hyperdrive_player2_pos = [20, bt_rareté_épique2_pos[1] + bt_rareté_épique2_size[1] + 35]

        statut_hyperdrive_player2 = pygame.Surface((175, 25))
        statut_hyperdrive_player2.fill("#999999")
        statut_hyperdrive_player2_size = [175, 25]
        statut_hyperdrive_player2_pos = [20, hyperdrive_player2_pos[1] + hyperdrive_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 5 :
            titre_Statut_hyperdrive_player2 = "Statut : Equipe"
        elif succès_temps_2_player_2 :
            titre_Statut_hyperdrive_player2 = "Statut : Possede"
        else :
            titre_Statut_hyperdrive_player2 = "Statut : Non possede"
        font_titre_statut_hyperdrive_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_hyperdrive_player2_img = font_titre_statut_hyperdrive_player2.render(titre_Statut_hyperdrive_player2, True, (255, 255, 255))
        titre_statut_hyperdrive_player2_dimensions = titre_statut_hyperdrive_player2_img.get_size()
        titre_statut_hyperdrive_player2_pos = [statut_hyperdrive_player2_pos[0] + statut_hyperdrive_player2_size[0] / 2 - titre_statut_hyperdrive_player2_dimensions[0] / 2, statut_hyperdrive_player2_pos[1] + statut_hyperdrive_player2_size[1] / 2 - titre_statut_hyperdrive_player2_dimensions[1] / 2]

        font_nope_player2 = pygame.font.Font(Arcade, 35)
        nope_player2_img = font_nope_player2.render("Nope (usage unique) : Contre l'effet nefaste d'un I-Meme adverse", True, (255, 255, 255))
        nope_player2_dimensions = nope_player2_img.get_size()
        nope_player2_pos = [20, statut_hyperdrive_player2_pos[1] + statut_hyperdrive_player2_size[1] + 35]

        statut_nope_player2 = pygame.Surface((175, 25))
        statut_nope_player2.fill("#999999")
        statut_nope_player2_size = [175, 25]
        statut_nope_player2_pos = [20, nope_player2_pos[1] + nope_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 6 :
            titre_Statut_nope_player2 = "Statut : Equipe"
        elif succès_score_2_player_2 :
            titre_Statut_nope_player2 = "Statut : Possede"
        else :
            titre_Statut_nope_player2 = "Statut : Non possede"
        font_titre_statut_nope_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_nope_player2_img = font_titre_statut_nope_player2.render(titre_Statut_nope_player2, True, (255, 255, 255))
        titre_statut_nope_player2_dimensions = titre_statut_nope_player2_img.get_size()
        titre_statut_nope_player2_pos = [statut_nope_player2_pos[0] + statut_nope_player2_size[0] / 2 - titre_statut_nope_player2_dimensions[0] / 2, statut_nope_player2_pos[1] + statut_nope_player2_size[1] / 2 - titre_statut_nope_player2_dimensions[1] / 2]

        font_gandalf_player2 = pygame.font.Font(Arcade, 35)
        gandalf_player2_img = font_gandalf_player2.render("Gandalf : Erige un mur en face de l'adversaire", True, (255, 255, 255))
        gandalf_player2_dimensions = gandalf_player2_img.get_size()
        gandalf_player2_pos = [20, statut_nope_player2_pos[1] + statut_nope_player2_size[1] + 35]

        statut_gandalf_player2 = pygame.Surface((175, 25))
        statut_gandalf_player2.fill("#999999")
        statut_gandalf_player2_size = [175, 25]
        statut_gandalf_player2_pos = [20, gandalf_player2_pos[1] + gandalf_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 7 :
            titre_Statut_gandalf_player2 = "Statut : Equipe"
        elif succès_frôlements_2_player_2 :
            titre_Statut_gandalf_player2 = "Statut : Possede"
        else :
            titre_Statut_gandalf_player2 = "Statut : Non possede"
        font_titre_statut_gandalf_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_gandalf_player2_img = font_titre_statut_gandalf_player2.render(titre_Statut_gandalf_player2, True, (255, 255, 255))
        titre_statut_gandalf_player2_dimensions = titre_statut_gandalf_player2_img.get_size()
        titre_statut_gandalf_player2_pos = [statut_gandalf_player2_pos[0] + statut_gandalf_player2_size[0] / 2 - titre_statut_gandalf_player2_dimensions[0] / 2, statut_gandalf_player2_pos[1] + statut_gandalf_player2_size[1] / 2 - titre_statut_gandalf_player2_dimensions[1] / 2]

        font_death_star_player2 = pygame.font.Font(Arcade, 35)
        death_star_player2_img = font_death_star_player2.render("Death Star : Tire un rayon laser dans la direction actuelle", True, (255, 255, 255))
        death_star_player2_dimensions = death_star_player2_img.get_size()
        death_star_player2_pos = [20, statut_gandalf_player2_pos[1] + statut_gandalf_player2_size[1] + 35]

        statut_death_star_player2 = pygame.Surface((175, 25))
        statut_death_star_player2.fill("#999999")
        statut_death_star_player2_size = [175, 25]
        statut_death_star_player2_pos = [20, death_star_player2_pos[1] + death_star_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 8 :
            titre_Statut_death_star_player2 = "Statut : Equipe"
        elif succès_collectibles_2_player_2 :
            titre_Statut_death_star_player2 = "Statut : Possede"
        else :
            titre_Statut_death_star_player2 = "Statut : Non possede"
        font_titre_statut_death_star_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_death_star_player2_img = font_titre_statut_death_star_player2.render(titre_Statut_death_star_player2, True, (255, 255, 255))
        titre_statut_death_star_player2_dimensions = titre_statut_death_star_player2_img.get_size()
        titre_statut_death_star_player2_pos = [statut_death_star_player2_pos[0] + statut_death_star_player2_size[0] / 2 - titre_statut_death_star_player2_dimensions[0] / 2, statut_death_star_player2_pos[1] + statut_death_star_player2_size[1] / 2 - titre_statut_death_star_player2_dimensions[1] / 2]

        #----------------------------------------------------------------------LEGENDAIRE---------------------------------------------------------------------------

        bt_rareté_légendaire2 = pygame.Surface((300, 50))
        bt_rareté_légendaire2.fill("#999999")
        bt_rareté_légendaire2_size = [300, 50]
        bt_rareté_légendaire2_pos = [bt_rareté_épique2_pos[0] + bt_rareté_épique2_size[0] + 20, titre_menu_i_memes_pos[1] + titre_menu_i_memes_dimensions[1] + 75 + bt_rareté_légendaire2_size[1]]

        font_titre_bt_rareté_légendaire2 = pygame.font.Font(Technos, 25)
        titre_bt_rareté_légendaire2_img = font_titre_bt_rareté_légendaire2.render("Legendaire", True, (255, 255, 255))
        titre_bt_rareté_légendaire2_dimensions = titre_bt_rareté_légendaire2_img.get_size()
        titre_bt_rareté_légendaire2_pos = [bt_rareté_légendaire2_pos[0] + bt_rareté_légendaire2_size[0] / 2 - titre_bt_rareté_légendaire2_dimensions[0] / 2, bt_rareté_légendaire2_pos[1] + bt_rareté_légendaire2_size[1] / 2 - titre_bt_rareté_légendaire2_dimensions[1] / 2]


        font_thanos_player2 = pygame.font.Font(Arcade, 35)
        thanos_player2_img = font_thanos_player2.render("Thanos : Fais disparaitre toutes les trainees de la grille", True, (255, 255, 255))
        thanos_player2_dimensions = thanos_player2_img.get_size()
        thanos_player2_pos = [20, bt_rareté_légendaire2_pos[1] + bt_rareté_légendaire2_size[1] + 35]

        statut_thanos_player2 = pygame.Surface((175, 25))
        statut_thanos_player2.fill("#999999")
        statut_thanos_player2_size = [175, 25]
        statut_thanos_player2_pos = [20, thanos_player2_pos[1] + thanos_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 9 :
            titre_Statut_thanos_player2 = "Statut : Equipe"
        elif succès_temps_caché_player_2 :
            titre_Statut_thanos_player2 = "Statut : Possede"
        else :
            titre_Statut_thanos_player2 = "Statut : Non possede"
        font_titre_statut_thanos_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_thanos_player2_img = font_titre_statut_thanos_player2.render(titre_Statut_thanos_player2, True, (255, 255, 255))
        titre_statut_thanos_player2_dimensions = titre_statut_thanos_player2_img.get_size()
        titre_statut_thanos_player2_pos = [statut_thanos_player2_pos[0] + statut_thanos_player2_size[0] / 2 - titre_statut_thanos_player2_dimensions[0] / 2, statut_thanos_player2_pos[1] + statut_thanos_player2_size[1] / 2 - titre_statut_thanos_player2_dimensions[1] / 2]

        font_c_est_quoi_ce_monde_player2 = pygame.font.Font(Arcade, 35)
        c_est_quoi_ce_monde_player2_img = font_c_est_quoi_ce_monde_player2.render("C'est quoi ce monde ? : Inverse les touches de l'adversaire pendant 5 secondes", True, (255, 255, 255))
        c_est_quoi_ce_monde_player2_dimensions = c_est_quoi_ce_monde_player2_img.get_size()
        c_est_quoi_ce_monde_player2_pos = [20, statut_thanos_player2_pos[1] + statut_thanos_player2_size[1] + 35]

        statut_c_est_quoi_ce_monde_player2 = pygame.Surface((175, 25))
        statut_c_est_quoi_ce_monde_player2.fill("#999999")
        statut_c_est_quoi_ce_monde_player2_size = [175, 25]
        statut_c_est_quoi_ce_monde_player2_pos = [20, c_est_quoi_ce_monde_player2_pos[1] + c_est_quoi_ce_monde_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 10 :
            titre_Statut_c_est_quoi_ce_monde_player2 = "Statut : Equipe"
        elif succès_score_caché_player_2 :
            titre_Statut_c_est_quoi_ce_monde_player2 = "Statut : Possede"
        else :
            titre_Statut_c_est_quoi_ce_monde_player2 = "Statut : Non possede"
        font_titre_statut_c_est_quoi_ce_monde_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_c_est_quoi_ce_monde_player2_img = font_titre_statut_c_est_quoi_ce_monde_player2.render(titre_Statut_c_est_quoi_ce_monde_player2, True, (255, 255, 255))
        titre_statut_c_est_quoi_ce_monde_player2_dimensions = titre_statut_c_est_quoi_ce_monde_player2_img.get_size()
        titre_statut_c_est_quoi_ce_monde_player2_pos = [statut_c_est_quoi_ce_monde_player2_pos[0] + statut_c_est_quoi_ce_monde_player2_size[0] / 2 - titre_statut_c_est_quoi_ce_monde_player2_dimensions[0] / 2, statut_c_est_quoi_ce_monde_player2_pos[1] + statut_c_est_quoi_ce_monde_player2_size[1] / 2 - titre_statut_c_est_quoi_ce_monde_player2_dimensions[1] / 2]

        font_virtual_insanity_player2 = pygame.font.Font(Arcade, 35)
        virtual_insanity_player2_img = font_virtual_insanity_player2.render("Virtual Insanity : L'adversaire ne peut plus se diriger et est ralentit pendant 5 secondes", True, (255, 255, 255))
        virtual_insanity_player2_dimensions = virtual_insanity_player2_img.get_size()
        virtual_insanity_player2_pos = [20, statut_c_est_quoi_ce_monde_player2_pos[1] + statut_c_est_quoi_ce_monde_player2_size[1] + 35]

        statut_virtual_insanity_player2 = pygame.Surface((175, 25))
        statut_virtual_insanity_player2.fill("#999999")
        statut_virtual_insanity_player2_size = [175, 25]
        statut_virtual_insanity_player2_pos = [20, virtual_insanity_player2_pos[1] + virtual_insanity_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 11 :
            titre_Statut_virtual_insanity_player2 = "Statut : Equipe"
        elif succès_frôlements_caché_player_2 :
            titre_Statut_virtual_insanity_player2 = "Statut : Possede"
        else :
            titre_Statut_virtual_insanity_player2 = "Statut : Non possede"
        font_titre_statut_virtual_insanity_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_virtual_insanity_player2_img = font_titre_statut_virtual_insanity_player2.render(titre_Statut_virtual_insanity_player2, True, (255, 255, 255))
        titre_statut_virtual_insanity_player2_dimensions = titre_statut_virtual_insanity_player2_img.get_size()
        titre_statut_virtual_insanity_player2_pos = [statut_virtual_insanity_player2_pos[0] + statut_virtual_insanity_player2_size[0] / 2 - titre_statut_virtual_insanity_player2_dimensions[0] / 2, statut_virtual_insanity_player2_pos[1] + statut_virtual_insanity_player2_size[1] / 2 - titre_statut_virtual_insanity_player2_dimensions[1] / 2]

        font_la_peace_player2 = pygame.font.Font(Arcade, 35)
        la_peace_player2_img = font_la_peace_player.render("La Peace : Vous et votre adversaire cessez de vous battre et trouvez La Peace", True, (255, 255, 255))
        la_peace_player2_dimensions = la_peace_player2_img.get_size()
        la_peace_player2_pos = [20, statut_virtual_insanity_player2_pos[1] + statut_virtual_insanity_player2_size[1] + 35]

        statut_la_peace_player2 = pygame.Surface((175, 25))
        statut_la_peace_player2.fill("#999999")
        statut_la_peace_player2_size = [175, 25]
        statut_la_peace_player2_pos = [20, la_peace_player2_pos[1] + la_peace_player2_dimensions[1] + 10]

        if i_meme_sélectionné_player_2 == 12 :
            titre_Statut_la_peace_player2 = "Statut : Equipe"
        elif succès_collectibles_caché_player_2 :
            titre_Statut_la_peace_player2 = "Statut : Possede"
        else :
            titre_Statut_la_peace_player2 = "Statut : Non possede"
        font_titre_statut_la_peace_player2 = pygame.font.Font(Arcade, 15)
        titre_statut_la_peace_player2_img = font_titre_statut_la_peace_player2.render(titre_Statut_la_peace_player2, True, (255, 255, 255))
        titre_statut_la_peace_player2_dimensions = titre_statut_la_peace_player2_img.get_size()
        titre_statut_la_peace_player2_pos = [statut_la_peace_player2_pos[0] + statut_la_peace_player2_size[0] / 2 - titre_statut_la_peace_player2_dimensions[0] / 2, statut_la_peace_player2_pos[1] + statut_la_peace_player2_size[1] / 2 - titre_statut_la_peace_player2_dimensions[1] / 2]


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------------BT RETOUR---------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        bt_retour = pygame.Surface((600, 100))
        bt_retour.fill("#999999")
        bt_retour_size = [600, 100]
        bt_retour_pos = [screen_size[0] / 2 - bt_retour_size[0] / 2, screen_size[1] - bt_retour_size[1] - 5]

        font_titre_bt_retour = pygame.font.Font(Technos, 50)
        titre_bt_retour_img = font_titre_bt_retour.render("Retour", True, (255, 255, 255))
        titre_bt_retour_dimensions = titre_bt_retour_img.get_size()
        titre_bt_retour_pos = [screen_size[0] / 2 - titre_bt_retour_dimensions[0] / 2, bt_retour_pos[1] + bt_retour_size[1] / 2 - titre_bt_retour_dimensions[1] / 2]


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #----------------------------------------------------------------------BT QUITTER---------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------

        bt_retour2 = pygame.Surface((600, 100))
        bt_retour2.fill("#999999")
        bt_retour2_size = [600, 100]
        bt_retour2_pos = [screen_size[0] / 2 - bt_retour2_size[0] / 2, screen_size[1] - bt_retour2_size[1] - bt_retour_size[1] - 25]

        font_titre_bt_retour2 = pygame.font.Font(Technos, 35)
        titre_bt_retour2_img = font_titre_bt_retour2.render("Retour au menu", True, (255, 255, 255))
        titre_bt_retour2_dimensions = titre_bt_retour2_img.get_size()
        titre_bt_retour2_pos = [screen_size[0] / 2 - titre_bt_retour2_dimensions[0] / 2, bt_retour2_pos[1] + bt_retour2_size[1] / 2 - titre_bt_retour2_dimensions[1] / 2]


        #-----------------------------------------------------------------------------------------------------------------------------------------------------------
        #---------------------------------------------------------------------ORGANISATION--------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------------------------------------------


        sélection_joueurs = 1
        sélection_rareté_joueur_1 = 2
        rareté_rare_joueur_1 = 3
        rareté_épique_joueur_1 = 4
        rareté_légendaire_joueur_1 = 5
        sélection_rareté_joueur_2 = 6
        rareté_rare_joueur_2 = 7
        rareté_épique_joueur_2 = 8
        rareté_légendaire_joueur_2 = 9


        fenêtre_actuelle = sélection_joueurs

        mouse = pygame.mouse.get_pos()

        clique_gauche = pygame.mouse.get_pressed()[0]

        if clique_gauche :
            if mouse[0] >= bt_joueur_1_pos[0] and mouse[0] <= bt_joueur_1_pos[0] + bt_joueur_1_size[0] and mouse[1] >= bt_joueur_1_pos[1] and mouse[1] <= bt_joueur_1_pos[1] + bt_joueur_1_size[1] :
                fenêtre_actuelle = sélection_rareté_joueur_1

            if mouse[0] >= bt_rareté_rare_pos[0] and mouse[0] <= bt_rareté_rare_pos[0] + bt_rareté_rare_size[0] and mouse[1] >= bt_rareté_rare_pos[1] and mouse[1] <= bt_rareté_rare_pos[1] + bt_rareté_rare_size[1] :
                fenêtre_actuelle = rareté_rare_joueur_1

            if mouse[0] >= bt_rareté_épique_pos[0] and mouse[0] <= bt_rareté_épique_pos[0] + bt_rareté_épique_size[0] and mouse[1] >= bt_rareté_épique_pos[1] and mouse[1] <= bt_rareté_épique_pos[1] + bt_rareté_épique_size[1] :
                fenêtre_actuelle = rareté_épique_joueur_1

            if mouse[0] >= bt_rareté_légendaire_pos[0] and mouse[0] <= bt_rareté_légendaire_pos[0] + bt_rareté_légendaire_size[0] and mouse[1] >= bt_rareté_légendaire_pos[1] and mouse[1] <= bt_rareté_légendaire_pos[1] + bt_rareté_légendaire_size[1] :
                fenêtre_actuelle = rareté_légendaire_joueur_1


            if mouse[0] >= bt_joueur_2_pos[0] and mouse[0] <= bt_joueur_2_pos[0] + bt_joueur_2_size[0] and mouse[1] >= bt_joueur_2_pos[1] and mouse[1] <= bt_joueur_2_pos[1] + bt_joueur_2_size[1] :
                fenêtre_actuelle = sélection_rareté_joueur_2

            if mouse[0] >= bt_rareté_rare2_pos[0] and mouse[0] <= bt_rareté_rare2_pos[0] + bt_rareté_rare2_size[0] and mouse[1] >= bt_rareté_rare2_pos[1] and mouse[1] <= bt_rareté_rare2_pos[1] + bt_rareté_rare2_size[1] :
                fenêtre_actuelle = rareté_rare_joueur_2

            if mouse[0] >= bt_rareté_épique2_pos[0] and mouse[0] <= bt_rareté_épique2_pos[0] + bt_rareté_épique2_size[0] and mouse[1] >= bt_rareté_épique2_pos[1] and mouse[1] <= bt_rareté_épique2_pos[1] + bt_rareté_épique2_size[1] :
                fenêtre_actuelle = rareté_épique_joueur_2

            if mouse[0] >= bt_rareté_légendaire2_pos[0] and mouse[0] <= bt_rareté_légendaire2_pos[0] + bt_rareté_légendaire2_size[0] and mouse[1] >= bt_rareté_légendaire2_pos[1] and mouse[1] <= bt_rareté_légendaire2_pos[1] + bt_rareté_légendaire2_size[1] :
                fenêtre_actuelle = rareté_légendaire_joueur_2

            if mouse[0] >= bt_retour_pos[0] and mouse[0] <= bt_retour_pos[0] + bt_retour_size[0] and mouse[1] >= bt_retour_pos[1] and mouse[1] <= bt_retour_pos[1] + bt_retour_size[1] :
                fenêtre_actuelle = sélection_joueurs


            if mouse[0] >= bt_retour2_pos[0] and mouse[0] <= bt_retour2_pos[0] + bt_retour2_size[0] and mouse[1] >= bt_retour2_pos[1] and mouse[1] <= bt_retour2_pos[1] + bt_retour2_size[1] :
                mode_actuel = MODE_ACCUEIL



            if mouse[0] >= statut_red_bull_player_pos[0] and mouse[0] <= statut_red_bull_player_pos[0] + statut_red_bull_player_size[0] and mouse[1] >= statut_red_bull_player_pos[1] and mouse[1] <= statut_red_bull_player_pos[1] + statut_red_bull_player_size[1] :
                if succès_temps_1_player :
                    if i_meme_sélectionné_player != 1 :
                        i_meme_sélectionné_player = 1
                        cooldown_i_meme_rare_sélectionné_player = cooldown_i_meme_red_bull_player
                        cooldown_i_meme_sélectionné_player = cooldown_i_meme_rare_sélectionné_player
                
                fenêtre_actuelle = rareté_rare_joueur_1

            if mouse[0] >= statut_disparition_player_pos[0] and mouse[0] <= statut_disparition_player_pos[0] + statut_disparition_player_size[0] and mouse[1] >= statut_disparition_player_pos[1] and mouse[1] <= statut_disparition_player_pos[1] + statut_disparition_player_size[1] :
                if succès_score_1_player :
                    if i_meme_sélectionné_player != 2 :
                        i_meme_sélectionné_player = 2
                        cooldown_i_meme_rare_sélectionné_player = cooldown_i_meme_disparition_player
                        cooldown_i_meme_sélectionné_player = cooldown_i_meme_rare_sélectionné_player

                fenêtre_actuelle = rareté_rare_joueur_1

            if mouse[0] >= statut_jackpot_player_pos[0] and mouse[0] <= statut_jackpot_player_pos[0] + statut_jackpot_player_size[0] and mouse[1] >= statut_jackpot_player_pos[1] and mouse[1] <= statut_jackpot_player_pos[1] + statut_jackpot_player_size[1] :
                if succès_frôlements_1_player :
                    if i_meme_sélectionné_player != 3 :
                        i_meme_sélectionné_player = 3

                fenêtre_actuelle = rareté_rare_joueur_1

            if mouse[0] >= statut_devil_never_cry_player_pos[0] and mouse[0] <= statut_devil_never_cry_player_pos[0] + statut_devil_never_cry_player_size[0] and mouse[1] >= statut_devil_never_cry_player_pos[1] and mouse[1] <= statut_devil_never_cry_player_pos[1] + statut_devil_never_cry_player_size[1] :
                if succès_collectibles_1_player :
                    if i_meme_sélectionné_player != 4 :
                        i_meme_sélectionné_player = 4

                fenêtre_actuelle = rareté_rare_joueur_1

            if mouse[0] >= statut_hyperdrive_player_pos[0] and mouse[0] <= statut_hyperdrive_player_pos[0] + statut_hyperdrive_player_size[0] and mouse[1] >= statut_hyperdrive_player_pos[1] and mouse[1] <= statut_hyperdrive_player_pos[1] + statut_hyperdrive_player_size[1] :
                if succès_temps_2_player :
                    if i_meme_sélectionné_player != 5 :
                        i_meme_sélectionné_player = 5

                fenêtre_actuelle = rareté_épique_joueur_1

            if mouse[0] >= statut_nope_player_pos[0] and mouse[0] <= statut_nope_player_pos[0] + statut_nope_player_size[0] and mouse[1] >= statut_nope_player_pos[1] and mouse[1] <= statut_nope_player_pos[1] + statut_nope_player_size[1] :
                if succès_score_2_player :
                    if i_meme_sélectionné_player != 6 :
                        i_meme_sélectionné_player = 6

                fenêtre_actuelle = rareté_épique_joueur_1

            if mouse[0] >= statut_gandalf_player_pos[0] and mouse[0] <= statut_gandalf_player_pos[0] + statut_gandalf_player_size[0] and mouse[1] >= statut_gandalf_player_pos[1] and mouse[1] <= statut_gandalf_player_pos[1] + statut_gandalf_player_size[1] :
                if succès_frôlements_2_player :
                    if i_meme_sélectionné_player != 7 :
                        i_meme_sélectionné_player = 7

                fenêtre_actuelle = rareté_épique_joueur_1

            if mouse[0] >= statut_death_star_player_pos[0] and mouse[0] <= statut_death_star_player_pos[0] + statut_death_star_player_size[0] and mouse[1] >= statut_death_star_player_pos[1] and mouse[1] <= statut_death_star_player_pos[1] + statut_death_star_player_size[1] :
                if succès_collectibles_2_player :
                    if i_meme_sélectionné_player != 8 :
                        i_meme_sélectionné_player = 8

                fenêtre_actuelle = rareté_épique_joueur_1

            if mouse[0] >= statut_thanos_player_pos[0] and mouse[0] <= statut_thanos_player_pos[0] + statut_thanos_player_size[0] and mouse[1] >= statut_thanos_player_pos[1] and mouse[1] <= statut_thanos_player_pos[1] + statut_thanos_player_size[1] :
                if succès_temps_caché_player :
                    if i_meme_sélectionné_player != 9 :
                        i_meme_sélectionné_player = 9

                fenêtre_actuelle = rareté_légendaire_joueur_1

            if mouse[0] >= statut_c_est_quoi_ce_monde_player_pos[0] and mouse[0] <= statut_c_est_quoi_ce_monde_player_pos[0] + statut_c_est_quoi_ce_monde_player_size[0] and mouse[1] >= statut_c_est_quoi_ce_monde_player_pos[1] and mouse[1] <= statut_c_est_quoi_ce_monde_player_pos[1] + statut_c_est_quoi_ce_monde_player_size[1] :
                if succès_score_caché_player :
                    if i_meme_sélectionné_player != 10 :
                        i_meme_sélectionné_player = 10

                fenêtre_actuelle = rareté_légendaire_joueur_1

            if mouse[0] >= statut_virtual_insanity_player_pos[0] and mouse[0] <= statut_virtual_insanity_player_pos[0] + statut_virtual_insanity_player_size[0] and mouse[1] >= statut_virtual_insanity_player_pos[1] and mouse[1] <= statut_virtual_insanity_player_pos[1] + statut_virtual_insanity_player_size[1] :
                if succès_frôlements_caché_player :
                    if i_meme_sélectionné_player != 11 :
                        i_meme_sélectionné_player = 11

                fenêtre_actuelle = rareté_légendaire_joueur_1

            if mouse[0] >= statut_la_peace_player_pos[0] and mouse[0] <= statut_la_peace_player_pos[0] + statut_la_peace_player_size[0] and mouse[1] >= statut_la_peace_player_pos[1] and mouse[1] <= statut_la_peace_player_pos[1] + statut_la_peace_player_size[1] :
                if succès_collectibles_caché_player :
                    if i_meme_sélectionné_player != 12 :
                        i_meme_sélectionné_player = 12

                fenêtre_actuelle = rareté_légendaire_joueur_1


            if mouse[0] >= statut_red_bull_player2_pos[0] and mouse[0] <= statut_red_bull_player2_pos[0] + statut_red_bull_player2_size[0] and mouse[1] >= statut_red_bull_player2_pos[1] and mouse[1] <= statut_red_bull_player2_pos[1] + statut_red_bull_player2_size[1] :
                if succès_temps_1_player_2 :
                    i_meme_sélectionné_player_2 = 1
                    cooldown_i_meme_rare_sélectionné_player_2 = cooldown_i_meme_red_bull_player_2
                    cooldown_i_meme_sélectionné_player_2 = cooldown_i_meme_rare_sélectionné_player_2

                fenêtre_actuelle = rareté_rare_joueur_2

            if mouse[0] >= statut_disparition_player2_pos[0] and mouse[0] <= statut_disparition_player2_pos[0] + statut_disparition_player2_size[0] and mouse[1] >= statut_disparition_player2_pos[1] and mouse[1] <= statut_disparition_player2_pos[1] + statut_disparition_player2_size[1] :
                if succès_score_1_player_2 :
                    if i_meme_sélectionné_player_2 != 2 :
                        cooldown_i_meme_rare_sélectionné_player_2 = cooldown_i_meme_disparition_player_2
                        cooldown_i_meme_sélectionné_player_2 = cooldown_i_meme_rare_sélectionné_player_2
                        i_meme_sélectionné_player_2 = 2
                
                fenêtre_actuelle = rareté_rare_joueur_2

            if mouse[0] >= statut_jackpot_player2_pos[0] and mouse[0] <= statut_jackpot_player2_pos[0] + statut_jackpot_player2_size[0] and mouse[1] >= statut_jackpot_player2_pos[1] and mouse[1] <= statut_jackpot_player2_pos[1] + statut_jackpot_player2_size[1] :
                if succès_frôlements_1_player_2 :
                    if i_meme_sélectionné_player_2 != 3 :
                        i_meme_sélectionné_player_2 = 3

                fenêtre_actuelle = rareté_rare_joueur_2

            if mouse[0] >= statut_devil_never_cry_player2_pos[0] and mouse[0] <= statut_devil_never_cry_player2_pos[0] + statut_devil_never_cry_player2_size[0] and mouse[1] >= statut_devil_never_cry_player2_pos[1] and mouse[1] <= statut_devil_never_cry_player2_pos[1] + statut_devil_never_cry_player2_size[1] :
                if succès_collectibles_1_player_2 :
                    if i_meme_sélectionné_player_2 != 4 :
                        i_meme_sélectionné_player_2 = 4

                fenêtre_actuelle = rareté_rare_joueur_2

            if mouse[0] >= statut_hyperdrive_player2_pos[0] and mouse[0] <= statut_hyperdrive_player2_pos[0] + statut_hyperdrive_player2_size[0] and mouse[1] >= statut_hyperdrive_player2_pos[1] and mouse[1] <= statut_hyperdrive_player2_pos[1] + statut_hyperdrive_player2_size[1] :
                if succès_temps_2_player_2 :
                    if i_meme_sélectionné_player_2 != 5 :
                        i_meme_sélectionné_player_2 = 5

                fenêtre_actuelle = rareté_épique_joueur_2

            if mouse[0] >= statut_nope_player2_pos[0] and mouse[0] <= statut_nope_player2_pos[0] + statut_nope_player2_size[0] and mouse[1] >= statut_nope_player2_pos[1] and mouse[1] <= statut_nope_player2_pos[1] + statut_nope_player2_size[1] :
                if succès_score_2_player_2 :
                    if i_meme_sélectionné_player_2 != 6 :
                        i_meme_sélectionné_player_2 = 6

                fenêtre_actuelle = rareté_épique_joueur_2

            if mouse[0] >= statut_gandalf_player2_pos[0] and mouse[0] <= statut_gandalf_player2_pos[0] + statut_gandalf_player2_size[0] and mouse[1] >= statut_gandalf_player2_pos[1] and mouse[1] <= statut_gandalf_player2_pos[1] + statut_gandalf_player2_size[1] :
                if succès_frôlements_2_player_2 :
                    if i_meme_sélectionné_player_2 != 7 :
                        i_meme_sélectionné_player_2 = 7

                fenêtre_actuelle = rareté_épique_joueur_2

            if mouse[0] >= statut_death_star_player2_pos[0] and mouse[0] <= statut_death_star_player2_pos[0] + statut_death_star_player2_size[0] and mouse[1] >= statut_death_star_player2_pos[1] and mouse[1] <= statut_death_star_player2_pos[1] + statut_death_star_player2_size[1] :
                if succès_collectibles_2_player_2 :
                    if i_meme_sélectionné_player_2 != 8 :
                        i_meme_sélectionné_player_2 = 8

                fenêtre_actuelle = rareté_épique_joueur_2

            if mouse[0] >= statut_thanos_player2_pos[0] and mouse[0] <= statut_thanos_player2_pos[0] + statut_thanos_player2_size[0] and mouse[1] >= statut_thanos_player2_pos[1] and mouse[1] <= statut_thanos_player2_pos[1] + statut_thanos_player2_size[1] :
                if succès_temps_caché_player_2 :
                    if i_meme_sélectionné_player_2 != 9 :
                        i_meme_sélectionné_player_2 = 9

                fenêtre_actuelle = rareté_légendaire_joueur_2

            if mouse[0] >= statut_c_est_quoi_ce_monde_player2_pos[0] and mouse[0] <= statut_c_est_quoi_ce_monde_player2_pos[0] + statut_c_est_quoi_ce_monde_player2_size[0] and mouse[1] >= statut_c_est_quoi_ce_monde_player2_pos[1] and mouse[1] <= statut_c_est_quoi_ce_monde_player2_pos[1] + statut_c_est_quoi_ce_monde_player2_size[1] :
                if succès_score_caché_player_2 :
                    if i_meme_sélectionné_player_2 != 10 :
                        i_meme_sélectionné_player_2 = 10

                fenêtre_actuelle = rareté_légendaire_joueur_2

            if mouse[0] >= statut_virtual_insanity_player2_pos[0] and mouse[0] <= statut_virtual_insanity_player2_pos[0] + statut_virtual_insanity_player2_size[0] and mouse[1] >= statut_virtual_insanity_player2_pos[1] and mouse[1] <= statut_virtual_insanity_player2_pos[1] + statut_virtual_insanity_player2_size[1] :
                if succès_frôlements_caché_player_2 :
                    if i_meme_sélectionné_player_2 != 11 :
                        i_meme_sélectionné_player_2 = 11

                fenêtre_actuelle = rareté_légendaire_joueur_2

            if mouse[0] >= statut_la_peace_player2_pos[0] and mouse[0] <= statut_la_peace_player2_pos[0] + statut_la_peace_player2_size[0] and mouse[1] >= statut_la_peace_player2_pos[1] and mouse[1] <= statut_la_peace_player2_pos[1] + statut_la_peace_player2_size[1] :
                if succès_collectibles_caché_player_2 :
                    if i_meme_sélectionné_player_2 != 12 :
                        i_meme_sélectionné_player_2 = 12

                fenêtre_actuelle = rareté_légendaire_joueur_2


            if fenêtre_actuelle == sélection_joueurs :
                screen.fill("#0B041F")
                screen.blit(titre_menu_i_memes_img, titre_menu_i_memes_pos)
                screen.blit(bt_joueur_1, bt_joueur_1_pos)
                screen.blit(titre_bt_joueur_1_img, titre_bt_joueur_1_pos)
                screen.blit(bt_joueur_2, bt_joueur_2_pos)
                screen.blit(titre_bt_joueur_2_img, titre_bt_joueur_2_pos)
                screen.blit(bt_retour2, bt_retour2_pos)
                screen.blit(titre_bt_retour2_img, titre_bt_retour2_pos)

            if fenêtre_actuelle == sélection_rareté_joueur_1 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_i_memes_img, titre_menu_i_memes_pos)
                screen.blit(_titre_bt_joueur_1_img, _titre_bt_joueur_1_pos)
                screen.blit(bt_rareté_rare, bt_rareté_rare_pos)
                screen.blit(titre_bt_rareté_rare_img, titre_bt_rareté_rare_pos)
                screen.blit(bt_rareté_épique, bt_rareté_épique_pos)
                screen.blit(titre_bt_rareté_épique_img, titre_bt_rareté_épique_pos)
                screen.blit(bt_rareté_légendaire, bt_rareté_légendaire_pos)
                screen.blit(titre_bt_rareté_légendaire_img, titre_bt_rareté_légendaire_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == rareté_rare_joueur_1 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_i_memes_img, titre_menu_i_memes_pos)
                screen.blit(_titre_bt_joueur_1_img, _titre_bt_joueur_1_pos)
                screen.blit(bt_rareté_rare, bt_rareté_rare_pos)
                screen.blit(titre_bt_rareté_rare_img, titre_bt_rareté_rare_pos)
                screen.blit(bt_rareté_épique, bt_rareté_épique_pos)
                screen.blit(titre_bt_rareté_épique_img, titre_bt_rareté_épique_pos)
                screen.blit(bt_rareté_légendaire, bt_rareté_légendaire_pos)
                screen.blit(titre_bt_rareté_légendaire_img, titre_bt_rareté_légendaire_pos)
                screen.blit(red_bull_player_img, red_bull_player_pos)
                screen.blit(statut_red_bull_player, statut_red_bull_player_pos)
                screen.blit(titre_statut_red_bull_player_img, titre_statut_red_bull_player_pos)
                screen.blit(disparition_player_img, disparition_player_pos)
                screen.blit(statut_disparition_player, statut_disparition_player_pos)
                screen.blit(titre_statut_disparition_player_img, titre_statut_disparition_player_pos)
                screen.blit(jackpot_player_img, jackpot_player_pos)
                screen.blit(statut_jackpot_player, statut_jackpot_player_pos)
                screen.blit(titre_statut_jackpot_player_img, titre_statut_jackpot_player_pos)
                screen.blit(devil_never_cry_player_img, devil_never_cry_player_pos)
                screen.blit(statut_devil_never_cry_player, statut_devil_never_cry_player_pos)
                screen.blit(titre_statut_devil_never_cry_player_img, titre_statut_devil_never_cry_player_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == rareté_épique_joueur_1 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_i_memes_img, titre_menu_i_memes_pos)
                screen.blit(_titre_bt_joueur_1_img, _titre_bt_joueur_1_pos)
                screen.blit(bt_rareté_rare, bt_rareté_rare_pos)
                screen.blit(titre_bt_rareté_rare_img, titre_bt_rareté_rare_pos)
                screen.blit(bt_rareté_épique, bt_rareté_épique_pos)
                screen.blit(titre_bt_rareté_épique_img, titre_bt_rareté_épique_pos)
                screen.blit(bt_rareté_légendaire, bt_rareté_légendaire_pos)
                screen.blit(titre_bt_rareté_légendaire_img, titre_bt_rareté_légendaire_pos)
                screen.blit(hyperdrive_player_img, hyperdrive_player_pos)
                screen.blit(statut_hyperdrive_player, statut_hyperdrive_player_pos)
                screen.blit(titre_statut_hyperdrive_player_img, titre_statut_hyperdrive_player_pos)
                screen.blit(nope_player_img, nope_player_pos)
                screen.blit(statut_nope_player, statut_nope_player_pos)
                screen.blit(titre_statut_nope_player_img, titre_statut_nope_player_pos)
                screen.blit(gandalf_player_img, gandalf_player_pos)
                screen.blit(statut_gandalf_player, statut_gandalf_player_pos)
                screen.blit(titre_statut_gandalf_player_img, titre_statut_gandalf_player_pos)
                screen.blit(death_star_player_img, death_star_player_pos)
                screen.blit(statut_death_star_player, statut_death_star_player_pos)
                screen.blit(titre_statut_death_star_player_img, titre_statut_death_star_player_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == rareté_légendaire_joueur_1 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_i_memes_img, titre_menu_i_memes_pos)
                screen.blit(_titre_bt_joueur_1_img, _titre_bt_joueur_1_pos)
                screen.blit(bt_rareté_rare, bt_rareté_rare_pos)
                screen.blit(titre_bt_rareté_rare_img, titre_bt_rareté_rare_pos)
                screen.blit(bt_rareté_épique, bt_rareté_épique_pos)
                screen.blit(titre_bt_rareté_épique_img, titre_bt_rareté_épique_pos)
                screen.blit(bt_rareté_légendaire, bt_rareté_légendaire_pos)
                screen.blit(titre_bt_rareté_légendaire_img, titre_bt_rareté_légendaire_pos)
                if succès_temps_caché_player :
                    screen.blit(thanos_player_img, thanos_player_pos)
                    screen.blit(statut_thanos_player, statut_thanos_player_pos)
                    screen.blit(titre_statut_thanos_player_img, titre_statut_thanos_player_pos)
                if succès_score_caché_player :
                    screen.blit(c_est_quoi_ce_monde_player_img, c_est_quoi_ce_monde_player_pos)
                    screen.blit(statut_c_est_quoi_ce_monde_player, statut_c_est_quoi_ce_monde_player_pos)
                    screen.blit(titre_statut_c_est_quoi_ce_monde_player_img, titre_statut_c_est_quoi_ce_monde_player_pos)
                if succès_frôlements_caché_player :
                    screen.blit(virtual_insanity_player_img, virtual_insanity_player_pos)
                    screen.blit(statut_virtual_insanity_player, statut_virtual_insanity_player_pos)
                    screen.blit(titre_statut_virtual_insanity_player_img, titre_statut_virtual_insanity_player_pos)
                if succès_collectibles_caché_player :
                    screen.blit(la_peace_player_img, la_peace_player_pos)
                    screen.blit(statut_la_peace_player, statut_la_peace_player_pos)
                    screen.blit(titre_statut_la_peace_player_img, titre_statut_la_peace_player_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)


            if fenêtre_actuelle == sélection_rareté_joueur_2 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_i_memes_img, titre_menu_i_memes_pos)
                screen.blit(_titre_bt_joueur_2_img, _titre_bt_joueur_2_pos)
                screen.blit(bt_rareté_rare2, bt_rareté_rare2_pos)
                screen.blit(titre_bt_rareté_rare2_img, titre_bt_rareté_rare2_pos)
                screen.blit(bt_rareté_épique2, bt_rareté_épique2_pos)
                screen.blit(titre_bt_rareté_épique2_img, titre_bt_rareté_épique2_pos)
                screen.blit(bt_rareté_légendaire2, bt_rareté_légendaire2_pos)
                screen.blit(titre_bt_rareté_légendaire2_img, titre_bt_rareté_légendaire2_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == rareté_rare_joueur_2 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_i_memes_img, titre_menu_i_memes_pos)
                screen.blit(_titre_bt_joueur_2_img, _titre_bt_joueur_2_pos)
                screen.blit(bt_rareté_rare2, bt_rareté_rare2_pos)
                screen.blit(titre_bt_rareté_rare2_img, titre_bt_rareté_rare2_pos)
                screen.blit(bt_rareté_épique2, bt_rareté_épique2_pos)
                screen.blit(titre_bt_rareté_épique2_img, titre_bt_rareté_épique2_pos)
                screen.blit(bt_rareté_légendaire2, bt_rareté_légendaire2_pos)
                screen.blit(titre_bt_rareté_légendaire2_img, titre_bt_rareté_légendaire2_pos)
                screen.blit(red_bull_player2_img, red_bull_player2_pos)
                screen.blit(statut_red_bull_player2, statut_red_bull_player2_pos)
                screen.blit(titre_statut_red_bull_player2_img, titre_statut_red_bull_player2_pos)
                screen.blit(disparition_player2_img, disparition_player2_pos)
                screen.blit(statut_disparition_player2, statut_disparition_player2_pos)
                screen.blit(titre_statut_disparition_player2_img, titre_statut_disparition_player2_pos)
                screen.blit(jackpot_player2_img, jackpot_player2_pos)
                screen.blit(statut_jackpot_player2, statut_jackpot_player2_pos)
                screen.blit(titre_statut_jackpot_player2_img, titre_statut_jackpot_player2_pos)
                screen.blit(devil_never_cry_player2_img, devil_never_cry_player2_pos)
                screen.blit(statut_devil_never_cry_player2, statut_devil_never_cry_player2_pos)
                screen.blit(titre_statut_devil_never_cry_player2_img, titre_statut_devil_never_cry_player2_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == rareté_épique_joueur_2 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_i_memes_img, titre_menu_i_memes_pos)
                screen.blit(_titre_bt_joueur_2_img, _titre_bt_joueur_2_pos)
                screen.blit(bt_rareté_rare2, bt_rareté_rare2_pos)
                screen.blit(titre_bt_rareté_rare2_img, titre_bt_rareté_rare2_pos)
                screen.blit(bt_rareté_épique2, bt_rareté_épique2_pos)
                screen.blit(titre_bt_rareté_épique2_img, titre_bt_rareté_épique2_pos)
                screen.blit(bt_rareté_légendaire2, bt_rareté_légendaire2_pos)
                screen.blit(titre_bt_rareté_légendaire2_img, titre_bt_rareté_légendaire2_pos)
                screen.blit(hyperdrive_player2_img, hyperdrive_player2_pos)
                screen.blit(statut_hyperdrive_player2, statut_hyperdrive_player2_pos)
                screen.blit(titre_statut_hyperdrive_player2_img, titre_statut_hyperdrive_player2_pos)
                screen.blit(nope_player2_img, nope_player2_pos)
                screen.blit(statut_nope_player2, statut_nope_player2_pos)
                screen.blit(titre_statut_nope_player2_img, titre_statut_nope_player2_pos)
                screen.blit(gandalf_player2_img, gandalf_player2_pos)
                screen.blit(statut_gandalf_player2, statut_gandalf_player2_pos)
                screen.blit(titre_statut_gandalf_player2_img, titre_statut_gandalf_player2_pos)
                screen.blit(death_star_player2_img, death_star_player2_pos)
                screen.blit(statut_death_star_player2, statut_death_star_player2_pos)
                screen.blit(titre_statut_death_star_player2_img, titre_statut_death_star_player2_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)

            if fenêtre_actuelle == rareté_légendaire_joueur_2 :
                screen.fill("#0B041F")
                screen.blit(titre_menu_i_memes_img, titre_menu_i_memes_pos)
                screen.blit(_titre_bt_joueur_2_img, _titre_bt_joueur_2_pos)
                screen.blit(bt_rareté_rare2, bt_rareté_rare2_pos)
                screen.blit(titre_bt_rareté_rare2_img, titre_bt_rareté_rare2_pos)
                screen.blit(bt_rareté_épique2, bt_rareté_épique2_pos)
                screen.blit(titre_bt_rareté_épique2_img, titre_bt_rareté_épique2_pos)
                screen.blit(bt_rareté_légendaire2, bt_rareté_légendaire2_pos)
                screen.blit(titre_bt_rareté_légendaire2_img, titre_bt_rareté_légendaire2_pos)
                if succès_temps_caché_player_2 :
                    screen.blit(thanos_player2_img, thanos_player2_pos)
                    screen.blit(statut_thanos_player2, statut_thanos_player2_pos)
                    screen.blit(titre_statut_thanos_player2_img, titre_statut_thanos_player2_pos)
                if succès_score_caché_player_2 :
                    screen.blit(c_est_quoi_ce_monde_player2_img, c_est_quoi_ce_monde_player2_pos)
                    screen.blit(statut_c_est_quoi_ce_monde_player2, statut_c_est_quoi_ce_monde_player2_pos)
                    screen.blit(titre_statut_c_est_quoi_ce_monde_player2_img, titre_statut_c_est_quoi_ce_monde_player2_pos)
                if succès_frôlements_caché_player_2 :
                    screen.blit(virtual_insanity_player2_img, virtual_insanity_player2_pos)
                    screen.blit(statut_virtual_insanity_player2, statut_virtual_insanity_player2_pos)
                    screen.blit(titre_statut_virtual_insanity_player2_img, titre_statut_virtual_insanity_player2_pos)
                if succès_collectibles_caché_player_2 :
                    screen.blit(la_peace_player2_img, la_peace_player2_pos)
                    screen.blit(statut_la_peace_player2, statut_la_peace_player2_pos)
                    screen.blit(titre_statut_la_peace_player2_img, titre_statut_la_peace_player2_pos)
                screen.blit(bt_retour, bt_retour_pos)
                screen.blit(titre_bt_retour_img, titre_bt_retour_pos)



    pygame.display.flip()
    clock.tick(60)

pygame.quit