txns = [
    ["Milk", "Bread"],
    ["Milk", "Bread", "Butter"],
    ["Milk"],
    ["Bread"],
    ["Milk", "Bread"]
]

milk_count = sum(1 for t in txns if "Milk" in t)
both_count = sum(1 for t in txns if "Milk" in t and "Bread" in t)
print("Confidence:", both_count / milk_count)
