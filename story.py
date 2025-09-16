def intro():
    print("You wake up falling from the sky, hundreds of miles per hour.")
    print("You notice a parachute backpack to your RIGHT.")
    print("You notice your best friend to your LEFT.")
    print("Below you, a shimmering rift opens at the CENTER.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You flail in indecision. The wind howls…and the moment passes.")

def left_path():
    print("You veer left toward your best friend, hoping you can help.")

def right_path():
    print("You dive right toward the parachute backpack.")

def center_path():
    print("You aim for the rift—time slows, colors smear, and you pass into a quiet void.")
    print("A voice whispers: 'Not yet.' You’re flung back into the sky, wiser and scared.")

if __name__ == "__main__":
    intro()
