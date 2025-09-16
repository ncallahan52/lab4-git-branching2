# Villain timeline
def intro():
    print("You wake up falling. The wind is a roar.")
    print("RIGHT: a parachute. LEFT: your best friend. CENTER: a humming rift.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("The sky judges quickly.")

def left_path():
    print("You reach for your friend, but distance grows. Your heart aches.")

def right_path():
    print("You seize the parachute—but a second pack appears with a whisper:")
    print("'Use it for yourself (self) or share it (share)? Choose.'")
    pick = input("(self/share): ").strip().lower()
    if pick == "self":
        print("You pull alone. Power feels warm; your friend spirals away.")
        print("A cold coin appears in your palm. Corruption begins.")
    else:
        print("You split the harness and angle back. The whisper fades, disappointed.")
        print("Not a villain today.")

def center_path():
    print("You glance into the rift and see a darker you smiling back. You look away.")

if __name__ == "__main__":
    intro()
