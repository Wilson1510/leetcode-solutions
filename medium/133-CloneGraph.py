"""
Complexity:
- Time  : O(v + e)
- Space : O(v + e)
"""
from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        visited = set()
        result = []
        stack = [self]

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)

            neighbor_vals = [n.val for n in node.neighbors]
            result.append(f"{node.val}: {neighbor_vals}")

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

        return "\n".join(sorted(result))


class Solution:
    # Runtime: 45ms
    # Memory Usage: 20MB
    def build_graph(self, adj_list):
        if not adj_list:
            return None

        # Step 1: buat semua node
        nodes = {}
        for i in range(len(adj_list)):
            nodes[i + 1] = Node(i + 1)

        # Step 2: hubungkan neighbors
        for i, neighbors in enumerate(adj_list):
            for neighbor in neighbors:
                nodes[i + 1].neighbors.append(nodes[neighbor])

        # Return node pertama
        return nodes[1]

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        stack = [node]
        nodes = {}

        while stack:
            current = stack.pop()
            if current.val not in nodes:
                nodes[current.val] = Node(current.val)
            for neighbor in current.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val)
                    stack.append(neighbor)
                nodes[current.val].neighbors.append(nodes[neighbor.val])
        return nodes[node.val]

    # Best time complexity solution (22ms)
    def cloneGraphBestTime(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {}  # original -> clone

        def dfs(curr: 'Node') -> 'Node':
            if curr in clones:
                return clones[curr]

            copy = Node(curr.val)
            clones[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)   

    # Best memory complexity solution (17.3MB)
    def cloneGraphBestSolution(self, node: Optional['Node']) -> Optional['Node']:
        def cloneGraph_helper(node):
            if node.val in cloned_node:
                return cloned_node[node.val]
            new_node = Node(node.val)
            cloned_node[node.val] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(cloneGraph_helper(neighbor))
            return new_node

        cloned_node = {}
        return_node = None
        if node:
            return_node = cloneGraph_helper(node)
        return return_node


if __name__ == "__main__":
    s = Solution()
    node = s.build_graph([[2,4],[1,3],[2,4],[1,3]])
    print(s.cloneGraph(node))

    node = s.build_graph([[]])
    print(s.cloneGraph(node))

    node = s.build_graph([])
    print(s.cloneGraph(node))
