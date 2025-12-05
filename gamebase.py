from engine import (
    create_party,
    get_winner,
    make_ai_move
)

def print_grid(party:dict):
    for i in range (6): #lignes
        line = "|"
        for j in range (7): #colonnes
            line += "| "
            try :
                line += party[j][5-i]
            except IndexError:
                line += " "
            line += " "
        line += "||"
        print(line)
        print("-"*30)
    print("   0   1   2   3   4   5   6")
        

def human_turn(party:dict):
    print_grid(party)
    has_played=False
    while not has_played:
        column = input("Veuillez entrer le n° de la colonne dans lequel glisser votre token.")
        try:
            move = int(column)
        except ValueError:
            print("Reste concentré...")
            continue
        if not 0 <= move <= 6:
            print("J'aime ton enthousiasme, mais il va falloir se cadrer un peu...")
            continue
        if len(party[move]) < 6:
            party[move].append("X")
            has_played=True
        else:
            print("Cette colonne est déjà pleine, ce coup est complètement stupide. Recommence.")
            continue

def play_game():
    party = create_party()
    while get_winner(party) is None:
        party, move, nodes = make_ai_move(party)
        print(f"[IA] joue en {move}")
        print(f"[IA] Noeuds explorés : {nodes}")
        winner = get_winner(party)
        if winner is not None:
            break
        
        human_turn(party)
        winner = get_winner(party)
        if winner is not None:
            break
    print_grid(party)
    winner = get_winner(party)
    if winner == "draw":
        print("C'est un match nul !")
    elif winner == "X":
        print("C'est Sara qui gagne... T_T")
    else:
        print("HAHAHAHAHAHAHAHAHAHA C'EST QUI L'PATRON ?!!")

if __name__ == "__main__":
    play_game()