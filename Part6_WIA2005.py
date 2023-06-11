def find_trolley_items(items, capacity):
    n = len(items)
    dp = [0] * (capacity + 1)
    chosen = [[] for _ in range(capacity + 1)]

    item_names = {
        12: "Sack of Corn",
        5: "Hoe",
        10: "Oil Tank",
        4: "Tyre"
    }

    for i in range(n):
        weight = items[i]
        for j in range(capacity, weight - 1, -1):
            if dp[j] < dp[j - weight] + weight:
                dp[j] = dp[j - weight] + weight
                chosen[j] = chosen[j - weight] + [(weight, item_names[weight])]
                

    max_weight = dp[capacity]
    chosen_items = chosen[capacity]
    return max_weight, chosen_items

# Example usage
items = [12, 5, 10, 4, 4, 4, 4]
capacity = 30

max_weight, chosen_items = find_trolley_items(items, capacity)
print("The items carried on the trolley are:")
for weight, name in chosen_items:
    print("- {} ({} kg)".format(name, weight))
