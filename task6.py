items = {
    "pizza":   {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi":   {"cost": 10, "calories": 100},
    "cola":    {"cost": 15, "calories": 220},
    "potato":  {"cost": 25, "calories": 350}
}

# Реалізую жадібний алгоритм: максимізую калорії/вартість
def greedy_algorithm(items, budget):
    ratio = {name: data["calories"]/data["cost"] for name, data in items.items()}
    # відсортовую за співвідношенням
    sorted_items = sorted(items.items(), key=lambda x: ratio[x[0]], reverse=True)
    chosen = []
    spent = 0
    for name, data in sorted_items:
        if spent + data["cost"] <= budget:
            chosen.append(name)
            spent += data["cost"]
    return chosen, spent, sum(items[n]['calories'] for n in chosen)

# Реалізую динамічне програмування (подібне до «рюкзака»)
def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)
    # dp[i][w] – макс калорії, використовуючи перші i предметів з бюджетом w
    dp = [[0]*(budget+1) for _ in range(n+1)]
    for i in range(1, n+1):
        cost = items[names[i-1]]["cost"]
        cal = items[names[i-1]]["calories"]
        for w in range(budget+1):
            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + cal)
            else:
                dp[i][w] = dp[i-1][w]
    # Відновлюю набір
    w = budget
    chosen = []
    for i in range(n,0,-1):
        if dp[i][w] != dp[i-1][w]:
            name = names[i-1]
            chosen.append(name)
            w -= items[name]["cost"]
    chosen.reverse()
    spent = sum(items[n]['cost'] for n in chosen)
    calories = dp[n][budget]
    return chosen, spent, calories

if __name__ == "__main__":
    BUDGET = 100
    print("Бюджет:", BUDGET)
    ch_g, cost_g, cal_g = greedy_algorithm(items, BUDGET)
    print("\nЖадібний результат:", ch_g, "витрачено", cost_g, "калорії", cal_g)

    ch_d, cost_d, cal_d = dynamic_programming(items, BUDGET)
    print("\nДП результат:", ch_d, "витрачено", cost_d, "калорії", cal_d)

