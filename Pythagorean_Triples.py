'''Pythagorean Triples

A Pythagorean Triple is a set of integers a, b and c such that a^2 + b^2 = c^2. For example, 3, 4 and 5 are Pythagorean triples because 3^2 + 4^2 = 5^2.
Given a number n, find a Pythagorean Triple for a given sum.

For example:
Input: 12
Output: 3, 4, 5 (because 3^2 + 4^2 = 5^2, and 3 + 4 + 5 = 12)

Input: 40
Output: 8, 15, 17 (because 8^2 + 15^2 = 17^2, and 8 + 15 + 17 = 40)
 
Input: 4
Output: No Triple'''

import math
c = math.sqrt(a**2 + b**2)
