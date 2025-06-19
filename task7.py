import random
from collections import Counter

def monte_carlo_dice(trials=100000):
    counter = Counter()
    for _ in range(trials):
        s = random.randint(1,6) + random.randint(1,6)
        counter[s] += 1
    probabilities = {s: (cnt / trials)*100 for s, cnt in counter.items()}
    return probabilities, counter

def analytical_probabilities():
    # Обчислюю точні ймовірності
    counts = Counter()
    for i in range(1,7):
        for j in range(1,7):
            counts[i+j] += 1
    total = 36
    return {s: (cnt/total)*100 for s, cnt in counts.items()}, counts

if __name__ == "__main__":
    trials = 100000
    mc_prob, mc_counts = monte_carlo_dice(trials)
    an_prob, an_counts = analytical_probabilities()

    print("Сума | Монте‑Карло % | Аналітична %")
    for s in range(2,13):
        print(f"{s:>4} | {mc_prob.get(s,0):>12.2f} | {an_prob[s]:>11.2f}")

