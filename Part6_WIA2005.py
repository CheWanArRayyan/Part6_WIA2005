def find_trolley_items(items, capacity):
    n = len(items)
    memo = {}

    item_names = {
        12: "Sack of Corn",
        5: "Hoe",
        10: "Oil Tank",
        4: "Tyre"
    }

    def find_max_weight(i, curr_capacity):
        if i == 0 or curr_capacity == 0:
            return 0

        if (i, curr_capacity) in memo:
            return memo[(i, curr_capacity)]

        weight = items[i - 1]
        if weight > curr_capacity:
            result = find_max_weight(i - 1, curr_capacity)
        else:
            include_item = weight + find_max_weight(i - 1, curr_capacity - weight)
            exclude_item = find_max_weight(i - 1, curr_capacity)
            result = max(include_item, exclude_item)

        memo[(i, curr_capacity)] = result
        return result

    max_weight = find_max_weight(n, capacity)

    def find_chosen_items(i, curr_capacity):
        if i <= 0 or curr_capacity <= 0:
            return []

        weight = items[i - 1]
        if weight > curr_capacity:
            return find_chosen_items(i - 1, curr_capacity)

        include_item = weight + find_max_weight(i - 1, curr_capacity - weight)
        exclude_item = find_max_weight(i - 1, curr_capacity)

        if include_item > exclude_item:
            chosen = find_chosen_items(i - 1, curr_capacity - weight)
            chosen.append((weight, item_names[weight]))
            return chosen
        else:
            return find_chosen_items(i - 1, curr_capacity)

    chosen_items = find_chosen_items(n, capacity)
    return max_weight, chosen_items

# Example usage
items = [12, 5, 10, 4, 4, 4, 4]
capacity = 30

max_weight, chosen_items = find_trolley_items(items, capacity)
print("The items carried on the trolley are:")
for weight, name in chosen_items:
    print("- {} ({} kg)".format(name, weight))
