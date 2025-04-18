# Time Complexity : O(n), where n is the number of employees
# Space Complexity : O(n), where n is the number of employees
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# In this approach, we will get the ids of all employees who are direct subordinates of the given employee id.
# we will iterater over this list, while adding the importance of each employee to the result, and adding the ids of their subordinates to the queue.
# We will repeat this process until the queue is empty.
# We will maintan 2 dictionaries - one for the importance of each employee and one for the subordinates of each employee.
# We will use a queue to perform BFS on the employees.

from collections import defaultdict, deque
class Solution:
    def getImportance(self, employees, id):
        # Create a dictionary to store the importance and subordinates of each employee
        imp, sub = {}, defaultdict()
        # Initialize the result variable
        res = 0

        # Iterate over the employees and populate the dictionaries
        for e in employees:
            imp[e.id] = e.importance
            sub[e.id] = e.subordinates

        # Initialize a queue to perform BFS
        q = deque()
        # Add the given employee id to the queue
        q.append(id)

        # Perform BFS
        while q:
            # Take a snapshot of the current level. We will process all the employees at this level in 1 iteration
            size = len(q)
            # Iterate over the employees at this level
            for i in range(size):
                # Pop the first employee from the queue
                emp = q.popleft()
                # Add the importance of the employee to the result
                res += imp[emp]

                # Add the subordinates of the employee to the queue
                for s in sub[emp]:
                    q.append(s)

        # After processing all the employees in the queue, we will have the total importance of the given employee
        return res