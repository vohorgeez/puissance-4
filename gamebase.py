def create_grid(party:dict):
    for i in range (6): #lignes
        line = "|"
        for j in range (7): #colonnes
            line += "| "
            try :
                line += party[j][6-i]
            except IndexError:
                line += " "
            line += " "
        line += "||"
        print(line)
        print("-"*30)
    print("   0   1   2   3   4   5   6")
        

def create_party():
    party = {}
    for i in range (7):
        party[i] = []
    return party

party = create_party()
print(party)
create_grid(party)