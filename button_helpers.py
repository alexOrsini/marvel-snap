import pyautogui
import random

# FILE PATHS AND COORDINATES FOR BUTTONS
# TODO: MAKE THIS DYNAMIC FOR ANY SCREEN DIMENSION/WINDOWED MODE
play_button = 'Buttons/play button.png'
play_button_tuple = (840, 770, 220, 120)
cancel_button = 'Buttons/cancel.png'
cancel_button_tuple = (850, 920, 200, 100)
retreat_button = 'Buttons/retreat.png'
retreat_button_tuple = (590, 940, 130, 50)
end_turn_text = 'Buttons/end turn.png'
playing_text = 'Buttons/playing.png'
waiting_text = 'Buttons/waiting.png'
end_turn_tuple = (1180, 920, 150, 90)
collect_rewards_button = 'Buttons/collect rewards.png'
collect_rewards_tuple = (1170, 930, 170, 70)
next_button = 'Buttons/next.png'
next_button_tuple = (1200, 950, 130, 70)


# DETERMINES IF PLAY BUTTON IS ON SCREEN
def play_button_visible():
    if pyautogui.locateOnScreen(play_button, region=play_button_tuple, confidence=0.95) is not None:
        return True
    return False


# CLICKS THE PLAY BUTTON
def click_play_button():
    x, y = pyautogui.locateCenterOnScreen(play_button, region=play_button_tuple, confidence=0.95)
    pyautogui.click((x + random.randint(0, 15)), (y + random.randint(0, 15)))


# DETERMINES IF CANCEL BUTTON IS ON SCREEN
def cancel_button_visible():
    if pyautogui.locateOnScreen(cancel_button, region=cancel_button_tuple, confidence=0.95) is not None:
        return True
    return False


# DETERMINES IF RETREAT BUTTON IS ON SCREEN
def retreat_button_visible():
    if pyautogui.locateOnScreen(retreat_button, region=retreat_button_tuple, confidence=0.95) is not None:
        return True
    return False


# DETERMINES END TURN BUTTON TEXT
def end_turn_button_text():
    if pyautogui.locateOnScreen(end_turn_text, region=end_turn_tuple, confidence=0.80) is not None:
        return "end turn"
    elif pyautogui.locateOnScreen(playing_text, region=end_turn_tuple, confidence=0.80) is not None:
        return "playing"
    elif pyautogui.locateOnScreen(waiting_text, region=end_turn_tuple, confidence=0.80) is not None:
        return "waiting"
    return "unknown"


# ENDS OUR TURN
def end_turn():
    x, y = pyautogui.locateCenterOnScreen(end_turn_text, region=end_turn_tuple, confidence=0.80)
    pyautogui.click((x + random.randint(0, 15)), (y + random.randint(0, 15)))


# DETERMINES IF COLLECT REWARDS BUTTON IS ON SCREEN
def collect_rewards_visible():
    if pyautogui.locateOnScreen(collect_rewards_button, region=collect_rewards_tuple, confidence=0.95) is not None:
        return True
    return False


# CLICKS THE PLAY BUTTON
def collect_rewards():
    x, y = pyautogui.locateCenterOnScreen(collect_rewards_button, region=collect_rewards_tuple, confidence=0.95)
    pyautogui.click((x + random.randint(0, 15)), (y + random.randint(0, 15)))


# DETERMINES IF NEXT BUTTON IS VISIBLE
def next_button_visible():
    if pyautogui.locateOnScreen(next_button, region=next_button_tuple, confidence=0.95) is not None:
        return True
    return False


# CLICKS THE PLAY BUTTON
def click_next_button():
    x, y = pyautogui.locateCenterOnScreen(next_button, region=next_button_tuple, confidence=0.95)
    pyautogui.click((x + random.randint(0, 15)), (y + random.randint(0, 15)))
