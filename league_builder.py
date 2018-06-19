import csv

players = []
sharks = []
dragons = []
raptors = []
yes = []
no = []

# This is the extra credit function.
# I made a list of dates, one for each team.
# I knew that in each list (sharks, raptors, dragons) the first index was the name of the team.
# So I said, if the name of i[0] is == to the team word, then assign this part of a list to this start variable.
def welcome(i):

    PRACTICE_DATES = ["1st of September, 2018", "3rd of September, 2018", "5th of September, 2018"]
    if i[0] == "Sharks":
        start = ''.join(PRACTICE_DATES[0])

    elif i[0] == "Raptors":
        start = ''.join(PRACTICE_DATES[1])

    elif i[0] == "Dragons":
        start = ''.join(PRACTICE_DATES[2])

    else:
        start = "Team"
    # Here I itterated through the list, except the first item in the list, I assigned variables.
    # I knew that it followed the format ["name", "something", "guardian", etcetc]
    for thing in i[1:]:
        name = thing[0]
        guardian = thing[3]
        file_name = ''.join(name.lower())
        file_name = file_name.replace(" ", "_")

        with open(file_name +'.txt', 'a') as individual:
            individual.write("Dear "+ ''.join(guardian) + ", your child {} has done excellent and has made it into the {}. They will begin practice on {}.".format(name, i[0], start))

# This is the part where I created my team.txt.
# I set it to append so that everything tea.write wrote, would be appending to the txt file.
def csvinput(x):
    with open("teams.txt", "a") as team:
        team.write(str(x[0]+ '\n\n'))
        for thing in x[1:]:
            team.write(', '.join(thing) + '\n')
        team.write('\n')


def main():

    # Here I have imported the csv file and put it into a list.
    # Player is a list of all the childrens information, it also has the main headers at index 0.
    with open("soccer_players.csv", newline='') as newcsv:
        player = csv.reader(newcsv, delimiter=',')
        players = list(player)


    # As mentioned above, I realised the first thing in the list is the coloumn headers,
    # so I removed the headers so that the only thing that remains is the players themselves
    del players[0]


    # Here is where I figure out how many players there are that have yes and how many have no.
    # I then separate them into two variables
    for header in players:
        # I figured out that the experience header was at index 2
        if header[2] == 'NO':
            no.append(header)
        else:
            yes.append(header)


    # I loop through each of the variables yes and no. One by one until they are empty,
    # thus distributing the experienced and non experienced players eqaully.
    while len(yes) > 1 or len(no) > 1:
        sharks.append(yes.pop())
        raptors.append(yes.pop())
        dragons.append(yes.pop())
        sharks.append(no.pop())
        raptors.append(no.pop())
        dragons.append(no.pop())
    else:
        # Once all of the team members have been given teams, I insert the team names into the list variables,
        # and place them at the front of the lists, so that they will be shown first.
        sharks.insert(0, "Sharks")
        raptors.insert(0, "Raptors")
        dragons.insert(0, "Dragons")

    # I use my function to append each team to the file 'teams.txt'.
    csvinput(sharks)
    csvinput(raptors)
    csvinput(dragons)


if __name__ == '__main__':
    main()
    welcome(sharks)
    welcome(raptors)
    welcome(dragons)
