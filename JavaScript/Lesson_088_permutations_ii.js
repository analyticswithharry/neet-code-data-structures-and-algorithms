// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 088 -- Permutations II
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 44
// =============================================================
//
// QUESTION:
//   Given a collection nums of numbers that might contain duplicates, return all possible unique permutations.
//   Example: [1,1,2] -> [[1,1,2],[1,2,1],[2,1,1]].
// =============================================================

var permuteUnique = function(nums){
  nums.sort((a,b)=>a-b); const res=[], used=Array(nums.length).fill(false), cur=[];
  const bt=()=>{
    if (cur.length===nums.length){ res.push([...cur]); return; }
    for (let i=0;i<nums.length;i++){
      if (used[i]) continue;
      if (i>0 && nums[i]===nums[i-1] && !used[i-1]) continue;
      used[i]=true; cur.push(nums[i]); bt(); cur.pop(); used[i]=false;
    }
  };
  bt(); return res;
};
console.log(JSON.stringify(permuteUnique([1,1,2])));
