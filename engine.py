max_depth = 6

def create_party():
    party = {}
    for i in range (7):
        party[i] = []
    return party

NODES_VISITED=0

def reset_node_counter():
    global NODES_VISITED
    NODES_VISITED=0

def get_node_counter():
    global NODES_VISITED
    return NODES_VISITED

def has_won(party:dict, player):
    for i in party.keys(): #colonnes
        for j in range(len(party[i])): #ligne
            try:
                if party[i][j] == party[i+1][j] == party[i+2][j] == party[i+3][j] == player:
                    return True
            except (KeyError, IndexError):
                pass
            try:
                if party[i][j] == party[i][j+1] == party[i][j+2] == party[i][j+3] == player:
                    return True
            except (KeyError, IndexError):
                pass
            try:
                if party[i][j] == party[i+1][j+1] == party[i+2][j+2] == party[i+3][j+3] == player:
                    return True
            except (KeyError, IndexError):
                pass
            try:
                if party[i][j] == party[i-1][j+1] == party[i-2][j+2] == party[i-3][j+3] == player:
                    return True
            except (KeyError, IndexError):
                pass
    return False

def is_full(party:dict):
    full = True
    for i in party.keys():
        if len(party[i]) < 6:
            full = False
    return full

def get_winner(party:dict):
    if has_won(party, "O"):
        return "O"
    elif has_won(party, "X"):
        return "X"
    elif is_full(party):
        return "draw"
    else:
        return None
    
def terminal_evaluation(party:dict):
    winner = get_winner(party)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif winner == "draw":
        return 0
    else:
        return None
    
def minimax_ab(party:dict, is_maximizing:bool, alpha, beta, depth=0):
    global NODES_VISITED
    NODES_VISITED += 1
    score = terminal_evaluation(party)
    if score is not None:
        return score
    if depth >= max_depth:
        return 0
    if is_maximizing:
        value=float("-inf")
        for i in range (7):
            if len(party[i]) < 6:
                party[i].append("O")
                value = max(value, minimax_ab(party, False, alpha, beta, depth+1))
                party[i].pop()
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value=float("inf")
        for i in range (7):
            if len(party[i]) < 6:
                party[i].append("X")
                value = min(value, minimax_ab(party, True, alpha, beta, depth+1))
                party[i].pop()
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

def choose_best_move(party:dict):
    reset_node_counter()
    best_move = None
    best_score = float("-inf")
    for i in range (7):
        if len(party[i]) < 6:
            party[i].append("O")
            score = minimax_ab(party, False, float("-inf"), float("inf"))
            party[i].pop()
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def apply_move(party:dict, move, player):
    updated_party = {k: v.copy() for k, v in party.items()}
    updated_party[move].append(player)
    return updated_party

def make_ai_move(party:dict):
    move = choose_best_move(party)
    nodes = get_node_counter()
    updated_party = apply_move(party, move, "O")
    return updated_party, move, nodes