# Write to functions in python. The first one genereates 6 integer numbers 
# between 1 and 6 inclusive. The second one calls this functions N times and counts 
# how many times each number is generated. We want to demonstrate Law of Large 
# Numbers (LLN) in probability theory with these 2 functions.

import random
from collections import Counter

def generate_six_rolls():
    """
    Purpose	: Generates 6 random integers between 1 and 6 inclusive.
			  Simulates rolling a 6-sided die 6 times.
	Input(s): none
	Outpu(s): an array of 6 integers
	Remarks	: Put additional notes here. 
    """
    return [random.randint(1, 6) for _ in range(6)]

"""
 	numbs =[0]*6
  	i = 1
  	while i<=6:
 	  numbs[i] += random.randint(1,6)
	   i+=1
    return numbs
    
"""

def demonstrate_lln(n_trials):
    """
    Calls generate_six_rolls() N times and counts the total occurrence 
    of each number (1-6) across all rolls.
    """
    total_counts = Counter()
    
    for _ in range(n_trials):
        rolls = generate_six_rolls()
        total_counts.update(rolls)
        
    # Ensure all numbers 1-6 are represented in the output, even if count is 0
    results = {num: total_counts.get(num, 0) for num in range(1, 7)}
    
    return results

# --- Demonstration ---
if __name__ == "__main__":
    # Small N
    small_n = 10
    print(f"Results for N = {small_n} trials (Total {small_n * 6} rolls):")
    small_results = demonstrate_lln(small_n)
    for num, count in small_results.items():
        percentage = (count / (small_n * 6)) * 100
        print(f"  Number {num}: {count} times ({percentage:.2f}%)")
        
    print("\n" + "="*40 + "\n")
    
    # Large N (LLN in action)
    large_n = 1000000
    print(f"Results for N = {large_n} trials (Total {large_n * 6} rolls):")
    large_results = demonstrate_lln(large_n)
    for num, count in large_results.items():
        percentage = (count / (large_n * 6)) * 100
        print(f"  Number {num}: {count} times ({percentage:.2f}%)")