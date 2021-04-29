import time
import random
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)
def intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers")
    print_pause("Rumor has it that a dragon is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.")
def house(items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens"
                " and out steps a dragon")
    print_pause("Eep! This is the dragon's house!")
    print_pause("The dragon attacks you!")
    if "sword" in items:
        print_pause("You snsheath your new sword.")
        print_pause("The sword of Ogoroth shines brightly in your hand"
                    "as you brace yourself for the attack.")
        print_pause("But the dragon takes a look at your shiny new toy"
                    "and runs away.")
        print_pause("You have rid the town of the dragon."
                    "You are victorious!")
        play_again(items)
    else:
        print_pause("You feel a bit under-prepared for this ,"
                    "what with only having a tiny dagger")
        print_pause("Would you like to (1) fight or (2) run away?")
        action = raw_input("1\n"
                           "2\n")
        if action == '1':
            fight(items)
        elif action == '2':
            run_away(items)
def fight(items):
    print_pause("You do your best...")
    print_pause("but your dagger is not match for the dragon")
    print_pause("You have been defeated!")
    play_again(items)
def run_away(items):
    print_pause("You run back into the field."
                "Luckily, you don't seem to have been followed.")
    print_pause("You find yourself again standing in the open field")
    choose_option(items)
def cave(items):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and"
                "take the sword with you.")
    print_pause("You walk back out to the field.")
    items.append("sword")
    choose_option(items)
def choose_option(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave")
    print_pause("What would you like to do?")
    print_pause("Please enter 1 or 2")
    option = raw_input("1. House\n"
                       "2. Cave\n")
    if option == '1':
        house(items)
    elif option == '2':
        cave(items)
def play_again(items):
    print_pause("Would you like to play again?")
    again = raw_input("1. Yes\n"
                      "2. No\n")
    if again == '1':
        choose_option(items)
    elif again == '2':
        print_pause("Ok Goodbye")
def play_game():
    items = []
    intro()
    choose_option(items)
play_game()