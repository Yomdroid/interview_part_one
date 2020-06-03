"""There are n people lined up, and each have a height represented as an integer. A murder has
happened right in front of them, and only people who are taller than everyone in front of them are
able to see what has happened. How many witnesses are there?"""

def witnesses(heights):
  maximum_height = 0
  no_of_witnesses = 0
  for i in range(len(heights) - 1,-1,-1):
    if heights[i] > maximum_height:
      no_of_witnesses += 1
    maximum_height = max(heights[i], maximum_height)
  return no_of_witnesses

print(witnesses([3, 6, 3, 4, 1]))