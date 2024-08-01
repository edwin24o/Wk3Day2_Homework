# Objective:
# The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, ranging from basic operations to advanced manipulations and best practices. You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative thinking and problem-solving.

# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# 1 - Destinations that both airlines fly to.
# 2 - Destinations unique to your airline.
# 3 - Whether there are any destinations that neither airline shares.
# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#-- 1 
same_routes = our_routes.intersection(competitor_routes)
print(f"Similar destinations: {same_routes}")
print("="* 50)

#-- 2
print(our_routes.difference(competitor_routes))
print("="* 50)

#-- 3
dont_share = our_routes.symmetric_difference(competitor_routes)
print(f"Neither airline shares: {dont_share}")