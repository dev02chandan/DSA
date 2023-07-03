def maximumActivities(start, finish):
    """
    Approach:
    1. Combine the start and finish times of activities using the `zip` function and sort them based on the finishing times.
    2. Initialize variables `end` to keep track of the current ending time and `ans` to track the number of activities selected.
    3. Iterate through the sorted activities and check if the starting time of the current activity is greater than or equal to the current ending time.
    4. If the condition is true, it means there is no overlap, and the current activity can be selected. Update the `end` variable to the finishing time of the current activity and increment the `ans` variable.
    5. Return the final count of selected activities.
    """

    combined = sorted(zip(start, finish), key=lambda x: x[1])

    end = 0  # Track the current ending time
    ans = 0  # Track the number of activities selected

    for act in combined:
        if act[0] >= end:
            # If the current activity's starting time is after or equal to the current ending time,
            # it can be selected as there is no overlap
            end = act[1]  # Update the current ending time
            ans += 1  # Increment the count of selected activities

    return ans


# Testcases
start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]
print(maximumActivities(start_times, finish_times))  # Output: 4

start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 10]
print(maximumActivities(start_times, finish_times))  # Output: 5

start_times = [1, 2, 3, 4, 5]
finish_times = [6, 7, 8, 9, 10]
print(maximumActivities(start_times, finish_times))  # Output: 5


# Time complexity: O(n log n)
# Space complexity: O(n)
