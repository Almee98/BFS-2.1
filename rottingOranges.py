# Time Complexity : O(n*m) where n is the number of rows and m is the number of columns
# Space Complexity : O(m*n), in case all the oranges are rotten
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach: BFS
# In this approach, we will use BFS to traverse the grid.
# We will maintain a queue to keep track of the rotten oranges and their positions.
# We will also keep track of the number of fresh oranges and the time taken to rot all the oranges.
# We will start by adding all the rotten oranges to the queue.
# Next, we will iterate over the queue and for each rotten orange, we will check its 4 neighbors (up, down, left, right).
# If any of the neighbors is a fresh orange, we will rot it and add it to the queue.
# We will also decrement the count of fresh oranges.
# Finally, we will return the time taken to rot all the oranges.

from collections import deque
class Solution:
    def orangesRotting(self, grid):
        # Calculate the number of rows and columns in the grid
        m, n = len(grid), len(grid[0])
        # Initialize a queue to perform BFS
        q = deque()
        # Initialize time and fresh oranges count
        time = 0
        fresh = 0
        # Define the directions for the 4 neighbors (up, down, left, right)
        dirs = [[-1,0], [1,0], [0,-1], [0,1]]

        # Iterate over the grid to find rotten oranges and fresh oranges
        for i in range(m):
            for j in range(n):
                # If the orange is rotten, add it to the queue
                if grid[i][j] == 2:
                    q.append([i,j])
                if grid[i][j] == 1:
                    fresh += 1

        # If there are no fresh oranges, we don't need to calculate time. So return 0
        if fresh == 0:
            return time
        
        # Perform BFS
        while q:
            # Take a snapshot of the current level. We will process all the rotten oranges at this level in 1 iteration
            size = len(q)
            # Increment the time
            time += 1
            # Process all the rotten oranges at this level
            for i in range(size):
                # Pop the first rotten orange from the queue, and get it's row and column
                row, col = q.popleft()
                # Iterate over the 4 neighbors of the rotten orange
                for d in dirs:
                    r = row + d[0]
                    c = col + d[1]
                    # Check if the neighbor is within bounds and is a fresh orange
                    if r >= 0 and c >= 0 and r < m and c < n:
                        if grid[r][c] == 0:
                            continue
                        # If the neighbor is a fresh orange, rot it and add it to the queue
                        if grid[r][c] == 1:
                            grid[r][c] = 2
                            q.append([r,c])
                            # Decrement the count of fresh oranges
                            fresh -= 1
                            # If there are no fresh oranges left, return the time taken to rot all the oranges
                            if fresh == 0:
                                return time

        # If there are still fresh oranges left, return -1
        return -1
    

# DFS Solution:
# Time Complexity : O(k*(n*m)) where n is the number of rows and m is the number of columns, k is a constant number of rotten oranges
# Space Complexity : O(m*n) at max for recursion stack

# Approcah: DFS
# In this approach, we will use DFS to traverse the grid.
# Similar to the BFS approach, we want to traverse the fresh oranges starting from all the rotten oranges.
# Since in DFS we can only explore one rotten orange at a time, we wil have to keep updating the time taken to rot an orange, if from one path we can rot it in a better time.
# We will start by iterating over the grid to find all the rotten oranges.
# For each rotten orange, we will perform DFS on its 4 neighbors (up, down, left, right).
class Solution:
    def orangesRotting(self, grid) -> int:
        m, n = len(grid), len(grid[0])
            #     top   right   down   left
        dirs = [[-1,0], [0,1], [1,0], [0,-1]]
        # Recursive function to calculate time taken to rot all the oranges from a specific orange
        def dfs(r, c, t):
            # base case - return in case of cell out of bounds and if the rotting time is less than or equal to current time
            if r<0 or c<0 or r==m or c==n or grid[r][c]==0:
                return
            
            # If the rotting time is less than the time for the current orange, we don't want to update its time, so return
            if grid[r][c] < t and grid[r][c] != 1:
                return
            
            # If the orange is fresh, and has a rotting time greater than the current time, we will rot it in a better time
            if grid[r][c] == 1 or grid[r][c] > t:
                grid[r][c] = t

            # Iterate over the 4 neighbors of the rotten orange and perform DFS on them
            for row, col in dirs:
                dfs(r+row, c+col, t+1)

        # Iterate over the grid to find rotten oranges
        for i in range(m):
            for j in range(n):
                # If a rotten orange is found, perform DFS from that orange
                if grid[i][j] == 2:
                    # We take an offset of 2 to avoid overwriting the rotten orange
                    time = 2
                    dfs(i, j, time)
    
        # Calculate the actual time taken by subtracting the offset from the time
        # Initialize time to 0
        time = 0
        for i in range(m):
            for j in range(n):
                # If a fresh orange is found, return -1
                if grid[i][j] == 1:
                    return -1
                # For all other oranges, we will update the maximum time taken to rot all the oranges
                elif grid[i][j] != 0:
                    time = max(time, grid[i][j]-2)

        # Return the time taken to rot all the oranges
        return time

# DFS Solution:
# This approach is similar to the previous one, just a different way of DFSing. 
class Solution:
    def orangesRotting(self, grid) -> int:
        m, n = len(grid), len(grid[0])
            #     top   right   down   left
        dirs = [[-1,0], [0,1], [1,0], [0,-1]]
        # Recursive function to calculate time taken to rot all the oranges from a specific orange
        def dfs(i, j, t):
            grid[i][j] = t

            for row, col in dirs:
                r = i + row
                c = j + col
                # Instead of a base check, we will only traverse the cells that are not out of bounds and have a rotting time greater than the current time
                if (r>=0 and c>=0 and r<m and c<n and (grid[r][c] == 1 or grid[r][c] > t)):
                    dfs(r, c, t+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    time = 2
                    dfs(i, j, time)
    
        time = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                elif grid[i][j] != 0:
                    time = max(time, grid[i][j]-2)

        return time