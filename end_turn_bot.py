from button_helpers import *
import time
import sys

# INITIALIZE VARIABLES FOR VERY START OF PROGRAM
game_counter = 0
current_turn = 0
previous_turn = 0


# FIND WHAT SCREEN WE'RE ON
def locate_screen():
    attempts = 0
    while attempts < 3:
        move_mouse_away()
        if play_button_visible():
            return "home"
        elif cancel_button_visible():
            return "matchmaking"
        elif retreat_button_visible():
            return "in game"
        elif collect_rewards_visible():
            return "end"
        elif next_button_visible():
            return "results"
        elif season_pass_screen():
            close_season_pass()
        attempts += 1
        if attempts != 3:
            time.sleep(1)
    sys.exit("Unable to locate screen after 3 attempts.")


# STARTS THE GAME
def reset_loop():
    global game_initialized
    global current_turn
    global current_screen
    global previous_turn

    game_initialized = False
    current_turn = 0
    current_screen = "home"
    previous_turn = 0
    move_mouse_away()


current_screen = locate_screen()
if current_screen != "home" and current_screen != "matchmaking":
    game_initialized = True
else:
    game_initialized = False

print("Beginning program...")

while 1:
    while current_screen == "home":
        current_screen = locate_screen()
        if play_button_visible():
            print("Starting a new match!")
            time.sleep(0.5)
            try:
                click_play_button()
            except:
                current_screen = locate_screen()
            time.sleep(1)
        if cancel_button_visible():
            print("Matchmaking started.")
            current_screen = "matchmaking"
            time.sleep(1)

    while current_screen == "matchmaking":
        if cancel_button_visible():
            print("Searching for opponent...")
            time.sleep(2)
        else:
            print("Opponent found, setting up game")
            current_screen = "in game"

    if not game_initialized:
        error_counter = 0
        while not retreat_button_visible():
            print("Game is still being setting up.")
            move_mouse_away()
            time.sleep(1)
            error_counter += 1
            if error_counter > 9:
                current_screen = locate_screen()
        print("Game has begun!")
        current_turn = 1
        game_initialized = True
        time.sleep(5)

    while current_screen == "in game":
        turn_status = end_turn_button_text()

        match turn_status:
            case "end turn":
                print("Ending turn " + str(current_turn) + ".")
                current_turn += 1
                try:
                    end_turn()
                except:
                    print("Hold on, something went wrong...")
                    time.sleep(5)
                    current_screen = locate_screen()
            case "playing":
                print("Turn is currently being played.")
            case "waiting":
                print("Waiting for opponent to move.")
            case "unknown":
                print("Waiting for turn " + str(current_turn - 1) + " to finish.")

        time.sleep(5)

        if not retreat_button_visible():
            if collect_rewards_visible():
                current_screen = "end"

    if current_screen == "end":
        collect_rewards()
        current_screen = "results"

    if current_screen == "results":
        while not next_button_visible():
            print("Collecting rewards...")
            time.sleep(3)
        click_next_button()

    print("Match completed!")
    game_counter += 1
    print("We have now completed " + str(game_counter) + " games.")

    reset_loop()

    while not play_button_visible():
        time.sleep(1)
