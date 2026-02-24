"""
Complexity:
- Time  : O(v + e)
- Space : O(v + e)
"""
from collections import deque, defaultdict
from typing import List


class Solution:
    # Runtime: 3ms
    # Memory Usage: 20.4MB
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Bangun Adjacency List dan hitung In-Degree
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1
        
        # 2. Masukkan semua course yang TIDAK punya prasyarat ke antrean (Queue)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        count = 0
        while queue:
            current = queue.popleft()
            count += 1
            
            # 3. Kurangi in-degree tetangganya
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                # Jika in-degree jadi 0, masukkan ke queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. Jika jumlah yang berhasil diproses == total course, berarti tidak ada cycle
        return count == numCourses

    # Best time complexity solution (0ms)
    def canFinishBestTime(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degree[course] += 1

        processing_queue = deque()

        for index, degree in enumerate(in_degree):
            if degree == 0:
                processing_queue.append(index)

        courses_taken = 0

        while processing_queue:
            prereq = processing_queue.popleft()
            courses_taken += 1

            if courses_taken == numCourses:
                return True

            for course in graph[prereq]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    processing_queue.append(course)

        return courses_taken == numCourses

    # Best memory complexity solution (18MB)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        
        q = deque([x for x in range(numCourses) if indegree[x] == 0])
        topoSort = []
        while q:
            curr = q.popleft()
            topoSort.append(curr)
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return len(topoSort) == numCourses


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(2, [[1, 0]])) # True
    print(s.canFinish(2, [[1, 0], [0, 1]])) # False
