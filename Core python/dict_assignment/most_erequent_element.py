# 🎒 Step 1: List of items
items = ["apple", "banana", "apple", "orange", "banana", "apple", "grape", "orange", "apple"]

# 🟢 Step 2: Create a dictionary to count occurrences
count_dict = {}

for item in items:
    if item in count_dict:
        count_dict[item] += 1  # Increment count if item exists
    else:
        count_dict[item] = 1   # Initialize count for new item

# 🔍 Step 3: Find the most frequent element
most_frequent = max(count_dict, key=count_dict.get)
highest_count = count_dict[most_frequent]

# 📊 Step 4: Display results
print("\n📈 Item Frequency:")
for item, count in count_dict.items():
    print(f"{item}: {count} times")

print(f"\n🏆 Most Frequent Item: '{most_frequent}' (Occurred {highest_count} times)")
