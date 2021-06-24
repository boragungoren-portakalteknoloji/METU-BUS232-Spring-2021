# A program to emulate the 2020 NBA drafting
# https://www.nba.com/news/2020-nba-draft-results-picks-1-60
# Uses sets. A better version will be implemented using a dictionary later.

players={"Anthony Edwards", "James Wiseman", "LaMelo Ball", "Patrick Williams", "Isaac Okoro", "Onyeka Okongwu", "Killian Hayes", "Obi Toppin",
          "Dani Avdija", "Jalen Smith"}
size= len(players)
print("We've got", size, "players to draft.")
# There is no order in a set.
# We use a for-each loop 
for player in players:
    print("Player", player, "is ready to be picked by a team.")

list_players = list(players)
# ^ This is ordered.
new_set = set(list_players)
#           ^ creates a set bject

print("Now waiting for the teams to announce their picks.")
# initial sets for teams. empty sets are created by calling set() with no parameter
timberwolves= set()
#              ^ without parameters empty set. 
# timberwolves = {} # this creates a dictionary! So please be careful about using set()
#              ^ {} literals is reserved for dictionaries, like [] reserved for lists
warriors = set()
hornets = set()
bulls = set()
cavaliers = set()

print("Set of players: ", players)
print("Timberwolves picked: ", "Anthony Edwards")
players.remove("Anthony Edwards")
#               ^ Find and remove this item from the set
#               We have to know (have a handle/reference to) the item we will remove.
# 
timberwolves.add("Anthony Edwards")
#             ^ add given item to set
print("Players not yet picked: ", players)
print("Timberwolves has now: ", timberwolves)
# Let's try to add Anthony once more
timberwolves.add("Anthony Edwards")
# Re-adding an item has no effect. 
print("I repeat, Timberwolves has now: ", timberwolves)

print("Warriors picked: ", "James Wiseman")
players.remove("James Wiseman")
warriors.add("James Wiseman")
print("Set of players: ", players)
print("Warriors (1): ", warriors)

# let's check if James Wiseman is in Timberwolves?
if "James Wiseman" in timberwolves:
    print("James Wiseman in Timberwolves")
else:
    print("James Wiseman not in Timberwolves")
    
print("Enabling Fantasy Basketball mode.")
print("Timberwolves decided to acquire Warriors' picks. All their picks are now Timberwolves'")
# We will use set union operation to create a new set that represents the union of both teams.
# Then we will assign this new set onto timberwolves.
timberwolves=timberwolves.union(warriors)
#               ^ this is our reference set
#                         ^ the function starts with timberwolves (reference set) and adds all items in timberwolves in a temporary set
#                           temporary set becomes {"Anthony Edwards"}
#                           then, it goes on toward the other set (warriors), and adds all items in warriors to the same temp. set.
#                           temporary set becomes {"Anthony Edwards", "James Wiseman"}
#                           then the function returns this temporary set
#           ^ with the assignment, timberwolves now is {"Anthony Edwards", "James Wiseman"}
#             the set warriors remains untouched
# Warriors are supposed to have lost all their picks, so let's clear their set
warriors.clear()
#         ^ "James Wiseman" disappears from warriors, but it is still in timberwolves. 
print("Timberwolves now:", timberwolves)
# output:
# Timberwolves now: {'Anthony Edwards', 'James Wiseman'}
print("Warriors now:", warriors)
# output:
# Warriors now: set()
#                ^ this is a bit peculiar, but since there is no literals for an empty set, we make do with set()