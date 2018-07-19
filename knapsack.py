#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  # !!!! IMPLEMENT ME
  # Brute Force Solution 

  # Recursively checking all combinations of items
  # Inputs: items, capacity, total value, bag items
  # Returns: the resulting value and the bag array of 
  # taken items
  
  """
  Brute force checks every possible combination 
  of items we could be taking and outputs the 
  combination with the best value. A single 
  recursive call will represent us picking up 
  the next item in the pile and deciding whether
  we want to add it to our bag or not.  

  Steps 
  =====
  
  1. Use recursion to exhaustively check every
  single conbination. 
  
  2. Base 1: We have no more items in the pile. 
  
  3. Base 2: We have one item left in the pile.
  Check to see if it fits in out bag's remaining 
  capacity. If it does, take it. Otherwise discard 
  it.  
  
  4. Calculate the overall value we have in our 
  knapsack if we take the item. 
  
  5. Calculate the overall value we have in our 
  knapsack if we do not take the item. 
  
  6. Compare the two resulting values: take the option 
  with the larger value. 
  """
  def knapsack_helper(items, capacity, value, bag): 
    if not items: 
      return value, bag
    elif len(items) == 1: 
      # Check if the last item fits or not 
      if items[0].size <= capacity: 
        # Take the item by setting its index in 'bag' to 1
        bag[items[0].index - 1] = 1 
        # Update our total value for taking this item 
        value += items[0].value 
        return value, bag
      else:
        # last item does not fit, just discard it 
        return value, bag 
    # We still have a bunch of items to consider
    # Chech to see if the item we just picked up fits
    # in our remaining bag capacity 
    elif items[0].size <= capacity: 
      # We can consider the overall value of this item
      # Make a copy of our bag 
      bag_copy = bag[:]
      bag_copy[items[0].index - 1] = 1
      r1 = knapsack_helper(items[1:], capacity - items[0].size, value + items[0].value, bag_copy)
      # We do not take the item in this universe 
      r2 = knapsack_helper(items[1:], capacity, value, bag)
      # Pick the universe that results in a larger value 
      return max(r1, r2, key=lambda tup: tup[0])
    else: 
    # Item does not fit, discard it and continue recursing 
      return knapsack_helper(items[1:], capacity, value, bag)
  # Call knapsack_helper function 
  return knapsack_helper(items, capacity, 0, [0] * len(items))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')