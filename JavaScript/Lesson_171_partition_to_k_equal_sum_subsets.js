// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 171 -- Partition to K Equal Sum Subsets
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 86
// =============================================================
//
// QUESTION:
//   Determine if nums can be partitioned into k subsets with equal sum.
// =============================================================
function canPartitionKSubsets(nums,k){const s=nums.reduce((a,b)=>a+b,0);if(s%k)return false;const t=s/k;nums.sort((a,b)=>b-a);if(nums[0]>t)return false;const b=new Array(k).fill(0);function bt(i){if(i===nums.length)return true;for(let j=0;j<k;j++){if(b[j]+nums[i]<=t){b[j]+=nums[i];if(bt(i+1))return true;b[j]-=nums[i];}if(b[j]===0)break;}return false;}return bt(0);}
console.log(canPartitionKSubsets([4,3,2,3,5,2,1],4));
