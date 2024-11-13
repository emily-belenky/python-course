

def dnc(base, combine):
    def logic_func(arr):
        if len(arr) == 1:
            return base(arr[0])
        else:
            bottom_half = logic_func(arr[:len(arr) // 2])
            top_half = logic_func(arr[len(arr) // 2:])
            return combine(bottom_half, top_half)

    return logic_func


def maxAreaHist(hist):
    if not hist:
        return 0
    if len(hist) == 1:
        return hist[0]
    min_index = hist.index(min(hist))
    # creates the max area possible using the lowest bar across the entire array
    maximum = hist[min_index] * len(hist)
    # uses recursion to calculate from one half of the array
    right = maxAreaHist(hist[min_index + 1:])
    # uses recursion to calculate from the other half of the array
    left = maxAreaHist(hist[:min_index])
    return max(maximum, right, left)
