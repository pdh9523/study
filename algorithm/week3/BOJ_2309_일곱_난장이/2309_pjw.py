def generate_subsets(nums):
    subsets = []

    def backtrack(start, current_subset):
            if len(current_subset) == 7:
                subsets.append(current_subset[:])

            for i in range(start, len(arr)):
                current_subset.append(arr[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
            
    backtrack(0, [])
    return subsets
arr = []
for i in range(9):
    N = int(input())
    arr.append(N)
result = generate_subsets(arr)
for i in range(len(result)):
    if sum(result[i]) == 100:
        alpha = result[i]

alpha.sort()
for i in range(len(alpha)):
    print(alpha[i])