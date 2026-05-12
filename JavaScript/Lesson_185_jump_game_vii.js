// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 185 -- Jump Game VII
// Category   : Greedy
// Difficulty : Medium
// Study Plan : Day 93
// =============================================================
//
// QUESTION:
//   Binary string s. Start at 0; can jump from i to any j with i+minJump<=j<=i+maxJump and s[j]='0'. Reach last index?
// =============================================================
function canReach(s,mn,mx){const n=s.length;if(s[n-1]!=='0'||s[0]!=='0')return false;const pre=new Array(n+1).fill(0);const r=new Array(n).fill(false);r[0]=true;pre[1]=1;for(let i=1;i<n;i++){if(s[i]==='0'){const lo=Math.max(0,i-mx),hi=i-mn;if(lo<=hi && pre[hi+1]-pre[lo]>0) r[i]=true;}pre[i+1]=pre[i]+(r[i]?1:0);}return r[n-1];}
console.log(canReach("011010",2,3));console.log(canReach("01101110",2,3));
