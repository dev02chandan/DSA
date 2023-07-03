def calculateMinPlatforms(at, dt, n):
    """
    Approach:
    - Sort the arrival and departure times arrays.
    - Initialize two pointers, i and j, to track the indices of arrival and departure times.
    - Initialize platforms and maxplatforms variables to keep track of the current and maximum number of platforms needed.
    - Iterate until both pointers are within the array bounds:
        - If the arrival time at index i is less than or equal to the departure time at index j:
            - Increment i and update the platforms count.
            - If the current platforms count is greater than the maximum platforms count, update the maximum platforms count.
        - Otherwise, increment j and decrement the platforms count.
    - Return the maximum platforms count.

    Time complexity: O(n log n) due to the sorting of the arrival and departure times.

    """

    if n == 0:
        return 0

    at.sort()
    dt.sort()

    i = 0  # Pointer for at
    j = 0  # Pointer for dt

    platforms = 0
    maxplatforms = 0

    while i < n and j < n:
        if at[i] <= dt[j]:
            i += 1
            platforms += 1
            if platforms > maxplatforms:
                maxplatforms = platforms
        else:
            j += 1
            platforms -= 1

    return maxplatforms


# Testcases
arrival_times = [900, 940, 950, 1100, 1500, 1800]
departure_times = [910, 1200, 1120, 1130, 1900, 2000]
print(calculateMinPlatforms(arrival_times,
      departure_times, len(arrival_times)))  # Output: 3

arrival_times = [900, 940, 950, 1100, 1500]
departure_times = [910, 1200, 1120, 1130, 1900]
print(calculateMinPlatforms(arrival_times,
      departure_times, len(arrival_times)))  # Output: 2

arrival_times = [900, 940, 950]
departure_times = [910, 1200, 1120]
print(calculateMinPlatforms(arrival_times,
      departure_times, len(arrival_times)))  # Output: 1
