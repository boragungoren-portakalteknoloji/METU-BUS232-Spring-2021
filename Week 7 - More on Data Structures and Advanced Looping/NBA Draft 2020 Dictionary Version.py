# A program to emulate the 2020 NBA drafting
# https://www.nba.com/news/2020-nba-draft-results-picks-1-60
# Uses sets and dictionaries

players= {"Anthony Edwards", "James Wiseman", "LaMelo Ball", "Patrick Williams", "Isaac Okoro", "Onyeka Okongwu", "Killian Hayes", "Obi Toppin",
          "Dani Avdija", "Jalen Smith"}
size= len(players)
print("We've got", size, "players to draft.")
for player in players:
    print("Player", player, "is ready to be picked by a team.")

# A dictionary creates a 1-1 mapping relation between pairs of objects
# In this example we will map from the team name (A string) to the picks (set of strings)
drafts = {} # empty dictionary created easily. 
# drafts["Timberwolves"] = set()
# # ^ access key-value pair with key as "Timberwolves" in dictionary drafts
# #                      ^ assign whatever is on the right as the value part of the key-value pair
# # In effect we created an empty set, and added it to the key-value pair (KV) "Timberwolves" ----> set()
# drafts["Warriors"] = set()
# drafts["Hornets"] = set()
# drafts["Bulls"] = set()
# drafts["Cavaliers"] = set()

# It is easier to automate the creation of the individual sets for each team in a dictionary
team_names ={"Timberwolves", "Warriors", "Hornets", "Bulls", "Cavaliers"}
for team_name in team_names:
    drafts[team_name] = set()
#           ^ create KV pair so that current value of team_name ---> set()

print("Teams are preparing for the picks.")
for team in drafts:
#   ^ team variable iterates over the key set.
    print("Team:", team, "is ready to pick")

print("Timberwolves picked: ", "Anthony Edwards")
players.remove("Anthony Edwards")
drafts["Timberwolves"].add("Anthony Edwards")
#   ^ This is the set object mapped by the string "Timberwolves"
#                   ^ So when we call add(), it is called from the mapped set object
print("Timberwolves now have: ", drafts["Timberwolves"])

print("Warriors picked: ", "James Wiseman")
players.remove("James Wiseman")
drafts["Warriors"].add("James Wiseman")
print("Warriors now have: ", drafts["Warriors"])
#                              ^ Again, we access the set() object

input("Press enter to see the drafts so far")
print(drafts)

# Now let's define a function to apply the steps in a pick carefully. 
def facilitate_pick(team_name, player_name, all_drafts, all_players):
    print("Team:", team_name, "is ready to pick a player")
    if team_name in all_drafts:
        if player_name in all_players:
            all_players.remove(player_name)
            drafts[team_name].add(player_name)
            print("They picked...", player_name)
        else:
            print("There is no such player.")
            return
    else:
        print("There is no such team.")
        return
    print("Draft pick complete.")
    print("Team", team_name, "after draft pick:", drafts[team_name])
    return

facilitate_pick("Hornets", "LaMelo Ball", drafts, players)
facilitate_pick("Bulls", "Patrick Williams", drafts, players)
facilitate_pick("Bulls", "Jalen Smith", drafts, players)
facilitate_pick("Cavaliers", "Isaac Okoro", drafts, players)

input("Press enter to see the drafts so far")
print(drafts)