from collections import deque

def water_jug_bfs(x, y, target):
    visited = set()
    queue = deque([(0, 0)])
    
    while queue:
        a, b = queue.popleft()
        
        if (a, b) in visited:
            continue
        
        visited.add((a, b))
        print(f"({a}, {b})")
        
        if a == target or b == target:
            return True
        
        queue.extend([
            (x, b), (a, y), (0, b), (a, 0),
            (a - min(a, y - b), b + min(a, y - b)),
            (a + min(b, x - a), b - min(b, x - a))
        ])
    return False

def water_jug_dfs(x, y, target, visited=set()):
    stack = [(0, 0)]
    
    while stack:
        a, b = stack.pop()
        
        if (a, b) in visited:
            continue
        
        visited.add((a, b))
        print(f"({a}, {b})")
        
        if a == target or b == target:
            return True
        
        stack.extend([
            (x, b), (a, y), (0, b), (a, 0),
            (a - min(a, y - b), b + min(a, y - b)),
            (a + min(b, x - a), b - min(b, x - a))
        ])
    return False

# Example Usage
X, Y, Z = 4, 3, 2
print("BFS Solution:")
water_jug_bfs(X, Y, Z)
print("DFS Solution:")
water_jug_dfs(X, Y, Z)