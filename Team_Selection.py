
import json

# Opening JSON file 'Teams_RCB.json'
file = open("Teams_RCB.json")

# returns JSON object as
# a dictionary
data = json.load(file)

# Closing file
file.close()

foreign_players = []  # taking lists to append the values for counting purpose
wicket_keeper = []
india_country = 'India' # Defining constant values for comparison
wicket_keeper_role = 'Wicket-keeper'

# looping through json data
for i in data['player']:
    # checking the value of country and comparing that with value as not India ,
    # so we will get the foreign country players
    if i['country'] != india_country:
        # appending those full values in list
        foreign_players.append(i)
    # checking the value of role and comparing that with wicket-keeper
    if i['role'] == wicket_keeper_role:
        # appending those full values in list
        wicket_keeper.append(i)

# if the length of foreign_players list is equal to 4  and wicket_keeper is equal or more than 1 in the team
if len(foreign_players) == 4 and len(wicket_keeper) >= 1:
    print("Team can play")  # All the conditions satisfied for Team to play
else:
    print("Team cannot play")









