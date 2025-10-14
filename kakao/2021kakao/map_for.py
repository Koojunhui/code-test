query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]

def parse_query(q):
    q = q.replace(" and", "")
    tokens = q.split()
    return ' '.join(tokens[:-1]), int(tokens[-1])

# for
for_parsed_queries = []
for q in query:
    for_parsed_queries.append(parse_query(q))
# map(function, iterable)
parsed_queries = list(map(parse_query, query))

# print(for_parsed_queries)
# print(parsed_queries)

list_a = [1, 2, 3]
list_A = list(map(lambda x: x**2, list_a))
print(list_A)

list_b = ["a", "b", "c"]
list_b = list(map(lambda str: str.upper(), list_b))
print(list_b)

list_c = [9, 8, 7]
list_c = list(map(lambda x, y: x + y, list_a, list_c))
print(list_c)