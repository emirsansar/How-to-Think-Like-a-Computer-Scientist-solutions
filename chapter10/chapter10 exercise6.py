#If you don’t know how tennis scoring works, ask a friend or consult Wikipedia. A single game in tennis between player A and player B always has a score.
# We want to think about the “state of the score” as a state machine. The game starts in state (0, 0), meaning neither player has any score yet.
# We’ll assume the first element in this pair is the score for player A. If player A wins the first point, the score becomes (15, 0). If B wins the first point, the state becomes (0, 15).
# Below are the first few states and transitions for a state diagram. In this diagram, each state has two possible outcomes
# (A wins the next point, or B does), and the uppermost arrow is always the transition that happens when A wins the point. Complete the diagram, showing all transitions and all states.
