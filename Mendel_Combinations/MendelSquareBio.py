from itertools import product
from prettytable import PrettyTable
table = PrettyTable()


def create_germ_cells(input_data):
    #Changing input into groups like ("A,a", "B,b") too AB ab aB ab
    groups = [group.split(",") for group in input_data]

    # With product we get all the possible combinations between the groups
    combinations = product(*groups)

    #now we put all combos into a single list we return back
    cells = []
    for combo in combinations:
        cells.append(combo)
        cells = [''.join(tup) for tup in cells]

    return cells


def crossing(name, GC1,GC2):
    #We create the germ cells for the Allels we pass
    GC1 = create_germ_cells(GC1)
    GC2 = create_germ_cells(GC2)

    #The table.clear() is for the PrettyTable we create
    #First we clear it and then while running the programm pass new colums into it
    table.clear()
    table.add_column(name, GC2)

    solution = []
    i = 0
    while i < len(GC1):
        s = 0
        #Tablelist is for storing data for a colum 
        Tablelist = []

        while s < len(GC2):
            kombination = GC1[i] + GC2[s]
            solution.append(kombination)
            Tablelist.append(kombination)
            s = s+1

        table.add_column(GC1[i], Tablelist)
        i = i+1
    print(table)

    return solution