class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        d = d % n
        # for _ in range(d):
        #     first = arr[0]
        #     for i in range(1, n):
        #         arr[i - 1] = arr[i]
        #     arr[n - 1] = first
        arr[:] = arr[d:] + arr[:d]
