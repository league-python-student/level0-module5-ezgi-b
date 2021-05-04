"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk

def pet_feed(pet):
    if pet == "dog":
        print("You gave your dog food. It was very happy and wagged its tail a lot!")
        return 3
    if pet == "cat":
        print("You gave your cat food. It was pretty happy.")
        return 2
    if pet == "fish":
        print("You gave your fish food. It was sort of happy.")
        return 1
    if pet == "hamster":
        print("You gave your hamster food. It stuffed its cheeks and was very happy!")
        return 3

def pet_walk(pet):
    if pet == "dog":
        print("You gave took your dog on a walk. It wagged its tail all the time!")
        return 3
    if pet == "cat":
        print("You took your cat on a walk. It very was unimpressed and hated its collar.")
        return -3
    if pet == "fish":
        print("You tried to take your fish on a walk. It's water spilled all over the ground as you walked.")
        return -5
    if pet == "hamster":
        print("You took your hamster on a walk. It was scared of all the dogs it saw.")
        return -5

def pet_play(pet):
    if pet == "dog":
        print("You played frisbee and fetch with your dog. It was super happy and excited!")
        return 5
    if pet == "cat":
        print("You played with your cat by making it chase a laser.")
        return 3
    if pet == "fish":
        print("You tried to play with your fish by tapping on the glass. It was not happy.")
        return -1
    if pet == "hamster":
        print("You played with your hamster. It liked crawling over your hands.")
        return 3

def pet_pet(pet):
    if pet == "dog":
        print("You pet your dog. It was happy!")
        return 2
    if pet == "cat":
        print("You pet your cat. It started purring")
        return 3
    if pet == "fish":
        print("You tried pet your fish. It didn't like being poked")
        return -3
    if pet == "hamster":
        print("You pet your hamster. It was happy.")
        return 3


if __name__ == '__main__':
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!
    window = Tk()
    window.withdraw()
    pet = simpledialog.askstring(None, "What type of pet do you want? (dog, cat, fish, hamster)").lower()
    happiness = 5
    print("Happiness: " + str(happiness))
    while happiness != 10:
        activity = simpledialog.askstring(None, "What activity do you want to do? (Feed, Walk, Play, Pet)")
        if activity.lower() == "feed":
            happiness += pet_feed(pet)
        if activity.lower() == "walk":
            happiness += pet_walk(pet)
        if activity.lower() == "play":
            happiness += pet_play(pet)
        if activity.lower() == "pet":
            happiness += pet_pet(pet)
        if happiness > 10:
            happiness = 10
        print("Happiness: " + str(happiness))
