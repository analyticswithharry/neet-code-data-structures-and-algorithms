// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 100 -- Palindrome Partitioning
// Category   : Backtracking
// Difficulty : Medium
// Study Plan : Day 50
// =============================================================
//
// QUESTION:
//   Partition string s such that every substring is a palindrome. Return all possible partitions.
// =============================================================

var partition = function(s){
  const res=[], cur=[];
  const isPal=(x)=>{ for(let i=0,j=x.length-1;i<j;i++,j--) if(x[i]!==x[j]) return false; return true; };
  const bt=(i)=>{
    if (i===s.length){ res.push([...cur]); return; }
    for (let j=i+1;j<=s.length;j++){
      const sub=s.slice(i,j);
      if (isPal(sub)){ cur.push(sub); bt(j); cur.pop(); }
    }
  };
  bt(0); return res;
};
console.log(JSON.stringify(partition("aab")));
