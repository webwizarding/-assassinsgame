import random
import os

def assign_targets(players):
    targets = players[:]
    random.shuffle(targets)
    assignments = {}
    for i in range(len(players)):
        if players[i] == targets[i]:
            targets[i], targets[(i+1)%len(players)] = targets[(i+1)%len(players)], targets[i]
        assignments[players[i]] = targets[i]
    return assignments

def create_files(assignments):
    for player, target in assignments.items():
        with open(f'{player}.txt', 'w') as f:
            f.write(target)

players = ["bob4", "bob3", "bob2", "bob1"]
assignments = assign_targets(players)
create_files(assignments)
