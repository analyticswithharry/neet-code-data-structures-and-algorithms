"""Batch 5: NeetCode lessons 86-110 with embedded question + working solution."""
from _lesson_writer import write_lessons

LESSONS = []

# ---- 086 Longest Substring Without Repeating Characters ----
LESSONS.append((86, "Longest Substring Without Repeating Characters", "Sliding Window", "Medium", 43,
"""Given a string s, find the length of the longest substring without repeating characters.
Example: 'abcabcbb' -> 3 ('abc'); 'bbbbb' -> 1; 'pwwkew' -> 3.""",
{
"Python":'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}; l = 0; best = 0
        for r, c in enumerate(s):
            if c in seen and seen[c] >= l: l = seen[c] + 1
            seen[c] = r
            best = max(best, r - l + 1)
        return best

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
''',
"JavaScript":'''
var lengthOfLongestSubstring = function(s){
  const m = new Map(); let l=0, best=0;
  for (let r=0;r<s.length;r++){
    const c=s[r];
    if (m.has(c) && m.get(c)>=l) l = m.get(c)+1;
    m.set(c,r); best = Math.max(best, r-l+1);
  } return best;
};
console.log(lengthOfLongestSubstring("abcabcbb"), lengthOfLongestSubstring("pwwkew"));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int lengthOfLongestSubstring(String s){
        Map<Character,Integer> m = new HashMap<>();
        int l=0, best=0;
        for (int r=0;r<s.length();r++){
            char c=s.charAt(r);
            if (m.containsKey(c) && m.get(c)>=l) l = m.get(c)+1;
            m.put(c,r); best = Math.max(best, r-l+1);
        } return best;
    }
    public static void main(String[] a){
        __CLASS__ x = new __CLASS__();
        System.out.println(x.lengthOfLongestSubstring("abcabcbb"));
        System.out.println(x.lengthOfLongestSubstring("pwwkew"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    int lengthOfLongestSubstring(string s){
        unordered_map<char,int> m; int l=0, best=0;
        for (int r=0;r<(int)s.size();r++){
            char c=s[r];
            if (m.count(c) && m[c]>=l) l = m[c]+1;
            m[c]=r; best = max(best, r-l+1);
        } return best;
    }
};
int main(){ Solution s; cout<<s.lengthOfLongestSubstring("abcabcbb")<<" "<<s.lengthOfLongestSubstring("pwwkew")<<endl; }
''',
"Go":'''
package main
import "fmt"
func lengthOfLongestSubstring(s string) int {
    m := map[byte]int{}; l, best := 0, 0
    for r := 0; r < len(s); r++ {
        c := s[r]
        if v, ok := m[c]; ok && v >= l { l = v + 1 }
        m[c] = r
        if r-l+1 > best { best = r-l+1 }
    }
    return best
}
func main(){ fmt.Println(lengthOfLongestSubstring("abcabcbb"), lengthOfLongestSubstring("pwwkew")) }
''',
"R":'''
lengthOfLongestSubstring <- function(s){
  chars <- strsplit(s,"")[[1]]; m <- list(); l <- 1; best <- 0
  for (r in seq_along(chars)){
    c <- chars[r]
    if (!is.null(m[[c]]) && m[[c]] >= l) l <- m[[c]] + 1
    m[[c]] <- r
    best <- max(best, r - l + 1)
  }
  best
}
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))
''',
}))

# ---- 087 Subsets II ----
LESSONS.append((87, "Subsets II", "Backtracking", "Medium", 44,
"""Given an integer array nums that may contain duplicates, return all possible subsets (the power set), without duplicates.
Example: [1,2,2] -> [[],[1],[1,2],[1,2,2],[2],[2,2]].""",
{
"Python":'''
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort(); res = []; cur = []
        def bt(i):
            res.append(cur[:])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]: continue
                cur.append(nums[j]); bt(j+1); cur.pop()
        bt(0); return res

if __name__ == "__main__":
    print(Solution().subsetsWithDup([1,2,2]))
''',
"JavaScript":'''
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
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> subsetsWithDup(int[] nums){
        Arrays.sort(nums); bt(nums,0,new ArrayList<>()); return res;
    }
    void bt(int[] nums, int i, List<Integer> cur){
        res.add(new ArrayList<>(cur));
        for (int j=i;j<nums.length;j++){
            if (j>i && nums[j]==nums[j-1]) continue;
            cur.add(nums[j]); bt(nums,j+1,cur); cur.remove(cur.size()-1);
        }
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().subsetsWithDup(new int[]{1,2,2}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    vector<vector<int>> res;
    void bt(vector<int>& nums, int i, vector<int>& cur){
        res.push_back(cur);
        for (int j=i;j<(int)nums.size();j++){
            if (j>i && nums[j]==nums[j-1]) continue;
            cur.push_back(nums[j]); bt(nums,j+1,cur); cur.pop_back();
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums){
        sort(nums.begin(),nums.end()); vector<int> cur; bt(nums,0,cur); return res;
    }
};
int main(){ vector<int> a={1,2,2}; auto r=Solution().subsetsWithDup(a);
    for (auto& v: r){ cout<<"["; for(int x: v)cout<<x<<","; cout<<"] "; } cout<<endl; }
''',
"Go":'''
package main
import ( "fmt"; "sort" )
func subsetsWithDup(nums []int) [][]int {
    sort.Ints(nums); var res [][]int; cur := []int{}
    var bt func(int)
    bt = func(i int){
        tmp := make([]int, len(cur)); copy(tmp, cur); res = append(res, tmp)
        for j := i; j < len(nums); j++ {
            if j > i && nums[j] == nums[j-1] { continue }
            cur = append(cur, nums[j]); bt(j+1); cur = cur[:len(cur)-1]
        }
    }
    bt(0); return res
}
func main(){ fmt.Println(subsetsWithDup([]int{1,2,2})) }
''',
"R":'''
subsetsWithDup <- function(nums){
  nums <- sort(nums); res <- list(); cur <- c()
  bt <- function(i){
    res[[length(res)+1]] <<- cur
    j <- i
    while (j <= length(nums)){
      if (j > i && nums[j] == nums[j-1]) { j <- j+1; next }
      cur <<- c(cur, nums[j]); bt(j+1); cur <<- cur[-length(cur)]
      j <- j+1
    }
  }
  bt(1); res
}
print(subsetsWithDup(c(1,2,2)))
''',
}))

# ---- 088 Permutations II ----
LESSONS.append((88, "Permutations II", "Backtracking", "Medium", 44,
"""Given a collection nums of numbers that might contain duplicates, return all possible unique permutations.
Example: [1,1,2] -> [[1,1,2],[1,2,1],[2,1,1]].""",
{
"Python":'''
class Solution:
    def permuteUnique(self, nums):
        nums.sort(); res=[]; used=[False]*len(nums); cur=[]
        def bt():
            if len(cur)==len(nums): res.append(cur[:]); return
            for i in range(len(nums)):
                if used[i]: continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]: continue
                used[i]=True; cur.append(nums[i]); bt()
                cur.pop(); used[i]=False
        bt(); return res

if __name__ == "__main__":
    print(Solution().permuteUnique([1,1,2]))
''',
"JavaScript":'''
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
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    List<List<Integer>> res = new ArrayList<>();
    boolean[] used; int[] nums;
    public List<List<Integer>> permuteUnique(int[] n){
        Arrays.sort(n); nums=n; used=new boolean[n.length];
        bt(new ArrayList<>()); return res;
    }
    void bt(List<Integer> cur){
        if (cur.size()==nums.length){ res.add(new ArrayList<>(cur)); return; }
        for (int i=0;i<nums.length;i++){
            if (used[i]) continue;
            if (i>0 && nums[i]==nums[i-1] && !used[i-1]) continue;
            used[i]=true; cur.add(nums[i]); bt(cur); cur.remove(cur.size()-1); used[i]=false;
        }
    }
    public static void main(String[] a){ System.out.println(new __CLASS__().permuteUnique(new int[]{1,1,2})); }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    vector<vector<int>> res; vector<bool> used; vector<int> cur;
    void bt(vector<int>& nums){
        if (cur.size()==nums.size()){ res.push_back(cur); return; }
        for (int i=0;i<(int)nums.size();i++){
            if (used[i]) continue;
            if (i>0 && nums[i]==nums[i-1] && !used[i-1]) continue;
            used[i]=true; cur.push_back(nums[i]); bt(nums);
            cur.pop_back(); used[i]=false;
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums){
        sort(nums.begin(),nums.end()); used.assign(nums.size(),false); bt(nums); return res;
    }
};
int main(){ vector<int> a={1,1,2}; auto r=Solution().permuteUnique(a);
    for (auto& v: r){ cout<<"["; for(int x: v)cout<<x<<","; cout<<"] "; } cout<<endl; }
''',
"Go":'''
package main
import ( "fmt"; "sort" )
func permuteUnique(nums []int) [][]int {
    sort.Ints(nums); var res [][]int; used := make([]bool,len(nums)); cur := []int{}
    var bt func()
    bt = func(){
        if len(cur)==len(nums){ tmp:=make([]int,len(cur)); copy(tmp,cur); res=append(res,tmp); return }
        for i := 0; i < len(nums); i++ {
            if used[i] { continue }
            if i>0 && nums[i]==nums[i-1] && !used[i-1] { continue }
            used[i]=true; cur=append(cur,nums[i]); bt()
            cur=cur[:len(cur)-1]; used[i]=false
        }
    }
    bt(); return res
}
func main(){ fmt.Println(permuteUnique([]int{1,1,2})) }
''',
"R":'''
permuteUnique <- function(nums){
  nums <- sort(nums); n <- length(nums); res <- list(); used <- rep(FALSE,n); cur <- c()
  bt <- function(){
    if (length(cur)==n){ res[[length(res)+1]] <<- cur; return() }
    for (i in 1:n){
      if (used[i]) next
      if (i>1 && nums[i]==nums[i-1] && !used[i-1]) next
      used[i] <<- TRUE; cur <<- c(cur, nums[i]); bt()
      cur <<- cur[-length(cur)]; used[i] <<- FALSE
    }
  }
  bt(); res
}
print(permuteUnique(c(1,1,2)))
''',
}))

# ---- 089 Reconstruct Itinerary ----
LESSONS.append((89, "Reconstruct Itinerary", "Advanced Graphs", "Hard", 45,
"""Given a list of airline tickets [from,to], reconstruct the itinerary in order, starting from 'JFK'. If multiple valid, return the lexicographically smallest one.""",
{
"Python":'''
import heapq
class Solution:
    def findItinerary(self, tickets):
        g = {}
        for a,b in tickets: g.setdefault(a,[]).append(b)
        for k in g: g[k].sort(reverse=True)
        st=["JFK"]; res=[]
        while st:
            while g.get(st[-1]): st.append(g[st[-1]].pop())
            res.append(st.pop())
        return res[::-1]

if __name__ == "__main__":
    print(Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
''',
"JavaScript":'''
var findItinerary = function(tickets){
  const g={}; for (const [a,b] of tickets){ (g[a]=g[a]||[]).push(b); }
  for (const k in g) g[k].sort().reverse();
  const st=["JFK"], res=[];
  while (st.length){
    while (g[st[st.length-1]] && g[st[st.length-1]].length) st.push(g[st[st.length-1]].pop());
    res.push(st.pop());
  }
  return res.reverse();
};
console.log(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public List<String> findItinerary(List<List<String>> tickets){
        Map<String, PriorityQueue<String>> g = new HashMap<>();
        for (List<String> t: tickets) g.computeIfAbsent(t.get(0), k->new PriorityQueue<>()).add(t.get(1));
        Deque<String> st = new ArrayDeque<>(); st.push("JFK");
        LinkedList<String> res = new LinkedList<>();
        while (!st.isEmpty()){
            while (g.containsKey(st.peek()) && !g.get(st.peek()).isEmpty()) st.push(g.get(st.peek()).poll());
            res.addFirst(st.pop());
        }
        return res;
    }
    public static void main(String[] a){
        List<List<String>> t = Arrays.asList(Arrays.asList("MUC","LHR"),Arrays.asList("JFK","MUC"),Arrays.asList("SFO","SJC"),Arrays.asList("LHR","SFO"));
        System.out.println(new __CLASS__().findItinerary(t));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    vector<string> findItinerary(vector<vector<string>>& tickets){
        map<string, multiset<string>> g;
        for (auto& t: tickets) g[t[0]].insert(t[1]);
        vector<string> st={"JFK"}, res;
        while (!st.empty()){
            while (g.count(st.back()) && !g[st.back()].empty()){
                auto it = g[st.back()].begin(); string nxt = *it; g[st.back()].erase(it); st.push_back(nxt);
            }
            res.push_back(st.back()); st.pop_back();
        }
        reverse(res.begin(), res.end()); return res;
    }
};
int main(){ vector<vector<string>> t={{"MUC","LHR"},{"JFK","MUC"},{"SFO","SJC"},{"LHR","SFO"}};
    for (auto& s: Solution().findItinerary(t)) cout<<s<<" "; cout<<endl; }
''',
"Go":'''
package main
import ( "fmt"; "sort" )
func findItinerary(tickets [][]string) []string {
    g := map[string][]string{}
    for _, t := range tickets { g[t[0]] = append(g[t[0]], t[1]) }
    for k := range g { sort.Sort(sort.Reverse(sort.StringSlice(g[k]))) }
    st := []string{"JFK"}; res := []string{}
    for len(st) > 0 {
        top := st[len(st)-1]
        for len(g[top]) > 0 {
            n := len(g[top]); nxt := g[top][n-1]; g[top] = g[top][:n-1]
            st = append(st, nxt); top = nxt
        }
        res = append(res, st[len(st)-1]); st = st[:len(st)-1]
    }
    for i,j:=0,len(res)-1; i<j; i,j=i+1,j-1 { res[i],res[j]=res[j],res[i] }
    return res
}
func main(){ fmt.Println(findItinerary([][]string{{"MUC","LHR"},{"JFK","MUC"},{"SFO","SJC"},{"LHR","SFO"}})) }
''',
"R":'''
findItinerary <- function(tickets){
  g <- list()
  for (t in tickets){ a<-t[1]; b<-t[2]; g[[a]] <- c(g[[a]], b) }
  for (k in names(g)) g[[k]] <- sort(g[[k]], decreasing=TRUE)
  st <- c("JFK"); res <- c()
  while (length(st) > 0){
    top <- st[length(st)]
    while (!is.null(g[[top]]) && length(g[[top]]) > 0){
      nxt <- g[[top]][length(g[[top]])]; g[[top]] <- g[[top]][-length(g[[top]])]
      st <- c(st, nxt); top <- nxt
    }
    res <- c(res, st[length(st)]); st <- st[-length(st)]
  }
  rev(res)
}
print(findItinerary(list(c("MUC","LHR"),c("JFK","MUC"),c("SFO","SJC"),c("LHR","SFO"))))
''',
}))

# ---- 090 Swim In Rising Water ----
LESSONS.append((90, "Swim In Rising Water", "Advanced Graphs", "Hard", 45,
"""On an n x n grid, grid[i][j] is the elevation. You start at (0,0) and want to reach (n-1,n-1). At time t the water level is t and you can move to a 4-neighbor cell if both are <= t. Return the minimum t.""",
{
"Python":'''
import heapq
class Solution:
    def swimInWater(self, grid):
        n = len(grid); h=[(grid[0][0],0,0)]; seen={(0,0)}; ans=0
        while h:
            v,r,c = heapq.heappop(h); ans = max(ans,v)
            if r==n-1 and c==n-1: return ans
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in seen:
                    seen.add((nr,nc)); heapq.heappush(h,(grid[nr][nc],nr,nc))
        return -1

if __name__ == "__main__":
    print(Solution().swimInWater([[0,2],[1,3]]))
''',
"JavaScript":'''
class MinHeap{ constructor(){this.a=[];} push(x){this.a.push(x); this._up(this.a.length-1);}
  pop(){const t=this.a[0],l=this.a.pop(); if(this.a.length){this.a[0]=l; this._dn(0);} return t;}
  size(){return this.a.length;}
  _up(i){while(i>0){const p=(i-1)>>1; if(this.a[p][0]>this.a[i][0]){[this.a[p],this.a[i]]=[this.a[i],this.a[p]]; i=p;} else break;}}
  _dn(i){const n=this.a.length; while(true){let l=2*i+1,r=2*i+2,s=i;
    if(l<n&&this.a[l][0]<this.a[s][0])s=l; if(r<n&&this.a[r][0]<this.a[s][0])s=r;
    if(s===i)break; [this.a[s],this.a[i]]=[this.a[i],this.a[s]]; i=s;}}
}
var swimInWater = function(grid){
  const n=grid.length; const h=new MinHeap(); h.push([grid[0][0],0,0]);
  const seen=new Set(["0,0"]); let ans=0;
  const dirs=[[1,0],[-1,0],[0,1],[0,-1]];
  while (h.size()){
    const [v,r,c]=h.pop(); ans=Math.max(ans,v);
    if (r===n-1 && c===n-1) return ans;
    for (const [dr,dc] of dirs){
      const nr=r+dr,nc=c+dc; const k=nr+","+nc;
      if (nr>=0&&nr<n&&nc>=0&&nc<n&&!seen.has(k)){ seen.add(k); h.push([grid[nr][nc],nr,nc]); }
    }
  } return -1;
};
console.log(swimInWater([[0,2],[1,3]]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int swimInWater(int[][] grid){
        int n=grid.length; PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[0]-b[0]);
        pq.add(new int[]{grid[0][0],0,0}); boolean[][] seen=new boolean[n][n]; seen[0][0]=true; int ans=0;
        int[][] d={{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.isEmpty()){
            int[] x=pq.poll(); ans=Math.max(ans,x[0]);
            if (x[1]==n-1 && x[2]==n-1) return ans;
            for (int[] dd: d){ int nr=x[1]+dd[0], nc=x[2]+dd[1];
                if (nr>=0&&nr<n&&nc>=0&&nc<n&&!seen[nr][nc]){ seen[nr][nc]=true; pq.add(new int[]{grid[nr][nc],nr,nc}); } }
        } return -1;
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().swimInWater(new int[][]{{0,2},{1,3}}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    int swimInWater(vector<vector<int>>& g){
        int n=g.size(); priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<>> pq;
        pq.push({g[0][0],0,0}); vector<vector<bool>> seen(n,vector<bool>(n,false)); seen[0][0]=true; int ans=0;
        int dr[]={1,-1,0,0}, dc[]={0,0,1,-1};
        while (!pq.empty()){
            auto [v,r,c]=pq.top(); pq.pop(); ans=max(ans,v);
            if (r==n-1 && c==n-1) return ans;
            for (int k=0;k<4;k++){ int nr=r+dr[k], nc=c+dc[k];
                if (nr>=0&&nr<n&&nc>=0&&nc<n&&!seen[nr][nc]){ seen[nr][nc]=true; pq.push({g[nr][nc],nr,nc}); } }
        } return -1;
    }
};
int main(){ vector<vector<int>> g={{0,2},{1,3}}; cout<<Solution().swimInWater(g)<<endl; }
''',
"Go":'''
package main
import ( "container/heap"; "fmt" )
type Item struct{ v,r,c int }
type PQ []Item
func (p PQ) Len()int{return len(p)}
func (p PQ) Less(i,j int)bool{return p[i].v<p[j].v}
func (p PQ) Swap(i,j int){p[i],p[j]=p[j],p[i]}
func (p *PQ) Push(x any){*p=append(*p,x.(Item))}
func (p *PQ) Pop()any{o:=*p; n:=len(o); x:=o[n-1]; *p=o[:n-1]; return x}
func swimInWater(g [][]int) int {
    n:=len(g); pq:=&PQ{}; heap.Init(pq); heap.Push(pq, Item{g[0][0],0,0})
    seen:=make([][]bool,n); for i:=range seen{seen[i]=make([]bool,n)}; seen[0][0]=true; ans:=0
    dr:=[]int{1,-1,0,0}; dc:=[]int{0,0,1,-1}
    for pq.Len()>0 {
        x:=heap.Pop(pq).(Item); if x.v>ans{ans=x.v}
        if x.r==n-1 && x.c==n-1 { return ans }
        for k:=0;k<4;k++{ nr,nc:=x.r+dr[k],x.c+dc[k]
            if nr>=0&&nr<n&&nc>=0&&nc<n&&!seen[nr][nc]{ seen[nr][nc]=true; heap.Push(pq, Item{g[nr][nc],nr,nc}) }
        }
    }
    return -1
}
func main(){ fmt.Println(swimInWater([][]int{{0,2},{1,3}})) }
''',
"R":'''
swimInWater <- function(grid){
  n <- nrow(grid); pq <- list(c(grid[1,1],1,1))
  key <- function(r,c) paste(r,c,sep=",")
  seen <- new.env(hash=TRUE); assign(key(1,1), TRUE, envir=seen); ans <- 0
  dr <- c(1,-1,0,0); dc <- c(0,0,1,-1)
  while (length(pq) > 0){
    vs <- sapply(pq, function(x) x[1]); i <- which.min(vs)
    x <- pq[[i]]; pq[[i]] <- NULL; ans <- max(ans, x[1])
    if (x[2]==n && x[3]==n) return(ans)
    for (k in 1:4){
      nr <- x[2]+dr[k]; nc <- x[3]+dc[k]
      if (nr>=1 && nr<=n && nc>=1 && nc<=n && !exists(key(nr,nc), envir=seen, inherits=FALSE)){
        assign(key(nr,nc), TRUE, envir=seen); pq[[length(pq)+1]] <- c(grid[nr,nc],nr,nc)
      }
    }
  }
  -1
}
print(swimInWater(matrix(c(0,1,2,3), nrow=2, byrow=TRUE)))
''',
}))

# ---- 091 Single Threaded CPU ----
LESSONS.append((91, "Single Threaded CPU", "Heap Priority Queue", "Medium", 46,
"""You have tasks[i] = [enqueueTime, processingTime]. CPU picks the task with shortest processing time available; ties broken by index. Return order of indices.""",
{
"Python":'''
import heapq
class Solution:
    def getOrder(self, tasks):
        idx = sorted(range(len(tasks)), key=lambda i: tasks[i][0])
        h=[]; res=[]; t=0; i=0
        while i < len(idx) or h:
            if not h:
                t = max(t, tasks[idx[i]][0])
            while i < len(idx) and tasks[idx[i]][0] <= t:
                heapq.heappush(h, (tasks[idx[i]][1], idx[i])); i += 1
            p, j = heapq.heappop(h); t += p; res.append(j)
        return res

if __name__ == "__main__":
    print(Solution().getOrder([[1,2],[2,4],[3,2],[4,1]]))
''',
"JavaScript":'''
class MinHeap{ constructor(c){this.a=[];this.c=c;} size(){return this.a.length;}
  push(x){this.a.push(x);this._u(this.a.length-1);}
  pop(){const t=this.a[0],l=this.a.pop(); if(this.a.length){this.a[0]=l;this._d(0);} return t;}
  _u(i){while(i>0){const p=(i-1)>>1; if(this.c(this.a[p],this.a[i])>0){[this.a[p],this.a[i]]=[this.a[i],this.a[p]];i=p;}else break;}}
  _d(i){const n=this.a.length; while(true){let l=2*i+1,r=2*i+2,s=i;
    if(l<n&&this.c(this.a[l],this.a[s])<0)s=l; if(r<n&&this.c(this.a[r],this.a[s])<0)s=r;
    if(s===i)break; [this.a[s],this.a[i]]=[this.a[i],this.a[s]]; i=s;}}
}
var getOrder = function(tasks){
  const idx=tasks.map((_,i)=>i).sort((a,b)=>tasks[a][0]-tasks[b][0]);
  const h=new MinHeap((x,y)=>x[0]!==y[0]?x[0]-y[0]:x[1]-y[1]);
  let t=0,i=0; const res=[];
  while (i<idx.length || h.size()){
    if (!h.size()) t=Math.max(t, tasks[idx[i]][0]);
    while (i<idx.length && tasks[idx[i]][0]<=t){ h.push([tasks[idx[i]][1],idx[i]]); i++; }
    const [p,j]=h.pop(); t+=p; res.push(j);
  } return res;
};
console.log(getOrder([[1,2],[2,4],[3,2],[4,1]]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int[] getOrder(int[][] tasks){
        Integer[] idx = new Integer[tasks.length];
        for (int i=0;i<idx.length;i++) idx[i]=i;
        Arrays.sort(idx,(a,b)->tasks[a][0]-tasks[b][0]);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[0]!=b[0]?a[0]-b[0]:a[1]-b[1]);
        long t=0; int i=0; int[] res = new int[tasks.length]; int k=0;
        while (i<idx.length || !pq.isEmpty()){
            if (pq.isEmpty()) t = Math.max(t, tasks[idx[i]][0]);
            while (i<idx.length && tasks[idx[i]][0]<=t){ pq.add(new int[]{tasks[idx[i]][1], idx[i]}); i++; }
            int[] x = pq.poll(); t += x[0]; res[k++] = x[1];
        }
        return res;
    }
    public static void main(String[] a){
        System.out.println(Arrays.toString(new __CLASS__().getOrder(new int[][]{{1,2},{2,4},{3,2},{4,1}})));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    vector<int> getOrder(vector<vector<int>>& tasks){
        int n=tasks.size(); vector<int> idx(n); iota(idx.begin(),idx.end(),0);
        sort(idx.begin(),idx.end(), [&](int a,int b){return tasks[a][0]<tasks[b][0];});
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
        long long t=0; int i=0; vector<int> res;
        while (i<n || !pq.empty()){
            if (pq.empty()) t=max(t, (long long)tasks[idx[i]][0]);
            while (i<n && tasks[idx[i]][0]<=t){ pq.push({tasks[idx[i]][1], idx[i]}); i++; }
            auto [p,j]=pq.top(); pq.pop(); t+=p; res.push_back(j);
        }
        return res;
    }
};
int main(){ vector<vector<int>> t={{1,2},{2,4},{3,2},{4,1}};
    for (int x: Solution().getOrder(t)) cout<<x<<" "; cout<<endl; }
''',
"Go":'''
package main
import ( "container/heap"; "fmt"; "sort" )
type T struct{ p,i int }
type H []T
func (h H) Len()int{return len(h)}
func (h H) Less(i,j int)bool{ if h[i].p!=h[j].p{return h[i].p<h[j].p}; return h[i].i<h[j].i }
func (h H) Swap(i,j int){h[i],h[j]=h[j],h[i]}
func (h *H) Push(x any){*h=append(*h,x.(T))}
func (h *H) Pop()any{o:=*h; n:=len(o); x:=o[n-1]; *h=o[:n-1]; return x}
func getOrder(tasks [][]int) []int {
    n:=len(tasks); idx:=make([]int,n); for i:=range idx{idx[i]=i}
    sort.Slice(idx, func(a,b int)bool{return tasks[idx[a]][0]<tasks[idx[b]][0]})
    h:=&H{}; heap.Init(h); var t int64=0; i:=0; res:=[]int{}
    for i<n || h.Len()>0 {
        if h.Len()==0 { if int64(tasks[idx[i]][0])>t { t=int64(tasks[idx[i]][0]) } }
        for i<n && int64(tasks[idx[i]][0])<=t { heap.Push(h, T{tasks[idx[i]][1], idx[i]}); i++ }
        x:=heap.Pop(h).(T); t+=int64(x.p); res=append(res,x.i)
    }
    return res
}
func main(){ fmt.Println(getOrder([][]int{{1,2},{2,4},{3,2},{4,1}})) }
''',
"R":'''
getOrder <- function(tasks){
  n <- length(tasks); idx <- order(sapply(tasks, function(x) x[1]))
  h <- list(); t <- 0; i <- 1; res <- c()
  while (i <= n || length(h) > 0){
    if (length(h)==0) t <- max(t, tasks[[idx[i]]][1])
    while (i <= n && tasks[[idx[i]]][1] <= t){
      h[[length(h)+1]] <- c(tasks[[idx[i]]][2], idx[i]); i <- i+1
    }
    pv <- sapply(h, function(x) x[1]); pi <- sapply(h, function(x) x[2])
    ord <- order(pv, pi); j <- ord[1]
    t <- t + h[[j]][1]; res <- c(res, h[[j]][2]); h[[j]] <- NULL
  }
  res
}
print(getOrder(list(c(1,2),c(2,4),c(3,2),c(4,1))))
''',
}))

# ---- 092 Reorganize String ----
LESSONS.append((92, "Reorganize String", "Heap Priority Queue", "Medium", 46,
"""Given a string s, rearrange so no two adjacent chars are equal. Return the rearranged string, or '' if impossible.""",
{
"Python":'''
import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s):
        cnt = Counter(s); n=len(s)
        if max(cnt.values()) > (n+1)//2: return ""
        h = [(-v,k) for k,v in cnt.items()]; heapq.heapify(h)
        res=[]
        while len(h)>=2:
            v1,c1=heapq.heappop(h); v2,c2=heapq.heappop(h)
            res.append(c1); res.append(c2)
            if v1+1<0: heapq.heappush(h,(v1+1,c1))
            if v2+1<0: heapq.heappush(h,(v2+1,c2))
        if h: res.append(h[0][1])
        return "".join(res)

if __name__ == "__main__":
    print(Solution().reorganizeString("aab"))
    print(Solution().reorganizeString("aaab"))
''',
"JavaScript":'''
var reorganizeString = function(s){
  const c={}; for (const ch of s) c[ch]=(c[ch]||0)+1;
  const n=s.length; let mx=0; for (const k in c) mx=Math.max(mx,c[k]);
  if (mx > Math.floor((n+1)/2)) return "";
  const arr=Object.entries(c).sort((a,b)=>b[1]-a[1]);
  const res=Array(n);
  let i=0;
  for (const [ch,cnt] of arr){
    for (let k=0;k<cnt;k++){
      if (i>=n) i=1;
      res[i]=ch; i+=2;
    }
  }
  return res.join("");
};
console.log(reorganizeString("aab"), JSON.stringify(reorganizeString("aaab")));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public String reorganizeString(String s){
        int[] c = new int[26];
        for (char ch: s.toCharArray()) c[ch-'a']++;
        int n=s.length(), mx=0, idx=0;
        for (int i=0;i<26;i++) if (c[i]>mx){ mx=c[i]; idx=i; }
        if (mx > (n+1)/2) return "";
        char[] res = new char[n]; int i=0;
        while (c[idx]>0){ res[i]=(char)('a'+idx); i+=2; c[idx]--; }
        for (int k=0;k<26;k++){
            while (c[k]>0){ if (i>=n) i=1; res[i]=(char)('a'+k); i+=2; c[k]--; }
        }
        return new String(res);
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().reorganizeString("aab"));
        System.out.println("[" + new __CLASS__().reorganizeString("aaab") + "]");
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    string reorganizeString(string s){
        int c[26]={0}; for (char ch: s) c[ch-'a']++;
        int n=s.size(), mx=0, idx=0;
        for (int i=0;i<26;i++) if (c[i]>mx){ mx=c[i]; idx=i; }
        if (mx > (n+1)/2) return "";
        string res(n,' '); int i=0;
        while (c[idx]>0){ res[i]='a'+idx; i+=2; c[idx]--; }
        for (int k=0;k<26;k++){
            while (c[k]>0){ if (i>=n) i=1; res[i]='a'+k; i+=2; c[k]--; }
        }
        return res;
    }
};
int main(){ cout<<Solution().reorganizeString("aab")<<" ["<<Solution().reorganizeString("aaab")<<"]"<<endl; }
''',
"Go":'''
package main
import "fmt"
func reorganizeString(s string) string {
    c := [26]int{}; for i := range s { c[s[i]-'a']++ }
    n := len(s); mx, idx := 0, 0
    for i := 0; i < 26; i++ { if c[i] > mx { mx, idx = c[i], i } }
    if mx > (n+1)/2 { return "" }
    res := make([]byte, n); i := 0
    for c[idx] > 0 { res[i] = byte('a'+idx); i += 2; c[idx]-- }
    for k := 0; k < 26; k++ {
        for c[k] > 0 { if i >= n { i = 1 }; res[i] = byte('a'+k); i += 2; c[k]-- }
    }
    return string(res)
}
func main(){ fmt.Println(reorganizeString("aab"), "["+reorganizeString("aaab")+"]") }
''',
"R":'''
reorganizeString <- function(s){
  chars <- strsplit(s,"")[[1]]; tab <- table(chars); n <- length(chars)
  if (max(tab) > (n+1) %/% 2 + (n+1) %% 2) {
    if (max(tab) > ceiling(n/2)) return("")
  }
  ord <- names(sort(tab, decreasing=TRUE))
  res <- character(n); i <- 1
  for (ch in ord){
    cnt <- tab[[ch]]
    for (k in 1:cnt){
      if (i > n) i <- 2
      res[i] <- ch; i <- i + 2
    }
  }
  paste(res, collapse="")
}
print(reorganizeString("aab"))
print(paste0("[", reorganizeString("aaab"), "]"))
''',
}))

# ---- 093 Alien Dictionary ----
LESSONS.append((93, "Alien Dictionary", "Advanced Graphs", "Hard", 47,
"""Given a sorted list of words from an alien language, derive the order of letters. Return any valid order or '' if impossible.""",
{
"Python":'''
from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words):
        g = defaultdict(set); ind = {c:0 for w in words for c in w}
        for a,b in zip(words, words[1:]):
            for x,y in zip(a,b):
                if x!=y:
                    if y not in g[x]: g[x].add(y); ind[y]+=1
                    break
            else:
                if len(a)>len(b): return ""
        q = deque([c for c in ind if ind[c]==0]); res=[]
        while q:
            c = q.popleft(); res.append(c)
            for nx in g[c]:
                ind[nx]-=1
                if ind[nx]==0: q.append(nx)
        return "".join(res) if len(res)==len(ind) else ""

if __name__ == "__main__":
    print(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]))
''',
"JavaScript":'''
var alienOrder = function(words){
  const g={}, ind={};
  for (const w of words) for (const c of w){ g[c]=g[c]||new Set(); ind[c]=ind[c]||0; }
  for (let i=0;i<words.length-1;i++){
    const a=words[i], b=words[i+1]; let found=false;
    const m=Math.min(a.length,b.length);
    for (let j=0;j<m;j++){
      if (a[j]!==b[j]){
        if (!g[a[j]].has(b[j])){ g[a[j]].add(b[j]); ind[b[j]]++; }
        found=true; break;
      }
    }
    if (!found && a.length>b.length) return "";
  }
  const q=[]; for (const c in ind) if (ind[c]===0) q.push(c);
  const res=[];
  while (q.length){
    const c=q.shift(); res.push(c);
    for (const nx of g[c]){ ind[nx]--; if (ind[nx]===0) q.push(nx); }
  }
  return res.length===Object.keys(ind).length ? res.join("") : "";
};
console.log(alienOrder(["wrt","wrf","er","ett","rftt"]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public String alienOrder(String[] words){
        Map<Character, Set<Character>> g = new HashMap<>();
        Map<Character, Integer> ind = new HashMap<>();
        for (String w: words) for (char c: w.toCharArray()){ g.putIfAbsent(c,new HashSet<>()); ind.putIfAbsent(c,0); }
        for (int i=0;i<words.length-1;i++){
            String a=words[i], b=words[i+1]; boolean found=false;
            int m=Math.min(a.length(),b.length());
            for (int j=0;j<m;j++){
                char x=a.charAt(j), y=b.charAt(j);
                if (x!=y){ if (g.get(x).add(y)) ind.merge(y,1,Integer::sum); found=true; break; }
            }
            if (!found && a.length()>b.length()) return "";
        }
        Deque<Character> q = new ArrayDeque<>();
        for (var e: ind.entrySet()) if (e.getValue()==0) q.add(e.getKey());
        StringBuilder sb = new StringBuilder();
        while (!q.isEmpty()){
            char c=q.poll(); sb.append(c);
            for (char nx: g.get(c)){ ind.merge(nx,-1,Integer::sum); if (ind.get(nx)==0) q.add(nx); }
        }
        return sb.length()==ind.size() ? sb.toString() : "";
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().alienOrder(new String[]{"wrt","wrf","er","ett","rftt"}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    string alienOrder(vector<string>& words){
        unordered_map<char, unordered_set<char>> g;
        unordered_map<char,int> ind;
        for (auto& w: words) for (char c: w){ g[c]; if (!ind.count(c)) ind[c]=0; }
        for (int i=0;i+1<(int)words.size();i++){
            auto& a=words[i]; auto& b=words[i+1]; bool found=false;
            int m=min(a.size(),b.size());
            for (int j=0;j<m;j++){
                if (a[j]!=b[j]){ if (g[a[j]].insert(b[j]).second) ind[b[j]]++; found=true; break; }
            }
            if (!found && a.size()>b.size()) return "";
        }
        queue<char> q; for (auto& p: ind) if (p.second==0) q.push(p.first);
        string res;
        while (!q.empty()){
            char c=q.front(); q.pop(); res+=c;
            for (char nx: g[c]) if (--ind[nx]==0) q.push(nx);
        }
        return res.size()==ind.size() ? res : "";
    }
};
int main(){ vector<string> w={"wrt","wrf","er","ett","rftt"}; cout<<Solution().alienOrder(w)<<endl; }
''',
"Go":'''
package main
import "fmt"
func alienOrder(words []string) string {
    g := map[byte]map[byte]bool{}; ind := map[byte]int{}
    for _, w := range words { for i := 0; i < len(w); i++ {
        if _, ok := g[w[i]]; !ok { g[w[i]] = map[byte]bool{} }
        if _, ok := ind[w[i]]; !ok { ind[w[i]] = 0 }
    }}
    for i := 0; i < len(words)-1; i++ {
        a, b := words[i], words[i+1]; found := false
        m := len(a); if len(b) < m { m = len(b) }
        for j := 0; j < m; j++ {
            if a[j] != b[j] { if !g[a[j]][b[j]] { g[a[j]][b[j]] = true; ind[b[j]]++ }; found = true; break }
        }
        if !found && len(a) > len(b) { return "" }
    }
    q := []byte{}; for c, v := range ind { if v == 0 { q = append(q, c) } }
    res := []byte{}
    for len(q) > 0 {
        c := q[0]; q = q[1:]; res = append(res, c)
        for nx := range g[c] { ind[nx]--; if ind[nx] == 0 { q = append(q, nx) } }
    }
    if len(res) != len(ind) { return "" }
    return string(res)
}
func main(){ fmt.Println(alienOrder([]string{"wrt","wrf","er","ett","rftt"})) }
''',
"R":'''
alienOrder <- function(words){
  g <- list(); ind <- list()
  for (w in words) for (c in strsplit(w,"")[[1]]){ if(is.null(g[[c]])) g[[c]] <- c(); if(is.null(ind[[c]])) ind[[c]] <- 0 }
  if (length(words) > 1) for (i in 1:(length(words)-1)){
    a <- strsplit(words[i],"")[[1]]; b <- strsplit(words[i+1],"")[[1]]; found <- FALSE
    m <- min(length(a), length(b))
    if (m > 0) for (j in 1:m){
      if (a[j] != b[j]){ if (!(b[j] %in% g[[a[j]]])){ g[[a[j]]] <- c(g[[a[j]]], b[j]); ind[[b[j]]] <- ind[[b[j]]] + 1 }; found <- TRUE; break }
    }
    if (!found && length(a) > length(b)) return("")
  }
  q <- names(ind)[sapply(names(ind), function(c) ind[[c]] == 0)]
  res <- c()
  while (length(q) > 0){
    c <- q[1]; q <- q[-1]; res <- c(res, c)
    for (nx in g[[c]]){ ind[[nx]] <- ind[[nx]] - 1; if (ind[[nx]] == 0) q <- c(q, nx) }
  }
  if (length(res) != length(ind)) return("")
  paste(res, collapse="")
}
print(alienOrder(c("wrt","wrf","er","ett","rftt")))
''',
}))

# ---- 094 Find Critical and Pseudo Critical Edges in MST ----
LESSONS.append((94, "Find Critical and Pseudo Critical Edges in MST", "Advanced Graphs", "Hard", 47,
"""Given n nodes and weighted edges, find indices of critical and pseudo-critical edges in any MST.""",
{
"Python":'''
class DSU:
    def __init__(self,n): self.p=list(range(n)); self.r=[0]*n; self.cnt=n
    def f(self,x):
        while self.p[x]!=x: self.p[x]=self.p[self.p[x]]; x=self.p[x]
        return x
    def u(self,a,b):
        a,b=self.f(a),self.f(b)
        if a==b: return False
        if self.r[a]<self.r[b]: a,b=b,a
        self.p[b]=a
        if self.r[a]==self.r[b]: self.r[a]+=1
        self.cnt-=1; return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        for i,e in enumerate(edges): e.append(i)
        edges.sort(key=lambda e: e[2])
        def kruskal(skip=-1, force=-1):
            d=DSU(n); w=0
            if force>=0:
                u,v,wt,_ = edges[force]
                if not d.u(u,v): return float('inf')
                w += wt
            for i,(u,v,wt,_) in enumerate(edges):
                if i==skip: continue
                if d.u(u,v): w += wt
            return w if d.cnt==1 else float('inf')
        base = kruskal()
        crit, pseu = [], []
        for i,(u,v,wt,oi) in enumerate(edges):
            if kruskal(skip=i) > base: crit.append(oi)
            elif kruskal(force=i) == base: pseu.append(oi)
        return [crit, pseu]

if __name__ == "__main__":
    print(Solution().findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))
''',
"JavaScript":'''
class DSU{ constructor(n){this.p=Array(n).fill(0).map((_,i)=>i); this.r=Array(n).fill(0); this.cnt=n;}
  f(x){ while(this.p[x]!==x){this.p[x]=this.p[this.p[x]]; x=this.p[x];} return x; }
  u(a,b){ a=this.f(a); b=this.f(b); if(a===b) return false;
    if(this.r[a]<this.r[b]){[a,b]=[b,a];} this.p[b]=a;
    if(this.r[a]===this.r[b]) this.r[a]++; this.cnt--; return true;}
}
var findCriticalAndPseudoCriticalEdges = function(n, edges){
  edges.forEach((e,i)=>e.push(i));
  edges.sort((a,b)=>a[2]-b[2]);
  const k=(skip=-1,force=-1)=>{
    const d=new DSU(n); let w=0;
    if (force>=0){ const [u,v,wt]=edges[force]; if(!d.u(u,v)) return Infinity; w+=wt; }
    for (let i=0;i<edges.length;i++){ if(i===skip) continue; const [u,v,wt]=edges[i]; if(d.u(u,v)) w+=wt; }
    return d.cnt===1 ? w : Infinity;
  };
  const base=k(); const crit=[], pseu=[];
  for (let i=0;i<edges.length;i++){
    if (k(i,-1) > base) crit.push(edges[i][3]);
    else if (k(-1,i) === base) pseu.push(edges[i][3]);
  }
  return [crit, pseu];
};
console.log(JSON.stringify(findCriticalAndPseudoCriticalEdges(5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]])));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class DSU { int[] p,r; int cnt;
        DSU(int n){ p=new int[n]; r=new int[n]; cnt=n; for(int i=0;i<n;i++) p[i]=i; }
        int f(int x){ while(p[x]!=x){p[x]=p[p[x]]; x=p[x];} return x; }
        boolean u(int a,int b){ a=f(a); b=f(b); if(a==b) return false;
            if(r[a]<r[b]){int t=a;a=b;b=t;} p[b]=a; if(r[a]==r[b]) r[a]++; cnt--; return true; }
    }
    int n; int[][] E;
    int kruskal(int skip, int force){
        DSU d=new DSU(n); int w=0;
        if (force>=0){ if(!d.u(E[force][0],E[force][1])) return Integer.MAX_VALUE; w+=E[force][2]; }
        for (int i=0;i<E.length;i++){ if(i==skip) continue; if(d.u(E[i][0],E[i][1])) w+=E[i][2]; }
        return d.cnt==1 ? w : Integer.MAX_VALUE;
    }
    public List<List<Integer>> findCriticalAndPseudoCriticalEdges(int n, int[][] edges){
        this.n=n; int[][] e=new int[edges.length][4];
        for (int i=0;i<edges.length;i++){ e[i][0]=edges[i][0]; e[i][1]=edges[i][1]; e[i][2]=edges[i][2]; e[i][3]=i; }
        Arrays.sort(e,(a,b)->a[2]-b[2]); E=e;
        int base=kruskal(-1,-1);
        List<Integer> crit=new ArrayList<>(), pseu=new ArrayList<>();
        for (int i=0;i<e.length;i++){
            if (kruskal(i,-1) > base) crit.add(e[i][3]);
            else if (kruskal(-1,i) == base) pseu.add(e[i][3]);
        }
        return Arrays.asList(crit, pseu);
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().findCriticalAndPseudoCriticalEdges(5, new int[][]{{0,1,1},{1,2,1},{2,3,2},{0,3,2},{0,4,3},{3,4,3},{1,4,6}}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
struct DSU { vector<int> p,r; int cnt;
    DSU(int n):p(n),r(n,0),cnt(n){ iota(p.begin(),p.end(),0); }
    int f(int x){ while(p[x]!=x){ p[x]=p[p[x]]; x=p[x]; } return x; }
    bool u(int a,int b){ a=f(a); b=f(b); if(a==b) return false;
        if(r[a]<r[b]) swap(a,b); p[b]=a; if(r[a]==r[b]) r[a]++; cnt--; return true; }
};
class Solution { public:
    int n; vector<vector<int>> E;
    int kruskal(int skip, int force){
        DSU d(n); int w=0;
        if (force>=0){ if(!d.u(E[force][0],E[force][1])) return INT_MAX; w+=E[force][2]; }
        for (int i=0;i<(int)E.size();i++){ if(i==skip) continue; if(d.u(E[i][0],E[i][1])) w+=E[i][2]; }
        return d.cnt==1 ? w : INT_MAX;
    }
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int N, vector<vector<int>>& edges){
        n=N; E=edges; for (int i=0;i<(int)E.size();i++) E[i].push_back(i);
        sort(E.begin(),E.end(),[](auto&a,auto&b){return a[2]<b[2];});
        int base=kruskal(-1,-1); vector<int> crit, pseu;
        for (int i=0;i<(int)E.size();i++){
            if (kruskal(i,-1) > base) crit.push_back(E[i][3]);
            else if (kruskal(-1,i) == base) pseu.push_back(E[i][3]);
        }
        return {crit, pseu};
    }
};
int main(){ vector<vector<int>> e={{0,1,1},{1,2,1},{2,3,2},{0,3,2},{0,4,3},{3,4,3},{1,4,6}};
    auto r=Solution().findCriticalAndPseudoCriticalEdges(5,e);
    for (auto& v: r){ cout<<"["; for(int x: v)cout<<x<<","; cout<<"] "; } cout<<endl; }
''',
"Go":'''
package main
import ( "fmt"; "sort" )
type DSU struct{ p, r []int; cnt int }
func NewDSU(n int) *DSU { d:=&DSU{p:make([]int,n), r:make([]int,n), cnt:n}; for i:=range d.p{d.p[i]=i}; return d }
func (d *DSU) f(x int) int { for d.p[x]!=x { d.p[x]=d.p[d.p[x]]; x=d.p[x] }; return x }
func (d *DSU) u(a,b int) bool { a,b=d.f(a),d.f(b); if a==b{return false}
    if d.r[a]<d.r[b]{a,b=b,a}; d.p[b]=a; if d.r[a]==d.r[b]{d.r[a]++}; d.cnt--; return true }
func findCriticalAndPseudoCriticalEdges(n int, edges [][]int) [][]int {
    E := make([][]int, len(edges))
    for i, e := range edges { E[i] = []int{e[0], e[1], e[2], i} }
    sort.Slice(E, func(i,j int) bool { return E[i][2] < E[j][2] })
    kruskal := func(skip, force int) int {
        d := NewDSU(n); w := 0
        if force >= 0 { if !d.u(E[force][0], E[force][1]) { return 1<<30 }; w += E[force][2] }
        for i, e := range E { if i==skip { continue }; if d.u(e[0], e[1]) { w += e[2] } }
        if d.cnt != 1 { return 1<<30 }; return w
    }
    base := kruskal(-1,-1)
    crit, pseu := []int{}, []int{}
    for i, e := range E {
        if kruskal(i,-1) > base { crit = append(crit, e[3]) } else if kruskal(-1,i) == base { pseu = append(pseu, e[3]) }
    }
    return [][]int{crit, pseu}
}
func main(){ fmt.Println(findCriticalAndPseudoCriticalEdges(5, [][]int{{0,1,1},{1,2,1},{2,3,2},{0,3,2},{0,4,3},{3,4,3},{1,4,6}})) }
''',
"R":'''
findCriticalAndPseudoCriticalEdges <- function(n, edges){
  E <- lapply(seq_along(edges), function(i) c(edges[[i]], i-1))
  E <- E[order(sapply(E, function(e) e[3]))]
  dsu_new <- function(n) list(p=0:(n-1), r=rep(0,n), cnt=n)
  dsu_f <- function(d,x){ while(d$p[x+1]!=x){ d$p[x+1] <<- d$p[d$p[x+1]+1]; x <- d$p[x+1] }; x }
  dsu_u <- function(d,a,b){
    a <- dsu_f(d,a); b <- dsu_f(d,b); if(a==b) return(list(d=d, ok=FALSE))
    if(d$r[a+1]<d$r[b+1]){ t<-a; a<-b; b<-t }
    d$p[b+1] <- a; if(d$r[a+1]==d$r[b+1]) d$r[a+1] <- d$r[a+1]+1; d$cnt <- d$cnt-1
    list(d=d, ok=TRUE)
  }
  kruskal <- function(skip, force){
    d <- dsu_new(n); w <- 0
    if (force >= 0){ res <- dsu_u(d, E[[force+1]][1], E[[force+1]][2]); if(!res$ok) return(Inf); d <- res$d; w <- w + E[[force+1]][3] }
    for (i in seq_along(E)){ if (i-1 == skip) next; res <- dsu_u(d, E[[i]][1], E[[i]][2]); if(res$ok){ d <- res$d; w <- w + E[[i]][3] } }
    if (d$cnt != 1) return(Inf); w
  }
  base <- kruskal(-1,-1); crit <- c(); pseu <- c()
  for (i in seq_along(E)){
    if (kruskal(i-1,-1) > base) crit <- c(crit, E[[i]][4])
    else if (kruskal(-1,i-1) == base) pseu <- c(pseu, E[[i]][4])
  }
  list(crit, pseu)
}
print(findCriticalAndPseudoCriticalEdges(5, list(c(0,1,1),c(1,2,1),c(2,3,2),c(0,3,2),c(0,4,3),c(3,4,3),c(1,4,6))))
''',
}))

# ---- 095 Happy Number ----
LESSONS.append((95, "Happy Number", "Math and Geometry", "Easy", 48,
"""A number is happy if repeatedly summing the squares of its digits eventually equals 1. Return true if n is happy.""",
{
"Python":'''
class Solution:
    def isHappy(self, n):
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = sum(int(c)**2 for c in str(n))
        return n==1

if __name__ == "__main__":
    print(Solution().isHappy(19))
    print(Solution().isHappy(2))
''',
"JavaScript":'''
var isHappy = function(n){
  const seen=new Set();
  while (n!==1 && !seen.has(n)){
    seen.add(n);
    let s=0; while(n>0){ const d=n%10; s+=d*d; n=Math.floor(n/10); } n=s;
  }
  return n===1;
};
console.log(isHappy(19), isHappy(2));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public boolean isHappy(int n){
        Set<Integer> seen = new HashSet<>();
        while (n!=1 && !seen.contains(n)){
            seen.add(n); int s=0;
            while (n>0){ int d=n%10; s+=d*d; n/=10; } n=s;
        }
        return n==1;
    }
    public static void main(String[] a){
        __CLASS__ x=new __CLASS__(); System.out.println(x.isHappy(19)); System.out.println(x.isHappy(2));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    bool isHappy(int n){
        unordered_set<int> seen;
        while (n!=1 && !seen.count(n)){
            seen.insert(n); int s=0;
            while (n>0){ int d=n%10; s+=d*d; n/=10; } n=s;
        }
        return n==1;
    }
};
int main(){ Solution s; cout<<s.isHappy(19)<<" "<<s.isHappy(2)<<endl; }
''',
"Go":'''
package main
import "fmt"
func isHappy(n int) bool {
    seen := map[int]bool{}
    for n != 1 && !seen[n] {
        seen[n] = true; s := 0
        for n > 0 { d := n%10; s += d*d; n /= 10 }
        n = s
    }
    return n == 1
}
func main(){ fmt.Println(isHappy(19), isHappy(2)) }
''',
"R":'''
isHappy <- function(n){
  seen <- c()
  while (n != 1 && !(n %in% seen)){
    seen <- c(seen, n); s <- 0
    while (n > 0){ d <- n %% 10; s <- s + d*d; n <- n %/% 10 }
    n <- s
  }
  n == 1
}
print(isHappy(19)); print(isHappy(2))
''',
}))

# ---- 096 Rotate Image ----
LESSONS.append((96, "Rotate Image", "Math and Geometry", "Medium", 48,
"""Rotate an n x n 2D matrix 90 degrees clockwise in-place.""",
{
"Python":'''
class Solution:
    def rotate(self, m):
        n=len(m)
        for i in range(n):
            for j in range(i+1,n): m[i][j], m[j][i] = m[j][i], m[i][j]
        for row in m: row.reverse()

if __name__ == "__main__":
    m=[[1,2,3],[4,5,6],[7,8,9]]; Solution().rotate(m); print(m)
''',
"JavaScript":'''
var rotate = function(m){
  const n=m.length;
  for (let i=0;i<n;i++) for (let j=i+1;j<n;j++) [m[i][j], m[j][i]]=[m[j][i], m[i][j]];
  for (const r of m) r.reverse();
};
const m=[[1,2,3],[4,5,6],[7,8,9]]; rotate(m); console.log(JSON.stringify(m));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public void rotate(int[][] m){
        int n=m.length;
        for (int i=0;i<n;i++) for (int j=i+1;j<n;j++){ int t=m[i][j]; m[i][j]=m[j][i]; m[j][i]=t; }
        for (int[] r: m) for (int i=0,j=n-1;i<j;i++,j--){ int t=r[i]; r[i]=r[j]; r[j]=t; }
    }
    public static void main(String[] a){
        int[][] m={{1,2,3},{4,5,6},{7,8,9}}; new __CLASS__().rotate(m);
        System.out.println(Arrays.deepToString(m));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    void rotate(vector<vector<int>>& m){
        int n=m.size();
        for (int i=0;i<n;i++) for (int j=i+1;j<n;j++) swap(m[i][j], m[j][i]);
        for (auto& r: m) reverse(r.begin(), r.end());
    }
};
int main(){ vector<vector<int>> m={{1,2,3},{4,5,6},{7,8,9}}; Solution().rotate(m);
    for (auto& r: m){ for (int x: r) cout<<x<<" "; cout<<endl; } }
''',
"Go":'''
package main
import "fmt"
func rotate(m [][]int) {
    n := len(m)
    for i := 0; i < n; i++ { for j := i+1; j < n; j++ { m[i][j], m[j][i] = m[j][i], m[i][j] } }
    for _, r := range m { for i, j := 0, n-1; i < j; i, j = i+1, j-1 { r[i], r[j] = r[j], r[i] } }
}
func main(){ m := [][]int{{1,2,3},{4,5,6},{7,8,9}}; rotate(m); fmt.Println(m) }
''',
"R":'''
rotate <- function(m){
  n <- nrow(m); res <- matrix(0, n, n)
  for (i in 1:n) for (j in 1:n) res[i, n-j+1] <- m[j, i]
  res
}
print(rotate(matrix(1:9, 3, 3, byrow=TRUE)))
''',
}))

# ---- 097 Majority Element ----
LESSONS.append((97, "Majority Element", "Arrays and Hashing", "Easy", 49,
"""Given an array of size n, return the element that appears more than n/2 times.""",
{
"Python":'''
class Solution:
    def majorityElement(self, nums):
        cand=0; cnt=0
        for n in nums:
            if cnt==0: cand=n
            cnt += 1 if n==cand else -1
        return cand

if __name__ == "__main__":
    print(Solution().majorityElement([3,2,3]))
    print(Solution().majorityElement([2,2,1,1,1,2,2]))
''',
"JavaScript":'''
var majorityElement = function(nums){
  let cand=0, cnt=0;
  for (const n of nums){ if (cnt===0) cand=n; cnt += n===cand?1:-1; }
  return cand;
};
console.log(majorityElement([3,2,3]), majorityElement([2,2,1,1,1,2,2]));
''',
"Java":'''
public class __CLASS__ {
    public int majorityElement(int[] nums){
        int cand=0, cnt=0;
        for (int n: nums){ if (cnt==0) cand=n; cnt += n==cand?1:-1; }
        return cand;
    }
    public static void main(String[] a){
        __CLASS__ x=new __CLASS__();
        System.out.println(x.majorityElement(new int[]{3,2,3}));
        System.out.println(x.majorityElement(new int[]{2,2,1,1,1,2,2}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    int majorityElement(vector<int>& nums){
        int cand=0, cnt=0;
        for (int n: nums){ if (cnt==0) cand=n; cnt += n==cand?1:-1; }
        return cand;
    }
};
int main(){ vector<int> a={3,2,3}, b={2,2,1,1,1,2,2};
    cout<<Solution().majorityElement(a)<<" "<<Solution().majorityElement(b)<<endl; }
''',
"Go":'''
package main
import "fmt"
func majorityElement(nums []int) int {
    cand, cnt := 0, 0
    for _, n := range nums { if cnt==0 { cand=n }; if n==cand { cnt++ } else { cnt-- } }
    return cand
}
func main(){ fmt.Println(majorityElement([]int{3,2,3}), majorityElement([]int{2,2,1,1,1,2,2})) }
''',
"R":'''
majorityElement <- function(nums){
  cand <- 0; cnt <- 0
  for (n in nums){ if (cnt==0) cand <- n; cnt <- cnt + ifelse(n==cand, 1, -1) }
  cand
}
print(majorityElement(c(3,2,3)))
print(majorityElement(c(2,2,1,1,1,2,2)))
''',
}))

# ---- 098 Sort Colors ----
LESSONS.append((98, "Sort Colors", "Arrays and Hashing", "Medium", 49,
"""Sort an array containing only 0, 1, 2 in-place (Dutch national flag).""",
{
"Python":'''
class Solution:
    def sortColors(self, nums):
        l, m, r = 0, 0, len(nums)-1
        while m <= r:
            if nums[m]==0: nums[l],nums[m]=nums[m],nums[l]; l+=1; m+=1
            elif nums[m]==2: nums[r],nums[m]=nums[m],nums[r]; r-=1
            else: m+=1

if __name__ == "__main__":
    a=[2,0,2,1,1,0]; Solution().sortColors(a); print(a)
''',
"JavaScript":'''
var sortColors = function(nums){
  let l=0, m=0, r=nums.length-1;
  while (m<=r){
    if (nums[m]===0){ [nums[l],nums[m]]=[nums[m],nums[l]]; l++; m++; }
    else if (nums[m]===2){ [nums[r],nums[m]]=[nums[m],nums[r]]; r--; }
    else m++;
  }
};
const a=[2,0,2,1,1,0]; sortColors(a); console.log(JSON.stringify(a));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public void sortColors(int[] nums){
        int l=0, m=0, r=nums.length-1;
        while (m<=r){
            if (nums[m]==0){ int t=nums[l]; nums[l]=nums[m]; nums[m]=t; l++; m++; }
            else if (nums[m]==2){ int t=nums[r]; nums[r]=nums[m]; nums[m]=t; r--; }
            else m++;
        }
    }
    public static void main(String[] a){
        int[] x={2,0,2,1,1,0}; new __CLASS__().sortColors(x); System.out.println(Arrays.toString(x));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    void sortColors(vector<int>& nums){
        int l=0, m=0, r=nums.size()-1;
        while (m<=r){
            if (nums[m]==0){ swap(nums[l],nums[m]); l++; m++; }
            else if (nums[m]==2){ swap(nums[r],nums[m]); r--; }
            else m++;
        }
    }
};
int main(){ vector<int> a={2,0,2,1,1,0}; Solution().sortColors(a);
    for (int x: a) cout<<x<<" "; cout<<endl; }
''',
"Go":'''
package main
import "fmt"
func sortColors(nums []int) {
    l, m, r := 0, 0, len(nums)-1
    for m <= r {
        if nums[m]==0 { nums[l], nums[m] = nums[m], nums[l]; l++; m++
        } else if nums[m]==2 { nums[r], nums[m] = nums[m], nums[r]; r--
        } else { m++ }
    }
}
func main(){ a := []int{2,0,2,1,1,0}; sortColors(a); fmt.Println(a) }
''',
"R":'''
sortColors <- function(nums){
  l <- 1; m <- 1; r <- length(nums)
  while (m <= r){
    if (nums[m]==0){ tmp<-nums[l]; nums[l]<-nums[m]; nums[m]<-tmp; l<-l+1; m<-m+1
    } else if (nums[m]==2){ tmp<-nums[r]; nums[r]<-nums[m]; nums[m]<-tmp; r<-r-1
    } else { m<-m+1 }
  }
  nums
}
print(sortColors(c(2,0,2,1,1,0)))
''',
}))

# ---- 099 Word Search ----
LESSONS.append((99, "Word Search", "Backtracking", "Medium", 50,
"""Given an m x n board and a word, return true if the word exists by sequentially adjacent cells (no reuse).""",
{
"Python":'''
class Solution:
    def exist(self, board, word):
        R,C = len(board), len(board[0])
        def dfs(r,c,i):
            if i==len(word): return True
            if r<0 or r>=R or c<0 or c>=C or board[r][c]!=word[i]: return False
            tmp=board[r][c]; board[r][c]='#'
            ok = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            board[r][c]=tmp; return ok
        for r in range(R):
            for c in range(C):
                if dfs(r,c,0): return True
        return False

if __name__ == "__main__":
    print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
''',
"JavaScript":'''
var exist = function(board, word){
  const R=board.length, C=board[0].length;
  const dfs=(r,c,i)=>{
    if (i===word.length) return true;
    if (r<0||r>=R||c<0||c>=C||board[r][c]!==word[i]) return false;
    const t=board[r][c]; board[r][c]='#';
    const ok = dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1);
    board[r][c]=t; return ok;
  };
  for (let r=0;r<R;r++) for (let c=0;c<C;c++) if (dfs(r,c,0)) return true;
  return false;
};
console.log(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"));
''',
"Java":'''
public class __CLASS__ {
    char[][] b; String w;
    boolean dfs(int r,int c,int i){
        if (i==w.length()) return true;
        if (r<0||r>=b.length||c<0||c>=b[0].length||b[r][c]!=w.charAt(i)) return false;
        char t=b[r][c]; b[r][c]='#';
        boolean ok = dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1);
        b[r][c]=t; return ok;
    }
    public boolean exist(char[][] board, String word){
        b=board; w=word;
        for (int r=0;r<b.length;r++) for (int c=0;c<b[0].length;c++) if (dfs(r,c,0)) return true;
        return false;
    }
    public static void main(String[] a){
        char[][] bd={{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
        System.out.println(new __CLASS__().exist(bd, "ABCCED"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    vector<vector<char>>* B; string W;
    bool dfs(int r,int c,int i){
        if (i==(int)W.size()) return true;
        if (r<0||r>=(int)B->size()||c<0||c>=(int)(*B)[0].size()||(*B)[r][c]!=W[i]) return false;
        char t=(*B)[r][c]; (*B)[r][c]='#';
        bool ok = dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1);
        (*B)[r][c]=t; return ok;
    }
    bool exist(vector<vector<char>>& board, string word){
        B=&board; W=word;
        for (int r=0;r<(int)board.size();r++) for (int c=0;c<(int)board[0].size();c++) if (dfs(r,c,0)) return true;
        return false;
    }
};
int main(){ vector<vector<char>> b={{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    cout<<Solution().exist(b, "ABCCED")<<endl; }
''',
"Go":'''
package main
import "fmt"
func exist(board [][]byte, word string) bool {
    R, C := len(board), len(board[0])
    var dfs func(r,c,i int) bool
    dfs = func(r,c,i int) bool {
        if i == len(word) { return true }
        if r<0||r>=R||c<0||c>=C||board[r][c]!=word[i] { return false }
        t := board[r][c]; board[r][c] = '#'
        ok := dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1)
        board[r][c] = t; return ok
    }
    for r := 0; r < R; r++ { for c := 0; c < C; c++ { if dfs(r,c,0) { return true } } }
    return false
}
func main(){ b := [][]byte{[]byte("ABCE"), []byte("SFCS"), []byte("ADEE")}; fmt.Println(exist(b, "ABCCED")) }
''',
"R":'''
exist <- function(board, word){
  R <- length(board); C <- length(board[[1]])
  dfs <- function(r,c,i){
    if (i > nchar(word)) return(TRUE)
    if (r<1||r>R||c<1||c>C||board[[r]][c] != substr(word,i,i)) return(FALSE)
    t <- board[[r]][c]; board[[r]][c] <<- "#"
    ok <- dfs(r+1,c,i+1)||dfs(r-1,c,i+1)||dfs(r,c+1,i+1)||dfs(r,c-1,i+1)
    board[[r]][c] <<- t; ok
  }
  for (r in 1:R) for (c in 1:C) if (dfs(r,c,1)) return(TRUE)
  FALSE
}
b <- list(c("A","B","C","E"), c("S","F","C","S"), c("A","D","E","E"))
print(exist(b, "ABCCED"))
''',
}))

# ---- 100 Palindrome Partitioning ----
LESSONS.append((100, "Palindrome Partitioning", "Backtracking", "Medium", 50,
"""Partition string s such that every substring is a palindrome. Return all possible partitions.""",
{
"Python":'''
class Solution:
    def partition(self, s):
        res=[]; cur=[]
        def isPal(x): return x==x[::-1]
        def bt(i):
            if i==len(s): res.append(cur[:]); return
            for j in range(i+1, len(s)+1):
                if isPal(s[i:j]):
                    cur.append(s[i:j]); bt(j); cur.pop()
        bt(0); return res

if __name__ == "__main__":
    print(Solution().partition("aab"))
''',
"JavaScript":'''
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
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    List<List<String>> res = new ArrayList<>();
    boolean isPal(String s){ for (int i=0,j=s.length()-1;i<j;i++,j--) if (s.charAt(i)!=s.charAt(j)) return false; return true; }
    void bt(String s, int i, List<String> cur){
        if (i==s.length()){ res.add(new ArrayList<>(cur)); return; }
        for (int j=i+1;j<=s.length();j++){
            String sub = s.substring(i,j);
            if (isPal(sub)){ cur.add(sub); bt(s,j,cur); cur.remove(cur.size()-1); }
        }
    }
    public List<List<String>> partition(String s){ bt(s,0,new ArrayList<>()); return res; }
    public static void main(String[] a){ System.out.println(new __CLASS__().partition("aab")); }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    vector<vector<string>> res; vector<string> cur;
    bool isPal(const string& s){ for (int i=0,j=s.size()-1;i<j;i++,j--) if (s[i]!=s[j]) return false; return true; }
    void bt(const string& s, int i){
        if (i==(int)s.size()){ res.push_back(cur); return; }
        for (int j=i+1;j<=(int)s.size();j++){
            string sub = s.substr(i, j-i);
            if (isPal(sub)){ cur.push_back(sub); bt(s, j); cur.pop_back(); }
        }
    }
    vector<vector<string>> partition(string s){ bt(s, 0); return res; }
};
int main(){ for (auto& v: Solution().partition("aab")){ cout<<"["; for (auto& x: v) cout<<x<<","; cout<<"] "; } cout<<endl; }
''',
"Go":'''
package main
import "fmt"
func partition(s string) [][]string {
    var res [][]string; cur := []string{}
    isPal := func(x string) bool { for i,j:=0,len(x)-1; i<j; i,j=i+1,j-1 { if x[i]!=x[j] { return false } }; return true }
    var bt func(int)
    bt = func(i int){
        if i == len(s) { tmp := make([]string, len(cur)); copy(tmp, cur); res = append(res, tmp); return }
        for j := i+1; j <= len(s); j++ {
            sub := s[i:j]; if isPal(sub) { cur = append(cur, sub); bt(j); cur = cur[:len(cur)-1] }
        }
    }
    bt(0); return res
}
func main(){ fmt.Println(partition("aab")) }
''',
"R":'''
partition <- function(s){
  res <- list(); cur <- c()
  isPal <- function(x){ y <- strsplit(x,"")[[1]]; all(y == rev(y)) }
  bt <- function(i){
    if (i > nchar(s)){ res[[length(res)+1]] <<- cur; return() }
    for (j in i:nchar(s)){
      sub <- substr(s, i, j); if (isPal(sub)){ cur <<- c(cur, sub); bt(j+1); cur <<- cur[-length(cur)] }
    }
  }
  bt(1); res
}
print(partition("aab"))
''',
}))

# ---- 101 Minimum Path Sum ----
LESSONS.append((101, "Minimum Path Sum", "2-D Dynamic Programming", "Medium", 51,
"""Given an m x n grid filled with non-negative numbers, find the minimum path sum from top-left to bottom-right (only moves right or down).""",
{
"Python":'''
class Solution:
    def minPathSum(self, g):
        R,C=len(g),len(g[0])
        for i in range(R):
            for j in range(C):
                if i==0 and j==0: continue
                if i==0: g[i][j]+=g[i][j-1]
                elif j==0: g[i][j]+=g[i-1][j]
                else: g[i][j]+=min(g[i-1][j], g[i][j-1])
        return g[-1][-1]

if __name__ == "__main__":
    print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
''',
"JavaScript":'''
var minPathSum = function(g){
  const R=g.length, C=g[0].length;
  for (let i=0;i<R;i++) for (let j=0;j<C;j++){
    if (i===0 && j===0) continue;
    if (i===0) g[i][j]+=g[i][j-1];
    else if (j===0) g[i][j]+=g[i-1][j];
    else g[i][j]+=Math.min(g[i-1][j], g[i][j-1]);
  }
  return g[R-1][C-1];
};
console.log(minPathSum([[1,3,1],[1,5,1],[4,2,1]]));
''',
"Java":'''
public class __CLASS__ {
    public int minPathSum(int[][] g){
        int R=g.length, C=g[0].length;
        for (int i=0;i<R;i++) for (int j=0;j<C;j++){
            if (i==0 && j==0) continue;
            if (i==0) g[i][j]+=g[i][j-1];
            else if (j==0) g[i][j]+=g[i-1][j];
            else g[i][j]+=Math.min(g[i-1][j], g[i][j-1]);
        }
        return g[R-1][C-1];
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().minPathSum(new int[][]{{1,3,1},{1,5,1},{4,2,1}}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    int minPathSum(vector<vector<int>>& g){
        int R=g.size(), C=g[0].size();
        for (int i=0;i<R;i++) for (int j=0;j<C;j++){
            if (i==0 && j==0) continue;
            if (i==0) g[i][j]+=g[i][j-1];
            else if (j==0) g[i][j]+=g[i-1][j];
            else g[i][j]+=min(g[i-1][j], g[i][j-1]);
        }
        return g[R-1][C-1];
    }
};
int main(){ vector<vector<int>> g={{1,3,1},{1,5,1},{4,2,1}}; cout<<Solution().minPathSum(g)<<endl; }
''',
"Go":'''
package main
import "fmt"
func minPathSum(g [][]int) int {
    R, C := len(g), len(g[0])
    for i := 0; i < R; i++ { for j := 0; j < C; j++ {
        if i==0 && j==0 { continue }
        if i==0 { g[i][j]+=g[i][j-1]
        } else if j==0 { g[i][j]+=g[i-1][j]
        } else { a, b := g[i-1][j], g[i][j-1]; if a<b { g[i][j]+=a } else { g[i][j]+=b } }
    }}
    return g[R-1][C-1]
}
func main(){ fmt.Println(minPathSum([][]int{{1,3,1},{1,5,1},{4,2,1}})) }
''',
"R":'''
minPathSum <- function(g){
  R <- nrow(g); C <- ncol(g)
  for (i in 1:R) for (j in 1:C){
    if (i==1 && j==1) next
    if (i==1) g[i,j] <- g[i,j] + g[i,j-1]
    else if (j==1) g[i,j] <- g[i,j] + g[i-1,j]
    else g[i,j] <- g[i,j] + min(g[i-1,j], g[i,j-1])
  }
  g[R,C]
}
print(minPathSum(matrix(c(1,3,1,1,5,1,4,2,1), 3, 3, byrow=TRUE)))
''',
}))

# ---- 102 Longest Common Subsequence ----
LESSONS.append((102, "Longest Common Subsequence", "2-D Dynamic Programming", "Medium", 51,
"""Given two strings text1 and text2, return the length of their longest common subsequence.""",
{
"Python":'''
class Solution:
    def longestCommonSubsequence(self, a, b):
        m,n=len(a),len(b)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if a[i]==b[j]: dp[i+1][j+1]=dp[i][j]+1
                else: dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j])
        return dp[m][n]

if __name__ == "__main__":
    print(Solution().longestCommonSubsequence("abcde","ace"))
''',
"JavaScript":'''
var longestCommonSubsequence = function(a, b){
  const m=a.length, n=b.length;
  const dp=Array.from({length:m+1},()=>Array(n+1).fill(0));
  for (let i=0;i<m;i++) for (let j=0;j<n;j++){
    if (a[i]===b[j]) dp[i+1][j+1]=dp[i][j]+1;
    else dp[i+1][j+1]=Math.max(dp[i][j+1], dp[i+1][j]);
  }
  return dp[m][n];
};
console.log(longestCommonSubsequence("abcde","ace"));
''',
"Java":'''
public class __CLASS__ {
    public int longestCommonSubsequence(String a, String b){
        int m=a.length(), n=b.length();
        int[][] dp=new int[m+1][n+1];
        for (int i=0;i<m;i++) for (int j=0;j<n;j++){
            if (a.charAt(i)==b.charAt(j)) dp[i+1][j+1]=dp[i][j]+1;
            else dp[i+1][j+1]=Math.max(dp[i][j+1], dp[i+1][j]);
        }
        return dp[m][n];
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().longestCommonSubsequence("abcde","ace"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    int longestCommonSubsequence(string a, string b){
        int m=a.size(), n=b.size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        for (int i=0;i<m;i++) for (int j=0;j<n;j++){
            if (a[i]==b[j]) dp[i+1][j+1]=dp[i][j]+1;
            else dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j]);
        }
        return dp[m][n];
    }
};
int main(){ cout<<Solution().longestCommonSubsequence("abcde","ace")<<endl; }
''',
"Go":'''
package main
import "fmt"
func longestCommonSubsequence(a, b string) int {
    m, n := len(a), len(b)
    dp := make([][]int, m+1); for i := range dp { dp[i] = make([]int, n+1) }
    for i := 0; i < m; i++ { for j := 0; j < n; j++ {
        if a[i]==b[j] { dp[i+1][j+1] = dp[i][j]+1
        } else { x, y := dp[i][j+1], dp[i+1][j]; if x>y { dp[i+1][j+1]=x } else { dp[i+1][j+1]=y } }
    }}
    return dp[m][n]
}
func main(){ fmt.Println(longestCommonSubsequence("abcde","ace")) }
''',
"R":'''
longestCommonSubsequence <- function(a, b){
  m <- nchar(a); n <- nchar(b); dp <- matrix(0, m+1, n+1)
  ca <- strsplit(a,"")[[1]]; cb <- strsplit(b,"")[[1]]
  for (i in 1:m) for (j in 1:n){
    if (ca[i]==cb[j]) dp[i+1, j+1] <- dp[i,j] + 1
    else dp[i+1, j+1] <- max(dp[i, j+1], dp[i+1, j])
  }
  dp[m+1, n+1]
}
print(longestCommonSubsequence("abcde","ace"))
''',
}))

# ---- 103 Merge Intervals ----
LESSONS.append((103, "Merge Intervals", "Intervals", "Medium", 52,
"""Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals.""",
{
"Python":'''
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0]); res=[]
        for s,e in intervals:
            if res and s <= res[-1][1]: res[-1][1]=max(res[-1][1], e)
            else: res.append([s,e])
        return res

if __name__ == "__main__":
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
''',
"JavaScript":'''
var merge = function(intervals){
  intervals.sort((a,b)=>a[0]-b[0]);
  const res=[];
  for (const [s,e] of intervals){
    if (res.length && s<=res[res.length-1][1]) res[res.length-1][1]=Math.max(res[res.length-1][1], e);
    else res.push([s,e]);
  }
  return res;
};
console.log(JSON.stringify(merge([[1,3],[2,6],[8,10],[15,18]])));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int[][] merge(int[][] intervals){
        Arrays.sort(intervals, (a,b)->a[0]-b[0]);
        List<int[]> res = new ArrayList<>();
        for (int[] x: intervals){
            if (!res.isEmpty() && x[0] <= res.get(res.size()-1)[1])
                res.get(res.size()-1)[1] = Math.max(res.get(res.size()-1)[1], x[1]);
            else res.add(new int[]{x[0], x[1]});
        }
        return res.toArray(new int[0][]);
    }
    public static void main(String[] a){
        int[][] r = new __CLASS__().merge(new int[][]{{1,3},{2,6},{8,10},{15,18}});
        System.out.println(Arrays.deepToString(r));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    vector<vector<int>> merge(vector<vector<int>>& intervals){
        sort(intervals.begin(), intervals.end()); vector<vector<int>> res;
        for (auto& x: intervals){
            if (!res.empty() && x[0]<=res.back()[1]) res.back()[1]=max(res.back()[1], x[1]);
            else res.push_back(x);
        }
        return res;
    }
};
int main(){ vector<vector<int>> v={{1,3},{2,6},{8,10},{15,18}};
    for (auto& r: Solution().merge(v)){ cout<<"["<<r[0]<<","<<r[1]<<"] "; } cout<<endl; }
''',
"Go":'''
package main
import ( "fmt"; "sort" )
func merge(intervals [][]int) [][]int {
    sort.Slice(intervals, func(i,j int) bool { return intervals[i][0] < intervals[j][0] })
    res := [][]int{}
    for _, x := range intervals {
        if n := len(res); n > 0 && x[0] <= res[n-1][1] { if x[1] > res[n-1][1] { res[n-1][1] = x[1] }
        } else { res = append(res, []int{x[0], x[1]}) }
    }
    return res
}
func main(){ fmt.Println(merge([][]int{{1,3},{2,6},{8,10},{15,18}})) }
''',
"R":'''
mergeIntervals <- function(intervals){
  intervals <- intervals[order(sapply(intervals, function(x) x[1]))]
  res <- list()
  for (x in intervals){
    n <- length(res)
    if (n > 0 && x[1] <= res[[n]][2]) res[[n]][2] <- max(res[[n]][2], x[2])
    else res[[length(res)+1]] <- x
  }
  res
}
print(mergeIntervals(list(c(1,3),c(2,6),c(8,10),c(15,18))))
''',
}))

# ---- 104 Non Overlapping Intervals ----
LESSONS.append((104, "Non Overlapping Intervals", "Intervals", "Medium", 52,
"""Given an array of intervals, return the minimum number of intervals to remove so the rest are non-overlapping.""",
{
"Python":'''
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1]); end=float('-inf'); rm=0
        for s,e in intervals:
            if s>=end: end=e
            else: rm+=1
        return rm

if __name__ == "__main__":
    print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
''',
"JavaScript":'''
var eraseOverlapIntervals = function(intervals){
  intervals.sort((a,b)=>a[1]-b[1]); let end=-Infinity, rm=0;
  for (const [s,e] of intervals){ if (s>=end) end=e; else rm++; }
  return rm;
};
console.log(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int eraseOverlapIntervals(int[][] intervals){
        Arrays.sort(intervals, (a,b)->a[1]-b[1]);
        int end = Integer.MIN_VALUE, rm = 0;
        for (int[] x: intervals){ if (x[0]>=end) end=x[1]; else rm++; }
        return rm;
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().eraseOverlapIntervals(new int[][]{{1,2},{2,3},{3,4},{1,3}}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals){
        sort(intervals.begin(), intervals.end(), [](auto&a, auto&b){return a[1]<b[1];});
        int end=INT_MIN, rm=0;
        for (auto& x: intervals){ if (x[0]>=end) end=x[1]; else rm++; }
        return rm;
    }
};
int main(){ vector<vector<int>> v={{1,2},{2,3},{3,4},{1,3}}; cout<<Solution().eraseOverlapIntervals(v)<<endl; }
''',
"Go":'''
package main
import ( "fmt"; "math"; "sort" )
func eraseOverlapIntervals(intervals [][]int) int {
    sort.Slice(intervals, func(i,j int) bool { return intervals[i][1] < intervals[j][1] })
    end, rm := math.MinInt32, 0
    for _, x := range intervals { if x[0] >= end { end = x[1] } else { rm++ } }
    return rm
}
func main(){ fmt.Println(eraseOverlapIntervals([][]int{{1,2},{2,3},{3,4},{1,3}})) }
''',
"R":'''
eraseOverlapIntervals <- function(intervals){
  intervals <- intervals[order(sapply(intervals, function(x) x[2]))]
  end <- -Inf; rm <- 0
  for (x in intervals){ if (x[1] >= end) end <- x[2] else rm <- rm + 1 }
  rm
}
print(eraseOverlapIntervals(list(c(1,2),c(2,3),c(3,4),c(1,3))))
''',
}))

# ---- 105 Merge Strings Alternately ----
LESSONS.append((105, "Merge Strings Alternately", "Two Pointers", "Easy", 53,
"""Given two strings, merge them by adding letters in alternating order, starting with word1. If one is longer, append the rest.""",
{
"Python":'''
class Solution:
    def mergeAlternately(self, a, b):
        res=[]; i=0
        while i<len(a) or i<len(b):
            if i<len(a): res.append(a[i])
            if i<len(b): res.append(b[i])
            i+=1
        return "".join(res)

if __name__ == "__main__":
    print(Solution().mergeAlternately("abc","pqr"))
    print(Solution().mergeAlternately("ab","pqrs"))
''',
"JavaScript":'''
var mergeAlternately = function(a, b){
  let res=""; let i=0;
  while (i<a.length || i<b.length){ if (i<a.length) res+=a[i]; if (i<b.length) res+=b[i]; i++; }
  return res;
};
console.log(mergeAlternately("abc","pqr"), mergeAlternately("ab","pqrs"));
''',
"Java":'''
public class __CLASS__ {
    public String mergeAlternately(String a, String b){
        StringBuilder sb = new StringBuilder(); int i=0;
        while (i<a.length() || i<b.length()){
            if (i<a.length()) sb.append(a.charAt(i));
            if (i<b.length()) sb.append(b.charAt(i));
            i++;
        }
        return sb.toString();
    }
    public static void main(String[] a){
        __CLASS__ x = new __CLASS__();
        System.out.println(x.mergeAlternately("abc","pqr"));
        System.out.println(x.mergeAlternately("ab","pqrs"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    string mergeAlternately(string a, string b){
        string r; int i=0;
        while (i<(int)a.size() || i<(int)b.size()){
            if (i<(int)a.size()) r+=a[i];
            if (i<(int)b.size()) r+=b[i];
            i++;
        }
        return r;
    }
};
int main(){ Solution s; cout<<s.mergeAlternately("abc","pqr")<<" "<<s.mergeAlternately("ab","pqrs")<<endl; }
''',
"Go":'''
package main
import "fmt"
func mergeAlternately(a, b string) string {
    r := []byte{}; i := 0
    for i < len(a) || i < len(b) {
        if i < len(a) { r = append(r, a[i]) }
        if i < len(b) { r = append(r, b[i]) }
        i++
    }
    return string(r)
}
func main(){ fmt.Println(mergeAlternately("abc","pqr"), mergeAlternately("ab","pqrs")) }
''',
"R":'''
mergeAlternately <- function(a, b){
  ca <- strsplit(a,"")[[1]]; cb <- strsplit(b,"")[[1]]
  n <- max(length(ca), length(cb)); r <- c()
  for (i in 1:n){
    if (i <= length(ca)) r <- c(r, ca[i])
    if (i <= length(cb)) r <- c(r, cb[i])
  }
  paste(r, collapse="")
}
print(mergeAlternately("abc","pqr")); print(mergeAlternately("ab","pqrs"))
''',
}))

# ---- 106 Rotate Array ----
LESSONS.append((106, "Rotate Array", "Two Pointers", "Medium", 53,
"""Rotate the array to the right by k steps in-place.""",
{
"Python":'''
class Solution:
    def rotate(self, nums, k):
        n=len(nums); k%=n
        nums[:] = nums[-k:] + nums[:-k]

if __name__ == "__main__":
    a=[1,2,3,4,5,6,7]; Solution().rotate(a,3); print(a)
''',
"JavaScript":'''
var rotate = function(nums, k){
  const n=nums.length; k = k % n;
  const rev = (l, r)=>{ while(l<r){ [nums[l], nums[r]]=[nums[r], nums[l]]; l++; r--; } };
  rev(0, n-1); rev(0, k-1); rev(k, n-1);
};
const a=[1,2,3,4,5,6,7]; rotate(a, 3); console.log(JSON.stringify(a));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public void rotate(int[] nums, int k){
        int n=nums.length; k%=n;
        rev(nums, 0, n-1); rev(nums, 0, k-1); rev(nums, k, n-1);
    }
    void rev(int[] a, int l, int r){ while (l<r){ int t=a[l]; a[l]=a[r]; a[r]=t; l++; r--; } }
    public static void main(String[] a){
        int[] x={1,2,3,4,5,6,7}; new __CLASS__().rotate(x, 3); System.out.println(Arrays.toString(x));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    void rotate(vector<int>& nums, int k){
        int n=nums.size(); k%=n;
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin()+k);
        reverse(nums.begin()+k, nums.end());
    }
};
int main(){ vector<int> a={1,2,3,4,5,6,7}; Solution().rotate(a, 3);
    for (int x: a) cout<<x<<" "; cout<<endl; }
''',
"Go":'''
package main
import "fmt"
func rotate(nums []int, k int) {
    n := len(nums); k %= n
    rev := func(l, r int){ for l<r { nums[l], nums[r] = nums[r], nums[l]; l++; r-- } }
    rev(0, n-1); rev(0, k-1); rev(k, n-1)
}
func main(){ a := []int{1,2,3,4,5,6,7}; rotate(a, 3); fmt.Println(a) }
''',
"R":'''
rotateArr <- function(nums, k){
  n <- length(nums); k <- k %% n
  c(nums[(n-k+1):n], nums[1:(n-k)])
}
print(rotateArr(c(1,2,3,4,5,6,7), 3))
''',
}))

# ---- 107 Implement Queue using Stacks ----
LESSONS.append((107, "Implement Queue using Stacks", "Stack", "Easy", 54,
"""Implement a FIFO queue using only two stacks.""",
{
"Python":'''
class MyQueue:
    def __init__(self): self.a=[]; self.b=[]
    def push(self, x): self.a.append(x)
    def pop(self):
        if not self.b:
            while self.a: self.b.append(self.a.pop())
        return self.b.pop()
    def peek(self):
        if not self.b:
            while self.a: self.b.append(self.a.pop())
        return self.b[-1]
    def empty(self): return not self.a and not self.b

if __name__ == "__main__":
    q=MyQueue(); q.push(1); q.push(2); print(q.peek()); print(q.pop()); print(q.empty())
''',
"JavaScript":'''
class MyQueue {
  constructor(){ this.a=[]; this.b=[]; }
  push(x){ this.a.push(x); }
  pop(){ if (!this.b.length) while (this.a.length) this.b.push(this.a.pop()); return this.b.pop(); }
  peek(){ if (!this.b.length) while (this.a.length) this.b.push(this.a.pop()); return this.b[this.b.length-1]; }
  empty(){ return !this.a.length && !this.b.length; }
}
const q=new MyQueue(); q.push(1); q.push(2); console.log(q.peek(), q.pop(), q.empty());
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    Deque<Integer> a = new ArrayDeque<>(), b = new ArrayDeque<>();
    public void push(int x){ a.push(x); }
    public int pop(){ peek(); return b.pop(); }
    public int peek(){ if (b.isEmpty()) while (!a.isEmpty()) b.push(a.pop()); return b.peek(); }
    public boolean empty(){ return a.isEmpty() && b.isEmpty(); }
    public static void main(String[] a){
        __CLASS__ q = new __CLASS__(); q.push(1); q.push(2);
        System.out.println(q.peek()); System.out.println(q.pop()); System.out.println(q.empty());
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class MyQueue {
    stack<int> a, b;
public:
    void push(int x){ a.push(x); }
    int pop(){ peek(); int t=b.top(); b.pop(); return t; }
    int peek(){ if (b.empty()) while (!a.empty()){ b.push(a.top()); a.pop(); } return b.top(); }
    bool empty(){ return a.empty() && b.empty(); }
};
int main(){ MyQueue q; q.push(1); q.push(2);
    cout<<q.peek()<<" "<<q.pop()<<" "<<q.empty()<<endl; }
''',
"Go":'''
package main
import "fmt"
type MyQueue struct { a, b []int }
func (q *MyQueue) Push(x int){ q.a = append(q.a, x) }
func (q *MyQueue) Pop() int { q.Peek(); n := len(q.b); x := q.b[n-1]; q.b = q.b[:n-1]; return x }
func (q *MyQueue) Peek() int {
    if len(q.b)==0 { for len(q.a)>0 { n:=len(q.a); q.b=append(q.b, q.a[n-1]); q.a=q.a[:n-1] } }
    return q.b[len(q.b)-1]
}
func (q *MyQueue) Empty() bool { return len(q.a)==0 && len(q.b)==0 }
func main(){ q := &MyQueue{}; q.Push(1); q.Push(2);
    fmt.Println(q.Peek(), q.Pop(), q.Empty()) }
''',
"R":'''
MyQueue <- function(){
  a <- c(); b <- c()
  push <- function(x) a <<- c(a, x)
  shift <- function(){ if (length(b)==0){ b <<- rev(a); a <<- c() } }
  pop <- function(){ shift(); x <- b[length(b)]; b <<- b[-length(b)]; x }
  peek <- function(){ shift(); b[length(b)] }
  empty <- function() length(a)==0 && length(b)==0
  list(push=push, pop=pop, peek=peek, empty=empty)
}
q <- MyQueue(); q$push(1); q$push(2); print(q$peek()); print(q$pop()); print(q$empty())
''',
}))

# ---- 108 Evaluate Reverse Polish Notation ----
LESSONS.append((108, "Evaluate Reverse Polish Notation", "Stack", "Medium", 54,
"""Evaluate an arithmetic expression in Reverse Polish Notation. Operators: +, -, *, /. Division truncates toward zero.""",
{
"Python":'''
class Solution:
    def evalRPN(self, tokens):
        st=[]
        for t in tokens:
            if t in "+-*/":
                b=st.pop(); a=st.pop()
                if t=='+': st.append(a+b)
                elif t=='-': st.append(a-b)
                elif t=='*': st.append(a*b)
                else: st.append(int(a/b))
            else: st.append(int(t))
        return st[0]

if __name__ == "__main__":
    print(Solution().evalRPN(["2","1","+","3","*"]))
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
''',
"JavaScript":'''
var evalRPN = function(tokens){
  const st=[];
  for (const t of tokens){
    if ("+-*/".includes(t) && t.length===1){
      const b=st.pop(), a=st.pop();
      if (t==='+') st.push(a+b);
      else if (t==='-') st.push(a-b);
      else if (t==='*') st.push(a*b);
      else st.push(a/b<0 ? Math.ceil(a/b) : Math.floor(a/b));
    } else st.push(parseInt(t,10));
  }
  return st[0];
};
console.log(evalRPN(["2","1","+","3","*"]), evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int evalRPN(String[] tokens){
        Deque<Integer> st = new ArrayDeque<>();
        for (String t: tokens){
            if (t.length()==1 && "+-*/".indexOf(t.charAt(0))>=0){
                int b=st.pop(), a=st.pop();
                switch (t.charAt(0)){
                    case '+': st.push(a+b); break;
                    case '-': st.push(a-b); break;
                    case '*': st.push(a*b); break;
                    default: st.push(a/b);
                }
            } else st.push(Integer.parseInt(t));
        }
        return st.peek();
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().evalRPN(new String[]{"2","1","+","3","*"}));
        System.out.println(new __CLASS__().evalRPN(new String[]{"10","6","9","3","+","-11","*","/","*","17","+","5","+"}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    int evalRPN(vector<string>& tokens){
        stack<long long> st;
        for (auto& t: tokens){
            if (t.size()==1 && string("+-*/").find(t[0])!=string::npos){
                long long b=st.top(); st.pop(); long long a=st.top(); st.pop();
                if (t=="+") st.push(a+b);
                else if (t=="-") st.push(a-b);
                else if (t=="*") st.push(a*b);
                else st.push(a/b);
            } else st.push(stoll(t));
        }
        return (int)st.top();
    }
};
int main(){ vector<string> a={"2","1","+","3","*"}, b={"10","6","9","3","+","-11","*","/","*","17","+","5","+"};
    cout<<Solution().evalRPN(a)<<" "<<Solution().evalRPN(b)<<endl; }
''',
"Go":'''
package main
import ( "fmt"; "strconv" )
func evalRPN(tokens []string) int {
    st := []int{}
    for _, t := range tokens {
        if len(t)==1 && (t=="+"||t=="-"||t=="*"||t=="/") {
            n := len(st); b, a := st[n-1], st[n-2]; st = st[:n-2]
            switch t { case "+": st = append(st, a+b); case "-": st = append(st, a-b); case "*": st = append(st, a*b); case "/": st = append(st, a/b) }
        } else { v, _ := strconv.Atoi(t); st = append(st, v) }
    }
    return st[0]
}
func main(){ fmt.Println(evalRPN([]string{"2","1","+","3","*"}), evalRPN([]string{"10","6","9","3","+","-11","*","/","*","17","+","5","+"})) }
''',
"R":'''
evalRPN <- function(tokens){
  st <- c()
  for (t in tokens){
    if (t %in% c("+","-","*","/")){
      b <- st[length(st)]; st <- st[-length(st)]
      a <- st[length(st)]; st <- st[-length(st)]
      v <- switch(t, "+"=a+b, "-"=a-b, "*"=a*b, "/"=trunc(a/b))
      st <- c(st, v)
    } else st <- c(st, as.integer(t))
  }
  st[1]
}
print(evalRPN(c("2","1","+","3","*")))
print(evalRPN(c("10","6","9","3","+","-11","*","/","*","17","+","5","+")))
''',
}))

# ---- 109 Best Time to Buy And Sell Stock ----
LESSONS.append((109, "Best Time to Buy And Sell Stock", "Sliding Window", "Easy", 55,
"""Given an array of stock prices where prices[i] is on day i, return the maximum profit from a single buy/sell. Return 0 if none.""",
{
"Python":'''
class Solution:
    def maxProfit(self, prices):
        lo=float('inf'); best=0
        for p in prices:
            lo=min(lo,p); best=max(best, p-lo)
        return best

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
''',
"JavaScript":'''
var maxProfit = function(prices){
  let lo=Infinity, best=0;
  for (const p of prices){ lo=Math.min(lo,p); best=Math.max(best, p-lo); }
  return best;
};
console.log(maxProfit([7,1,5,3,6,4]));
''',
"Java":'''
public class __CLASS__ {
    public int maxProfit(int[] prices){
        int lo=Integer.MAX_VALUE, best=0;
        for (int p: prices){ lo=Math.min(lo,p); best=Math.max(best, p-lo); }
        return best;
    }
    public static void main(String[] a){ System.out.println(new __CLASS__().maxProfit(new int[]{7,1,5,3,6,4})); }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    int maxProfit(vector<int>& prices){
        int lo=INT_MAX, best=0;
        for (int p: prices){ lo=min(lo,p); best=max(best, p-lo); }
        return best;
    }
};
int main(){ vector<int> p={7,1,5,3,6,4}; cout<<Solution().maxProfit(p)<<endl; }
''',
"Go":'''
package main
import ( "fmt"; "math" )
func maxProfit(prices []int) int {
    lo, best := math.MaxInt32, 0
    for _, p := range prices { if p<lo{lo=p}; if p-lo>best{best=p-lo} }
    return best
}
func main(){ fmt.Println(maxProfit([]int{7,1,5,3,6,4})) }
''',
"R":'''
maxProfit <- function(prices){
  lo <- Inf; best <- 0
  for (p in prices){ lo <- min(lo, p); best <- max(best, p - lo) }
  best
}
print(maxProfit(c(7,1,5,3,6,4)))
''',
}))

# ---- 110 Longest Repeating Character Replacement ----
LESSONS.append((110, "Longest Repeating Character Replacement", "Sliding Window", "Medium", 55,
"""Given a string s and integer k, you may change up to k characters. Return length of longest substring with all same characters.""",
{
"Python":'''
class Solution:
    def characterReplacement(self, s, k):
        cnt={}; l=0; mx=0; best=0
        for r,c in enumerate(s):
            cnt[c]=cnt.get(c,0)+1; mx=max(mx, cnt[c])
            if r-l+1 - mx > k:
                cnt[s[l]] -= 1; l += 1
            best=max(best, r-l+1)
        return best

if __name__ == "__main__":
    print(Solution().characterReplacement("ABAB", 2))
    print(Solution().characterReplacement("AABABBA", 1))
''',
"JavaScript":'''
var characterReplacement = function(s, k){
  const cnt={}; let l=0, mx=0, best=0;
  for (let r=0;r<s.length;r++){
    const c=s[r]; cnt[c]=(cnt[c]||0)+1; mx=Math.max(mx, cnt[c]);
    if (r-l+1 - mx > k){ cnt[s[l]]--; l++; }
    best = Math.max(best, r-l+1);
  }
  return best;
};
console.log(characterReplacement("ABAB", 2), characterReplacement("AABABBA", 1));
''',
"Java":'''
public class __CLASS__ {
    public int characterReplacement(String s, int k){
        int[] cnt = new int[26]; int l=0, mx=0, best=0;
        for (int r=0;r<s.length();r++){
            cnt[s.charAt(r)-'A']++; mx = Math.max(mx, cnt[s.charAt(r)-'A']);
            if (r-l+1 - mx > k){ cnt[s.charAt(l)-'A']--; l++; }
            best = Math.max(best, r-l+1);
        }
        return best;
    }
    public static void main(String[] a){
        __CLASS__ x = new __CLASS__();
        System.out.println(x.characterReplacement("ABAB", 2));
        System.out.println(x.characterReplacement("AABABBA", 1));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution { public:
    int characterReplacement(string s, int k){
        int cnt[26]={0}; int l=0, mx=0, best=0;
        for (int r=0;r<(int)s.size();r++){
            cnt[s[r]-'A']++; mx=max(mx, cnt[s[r]-'A']);
            if (r-l+1 - mx > k){ cnt[s[l]-'A']--; l++; }
            best=max(best, r-l+1);
        }
        return best;
    }
};
int main(){ Solution s; cout<<s.characterReplacement("ABAB",2)<<" "<<s.characterReplacement("AABABBA",1)<<endl; }
''',
"Go":'''
package main
import "fmt"
func characterReplacement(s string, k int) int {
    cnt := [26]int{}; l, mx, best := 0, 0, 0
    for r := 0; r < len(s); r++ {
        cnt[s[r]-'A']++; if cnt[s[r]-'A']>mx { mx = cnt[s[r]-'A'] }
        if r-l+1 - mx > k { cnt[s[l]-'A']--; l++ }
        if r-l+1 > best { best = r-l+1 }
    }
    return best
}
func main(){ fmt.Println(characterReplacement("ABAB",2), characterReplacement("AABABBA",1)) }
''',
"R":'''
characterReplacement <- function(s, k){
  chars <- strsplit(s,"")[[1]]; cnt <- list(); l <- 1; mx <- 0; best <- 0
  for (r in seq_along(chars)){
    c <- chars[r]; cnt[[c]] <- ifelse(is.null(cnt[[c]]), 1, cnt[[c]] + 1)
    if (cnt[[c]] > mx) mx <- cnt[[c]]
    while (r - l + 1 - mx > k){
      cl <- chars[l]; cnt[[cl]] <- cnt[[cl]] - 1; l <- l + 1
    }
    if (r - l + 1 > best) best <- r - l + 1
  }
  best
}
print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))
''',
}))

write_lessons(LESSONS)
