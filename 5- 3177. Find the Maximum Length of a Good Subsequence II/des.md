# 3177. Find the Maximum Length of a Good Subsequence II


You are given an integer array nums and a non-negative integer k. A sequence of integers seq is called good if there are at most k indices i in the range `[0, seq.length - 2]` such that `seq[i] != seq[i + 1]`.

Return the maximum possible length of a good `subsequence` of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
 

## Example 1:
```c
Input: nums = [1,2,1,1,3], k = 2

Output: 4
```

Explanation:

The maximum length subsequence is `[1,2,1,1]`.

## Example 2:

```c
Input: nums = [1,2,3,4,5,1], k = 0

Output: 2
```

Explanation:

The maximum length subsequence is `[1,.....,1]`.

 

Constraints:
```c
1 <= nums.length <= 5 * 103
1 <= nums[i] <= 109
0 <= k <= min(50, nums.length)
```