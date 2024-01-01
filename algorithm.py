# 1. Initialize Matrix/Hashtable to store moves and state and corresponding point values
# 2. Select a move from current game state
# 3. Make move, evaluate the move. Calculate a reward value. Reset game if move resulted in loss (but don't reset matrix)
# 4. Matrix/Hashtable at current state+move += alpha (learning rate) * reward * (some optional number that represents the current best move from that state)
# 5. Repeat 2 through 5 until win (or max iterations)