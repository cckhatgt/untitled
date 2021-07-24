
import pandas as pd
import pulp as pp
import numpy as np;

netflixData = pd.read_csv("data/netflix_titles.csv")
print(netflixData.head());
print(len(netflixData))
print(netflixData.info())

print(netflixData[['show_id', 'title']])
print("This is a testing line. \nLet'try again. ")

my_lp_problem = pp.LpProblem("My LP Problem", pp.LpMaximize)

x = pp.LpVariable('x', lowBound=0, cat='Continuous')
y = pp.LpVariable('y', lowBound=2, cat='Continuous')

# Objective function
my_lp_problem += 4 * x + 3 * y, "Z"

# Constraints
my_lp_problem += 2 * y <= 25 - x
my_lp_problem += 4 * y >= 2 * x - 8
my_lp_problem += y <= 2 * x - 5


my_lp_problem.solve()
print(pp.LpStatus)
print(my_lp_problem.status)
print(pp.LpStatus[my_lp_problem.status])

for variable in my_lp_problem.variables():
    print("This is solution: ", variable.name ,  "=",  variable.varValue);

print("Objective Value =", pp.value(my_lp_problem.objective))

assignments = [(i, j, k) for i in range(1, 3) for j in range(1, 6) for k in range(1, 3)]
print(len(assignments))
for thistuple in assignments:
    if (thistuple[2] == 2):
        print(thistuple[0], "==", thistuple[1], "==",thistuple[2])

print(pp.LpSolverDefault)
print(pp.PULP_CBC_CMD().available())


rooms = {'A': 100,
         'B': 50,
         'C': 50};

talks = {
    'Introduction to Python': 30,
    'Introduction to JavaScript': 30,
    'Introduction to C#': 60,
    'Introduction to Java': 90,
    'Introduction to C': 90
};


slots = [
    ('A', 0, 30),
    ('A', 30, 60),
    ('A', 90, 60),
    ('B', 0, 30),
    ('B', 30, 90),
    ('B', 120, 30),
    ('C', 0, 90),
    ('C', 90, 60)
];

problem = pp.LpProblem('Conference schedule', sense=pp.LpMaximize)

assign = {
    (talk, slot): pp.LpVariable('%r in slot %r' %
                  (talk, slot),
                cat=pp.LpBinary)
    for talk in talks
    for slot in slots
};

print(assign)

#Add slot constraints.
for slot in slots:
    problem.addConstraint(sum(assign[(talk, slot)] for talk in talks)<=1);

#Add talk constraints.
for talk in talks:
    problem.addConstraint(sum(assign[(talk, slot)] for slot in slots)==1);
    problem.addConstraint(sum(slot[2]*assign[(talk, slot)] for slot in slots)==talks[talk]);

#Talk must start later:

talk = 'Introduction to Python'
for slot in slots:
    if slot[1] < 90:
        problem.addConstraint(assign[(talk, slot)]==0);

talk_same_speaker = [
    'Introduction to C#',
    'Introduction to Java'
]

slots = [
    ('A', 0, 30),
    ('A', 30, 60),
    ('A', 90, 60),
    ('B', 0, 30),
    ('B', 30, 90),
    ('B', 120, 30),
    ('A', 0, 90),
    ('A', 90, 60)
]



blocks = {
    (room, start) : None
    for room in sorted(rooms)
    for start in range(0, 150, 30)


}

block_assign = {
    (talk, block): pp.LpVariable('%r in block %r' %
                                 (talk, block), cat=pp.LpBinary)

    for talk in talks
    for block in blocks
};

#Find blocks per slot
blocks_per_slot = {};
for slot in slots:
    room, start, duration = slot;
    slot_blocks = [];
    for block_time in range(start, start+duration, 30):
        blocks[(room, block_time)] = slot
        slot_blocks.append((room, block_time);
    blocks_per_slot[slot] = slot_blocks;


#Find blocks per start time
time_blocks = {
    start : [(room, start)
             for room in sorted(rooms)]
    for start in range(0, 150, 30)
}

#Add slot constraints:
for slot in slots:

    #Each slot may only be assigned at most once.
    problem.addConstraint(
        sum(assign[(talk, slot)] for talk in talks) <=1)

    #Tie the blocks to the corresponding slots
    for block in blocks_per_slot[slot]:
        for talk in talks:
        problem.addConstraint(assign[(talk, slot)] == block_assign[(talk, block)])


