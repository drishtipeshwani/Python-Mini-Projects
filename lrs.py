# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 21:25:14 2021

@author: Hrithik Sawhney

Longest Repeated Subsequence 

Time Complexity : O(n^2) 
Auxiliary Space : O(n^2)
"""
# Python3 program to find the
# longest repeated subsequence

# This function mainly returns LCS(str, str)
# with a condition that same characters
# at same index are not considered.
def longestRepeatedSubSeq(str):
	n = len(str)
	dp = [[0 for i in range(n+1)] for j in range(n+1)]
	
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if (str[i-1] == str[j-1] and i != j):
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i][j-1], dp[i-1][j])

	# This part of code finds the result
	# string using dp[][] Initialize result
	res = ''

	# Traverse dp[][] from bottom right
	i = n
	j = n
	while (i > 0 and j > 0):
		# If this cell is same as diagonally
		# adjacent cell just above it, then
		# same characters are present at
		# str[i-1] and str[j-1]. Append any
		# of them to result.
		if (dp[i][j] == dp[i-1][j-1] + 1):
			res += str[i-1]
			i -= 1
			j -= 1

		# Otherwise we move to the side
		# that gave us maximum result.
		elif (dp[i][j] == dp[i-1][j]):
			i -= 1
		else:
			j -= 1

	# Since we traverse dp[][] from bottom,
	# we get result in reverse order.
	res = ''.join(reversed(res))
	
	return res
	
# Driver Program
str = 'AABEBCDD'
print(longestRepeatedSubSeq(str))

