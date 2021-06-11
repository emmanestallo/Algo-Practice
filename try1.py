v, e, s = input().split()
v, e, s = int(v), int(e), int(s) 
cost = 0
last = s

def create_matrix(v,e):
    arr_2d = []
    visited = [] 

    for i in range(v):
        arr_2d.append([21]*v)
        visited.append(False)

    for j in range(e):
        src, dst, cost = input().split() 
        src, dst, cost = int(src), int(dst), int(cost) 
        arr_2d[src-1][dst-1] = cost

    return arr_2d, visited 


def find_min(arr):
    min = arr[0]
    min_index = 0 
    for i in range(1,len(arr)):
        if arr[i] < min:
            min = arr[i] 
            min_index = min_index + 1 
    return min_index+1 , min


def weighted_traversal(key):
    global cost 
    global last
    visited_matrix[key-1] = True
    w, cst = find_min(adj_matrix[key-1])
    if visited_matrix[w-1] == False:
        last = w 
        cost = cost + cst
        weighted_traversal(w)
    else: 
        adj_matrix[key-1][]
        

adj_matrix, visited_matrix = create_matrix(v, e)
weighted_traversal(s)
print(last, cost)

'''
for i in adj_matrix:
    print(i) 

vert, cost = find_min(adj_matrix[s-1])

print(vert)
print(cost)
print(visited_matrix)
'''