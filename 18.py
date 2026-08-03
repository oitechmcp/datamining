from itertools import combinations

txns = [
    ["Milk", "Bread", "Eggs"],
    ["Milk", "Bread"],
    ["Milk", "Eggs"],
    ["Bread", "Butter"],
    ["Milk", "Bread", "Butter"]
]
min_support = 2
items = sorted(list(set(item for t in txns for item in t)))

frequent = []
for k in range(1, len(items) + 1):
    itemsets = list(combinations(items, k))
    current = [itemset for itemset in itemsets if sum(1 for t in txns if set(itemset).issubset(t)) >= min_support]
    if not current:
        break
    frequent.extend(current)

print("Frequent Itemsets:", frequent)
