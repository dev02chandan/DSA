# Import necessary libraries
from os import *
from sys import *
from collections import *
from math import *


def jobScheduling(jobs):
    """
    Approach:
    - Sort the jobs based on their deadlines in descending order.
    - Initialize an array to keep track of the scheduled jobs.
    - Iterate through each job and for each job, iterate from its deadline to 0.
    - If a slot is available, assign the job to that slot, update the profit, and break the inner loop.
    - Return the total profit obtained.
    """

    # Sort the jobs based on their deadlines in descending order
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Get the maximum deadline
    n = max(job[0] for job in jobs)

    # Initialize an array to keep track of the scheduled jobs
    arr = [0] * n

    # Initialize the profit
    profit = 0

    # Iterate through each job
    for job in jobs:
        # Iterate from the job's deadline to 0
        for i in range(job[0] - 1, -1, -1):
            # If a slot is available, assign the job to that slot
            if arr[i] == 0:
                arr[i] = job[1]
                profit += job[1]
                break

    return profit


# Testcase
jobs = [[4, 70], [1, 90], [2, 60], [3, 80], [1, 120], [2, 100]]
print(jobScheduling(jobs))  # Output: 370

# Time Complexity: O(N^2), where N is the number of jobs
# Space Complexity: O(N), for the array to keep track of the scheduled jobs
