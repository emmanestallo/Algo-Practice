#we solve this using an adjacency matrix 
v, e, s = input().split()
v, e, s = int(v), int(e), int(s) 

def create_matrix():
    arr_2d = []
    visited = [] 

    for i in range(v):
        arr_2d.append([0]*v)
        visited.append([False]*v)

    for j in range(e):
        src, dst, cost = input().split() 
        src, dst, cost = int(src), int(dst), int(cost) 
        arr_2d[src-1][dst-1] = cost

    return arr_2d, visited 


def weight_traversal(mat):
    
    
    return last, cost  




'''
to_print, vis_mat = create_matrix() 
for i in range(len(to_print)):
    print(to_print[i])

for i in range(len(to_print)):    
    print(vis_mat[i])
''' 