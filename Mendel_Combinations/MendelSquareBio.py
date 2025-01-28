userinput = "abc"


def generate_combinations(letters):
        if not letters:
              return [""]
        # Rekursive function for the rest of the letters
        first_combis = generate_combinations(letters[1:])

        # Solution list for new combinations
        combinations = []
        
        # Für jede Kombination aus der rekursiven Rückgabe füge den aktuellen Buchstaben hinzu
        for kombi in first_combis:
            combinations.append(letters[0].upper() + kombi)  # Append uppercase letters
            combinations.append(letters[0].lower() + kombi)  # Append lowercase letters

        return combinations


possible_combinations = 2**(len(userinput)*2)

with open("Mendel_Kombinationsliste.txt", "w") as file:
    combinations =generate_combinations(userinput)
    i = 0
    while i <len(combinations):
        s = 0
        while s < len(combinations):
            kombination = combinations[i] + combinations[s]
            file.write(kombination +" ")
            s = s+1

        i = i+1

print("All",possible_combinations, " combinations saved in Mendel_kombinationsliste.txt")
