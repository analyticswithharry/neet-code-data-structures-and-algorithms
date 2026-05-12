// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 087 -- Subsets II
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 44
// =============================================================
//
// QUESTION:
//   Given an integer array nums that may contain duplicates, return all possible subsets (the power set), without duplicates.
//   Example: [1,2,2] -> [[],[1],[1,2],[1,2,2],[2],[2,2]].
// =============================================================

var subsetsWithDup = function(nums){
  nums.sort((a,b)=>a-b); const res=[], cur=[];
  const bt=(i)=>{ res.push([...cur]);
    for (let j=i;j<nums.length;j++){
      if (j>i && nums[j]===nums[j-1]) continue;
      cur.push(nums[j]); bt(j+1); cur.pop();
    }};
  bt(0); return res;
};
console.log(JSON.stringify(subsetsWithDup([1,2,2])));
