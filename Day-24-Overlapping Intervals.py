class Solution:
    def mergeOverlap(self, arr):
        arr.sort()
        ans = []
        ans.append(arr[0])

        for i in range(1, len(arr)):
            initial_left, initial_right = ans[-1]
            new_left, new_right = arr[i]

            if new_left <= initial_right:
                ans[-1] = [initial_left, max(initial_right, new_right)]
            else:
                ans.append(arr[i])

        return ans
