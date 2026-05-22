import random
import time
import sys

# Erhöht das Rekursionslimit in Python, um tiefere Bäume zu ermöglichen 
sys.setrecursionlimit(20000)

class GameNode:
    def __init__(self, depth, branching_factor, current_depth=0):
        self.current_depth = current_depth
        self.children = []
        self.value = None

        # Wenn wir am Blattknoten (Leaf) angekommen sind, weisen wir einen zufälligen Wert zu
        if current_depth == depth:
            self.value = random.randint(-100, 100)
        else:
            # Sonst erstellen wir die Kindknoten (Branching)
            for _ in range(branching_factor):
                self.children.append(GameNode(depth, branching_factor, current_depth + 1))

def minimax(node, is_maximizing, counter):
    counter['visited'] += 1
    
    # Basis-Fall: Blattknoten erreicht
    if not node.children:
        return node.value

    if is_maximizing:
        best_val = float('-inf')
        for child in node.children:
            value = minimax(child, False, counter)
            best_val = max(best_val, value)
        return best_val
    else:
        best_val = float('inf')
        for child in node.children:
            value = minimax(child, True, counter)
            best_val = min(best_val, value)
        return best_val

def alpha_beta(node, alpha, beta, is_maximizing, counter):
    counter['visited'] += 1
    
    #Basis-Fall: Blattknoten erreicht
    if not node.children:
        return node.value

    if is_maximizing:
        best_val = float('-inf')
        for child in node.children:
            value = alpha_beta(child, alpha, beta, False, counter)
            best_val = max(best_val, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                counter['pruned'] += 1
                break  # Beta-Cutoff (Pruning)
        return best_val
    else:
        best_val = float('inf')
        for child in node.children:
            value = alpha_beta(child, alpha, beta, True, counter)
            best_val = min(best_val, value)
            beta = min(beta, value)
            if beta <= alpha:
                counter['pruned'] += 1
                break  # Alpha-Cutoff (Pruning)
        return best_val

def run_benchmark():
    print("=== Game Theory Tree Search Benchmark ===")
    
    # Benutzereingabe
    try:
        branching = int(input("Branching-Faktor (Breite des Baums, z.B. 4): "))
        depth = int(input("Tiefe des Baums (z.B. 6 oder 7): "))
    except ValueError:
        print("Bitte valide Zahlen eingeben.")
        return

    print(f"\nGeneriere Baum (Tiefe: {depth}, Branching: {branching})...")
    start_tree = time.perf_counter()
    root = GameNode(depth, branching)
    end_tree = time.perf_counter()
    print(f"Baum erfolgreich generiert in {end_tree - start_tree:.4f} Sekunden.")
    
    # 1. Minimax Benchmark
    minimax_counter = {'visited': 0}
    start_time = time.perf_counter()
    minimax_res = minimax(root, True, minimax_counter)
    end_time = time.perf_counter()
    minimax_time = end_time - start_time

    # 2. Alpha-Beta Benchmark
    ab_counter = {'visited': 0, 'pruned': 0}
    start_time = time.perf_counter()
    ab_res = alpha_beta(root, float('-inf'), float('inf'), True, ab_counter)
    end_time = time.perf_counter()
    ab_time = end_time - start_time

    # Auswertung und Ergebnisse
    print("\n" + "="*30)
    print("ERGEBNISSE:")
    print("="*30)
    print(f"Bester Utility-Wert (Minimax):    {minimax_res}")
    print(f"Bester Utility-Wert (Alpha-Beta): {ab_res}  \n")
    
    print(f"--- Reines Minimax ---")
    print(f"Besuchte Knoten: {minimax_counter['visited']:,}")
    print(f"Benötigte Zeit:  {minimax_time:.6f} Sekunden")
    
    print(f"\n--- Alpha-Beta Pruning ---")
    print(f"Besuchte Knoten: {ab_counter['visited']:,}")
    print(f"Abgeschnittene Äste (Cutoffs): {ab_counter['pruned']:,}")
    print(f"Benötigte Zeit:  {ab_time:.6f} Sekunden")
    
    # Effizienz-Berechnung 
    saved_nodes = minimax_counter['visited'] - ab_counter['visited']
    if minimax_counter['visited'] > 0:
        pct_saved = (saved_nodes / minimax_counter['visited']) * 100
        print(f"\nEffizienz-Gewinn: Alpha-Beta hat {pct_saved:.2f}% weniger Knoten besucht!")

if __name__ == "__main__":
    run_benchmark()