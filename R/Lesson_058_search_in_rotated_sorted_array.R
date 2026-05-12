# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 058 -- Search in Rotated Sorted Array
# Category   : Binary Search
# Difficulty : Medium
# Study Plan : Day 29
# =============================================================
#
# QUESTION:
#   Search target in a rotated sorted array of unique values.
#   Return its index, or -1 if not found.
#
#   Example: nums=[4,5,6,7,0,1,2], target=0 -> 4
# =============================================================

search_rot <- function(nums, target) {
    l <- 1; r <- length(nums)
    while (l <= r) {
        mid <- (l+r) %/% 2
        if (nums[mid] == target) return(mid - 1)
        if (nums[l] <= nums[mid]) {
            if (nums[l] <= target && target < nums[mid]) r <- mid - 1 else l <- mid + 1
        } else {
            if (nums[mid] < target && target <= nums[r]) l <- mid + 1 else r <- mid - 1
        }
    }
    -1
}
print(search_rot(c(4,5,6,7,0,1,2), 0))
print(search_rot(c(4,5,6,7,0,1,2), 3))
