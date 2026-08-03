txns = [
    ["Milk", "Bread"],
    ["Milk", "Eggs"],
    ["Milk", "Bread", "Butter"],
    ["Bread", "Butter"],
    ["Milk", "Bread"]
]
itemset = {"Milk", "Bread"}
count = sum(1 for t in txns if itemset.issubset(t))
print("Support:", count / len(txns))
