# 🗳️ List of Votes (Each name represents one vote)
votes = [
    "Alice", "Bob", "Alice", "Charlie", "Alice", "Bob", "Charlie", 
    "Alice", "Bob", "Charlie", "Charlie", "Alice", "Bob"
]

# 🔄 Count votes using a dictionary
vote_count = {}

for name in votes:
    vote_count[name] = vote_count.get(name, 0) + 1

# 📊 Display vote counts
print("\n📈 Vote Count:")
for candidate, count in vote_count.items():
    print(f"{candidate}: {count} votes")

# 🏆 Find the winner
winner = max(vote_count, key=vote_count.get)
max_votes = vote_count[winner]

# 🥇 Display the winner
print(f"\n🏆 Winner: {winner} with {max_votes} votes!")
