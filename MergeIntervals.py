def mergeIntervals(intervals):
    # Intervals is a list of lists
    # What if I arrange in ascending order - acc to starting digit
    # and then I can check for intervals = will not take n time
    # Optimal - only one iteration and keep updating answer

    ans = []
    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals)):
        if len(ans) == 0:
            ans.append(intervals[i])
        if intervals[i][0] <= ans[-1][1]:
            ans[-1][1] = max(intervals[i][1], ans[-1][1])

        else:
            ans.append(intervals[i])

    return ans


print(mergeIntervals([[1, 4], [3, 5], [6, 8], [10, 12], [8, 9]]))
