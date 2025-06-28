class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        visited = [False] * numCourses
        path = [False] * numCourses

        def dfs(course):
            if path[course]:
                return False
            if visited[course]:
                return True

            path[course] = True
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            path[course] = False
            visited[course] = True
            return True

        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return False
        return True
