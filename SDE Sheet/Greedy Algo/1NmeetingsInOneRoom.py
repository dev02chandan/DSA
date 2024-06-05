def maximumMeetings(start, end):
    store = []

    # Create a list of meetings with their start time, end time, and index
    for index, (s, e) in enumerate(zip(start, end)):
        # We need 1-based indexing so adding +1 to index
        store.append([s, e, index + 1])

    # Sort the meetings according to their finishing times
    store.sort(key=lambda x: x[1])

    ans = []
    endlimit = -1

    # Traverse through the sorted meetings
    for i in store:
        # If the start time of the current meeting is greater than the last ended meeting
        if i[0] > endlimit:
            # Add the current meeting to the answer
            ans.append(i[2])
            # Update the end limit with the end time of the current meeting
            endlimit = i[1]

    return ans


"""
Approach:
- Create a list called 'store' to store the meetings with their start time, end time, and index.
- Traverse through the given 'start' and 'end' lists using 'enumerate' to get the index and corresponding elements.
- Add the meeting information to the 'store' list.
- Sort the 'store' list based on the finishing times of the meetings using the 'sort()' method and a lambda function as the key.
- Initialize an empty list called 'ans' to store the indices of the meetings to attend.
- Initialize a variable 'endlimit' to keep track of the last ended meeting's end time, initially set to -1.
- Traverse through the sorted meetings in the 'store' list.
- Check if the start time of the current meeting is greater than the 'endlimit'.
- If it is, add the index of the current meeting to the 'ans' list.
- Update the 'endlimit' with the end time of the current meeting.
- Return the 'ans' list containing the indices of the selected meetings.
"""

# Testcases
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
# The optimal order to attend the meetings: [1, 2, 4, 5]
# Indices of the selected meetings: [2, 3, 5, 6]
print(maximumMeetings(start, end))  # Output: [1, 2, 4, 5]

start = [1, 2, 3, 4, 5]
end = [2, 3, 4, 5, 6]
# The optimal order to attend the meetings: [1, 2, 3, 4, 5]
# Indices of the selected meetings: [1, 2, 3, 4, 5]
print(maximumMeetings(start, end))  # Output: [1, 3, 5]
