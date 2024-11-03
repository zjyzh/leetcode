from collections import defaultdict
'''
用滑动窗口配合哈希表，然后需要判断最小的滑动窗口
记住在移动l的时候，情况需要多判断两次

'''


class Solution:

    # Helper function to check if all required characters are within the current window
    def include(self, curhash, thash):
        # Check if all keys and their required frequencies in `thash` are met in `curhash`
        for char in thash:
            if curhash.get(char, 0) < thash[char]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        
        # Edge case: if `t` is longer than `s`, no solution possible
        if len(t) > len(s):
            return ''

        # Edge case: if `s` and `t` are identical, return `s` as it satisfies the condition
        if s == t:
            return s

        # Initialize character frequency dictionary for `t`
        thash = {}
        for char in t:
            thash[char] = thash.get(char, 0) + 1

        # Current window character frequency
        curhash = {}

        # Initialize pointers and variables for the sliding window
        l = 0  # Left pointer for the window
        r = 0  # Right pointer for the window
        resl, resr = 0, 0  # Track the best window
        min_length = float('inf')  # Initialize with infinity for finding minimum window
        inc = False  # Indicator if any valid window was found

        # Expand the window by moving the right pointer `r`
        while r < len(s):
            cur_char = s[r]

            # Update current window frequency only if character is in `t`
            if cur_char in thash:
                curhash[cur_char] = curhash.get(cur_char, 0) + 1

                # Check if the current window contains all characters from `t`
                if self.include(curhash, thash):
                    inc = True  # Mark that a valid window has been found

                    # Try to shrink the window from the left
                    while l <= r and (s[l] not in thash or curhash[s[l]] > thash[s[l]]):
                        # Decrease the frequency of `s[l]` in the current window
                        if s[l] in curhash and curhash[s[l]] > thash[s[l]]:
                            curhash[s[l]] -= 1
                        l += 1  # Move the left pointer right

                    # Update result if the current window is smaller than previous best
                    window_length = r - l + 1
                    if window_length < min_length:
                        min_length = window_length
                        resl, resr = l, r

                    # Move left pointer forward after updating the result
                    curhash[s[l]] -= 1
                    l += 1  # Continue to narrow down the window

            r += 1  # Expand the window by moving right pointer

        # Return the minimum window found or an empty string if no valid window exists
        return s[resl:resr+1] if inc else ''
