def intro():
    print("You wake up falling from the sky.")
    print("RIGHT: a parachute. LEFT: your best friend. CENTER: a shimmering rift.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("Hesitation is its own gravity.")

def left_path():
    print("You rocket left and link arms with your friend.")
    print("A DRAGON bursts from the clouds!")
    print("You time the fall, grab its horn, and yank—your friend pulls a flare.")
    print("The dragon reels; a rescue drone spots the flare and deploys a chute-for-two.")
    print("You land safely. Two heroes, one legend.")

def right_path():
    print("You catch the parachute midair and pop it, gliding toward safety.")

def center_path():
    print("You dip into the rift. Time slows—then kindly spits you back upward.")

if __name__ == "__main__":
    intro()
