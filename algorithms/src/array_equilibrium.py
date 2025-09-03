def find_array_equilibrium(arr):
    index = -1

    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i+1:])

        if left_sum == right_sum:
            index = i
            break

    return index