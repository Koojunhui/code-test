from itertools import combinations

str_list = ['a', 'b', 'c']
result = list(combinations('abc', 2))
print(result)


n_cols = 5
for r in range(1, n_cols + 1):
    for cols in combinations(range(n_cols), r):
        print
        # print(cols)


A = {1, 2}
B = {1, 2, 3}
# print(A.issubset(B))
# print(B.issubset(A))

# combinations(range(n), r) - 기본형
