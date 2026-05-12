// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 042 -- 3Sum
// Category   : Two Pointers
// Difficulty : Medium
// Study Plan : Day 21
// =============================================================
//
// QUESTION:
//   Given nums, return all unique triplets [a,b,c] such that a+b+c=0.
//
//   Example: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
// =============================================================

var threeSum = function(nums) {
    nums.sort((a,b)=>a-b); const res = [];
    for (let i=0;i<nums.length-2;i++) {
        if (i>0 && nums[i]===nums[i-1]) continue;
        let l=i+1, r=nums.length-1;
        while (l<r) {
            const s = nums[i]+nums[l]+nums[r];
            if (s<0) l++;
            else if (s>0) r--;
            else {
                res.push([nums[i],nums[l],nums[r]]);
                while (l<r && nums[l]===nums[l+1]) l++;
                while (l<r && nums[r]===nums[r-1]) r--;
                l++; r--;
            }
        }
    }
    return res;
};
console.log(threeSum([-1,0,1,2,-1,-4]));
