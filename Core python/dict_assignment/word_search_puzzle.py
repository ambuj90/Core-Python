# 🟢 Word Dictionary to Search
word_dict = ["CAT", "DOG", "BAT", "RAT", "CAR", "COT", "ART"]

# 🟡 Letter Grid (Puzzle)
grid = [
    ['C', 'A', 'T'],
    ['D', 'O', 'G'],
    ['B', 'A', 'R']
]

# 🔄 Function to Search Words in Grid
def word_search(grid, words):
    rows, cols = len(grid), len(grid[0])
    found_words = set()

    # 🟠 Helper function to perform DFS (Depth-First Search)
    def dfs(r, c, word, visited):
        if word in words:
            found_words.add(word)

        # Explore all 8 possible directions
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
            (-1, -1), (-1, 1), (1, -1), (1, 1) # Diagonal directions
        ]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                dfs(nr, nc, word + grid[nr][nc], visited)
                visited.remove((nr, nc))

    # 🔍 Start DFS from each cell
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, grid[i][j], {(i, j)})

    return found_words

# 🚀 Find and Display Words
found_words = word_search(grid, word_dict)
print("🔍 Words found in the puzzle:", found_words)


