from prettytable import PrettyTable
table = PrettyTable()

def generate_combinations(letters):
        if not letters:
              return [""]
        # Rekursive function for the rest of the letters
        first_combis = generate_combinations(letters[1:])

        # Solution list for new combinations
        solution = []

        # Für jede Kombination aus der rekursiven Rückgabe füge den aktuellen Buchstaben hinzu
        for kombi in first_combis:
            solution.append(letters[0].upper() + kombi)  # Append uppercase letters
            solution.append(letters[0].lower() + kombi)  # Append lowercase letters

        return solution

def create_Kombinationsquadrat(combinations):
        table.add_column("Kombinationsquadrat", combinations)
        combinations2 = combinations
        Kombinationsquadrat = []
        i = 0
        while i <len(combinations):
            s = 0
            Tablelist = []
            while s < len(combinations2):
                kombination = combinations[i] + combinations2[s]
                Kombinationsquadrat.append(kombination)
                Tablelist.append(kombination)
                s = s+1

            table.add_column(combinations[i], Tablelist)
            i = i+1

        return Kombinationsquadrat



userinput = "ab"
solution = create_Kombinationsquadrat(generate_combinations(userinput))
with open("Mendel_Kombinationsliste.txt", "w") as file:
    i = 0
    while i < len(solution):
        file.write(" "+solution[i]+" ")
        i = i+1
print("Succesfully saved in txt")