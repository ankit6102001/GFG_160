class Solution:
    def findTriplets(self, arr):
        # Your code here
        n = len(arr)
        result = set()
        mp = {}
        
        for i in range(n):
            for j in range(i + 1, n):
                pair_sum = arr[i] + arr[j]
                if pair_sum not in mp:
                    mp[pair_sum] = []
                mp[pair_sum].append((i, j))
        
        for i in range(n):
            req = -arr[i]
            if req in mp:
                for pair in mp[req]:
                    if i != pair[0] and i != pair[1]:
                        triplet = sorted([i, pair[0], pair[1]])
                        result.add(tuple(triplet))
        
        return [list(triplet) for triplet in result]
