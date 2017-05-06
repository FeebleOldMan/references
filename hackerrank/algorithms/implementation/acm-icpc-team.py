#!/usr/bin/env python

import itertools

TEST_MODE = False

def main():
  num_of_people, num_of_topics = map(int, raw_input().strip().split())
  knowledge = []
  for _i in xrange(num_of_people):
    knowledge.append(map(int, list(raw_input().strip())))
  print teamup(knowledge)

def teamup(knowledge):
  # create team combinations by permutating each player
  pairs = itertools.combinations(range(len(knowledge)), 2)
  team = []
  for pair in pairs:
    combined = []
    player_i = knowledge[pair[0]]
    player_j = knowledge[pair[1]]
    for x in range(len(knowledge[0])):
      combined.append(player_i[x] | player_j[x])
    team.append(sum(combined))
  # find max value of combined
  max_topics = max(team)
  # find number of times max value occurs
  num_of_teams = team.count(max_topics)
  return str(max_topics) +'\n'+ str(num_of_teams)

### v0.1
#def teamup(knowledge):
#  player1 = knowledge[:]
#  player2 = knowledge[:]
#  # create team combinations by permutating each player
#  team = []
#  for i, player_i in enumerate(player1):
#    for j, player_j in enumerate(player2):
#      if i != j:
#        combined = []
#        for x in range(len(player_i)):
#          combined.append(player_i[x] | player_j[x])
#        team.append(combined)
#  team = [sum(topics) for topics in team]
#  # find max value of combined
#  max_topics = max(team)
#  # find number of times max value occurs
#  num_of_teams = team.count(max_topics)/2  # division by 2 because combination technique above repeats grouping
#  return str(max_topics) +'\n'+ str(num_of_teams)

def test():
  print teamup([[1, 0, 1, 0, 1], [1, 1, 1, 0, 0], [1, 1, 0, 1, 0], [0, 0, 1, 0, 1]])
  return

test() if TEST_MODE else main()
