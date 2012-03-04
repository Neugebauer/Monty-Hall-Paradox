##Monty Hall Paradox
##proof that switching doors is the better move
##Brian Neugebauer 3/4/2012
##Had to write this to prove it to my friend. 
##
##Suppose you're on a game show (like Let's Make A Deal hosted by Monty Hall),
##and you're given the choice of three doors:
##Behind one door is a car; behind the others, goats.
##You pick a door, say No. 1 [but the door is not opened], and the host,
##who knows what's behind the doors, opens another door, say No. 3,
##which has a goat. He then says to you, "Do you want to pick door No. 2?"
##Is it to your advantage to switch your choice?
import random
stayWins = 0;
switchWins = 0;
trials = 100000;

for t in range(0,trials):
    Doors = ["Goat","Goat","Car"]
    random.shuffle(Doors)
    ##Choose your door randomly (2nd level of randomness, for your protection)
    firstChoice = random.choice(Doors)
    Doors.remove(firstChoice)
    ##Monty reveals a goat from the remaining doors
    Doors.remove("Goat")
    ##You can stay with your firstChoice or switch to the remaining door
    if firstChoice == "Car":
        stayWins += 1;
    elif Doors[0] == "Car":
        switchWins += 1;

print "stayWins: %d switchWins: %d" % (stayWins,switchWins)
print "Switching gives %f%% chance to win" % (switchWins/(trials/100.0))

 
