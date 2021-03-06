# dfs / bfs 
# dfs -> stack(sort by reverse)
# bfs -> queue(sort)
# notice that bi-direction
node, line, start = map(int, input().split())
matrix = [[] * (node+1) for _ in range(node+1)]
nodes = []
for i in range(line):
    node1, node2 = map(int, input().split())
    matrix[node1].append(node2)
    matrix[node2].append(node1)
for i in range(node):
    sorted(matrix[i])

## 노드에 번호를 부여해서 연결된 노드는 같은 행에 위치하도록 매트릭스를 설정한다. 

def bfs(matrix, start):
    ans = []
    queue = list()
    visited = list()
    queue.append(start)
    while queue:
        n = queue.pop(0)
        if n not in visited:
            ans.append(str(n)) ## 방법 1. 반드시 str형식으로 변환하는 것이 중요해 
            visited.append(n)
            queue.extend(sorted(matrix[n]))
    return ans        

def dfs(matrix, start):
    ans = []
    stack = list()
    visited = list()
    stack.append(start)
    while stack:
        n = stack.pop()
        if n not in visited:
            ans.append(n)
            visited.append(n)
            stack.extend(sorted(matrix[n], reverse=True))
    return ans        

if __name__ == "__main__": 
    print(*dfs(matrix, start)) ## 방법2. 역시 파이썬... 안에 성분만 출력해주는방법
    print(' '.join(bfs(matrix, start))) ## 방법1. 모르면 절대 못하는 방법이다. 반드시 알고 있을 것!
    

    