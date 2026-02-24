"""
Complexity:
- Time  : O(v + e)
- Space : O(v + e)
"""
from typing import List
from collections import deque


class Solution:
    # Runtime: 3ms
    # Memory Usage: 20.4MB
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degrees[dest] += 1
        
        queue = deque([i for i in range(numCourses) if in_degrees[i] == 0])
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in adj[current]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        return result if len(result) == numCourses else []

    # Best time complexity solution (0ms)
    def findOrderBestTime(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[]

        for i in range(numCourses):
            adj.append([])
        
        for u,v in prerequisites:
            adj[u].append(v)

        vis=[-1]*numCourses
        res=[]

        for i in range(numCourses):
            if vis[i]==-1:
                if not self.dfs(i,vis,adj,res):
                    return []
        
        return res

    def dfs(self,node,vis,adj,res):
        vis[node]=1

        for it in adj[node]:
            if vis[it]==-1:
                if not self.dfs(it,vis,adj,res):
                    return False
            if vis[it]==1:
                return False
        vis[node]=0
        res.append(node)
        return True

    # Best memory complexity solution (18.1MB)
    def findOrderBestMemory(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Initialize Graph and In-Degree count
        adj = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        
        # 2. Build the graph
        # pair is [course, prerequisite], so edge is prerequisite -> course
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
            
        # 3. Initialize Queue with courses having NO dependencies
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        result = []
        
        # 4. Process the queue
        while queue:
            current = queue.popleft()
            result.append(current)
            
            # Reduce in-degree of neighbors
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, dependencies are met
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 5. Check for cycles
        # If we couldn't process all courses, there's a cycle
        if len(result) == numCourses:
            return result
        else:
            return []


if __name__ == "__main__":
    s = Solution()

    print(s.findOrder(2, [[1, 0]])) # [0,1]
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0,2,1,3]
    print(s.findOrder(1, [])) # [0]
