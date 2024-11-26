def circularSubarraySum(arr):
    if len(arr) == 1:
        return arr[0]
    total_sum = sum(arr)

    def kadane(arr):
        max_sum = current_sum = arr[0]
        for num in arr[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

    def min_kadane(arr):
        min_sum = current_sum = arr[0]
        for num in arr[1:]:
            current_sum = min(num, current_sum + num)
            min_sum = min(min_sum, current_sum)
        return min_sum

    max_subarray = kadane(arr)
    min_subarray = min_kadane(arr)

    if total_sum == min_subarray:
        return max_subarray

    max_circular_sum = total_sum - min_subarray
    return max(max_subarray, max_circular_sum)
