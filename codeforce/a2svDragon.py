def can_defeat_dragons(s, dragons):
  """
  Determines if Kirito can defeat all dragons.

  Args:
    s: Kirito's initial strength.
    dragons: A list of tuples (dragon_strength, bonus_strength).

  Returns:
    True if Kirito can defeat all dragons, False otherwise.
  """

  dragons.sort()  # Sort dragons by strength for greedy approach

  for dragon_strength, bonus_strength in dragons:
    if s <= dragon_strength:
      return False  # Kirito cannot defeat this dragon
    s += bonus_strength  # Increase strength after defeating the dragon

  return True  # Kirito defeated all dragons

# Input
s, n = map(int, input().split())
dragons = []
for _ in range(n):
  xi, yi = map(int, input().split())
  dragons.append((xi, yi))

# Determine and print the result
if can_defeat_dragons(s, dragons):
  print("YES")
else:
  print("NO")
