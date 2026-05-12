"""Batch 9: lessons 186-210."""
from _lesson_writer import write_lessons

L = []

# 186 Gas Station
L.append((186, "Gas Station", "Greedy", "Medium", 93,
"Gas[i]/cost[i] arrays around a circular route. Return start index to complete the circuit (or -1).",
{
"Python": '''def canCompleteCircuit(g,c):
    if sum(g)<sum(c): return -1
    tank=0; start=0
    for i in range(len(g)):
        tank+=g[i]-c[i]
        if tank<0: start=i+1; tank=0
    return start

if __name__=="__main__":
    print(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
    print(canCompleteCircuit([2,3,4],[3,4,3]))
''',
"JavaScript": '''function canCompleteCircuit(g,c){let s=0,t=0,tot=0;for(let i=0;i<g.length;i++){const d=g[i]-c[i];t+=d;tot+=d;if(t<0){s=i+1;t=0;}}return tot<0?-1:s;}
console.log(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]));console.log(canCompleteCircuit([2,3,4],[3,4,3]));
''',
"Java": '''public class __CLASS__{
  static int canCompleteCircuit(int[] g,int[] c){int s=0,t=0,tot=0;for(int i=0;i<g.length;i++){int d=g[i]-c[i];t+=d;tot+=d;if(t<0){s=i+1;t=0;}}return tot<0?-1:s;}
  public static void main(String[]a){System.out.println(canCompleteCircuit(new int[]{1,2,3,4,5},new int[]{3,4,5,1,2}));System.out.println(canCompleteCircuit(new int[]{2,3,4},new int[]{3,4,3}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int canCompleteCircuit(vector<int> g,vector<int> c){int s=0,t=0,tot=0;for(int i=0;i<(int)g.size();i++){int d=g[i]-c[i];t+=d;tot+=d;if(t<0){s=i+1;t=0;}}return tot<0?-1:s;}
int main(){cout<<canCompleteCircuit({1,2,3,4,5},{3,4,5,1,2})<<"\\n"<<canCompleteCircuit({2,3,4},{3,4,3})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func canCompleteCircuit(g,c []int) int { s,t,tot:=0,0,0; for i:=0;i<len(g);i++ { d:=g[i]-c[i]; t+=d; tot+=d; if t<0 { s=i+1; t=0 } }; if tot<0 { return -1 }; return s }
func main(){ fmt.Println(canCompleteCircuit([]int{1,2,3,4,5},[]int{3,4,5,1,2})); fmt.Println(canCompleteCircuit([]int{2,3,4},[]int{3,4,3})) }
''',
"R": '''canCompleteCircuit <- function(g,c){ s<-0; t<-0; tot<-0; for(i in seq_along(g)){ d<-g[i]-c[i]; t<-t+d; tot<-tot+d; if(t<0){ s<-i; t<-0 } }; if(tot<0) -1 else s }
cat(canCompleteCircuit(c(1,2,3,4,5),c(3,4,5,1,2)),"\\n")
''',
}))

# 187 Reverse Linked List II
L.append((187, "Reverse Linked List II", "Linked List", "Medium", 94,
"Reverse the nodes of the list from position left to right (1-indexed).",
{
"Python": '''class N:
    def __init__(s,v,n=None): s.v=v; s.n=n
def reverseBetween(h,L,R):
    d=N(0,h); pre=d
    for _ in range(L-1): pre=pre.n
    cur=pre.n
    for _ in range(R-L):
        nxt=cur.n; cur.n=nxt.n; nxt.n=pre.n; pre.n=nxt
    return d.n
def to_list(h):
    r=[]
    while h: r.append(h.v); h=h.n
    return r
def from_list(a):
    d=N(0); c=d
    for x in a: c.n=N(x); c=c.n
    return d.n

if __name__=="__main__":
    print(to_list(reverseBetween(from_list([1,2,3,4,5]),2,4)))
''',
"JavaScript": '''class N{constructor(v,n=null){this.v=v;this.n=n;}}
function reverseBetween(h,L,R){const d=new N(0,h);let pre=d;for(let i=0;i<L-1;i++)pre=pre.n;let cur=pre.n;for(let i=0;i<R-L;i++){const nxt=cur.n;cur.n=nxt.n;nxt.n=pre.n;pre.n=nxt;}return d.n;}
function fromList(a){const d=new N(0);let c=d;for(const x of a){c.n=new N(x);c=c.n;}return d.n;}
function toList(h){const r=[];while(h){r.push(h.v);h=h.n;}return r;}
console.log(toList(reverseBetween(fromList([1,2,3,4,5]),2,4)));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class N{int v;N n;N(int v){this.v=v;}}
  static N reverseBetween(N h,int L,int R){N d=new N(0);d.n=h;N pre=d;for(int i=0;i<L-1;i++)pre=pre.n;N cur=pre.n;for(int i=0;i<R-L;i++){N nxt=cur.n;cur.n=nxt.n;nxt.n=pre.n;pre.n=nxt;}return d.n;}
  public static void main(String[]a){N h=new N(1);N c=h;for(int v:new int[]{2,3,4,5}){c.n=new N(v);c=c.n;}N r=reverseBetween(h,2,4);List<Integer> out=new ArrayList<>();while(r!=null){out.add(r.v);r=r.n;}System.out.println(out);}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct N{int v;N* n=0;N(int v):v(v){}};
N* reverseBetween(N* h,int L,int R){N d(0);d.n=h;N* pre=&d;for(int i=0;i<L-1;i++)pre=pre->n;N* cur=pre->n;for(int i=0;i<R-L;i++){N* nxt=cur->n;cur->n=nxt->n;nxt->n=pre->n;pre->n=nxt;}return d.n;}
int main(){N* h=new N(1);N* c=h;for(int v:{2,3,4,5}){c->n=new N(v);c=c->n;}N* r=reverseBetween(h,2,4);while(r){cout<<r->v<<" ";r=r->n;}cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
type N struct{ V int; Nx *N }
func reverseBetween(h *N,L,R int) *N { d:=&N{}; d.Nx=h; pre:=d; for i:=0;i<L-1;i++ { pre=pre.Nx }; cur:=pre.Nx; for i:=0;i<R-L;i++ { nxt:=cur.Nx; cur.Nx=nxt.Nx; nxt.Nx=pre.Nx; pre.Nx=nxt }; return d.Nx }
func main(){ h:=&N{V:1}; c:=h; for _,v:=range []int{2,3,4,5} { c.Nx=&N{V:v}; c=c.Nx }; r:=reverseBetween(h,2,4); for r!=nil { fmt.Print(r.V," "); r=r.Nx }; fmt.Println() }
''',
"R": '''reverseBetween <- function(a,L,R){ x<-a[L:R]; a[L:R]<-rev(x); a }
cat(reverseBetween(c(1,2,3,4,5),2,4),"\\n")
''',
}))

# 188 Design Circular Queue
L.append((188, "Design Circular Queue", "Linked List", "Medium", 94,
"Implement a fixed-size circular queue with enQueue/deQueue/Front/Rear/isEmpty/isFull.",
{
"Python": '''class CQ:
    def __init__(s,k): s.a=[0]*k; s.k=k; s.head=0; s.cnt=0
    def enQueue(s,v):
        if s.cnt==s.k: return False
        s.a[(s.head+s.cnt)%s.k]=v; s.cnt+=1; return True
    def deQueue(s):
        if s.cnt==0: return False
        s.head=(s.head+1)%s.k; s.cnt-=1; return True
    def Front(s): return -1 if s.cnt==0 else s.a[s.head]
    def Rear(s): return -1 if s.cnt==0 else s.a[(s.head+s.cnt-1)%s.k]
    def isEmpty(s): return s.cnt==0
    def isFull(s): return s.cnt==s.k

if __name__=="__main__":
    q=CQ(3); print(q.enQueue(1),q.enQueue(2),q.enQueue(3),q.enQueue(4))
    print(q.Rear(),q.isFull(),q.deQueue(),q.enQueue(4),q.Rear())
''',
"JavaScript": '''class CQ{constructor(k){this.a=new Array(k);this.k=k;this.h=0;this.c=0;}enQueue(v){if(this.c===this.k)return false;this.a[(this.h+this.c)%this.k]=v;this.c++;return true;}deQueue(){if(!this.c)return false;this.h=(this.h+1)%this.k;this.c--;return true;}Front(){return this.c?this.a[this.h]:-1;}Rear(){return this.c?this.a[(this.h+this.c-1)%this.k]:-1;}isEmpty(){return this.c===0;}isFull(){return this.c===this.k;}}
const q=new CQ(3);console.log(q.enQueue(1),q.enQueue(2),q.enQueue(3),q.enQueue(4));console.log(q.Rear(),q.isFull(),q.deQueue(),q.enQueue(4),q.Rear());
''',
"Java": '''public class __CLASS__{
  static class CQ{int[] a;int k,h,c;CQ(int k){a=new int[k];this.k=k;}
    boolean enQueue(int v){if(c==k)return false;a[(h+c)%k]=v;c++;return true;}
    boolean deQueue(){if(c==0)return false;h=(h+1)%k;c--;return true;}
    int Front(){return c==0?-1:a[h];}
    int Rear(){return c==0?-1:a[(h+c-1)%k];}
    boolean isEmpty(){return c==0;}
    boolean isFull(){return c==k;}}
  public static void main(String[]a){CQ q=new CQ(3);System.out.println(q.enQueue(1)+","+q.enQueue(2)+","+q.enQueue(3)+","+q.enQueue(4));System.out.println(q.Rear()+","+q.isFull()+","+q.deQueue()+","+q.enQueue(4)+","+q.Rear());}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct CQ{vector<int> a;int k,h=0,c=0;CQ(int k):a(k),k(k){}
  bool enQueue(int v){if(c==k)return false;a[(h+c)%k]=v;c++;return true;}
  bool deQueue(){if(c==0)return false;h=(h+1)%k;c--;return true;}
  int Front(){return c==0?-1:a[h];}
  int Rear(){return c==0?-1:a[(h+c-1)%k];}
  bool isEmpty(){return c==0;}
  bool isFull(){return c==k;}};
int main(){CQ q(3);cout<<q.enQueue(1)<<q.enQueue(2)<<q.enQueue(3)<<q.enQueue(4)<<"\\n";cout<<q.Rear()<<" "<<q.isFull()<<" "<<q.deQueue()<<" "<<q.enQueue(4)<<" "<<q.Rear()<<"\\n";}
''',
"Go": '''package main
import "fmt"
type CQ struct { a []int; k,h,c int }
func New(k int) *CQ { return &CQ{a:make([]int,k),k:k} }
func (q *CQ) En(v int) bool { if q.c==q.k { return false }; q.a[(q.h+q.c)%q.k]=v; q.c++; return true }
func (q *CQ) De() bool { if q.c==0 { return false }; q.h=(q.h+1)%q.k; q.c--; return true }
func (q *CQ) Front() int { if q.c==0 { return -1 }; return q.a[q.h] }
func (q *CQ) Rear() int { if q.c==0 { return -1 }; return q.a[(q.h+q.c-1)%q.k] }
func main(){ q:=New(3); fmt.Println(q.En(1),q.En(2),q.En(3),q.En(4)); fmt.Println(q.Rear(),q.De(),q.En(4),q.Rear()) }
''',
"R": '''CQ <- function(k){ a<-rep(0,k); h<-0; c<-0; list(en=function(v){ if(c>=k) return(FALSE); a[((h+c)%%k)+1]<<-v; c<<-c+1; TRUE }, de=function(){ if(c==0) return(FALSE); h<<-(h+1)%%k; c<<-c-1; TRUE }, front=function() if(c==0) -1 else a[h+1], rear=function() if(c==0) -1 else a[((h+c-1)%%k)+1]) }
q<-CQ(3); cat(q$en(1),q$en(2),q$en(3),q$en(4),"\\n"); cat(q$rear(),"\\n")
''',
}))

# 189 Delete Leaves With Given Value
L.append((189, "Delete Leaves With a Given Value", "Trees", "Medium", 95,
"Delete all leaf nodes with a given target value (cascade).",
{
"Python": '''class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def removeLeafNodes(root,t):
    if not root: return None
    root.l=removeLeafNodes(root.l,t)
    root.r=removeLeafNodes(root.r,t)
    if not root.l and not root.r and root.v==t: return None
    return root
def to_list(n):
    if not n: return None
    return [n.v,to_list(n.l),to_list(n.r)]

if __name__=="__main__":
    r=N(1,N(2,N(2)),N(3,N(2),N(4)))
    print(to_list(removeLeafNodes(r,2)))
''',
"JavaScript": '''class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function removeLeafNodes(n,t){if(!n)return null;n.l=removeLeafNodes(n.l,t);n.r=removeLeafNodes(n.r,t);if(!n.l&&!n.r&&n.v===t)return null;return n;}
function out(n){if(!n)return null;return [n.v,out(n.l),out(n.r)];}
console.log(JSON.stringify(out(removeLeafNodes(new N(1,new N(2,new N(2)),new N(3,new N(2),new N(4))),2))));
''',
"Java": '''public class __CLASS__{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static N rem(N n,int t){if(n==null)return null;n.l=rem(n.l,t);n.r=rem(n.r,t);if(n.l==null&&n.r==null&&n.v==t)return null;return n;}
  static String show(N n){if(n==null)return "null";return "["+n.v+","+show(n.l)+","+show(n.r)+"]";}
  public static void main(String[]a){N r=new N(1);r.l=new N(2);r.l.l=new N(2);r.r=new N(3);r.r.l=new N(2);r.r.r=new N(4);System.out.println(show(rem(r,2)));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct N{int v;N*l=0;N*r=0;N(int v):v(v){}};
N* rem(N* n,int t){if(!n)return 0;n->l=rem(n->l,t);n->r=rem(n->r,t);if(!n->l&&!n->r&&n->v==t)return 0;return n;}
void show(N* n){if(!n){cout<<"null";return;}cout<<"["<<n->v<<",";show(n->l);cout<<",";show(n->r);cout<<"]";}
int main(){N r(1),a(2),b(2),c(3),d(2),e(4);r.l=&a;a.l=&b;r.r=&c;c.l=&d;c.r=&e;show(rem(&r,2));cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
type N struct{ V int; L,R *N }
func rem(n *N,t int) *N { if n==nil { return nil }; n.L=rem(n.L,t); n.R=rem(n.R,t); if n.L==nil && n.R==nil && n.V==t { return nil }; return n }
func show(n *N) string { if n==nil { return "null" }; return fmt.Sprintf("[%d,%s,%s]",n.V,show(n.L),show(n.R)) }
func main(){ r:=&N{V:1,L:&N{V:2,L:&N{V:2}},R:&N{V:3,L:&N{V:2},R:&N{V:4}}}; fmt.Println(show(rem(r,2))) }
''',
"R": '''rem <- function(n,t){ if(is.null(n)) return(NULL); n$l<-rem(n$l,t); n$r<-rem(n$r,t); if(is.null(n$l)&&is.null(n$r)&&n$v==t) return(NULL); n }
nd <- function(v,l=NULL,r=NULL) list(v=v,l=l,r=r)
print(rem(nd(1,nd(2,nd(2)),nd(3,nd(2),nd(4))),2))
''',
}))

# 190 Binary Tree Maximum Path Sum
L.append((190, "Binary Tree Maximum Path Sum", "Trees", "Hard", 95,
"Path is any sequence of nodes connected by edges (with at least one node). Return the maximum sum.",
{
"Python": '''class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def maxPathSum(root):
    res=[float('-inf')]
    def dfs(n):
        if not n: return 0
        l=max(0,dfs(n.l)); r=max(0,dfs(n.r))
        res[0]=max(res[0],n.v+l+r)
        return n.v+max(l,r)
    dfs(root); return res[0]

if __name__=="__main__":
    print(maxPathSum(N(1,N(2),N(3))))
    print(maxPathSum(N(-10,N(9),N(20,N(15),N(7)))))
''',
"JavaScript": '''class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function maxPathSum(root){let res=-Infinity;function dfs(n){if(!n)return 0;const l=Math.max(0,dfs(n.l)),r=Math.max(0,dfs(n.r));res=Math.max(res,n.v+l+r);return n.v+Math.max(l,r);}dfs(root);return res;}
console.log(maxPathSum(new N(1,new N(2),new N(3))));console.log(maxPathSum(new N(-10,new N(9),new N(20,new N(15),new N(7)))));
''',
"Java": '''public class __CLASS__{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static int res; static int dfs(N n){if(n==null)return 0;int l=Math.max(0,dfs(n.l)),r=Math.max(0,dfs(n.r));res=Math.max(res,n.v+l+r);return n.v+Math.max(l,r);}
  static int maxPathSum(N r){res=Integer.MIN_VALUE;dfs(r);return res;}
  public static void main(String[]a){N r=new N(-10);r.l=new N(9);r.r=new N(20);r.r.l=new N(15);r.r.r=new N(7);System.out.println(maxPathSum(r));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct N{int v;N*l=0;N*r=0;N(int v):v(v){}};
int RES;
int dfs(N* n){if(!n)return 0;int l=max(0,dfs(n->l)),r=max(0,dfs(n->r));RES=max(RES,n->v+l+r);return n->v+max(l,r);}
int maxPathSum(N* r){RES=INT_MIN;dfs(r);return RES;}
int main(){N r(-10),a(9),b(20),c(15),d(7);r.l=&a;r.r=&b;b.l=&c;b.r=&d;cout<<maxPathSum(&r)<<"\\n";}
''',
"Go": '''package main
import "fmt"
type N struct{ V int; L,R *N }
var RES int
func dfs(n *N) int { if n==nil { return 0 }; l:=dfs(n.L); if l<0 { l=0 }; r:=dfs(n.R); if r<0 { r=0 }; if n.V+l+r>RES { RES=n.V+l+r }; if l>r { return n.V+l }; return n.V+r }
func maxPathSum(r *N) int { RES=-1<<30; dfs(r); return RES }
func main(){ r:=&N{V:-10,L:&N{V:9},R:&N{V:20,L:&N{V:15},R:&N{V:7}}}; fmt.Println(maxPathSum(r)) }
''',
"R": '''res <- -Inf
dfs <- function(n){ if(is.null(n)) return(0); l<-max(0,dfs(n$l)); r<-max(0,dfs(n$r)); res<<-max(res,n$v+l+r); n$v+max(l,r) }
maxPathSum <- function(r){ res<<- -Inf; dfs(r); res }
nd <- function(v,l=NULL,r=NULL) list(v=v,l=l,r=r)
cat(maxPathSum(nd(-10,nd(9),nd(20,nd(15),nd(7)))),"\\n")
''',
}))

# 191 N Queens II — same as totalNQueens
L.append((191, "N Queens II", "Backtracking", "Hard", 96,
"Return number of distinct solutions for n-queens.",
{
"Python": '''def totalNQueens(n):
    cnt=[0]; cols=set(); d1=set(); d2=set()
    def bt(r):
        if r==n: cnt[0]+=1; return
        for c in range(n):
            if c in cols or r-c in d1 or r+c in d2: continue
            cols.add(c); d1.add(r-c); d2.add(r+c); bt(r+1)
            cols.remove(c); d1.remove(r-c); d2.remove(r+c)
    bt(0); return cnt[0]

if __name__=="__main__":
    print(totalNQueens(4))
    print(totalNQueens(8))
''',
"JavaScript": '''function totalNQueens(n){let cnt=0;const c=new Set(),d1=new Set(),d2=new Set();function bt(r){if(r===n){cnt++;return;}for(let i=0;i<n;i++){if(c.has(i)||d1.has(r-i)||d2.has(r+i))continue;c.add(i);d1.add(r-i);d2.add(r+i);bt(r+1);c.delete(i);d1.delete(r-i);d2.delete(r+i);}}bt(0);return cnt;}
console.log(totalNQueens(4));console.log(totalNQueens(8));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int CNT; static int N; static Set<Integer> C,D1,D2;
  static void bt(int r){if(r==N){CNT++;return;}for(int i=0;i<N;i++){if(C.contains(i)||D1.contains(r-i)||D2.contains(r+i))continue;C.add(i);D1.add(r-i);D2.add(r+i);bt(r+1);C.remove(i);D1.remove(r-i);D2.remove(r+i);}}
  static int totalNQueens(int n){CNT=0;N=n;C=new HashSet<>();D1=new HashSet<>();D2=new HashSet<>();bt(0);return CNT;}
  public static void main(String[]a){System.out.println(totalNQueens(4));System.out.println(totalNQueens(8));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int CNT,N; set<int> C,D1,D2;
void bt(int r){if(r==N){CNT++;return;}for(int i=0;i<N;i++){if(C.count(i)||D1.count(r-i)||D2.count(r+i))continue;C.insert(i);D1.insert(r-i);D2.insert(r+i);bt(r+1);C.erase(i);D1.erase(r-i);D2.erase(r+i);}}
int totalNQueens(int n){CNT=0;N=n;C.clear();D1.clear();D2.clear();bt(0);return CNT;}
int main(){cout<<totalNQueens(4)<<"\\n"<<totalNQueens(8)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func totalNQueens(n int) int { cnt:=0; c:=map[int]bool{}; d1:=map[int]bool{}; d2:=map[int]bool{}; var bt func(r int); bt=func(r int){ if r==n { cnt++; return }; for i:=0;i<n;i++ { if c[i]||d1[r-i]||d2[r+i] { continue }; c[i]=true; d1[r-i]=true; d2[r+i]=true; bt(r+1); delete(c,i); delete(d1,r-i); delete(d2,r+i) } }; bt(0); return cnt }
func main(){ fmt.Println(totalNQueens(4)); fmt.Println(totalNQueens(8)) }
''',
"R": '''totalNQueens <- function(n){ cnt<-0; c<-c(); d1<-c(); d2<-c(); bt<-function(r){ if(r>n){ cnt<<-cnt+1; return() }; for(i in 1:n){ if((i %in% c)||((r-i)%in%d1)||((r+i)%in%d2)) next; c<<-c(c,i); d1<<-c(d1,r-i); d2<<-c(d2,r+i); bt(r+1); c<<-c[-length(c)]; d1<<-d1[-length(d1)]; d2<<-d2[-length(d2)] } }; bt(1); cnt }
cat(totalNQueens(4),"\\n")
''',
}))

# 192 Word Break II
L.append((192, "Word Break II", "Backtracking", "Hard", 96,
"Return all sentences obtainable by segmenting s using words from dict.",
{
"Python": '''def wordBreak(s,wd):
    w=set(wd); memo={}
    def dfs(i):
        if i==len(s): return [""]
        if i in memo: return memo[i]
        out=[]
        for j in range(i+1,len(s)+1):
            if s[i:j] in w:
                for t in dfs(j):
                    out.append(s[i:j]+(" "+t if t else ""))
        memo[i]=out; return out
    return dfs(0)

if __name__=="__main__":
    print(wordBreak("catsanddog",["cat","cats","and","sand","dog"]))
''',
"JavaScript": '''function wordBreak(s,wd){const w=new Set(wd),memo=new Map();function dfs(i){if(i===s.length)return [""];if(memo.has(i))return memo.get(i);const out=[];for(let j=i+1;j<=s.length;j++){const part=s.substring(i,j);if(w.has(part))for(const t of dfs(j))out.push(part+(t?" "+t:""));}memo.set(i,out);return out;}return dfs(0);}
console.log(wordBreak("catsanddog",["cat","cats","and","sand","dog"]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static Map<Integer,List<String>> M; static String S; static Set<String> W;
  static List<String> dfs(int i){if(i==S.length()){List<String> r=new ArrayList<>();r.add("");return r;}if(M.containsKey(i))return M.get(i);List<String> out=new ArrayList<>();for(int j=i+1;j<=S.length();j++){String p=S.substring(i,j);if(W.contains(p))for(String t:dfs(j))out.add(p+(t.isEmpty()?"":" "+t));}M.put(i,out);return out;}
  static List<String> wordBreak(String s,List<String> wd){M=new HashMap<>();S=s;W=new HashSet<>(wd);return dfs(0);}
  public static void main(String[]a){System.out.println(wordBreak("catsanddog",Arrays.asList("cat","cats","and","sand","dog")));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
unordered_map<int,vector<string>> M; string S; unordered_set<string> W;
vector<string> dfs(int i){if(i==(int)S.size())return {""};if(M.count(i))return M[i];vector<string> out;for(int j=i+1;j<=(int)S.size();j++){string p=S.substr(i,j-i);if(W.count(p))for(auto& t:dfs(j))out.push_back(p+(t.empty()?"":" "+t));}return M[i]=out;}
vector<string> wordBreak(string s,vector<string> wd){M.clear();S=s;W=unordered_set<string>(wd.begin(),wd.end());return dfs(0);}
int main(){auto r=wordBreak("catsanddog",{"cat","cats","and","sand","dog"});for(auto& s:r)cout<<s<<"\\n";}
''',
"Go": '''package main
import "fmt"
var M map[int][]string; var S string; var W map[string]bool
func dfs(i int) []string { if i==len(S) { return []string{""} }; if v,ok:=M[i]; ok { return v }; var out []string; for j:=i+1;j<=len(S);j++ { p:=S[i:j]; if W[p] { for _,t:=range dfs(j) { if t=="" { out=append(out,p) } else { out=append(out,p+" "+t) } } } }; M[i]=out; return out }
func wordBreak(s string,wd []string) []string { M=map[int][]string{}; S=s; W=map[string]bool{}; for _,x:=range wd { W[x]=true }; return dfs(0) }
func main(){ fmt.Println(wordBreak("catsanddog",[]string{"cat","cats","and","sand","dog"})) }
''',
"R": '''wordBreak <- function(s,wd){ w<-as.list(rep(TRUE,length(wd))); names(w)<-wd; memo<-list(); dfs<-function(i){ if(i>nchar(s)) return(list("")); k<-as.character(i); if(!is.null(memo[[k]])) return(memo[[k]]); out<-list(); for(j in i:nchar(s)){ p<-substr(s,i,j); if(!is.null(w[[p]])) for(t in dfs(j+1)) out[[length(out)+1]]<- if(nchar(t)==0) p else paste(p,t) }; memo[[k]]<<-out; out }; dfs(1) }
print(wordBreak("catsanddog",c("cat","cats","and","sand","dog")))
''',
}))

# 193 Interleaving String
L.append((193, "Interleaving String", "2-D Dynamic Programming", "Medium", 97,
"Determine whether s3 can be formed by interleaving s1 and s2.",
{
"Python": '''def isInterleave(a,b,c):
    if len(a)+len(b)!=len(c): return False
    dp=[[False]*(len(b)+1) for _ in range(len(a)+1)]
    dp[0][0]=True
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i and a[i-1]==c[i+j-1]: dp[i][j]|=dp[i-1][j]
            if j and b[j-1]==c[i+j-1]: dp[i][j]|=dp[i][j-1]
    return dp[len(a)][len(b)]

if __name__=="__main__":
    print(isInterleave("aabcc","dbbca","aadbbcbcac"))
    print(isInterleave("aabcc","dbbca","aadbbbaccc"))
''',
"JavaScript": '''function isInterleave(a,b,c){if(a.length+b.length!==c.length)return false;const dp=Array.from({length:a.length+1},()=>new Array(b.length+1).fill(false));dp[0][0]=true;for(let i=0;i<=a.length;i++)for(let j=0;j<=b.length;j++){if(i&&a[i-1]===c[i+j-1])dp[i][j]=dp[i][j]||dp[i-1][j];if(j&&b[j-1]===c[i+j-1])dp[i][j]=dp[i][j]||dp[i][j-1];}return dp[a.length][b.length];}
console.log(isInterleave("aabcc","dbbca","aadbbcbcac"));console.log(isInterleave("aabcc","dbbca","aadbbbaccc"));
''',
"Java": '''public class __CLASS__{
  static boolean isInterleave(String a,String b,String c){if(a.length()+b.length()!=c.length())return false;boolean[][] dp=new boolean[a.length()+1][b.length()+1];dp[0][0]=true;for(int i=0;i<=a.length();i++)for(int j=0;j<=b.length();j++){if(i>0 && a.charAt(i-1)==c.charAt(i+j-1)) dp[i][j]|=dp[i-1][j];if(j>0 && b.charAt(j-1)==c.charAt(i+j-1)) dp[i][j]|=dp[i][j-1];}return dp[a.length()][b.length()];}
  public static void main(String[]a){System.out.println(isInterleave("aabcc","dbbca","aadbbcbcac"));System.out.println(isInterleave("aabcc","dbbca","aadbbbaccc"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool isInterleave(string a,string b,string c){if(a.size()+b.size()!=c.size())return false;vector<vector<bool>> dp(a.size()+1,vector<bool>(b.size()+1,false));dp[0][0]=true;for(int i=0;i<=(int)a.size();i++)for(int j=0;j<=(int)b.size();j++){if(i&&a[i-1]==c[i+j-1])dp[i][j]=dp[i][j]||dp[i-1][j];if(j&&b[j-1]==c[i+j-1])dp[i][j]=dp[i][j]||dp[i][j-1];}return dp[a.size()][b.size()];}
int main(){cout<<boolalpha<<isInterleave("aabcc","dbbca","aadbbcbcac")<<"\\n"<<isInterleave("aabcc","dbbca","aadbbbaccc")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func isInterleave(a,b,c string) bool { if len(a)+len(b)!=len(c) { return false }; dp:=make([][]bool,len(a)+1); for i:=range dp { dp[i]=make([]bool,len(b)+1) }; dp[0][0]=true; for i:=0;i<=len(a);i++ { for j:=0;j<=len(b);j++ { if i>0 && a[i-1]==c[i+j-1] && dp[i-1][j] { dp[i][j]=true }; if j>0 && b[j-1]==c[i+j-1] && dp[i][j-1] { dp[i][j]=true } } }; return dp[len(a)][len(b)] }
func main(){ fmt.Println(isInterleave("aabcc","dbbca","aadbbcbcac")); fmt.Println(isInterleave("aabcc","dbbca","aadbbbaccc")) }
''',
"R": '''isInterleave <- function(a,b,c){ if(nchar(a)+nchar(b)!=nchar(c)) return(FALSE); dp<-matrix(FALSE,nchar(a)+1,nchar(b)+1); dp[1,1]<-TRUE; for(i in 1:(nchar(a)+1)) for(j in 1:(nchar(b)+1)){ if(i>1 && substr(a,i-1,i-1)==substr(c,i+j-2,i+j-2)) dp[i,j]<-dp[i,j]||dp[i-1,j]; if(j>1 && substr(b,j-1,j-1)==substr(c,i+j-2,i+j-2)) dp[i,j]<-dp[i,j]||dp[i,j-1] }; dp[nchar(a)+1,nchar(b)+1] }
cat(isInterleave("aabcc","dbbca","aadbbcbcac"),"\\n")
''',
}))

# 194 Stone Game (always returns true for even pile counts; classic solution)
L.append((194, "Stone Game", "2-D Dynamic Programming", "Medium", 97,
"Two players take stones from either end. Both play optimally. Return true if Alice wins.",
{
"Python": '''def stoneGame(p):
    n=len(p); dp=[[0]*n for _ in range(n)]
    for i in range(n): dp[i][i]=p[i]
    for L in range(2,n+1):
        for i in range(n-L+1):
            j=i+L-1
            dp[i][j]=max(p[i]-dp[i+1][j], p[j]-dp[i][j-1])
    return dp[0][n-1]>0

if __name__=="__main__":
    print(stoneGame([5,3,4,5]))
''',
"JavaScript": '''function stoneGame(p){const n=p.length;const dp=Array.from({length:n},()=>new Array(n).fill(0));for(let i=0;i<n;i++)dp[i][i]=p[i];for(let L=2;L<=n;L++)for(let i=0;i<=n-L;i++){const j=i+L-1;dp[i][j]=Math.max(p[i]-dp[i+1][j],p[j]-dp[i][j-1]);}return dp[0][n-1]>0;}
console.log(stoneGame([5,3,4,5]));
''',
"Java": '''public class __CLASS__{
  static boolean stoneGame(int[] p){int n=p.length;int[][] dp=new int[n][n];for(int i=0;i<n;i++)dp[i][i]=p[i];for(int L=2;L<=n;L++)for(int i=0;i<=n-L;i++){int j=i+L-1;dp[i][j]=Math.max(p[i]-dp[i+1][j],p[j]-dp[i][j-1]);}return dp[0][n-1]>0;}
  public static void main(String[]a){System.out.println(stoneGame(new int[]{5,3,4,5}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool stoneGame(vector<int> p){int n=p.size();vector<vector<int>> dp(n,vector<int>(n,0));for(int i=0;i<n;i++)dp[i][i]=p[i];for(int L=2;L<=n;L++)for(int i=0;i<=n-L;i++){int j=i+L-1;dp[i][j]=max(p[i]-dp[i+1][j],p[j]-dp[i][j-1]);}return dp[0][n-1]>0;}
int main(){cout<<boolalpha<<stoneGame({5,3,4,5})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func stoneGame(p []int) bool { n:=len(p); dp:=make([][]int,n); for i:=range dp { dp[i]=make([]int,n); dp[i][i]=p[i] }; for L:=2;L<=n;L++ { for i:=0;i<=n-L;i++ { j:=i+L-1; a:=p[i]-dp[i+1][j]; b:=p[j]-dp[i][j-1]; if a>b { dp[i][j]=a } else { dp[i][j]=b } } }; return dp[0][n-1]>0 }
func main(){ fmt.Println(stoneGame([]int{5,3,4,5})) }
''',
"R": '''stoneGame <- function(p){ n<-length(p); dp<-matrix(0,n,n); for(i in 1:n) dp[i,i]<-p[i]; if(n>=2) for(L in 2:n) for(i in 1:(n-L+1)){ j<-i+L-1; dp[i,j]<-max(p[i]-dp[i+1,j], p[j]-dp[i,j-1]) }; dp[1,n]>0 }
cat(stoneGame(c(5,3,4,5)),"\\n")
''',
}))

# 195 Boats to Save People
L.append((195, "Boats to Save People", "Two Pointers", "Medium", 98,
"Each boat holds at most 2 people, total weight <= limit. Return min boats.",
{
"Python": '''def numRescueBoats(p,limit):
    p.sort(); i=0; j=len(p)-1; b=0
    while i<=j:
        if p[i]+p[j]<=limit: i+=1
        j-=1; b+=1
    return b

if __name__=="__main__":
    print(numRescueBoats([1,2],3))
    print(numRescueBoats([3,2,2,1],3))
    print(numRescueBoats([3,5,3,4],5))
''',
"JavaScript": '''function numRescueBoats(p,limit){p.sort((a,b)=>a-b);let i=0,j=p.length-1,b=0;while(i<=j){if(p[i]+p[j]<=limit)i++;j--;b++;}return b;}
console.log(numRescueBoats([3,2,2,1],3));console.log(numRescueBoats([3,5,3,4],5));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int numRescueBoats(int[] p,int limit){Arrays.sort(p);int i=0,j=p.length-1,b=0;while(i<=j){if(p[i]+p[j]<=limit)i++;j--;b++;}return b;}
  public static void main(String[]a){System.out.println(numRescueBoats(new int[]{3,2,2,1},3));System.out.println(numRescueBoats(new int[]{3,5,3,4},5));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int numRescueBoats(vector<int> p,int limit){sort(p.begin(),p.end());int i=0,j=p.size()-1,b=0;while(i<=j){if(p[i]+p[j]<=limit)i++;j--;b++;}return b;}
int main(){cout<<numRescueBoats({3,2,2,1},3)<<"\\n"<<numRescueBoats({3,5,3,4},5)<<"\\n";}
''',
"Go": '''package main
import ("fmt"; "sort")
func numRescueBoats(p []int,limit int) int { sort.Ints(p); i,j,b:=0,len(p)-1,0; for i<=j { if p[i]+p[j]<=limit { i++ }; j--; b++ }; return b }
func main(){ fmt.Println(numRescueBoats([]int{3,2,2,1},3)); fmt.Println(numRescueBoats([]int{3,5,3,4},5)) }
''',
"R": '''numRescueBoats <- function(p,limit){ p<-sort(p); i<-1; j<-length(p); b<-0; while(i<=j){ if(p[i]+p[j]<=limit) i<-i+1; j<-j-1; b<-b+1 }; b }
cat(numRescueBoats(c(3,2,2,1),3),"\\n"); cat(numRescueBoats(c(3,5,3,4),5),"\\n")
''',
}))

# 196 Trapping Rain Water
L.append((196, "Trapping Rain Water", "Two Pointers", "Hard", 98,
"Compute total water trapped between bars given heights.",
{
"Python": '''def trap(h):
    l,r=0,len(h)-1; lm=rm=0; res=0
    while l<r:
        if h[l]<h[r]:
            if h[l]>=lm: lm=h[l]
            else: res+=lm-h[l]
            l+=1
        else:
            if h[r]>=rm: rm=h[r]
            else: res+=rm-h[r]
            r-=1
    return res

if __name__=="__main__":
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
''',
"JavaScript": '''function trap(h){let l=0,r=h.length-1,lm=0,rm=0,res=0;while(l<r){if(h[l]<h[r]){if(h[l]>=lm)lm=h[l];else res+=lm-h[l];l++;}else{if(h[r]>=rm)rm=h[r];else res+=rm-h[r];r--;}}return res;}
console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]));
''',
"Java": '''public class __CLASS__{
  static int trap(int[] h){int l=0,r=h.length-1,lm=0,rm=0,res=0;while(l<r){if(h[l]<h[r]){if(h[l]>=lm)lm=h[l];else res+=lm-h[l];l++;}else{if(h[r]>=rm)rm=h[r];else res+=rm-h[r];r--;}}return res;}
  public static void main(String[]a){System.out.println(trap(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int trap(vector<int> h){int l=0,r=h.size()-1,lm=0,rm=0,res=0;while(l<r){if(h[l]<h[r]){if(h[l]>=lm)lm=h[l];else res+=lm-h[l];l++;}else{if(h[r]>=rm)rm=h[r];else res+=rm-h[r];r--;}}return res;}
int main(){cout<<trap({0,1,0,2,1,0,1,3,2,1,2,1})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func trap(h []int) int { l,r:=0,len(h)-1; lm,rm,res:=0,0,0; for l<r { if h[l]<h[r] { if h[l]>=lm { lm=h[l] } else { res+=lm-h[l] }; l++ } else { if h[r]>=rm { rm=h[r] } else { res+=rm-h[r] }; r-- } }; return res }
func main(){ fmt.Println(trap([]int{0,1,0,2,1,0,1,3,2,1,2,1})) }
''',
"R": '''trap <- function(h){ l<-1; r<-length(h); lm<-0; rm<-0; res<-0; while(l<r){ if(h[l]<h[r]){ if(h[l]>=lm) lm<-h[l] else res<-res+lm-h[l]; l<-l+1 } else { if(h[r]>=rm) rm<-h[r] else res<-res+rm-h[r]; r<-r-1 } }; res }
cat(trap(c(0,1,0,2,1,0,1,3,2,1,2,1)),"\\n")
''',
}))

# 197 Median of Two Sorted Arrays
L.append((197, "Median of Two Sorted Arrays", "Binary Search", "Hard", 99,
"Find the median of the two sorted arrays in O(log(min(m,n))).",
{
"Python": '''def findMedianSortedArrays(a,b):
    if len(a)>len(b): a,b=b,a
    m,n=len(a),len(b); lo=0; hi=m
    while lo<=hi:
        i=(lo+hi)//2; j=(m+n+1)//2-i
        Lx=a[i-1] if i>0 else float('-inf')
        Rx=a[i] if i<m else float('inf')
        Ly=b[j-1] if j>0 else float('-inf')
        Ry=b[j] if j<n else float('inf')
        if Lx<=Ry and Ly<=Rx:
            if (m+n)%2: return max(Lx,Ly)
            return (max(Lx,Ly)+min(Rx,Ry))/2
        elif Lx>Ry: hi=i-1
        else: lo=i+1

if __name__=="__main__":
    print(findMedianSortedArrays([1,3],[2]))
    print(findMedianSortedArrays([1,2],[3,4]))
''',
"JavaScript": '''function findMedianSortedArrays(a,b){if(a.length>b.length)[a,b]=[b,a];const m=a.length,n=b.length;let lo=0,hi=m;while(lo<=hi){const i=(lo+hi)>>1;const j=((m+n+1)>>1)-i;const Lx=i>0?a[i-1]:-Infinity,Rx=i<m?a[i]:Infinity,Ly=j>0?b[j-1]:-Infinity,Ry=j<n?b[j]:Infinity;if(Lx<=Ry&&Ly<=Rx){if((m+n)&1)return Math.max(Lx,Ly);return (Math.max(Lx,Ly)+Math.min(Rx,Ry))/2;}else if(Lx>Ry)hi=i-1;else lo=i+1;}}
console.log(findMedianSortedArrays([1,3],[2]));console.log(findMedianSortedArrays([1,2],[3,4]));
''',
"Java": '''public class __CLASS__{
  static double findMedianSortedArrays(int[] a,int[] b){if(a.length>b.length){int[] t=a;a=b;b=t;}int m=a.length,n=b.length,lo=0,hi=m;while(lo<=hi){int i=(lo+hi)/2;int j=(m+n+1)/2-i;int Lx=i>0?a[i-1]:Integer.MIN_VALUE;int Rx=i<m?a[i]:Integer.MAX_VALUE;int Ly=j>0?b[j-1]:Integer.MIN_VALUE;int Ry=j<n?b[j]:Integer.MAX_VALUE;if(Lx<=Ry&&Ly<=Rx){if(((m+n)&1)==1)return Math.max(Lx,Ly);return (Math.max(Lx,Ly)+Math.min(Rx,Ry))/2.0;}else if(Lx>Ry)hi=i-1;else lo=i+1;}return 0;}
  public static void main(String[]a){System.out.println(findMedianSortedArrays(new int[]{1,3},new int[]{2}));System.out.println(findMedianSortedArrays(new int[]{1,2},new int[]{3,4}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
double findMedianSortedArrays(vector<int> a,vector<int> b){if(a.size()>b.size())swap(a,b);int m=a.size(),n=b.size(),lo=0,hi=m;while(lo<=hi){int i=(lo+hi)/2;int j=(m+n+1)/2-i;int Lx=i>0?a[i-1]:INT_MIN,Rx=i<m?a[i]:INT_MAX,Ly=j>0?b[j-1]:INT_MIN,Ry=j<n?b[j]:INT_MAX;if(Lx<=Ry&&Ly<=Rx){if((m+n)&1)return max(Lx,Ly);return (max(Lx,Ly)+min(Rx,Ry))/2.0;}else if(Lx>Ry)hi=i-1;else lo=i+1;}return 0;}
int main(){cout<<findMedianSortedArrays({1,3},{2})<<"\\n"<<findMedianSortedArrays({1,2},{3,4})<<"\\n";}
''',
"Go": '''package main
import ("fmt"; "math")
func findMedianSortedArrays(a,b []int) float64 { if len(a)>len(b) { a,b=b,a }; m,n:=len(a),len(b); lo,hi:=0,m; for lo<=hi { i:=(lo+hi)/2; j:=(m+n+1)/2-i; Lx:=math.MinInt32; if i>0 { Lx=a[i-1] }; Rx:=math.MaxInt32; if i<m { Rx=a[i] }; Ly:=math.MinInt32; if j>0 { Ly=b[j-1] }; Ry:=math.MaxInt32; if j<n { Ry=b[j] }; if Lx<=Ry && Ly<=Rx { mx:=Lx; if Ly>mx { mx=Ly }; if (m+n)%2==1 { return float64(mx) }; mn:=Rx; if Ry<mn { mn=Ry }; return (float64(mx)+float64(mn))/2.0 } else if Lx>Ry { hi=i-1 } else { lo=i+1 } }; return 0 }
func main(){ fmt.Println(findMedianSortedArrays([]int{1,3},[]int{2})); fmt.Println(findMedianSortedArrays([]int{1,2},[]int{3,4})) }
''',
"R": '''findMedianSortedArrays <- function(a,b){ x<-sort(c(a,b)); n<-length(x); if(n%%2==1) x[(n+1)/2] else (x[n/2]+x[n/2+1])/2 }
cat(findMedianSortedArrays(c(1,3),c(2)),"\\n"); cat(findMedianSortedArrays(c(1,2),c(3,4)),"\\n")
''',
}))

# 198 Find in Mountain Array (simulated locally with a normal array)
L.append((198, "Find in Mountain Array", "Binary Search", "Hard", 99,
"Mountain array: strictly increasing then strictly decreasing. Return min index with value=target.",
{
"Python": '''def findInMountainArray(target,a):
    lo,hi=0,len(a)-1
    while lo<hi:
        m=(lo+hi)//2
        if a[m]<a[m+1]: lo=m+1
        else: hi=m
    peak=lo
    def bs(l,r,asc):
        while l<=r:
            m=(l+r)//2
            v=a[m]
            if v==target: return m
            if asc:
                if v<target: l=m+1
                else: r=m-1
            else:
                if v>target: l=m+1
                else: r=m-1
        return -1
    i=bs(0,peak,True)
    if i!=-1: return i
    return bs(peak+1,len(a)-1,False)

if __name__=="__main__":
    print(findInMountainArray(3,[1,2,3,4,5,3,1]))
    print(findInMountainArray(3,[0,1,2,4,2,1]))
''',
"JavaScript": '''function findInMountainArray(target,a){let lo=0,hi=a.length-1;while(lo<hi){const m=(lo+hi)>>1;if(a[m]<a[m+1])lo=m+1;else hi=m;}const peak=lo;function bs(l,r,asc){while(l<=r){const m=(l+r)>>1;if(a[m]===target)return m;if(asc){if(a[m]<target)l=m+1;else r=m-1;}else{if(a[m]>target)l=m+1;else r=m-1;}}return -1;}const i=bs(0,peak,true);return i!==-1?i:bs(peak+1,a.length-1,false);}
console.log(findInMountainArray(3,[1,2,3,4,5,3,1]));
''',
"Java": '''public class __CLASS__{
  static int bs(int[] a,int l,int r,int t,boolean asc){while(l<=r){int m=(l+r)/2;if(a[m]==t)return m;if(asc){if(a[m]<t)l=m+1;else r=m-1;}else{if(a[m]>t)l=m+1;else r=m-1;}}return -1;}
  static int findInMountainArray(int t,int[] a){int lo=0,hi=a.length-1;while(lo<hi){int m=(lo+hi)/2;if(a[m]<a[m+1])lo=m+1;else hi=m;}int p=lo;int i=bs(a,0,p,t,true);return i!=-1?i:bs(a,p+1,a.length-1,t,false);}
  public static void main(String[]x){System.out.println(findInMountainArray(3,new int[]{1,2,3,4,5,3,1}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int bs(vector<int>& a,int l,int r,int t,bool asc){while(l<=r){int m=(l+r)/2;if(a[m]==t)return m;if(asc){if(a[m]<t)l=m+1;else r=m-1;}else{if(a[m]>t)l=m+1;else r=m-1;}}return -1;}
int findInMountainArray(int t,vector<int> a){int lo=0,hi=a.size()-1;while(lo<hi){int m=(lo+hi)/2;if(a[m]<a[m+1])lo=m+1;else hi=m;}int p=lo;int i=bs(a,0,p,t,true);return i!=-1?i:bs(a,p+1,a.size()-1,t,false);}
int main(){cout<<findInMountainArray(3,{1,2,3,4,5,3,1})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func bs(a []int,l,r,t int,asc bool) int { for l<=r { m:=(l+r)/2; if a[m]==t { return m }; if asc { if a[m]<t { l=m+1 } else { r=m-1 } } else { if a[m]>t { l=m+1 } else { r=m-1 } } }; return -1 }
func findInMountainArray(t int,a []int) int { lo,hi:=0,len(a)-1; for lo<hi { m:=(lo+hi)/2; if a[m]<a[m+1] { lo=m+1 } else { hi=m } }; i:=bs(a,0,lo,t,true); if i!=-1 { return i }; return bs(a,lo+1,len(a)-1,t,false) }
func main(){ fmt.Println(findInMountainArray(3,[]int{1,2,3,4,5,3,1})) }
''',
"R": '''findInMountainArray <- function(t,a){ idx<-which(a==t); if(length(idx)==0) -1 else idx[1]-1 }
cat(findInMountainArray(3,c(1,2,3,4,5,3,1)),"\\n")
''',
}))

# 199 Stone Game II
L.append((199, "Stone Game II", "2-D Dynamic Programming", "Medium", 100,
"Two players take stones from front; can take X piles where 1<=X<=2M (M starts at 1). Maximize own.",
{
"Python": '''def stoneGameII(p):
    n=len(p); suf=[0]*(n+1)
    for i in range(n-1,-1,-1): suf[i]=suf[i+1]+p[i]
    memo={}
    def dfs(i,M):
        if i+2*M>=n: return suf[i]
        if (i,M) in memo: return memo[(i,M)]
        best=0
        for x in range(1,2*M+1):
            best=max(best, suf[i]-dfs(i+x, max(M,x)))
        memo[(i,M)]=best; return best
    return dfs(0,1)

if __name__=="__main__":
    print(stoneGameII([2,7,9,4,4]))
''',
"JavaScript": '''function stoneGameII(p){const n=p.length;const suf=new Array(n+1).fill(0);for(let i=n-1;i>=0;i--)suf[i]=suf[i+1]+p[i];const memo=new Map();function dfs(i,M){if(i+2*M>=n)return suf[i];const k=i*100+M;if(memo.has(k))return memo.get(k);let best=0;for(let x=1;x<=2*M;x++)best=Math.max(best,suf[i]-dfs(i+x,Math.max(M,x)));memo.set(k,best);return best;}return dfs(0,1);}
console.log(stoneGameII([2,7,9,4,4]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] SUF; static int N; static int[][] M;
  static int dfs(int i,int m){if(i+2*m>=N)return SUF[i];if(M[i][m]!=-1)return M[i][m];int best=0;for(int x=1;x<=2*m;x++)best=Math.max(best,SUF[i]-dfs(i+x,Math.max(m,x)));return M[i][m]=best;}
  static int stoneGameII(int[] p){N=p.length;SUF=new int[N+1];for(int i=N-1;i>=0;i--)SUF[i]=SUF[i+1]+p[i];M=new int[N+1][N+1];for(int[] r:M)Arrays.fill(r,-1);return dfs(0,1);}
  public static void main(String[]a){System.out.println(stoneGameII(new int[]{2,7,9,4,4}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> SUF; int N; vector<vector<int>> MM;
int dfs(int i,int m){if(i+2*m>=N)return SUF[i];if(MM[i][m]!=-1)return MM[i][m];int best=0;for(int x=1;x<=2*m;x++)best=max(best,SUF[i]-dfs(i+x,max(m,x)));return MM[i][m]=best;}
int stoneGameII(vector<int> p){N=p.size();SUF.assign(N+1,0);for(int i=N-1;i>=0;i--)SUF[i]=SUF[i+1]+p[i];MM.assign(N+1,vector<int>(N+1,-1));return dfs(0,1);}
int main(){cout<<stoneGameII({2,7,9,4,4})<<"\\n";}
''',
"Go": '''package main
import "fmt"
var SUF []int; var N int; var MEMO map[int]int
func dfs(i,m int) int { if i+2*m>=N { return SUF[i] }; k:=i*1000+m; if v,ok:=MEMO[k]; ok { return v }; best:=0; for x:=1;x<=2*m;x++ { mx:=m; if x>mx { mx=x }; v:=SUF[i]-dfs(i+x,mx); if v>best { best=v } }; MEMO[k]=best; return best }
func stoneGameII(p []int) int { N=len(p); SUF=make([]int,N+1); for i:=N-1;i>=0;i-- { SUF[i]=SUF[i+1]+p[i] }; MEMO=map[int]int{}; return dfs(0,1) }
func main(){ fmt.Println(stoneGameII([]int{2,7,9,4,4})) }
''',
"R": '''stoneGameII <- function(p){ n<-length(p); suf<-rep(0,n+1); for(i in n:1) suf[i]<-suf[i+1]+p[i]; memo<-list(); dfs<-function(i,M){ if(i+2*M-1>=n) return(suf[i]); k<-paste(i,M); if(!is.null(memo[[k]])) return(memo[[k]]); best<-0; for(x in 1:(2*M)) best<-max(best,suf[i]-dfs(i+x,max(M,x))); memo[[k]]<<-best; best }; dfs(1,1) }
cat(stoneGameII(c(2,7,9,4,4)),"\\n")
''',
}))

# 200 Edit Distance
L.append((200, "Edit Distance", "2-D Dynamic Programming", "Medium", 100,
"Min number of insert/delete/replace ops to convert s1 to s2.",
{
"Python": '''def minDistance(a,b):
    m,n=len(a),len(b); dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0]=i
    for j in range(n+1): dp[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]: dp[i][j]=dp[i-1][j-1]
            else: dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[m][n]

if __name__=="__main__":
    print(minDistance("horse","ros"))
    print(minDistance("intention","execution"))
''',
"JavaScript": '''function minDistance(a,b){const m=a.length,n=b.length;const dp=Array.from({length:m+1},()=>new Array(n+1).fill(0));for(let i=0;i<=m;i++)dp[i][0]=i;for(let j=0;j<=n;j++)dp[0][j]=j;for(let i=1;i<=m;i++)for(let j=1;j<=n;j++){if(a[i-1]===b[j-1])dp[i][j]=dp[i-1][j-1];else dp[i][j]=1+Math.min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]);}return dp[m][n];}
console.log(minDistance("horse","ros"));console.log(minDistance("intention","execution"));
''',
"Java": '''public class __CLASS__{
  static int minDistance(String a,String b){int m=a.length(),n=b.length();int[][] dp=new int[m+1][n+1];for(int i=0;i<=m;i++)dp[i][0]=i;for(int j=0;j<=n;j++)dp[0][j]=j;for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){if(a.charAt(i-1)==b.charAt(j-1))dp[i][j]=dp[i-1][j-1];else dp[i][j]=1+Math.min(dp[i-1][j-1],Math.min(dp[i-1][j],dp[i][j-1]));}return dp[m][n];}
  public static void main(String[]a){System.out.println(minDistance("horse","ros"));System.out.println(minDistance("intention","execution"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int minDistance(string a,string b){int m=a.size(),n=b.size();vector<vector<int>> dp(m+1,vector<int>(n+1,0));for(int i=0;i<=m;i++)dp[i][0]=i;for(int j=0;j<=n;j++)dp[0][j]=j;for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){if(a[i-1]==b[j-1])dp[i][j]=dp[i-1][j-1];else dp[i][j]=1+min({dp[i-1][j],dp[i][j-1],dp[i-1][j-1]});}return dp[m][n];}
int main(){cout<<minDistance("horse","ros")<<"\\n"<<minDistance("intention","execution")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func minDistance(a,b string) int { m,n:=len(a),len(b); dp:=make([][]int,m+1); for i:=range dp { dp[i]=make([]int,n+1); dp[i][0]=i }; for j:=0;j<=n;j++ { dp[0][j]=j }; for i:=1;i<=m;i++ { for j:=1;j<=n;j++ { if a[i-1]==b[j-1] { dp[i][j]=dp[i-1][j-1] } else { mn:=dp[i-1][j]; if dp[i][j-1]<mn { mn=dp[i][j-1] }; if dp[i-1][j-1]<mn { mn=dp[i-1][j-1] }; dp[i][j]=1+mn } } }; return dp[m][n] }
func main(){ fmt.Println(minDistance("horse","ros")); fmt.Println(minDistance("intention","execution")) }
''',
"R": '''minDistance <- function(a,b){ m<-nchar(a); n<-nchar(b); dp<-matrix(0,m+1,n+1); for(i in 0:m) dp[i+1,1]<-i; for(j in 0:n) dp[1,j+1]<-j; if(m>=1) for(i in 1:m) for(j in 1:n){ if(substr(a,i,i)==substr(b,j,j)) dp[i+1,j+1]<-dp[i,j] else dp[i+1,j+1]<-1+min(dp[i,j+1],dp[i+1,j],dp[i,j]) }; dp[m+1,n+1] }
cat(minDistance("horse","ros"),"\\n")
''',
}))

# 201 Longest Increasing Path in Matrix
L.append((201, "Longest Increasing Path In a Matrix", "2-D Dynamic Programming", "Hard", 101,
"Find length of the longest strictly-increasing path in a 2D grid.",
{
"Python": '''def longestIncreasingPath(g):
    if not g: return 0
    R,C=len(g),len(g[0]); memo=[[0]*C for _ in range(R)]
    def dfs(r,c):
        if memo[r][c]: return memo[r][c]
        best=1
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<R and 0<=nc<C and g[nr][nc]>g[r][c]:
                best=max(best,1+dfs(nr,nc))
        memo[r][c]=best; return best
    return max(dfs(r,c) for r in range(R) for c in range(C))

if __name__=="__main__":
    print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
''',
"JavaScript": '''function longestIncreasingPath(g){if(!g.length)return 0;const R=g.length,C=g[0].length;const m=Array.from({length:R},()=>new Array(C).fill(0));function dfs(r,c){if(m[r][c])return m[r][c];let best=1;for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){const nr=r+dr,nc=c+dc;if(nr>=0&&nr<R&&nc>=0&&nc<C&&g[nr][nc]>g[r][c])best=Math.max(best,1+dfs(nr,nc));}m[r][c]=best;return best;}let res=0;for(let r=0;r<R;r++)for(let c=0;c<C;c++)res=Math.max(res,dfs(r,c));return res;}
console.log(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]));
''',
"Java": '''public class __CLASS__{
  static int R,C; static int[][] G,M; static int[][] DIR={{1,0},{-1,0},{0,1},{0,-1}};
  static int dfs(int r,int c){if(M[r][c]!=0)return M[r][c];int best=1;for(int[] d:DIR){int nr=r+d[0],nc=c+d[1];if(nr>=0&&nr<R&&nc>=0&&nc<C&&G[nr][nc]>G[r][c])best=Math.max(best,1+dfs(nr,nc));}return M[r][c]=best;}
  static int longestIncreasingPath(int[][] g){R=g.length;C=g[0].length;G=g;M=new int[R][C];int res=0;for(int r=0;r<R;r++)for(int c=0;c<C;c++)res=Math.max(res,dfs(r,c));return res;}
  public static void main(String[]a){System.out.println(longestIncreasingPath(new int[][]{{9,9,4},{6,6,8},{2,1,1}}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int R,C; vector<vector<int>> G,M; int DIR[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
int dfs(int r,int c){if(M[r][c])return M[r][c];int best=1;for(auto& d:DIR){int nr=r+d[0],nc=c+d[1];if(nr>=0&&nr<R&&nc>=0&&nc<C&&G[nr][nc]>G[r][c])best=max(best,1+dfs(nr,nc));}return M[r][c]=best;}
int longestIncreasingPath(vector<vector<int>> g){R=g.size();C=g[0].size();G=g;M.assign(R,vector<int>(C,0));int res=0;for(int r=0;r<R;r++)for(int c=0;c<C;c++)res=max(res,dfs(r,c));return res;}
int main(){cout<<longestIncreasingPath({{9,9,4},{6,6,8},{2,1,1}})<<"\\n";}
''',
"Go": '''package main
import "fmt"
var R,C int; var G,M [][]int
func dfs(r,c int) int { if M[r][c]!=0 { return M[r][c] }; best:=1; for _,d:=range [4][2]int{{1,0},{-1,0},{0,1},{0,-1}} { nr,nc:=r+d[0],c+d[1]; if nr>=0&&nr<R&&nc>=0&&nc<C&&G[nr][nc]>G[r][c] { v:=1+dfs(nr,nc); if v>best { best=v } } }; M[r][c]=best; return best }
func longestIncreasingPath(g [][]int) int { R=len(g); C=len(g[0]); G=g; M=make([][]int,R); for i:=range M { M[i]=make([]int,C) }; res:=0; for r:=0;r<R;r++ { for c:=0;c<C;c++ { v:=dfs(r,c); if v>res { res=v } } }; return res }
func main(){ fmt.Println(longestIncreasingPath([][]int{{9,9,4},{6,6,8},{2,1,1}})) }
''',
"R": '''longestIncreasingPath <- function(g){ R<-length(g); C<-length(g[[1]]); m<-matrix(0,R,C); dfs<-function(r,c){ if(m[r,c]>0) return(m[r,c]); best<-1; for(d in list(c(1,0),c(-1,0),c(0,1),c(0,-1))){ nr<-r+d[1]; nc<-c+d[2]; if(nr>=1&&nr<=R&&nc>=1&&nc<=C&&g[[nr]][nc]>g[[r]][c]) best<-max(best,1+dfs(nr,nc)) }; m[r,c]<<-best; best }; res<-0; for(r in 1:R) for(c in 1:C) res<-max(res,dfs(r,c)); res }
cat(longestIncreasingPath(list(c(9,9,4),c(6,6,8),c(2,1,1))),"\\n")
''',
}))

# 202 Distinct Subsequences
L.append((202, "Distinct Subsequences", "2-D Dynamic Programming", "Hard", 101,
"Number of distinct subsequences of s equal to t.",
{
"Python": '''def numDistinct(s,t):
    m,n=len(s),len(t); dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i-1][j]+(dp[i-1][j-1] if s[i-1]==t[j-1] else 0)
    return dp[m][n]

if __name__=="__main__":
    print(numDistinct("rabbbit","rabbit"))
''',
"JavaScript": '''function numDistinct(s,t){const m=s.length,n=t.length;const dp=Array.from({length:m+1},()=>new Array(n+1).fill(0));for(let i=0;i<=m;i++)dp[i][0]=1;for(let i=1;i<=m;i++)for(let j=1;j<=n;j++){dp[i][j]=dp[i-1][j]+(s[i-1]===t[j-1]?dp[i-1][j-1]:0);}return dp[m][n];}
console.log(numDistinct("rabbbit","rabbit"));
''',
"Java": '''public class __CLASS__{
  static int numDistinct(String s,String t){int m=s.length(),n=t.length();long[][] dp=new long[m+1][n+1];for(int i=0;i<=m;i++)dp[i][0]=1;for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){dp[i][j]=dp[i-1][j]+(s.charAt(i-1)==t.charAt(j-1)?dp[i-1][j-1]:0);}return (int)dp[m][n];}
  public static void main(String[]a){System.out.println(numDistinct("rabbbit","rabbit"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int numDistinct(string s,string t){int m=s.size(),n=t.size();vector<vector<long long>> dp(m+1,vector<long long>(n+1,0));for(int i=0;i<=m;i++)dp[i][0]=1;for(int i=1;i<=m;i++)for(int j=1;j<=n;j++){dp[i][j]=dp[i-1][j]+(s[i-1]==t[j-1]?dp[i-1][j-1]:0);}return (int)dp[m][n];}
int main(){cout<<numDistinct("rabbbit","rabbit")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func numDistinct(s,t string) int { m,n:=len(s),len(t); dp:=make([][]int,m+1); for i:=range dp { dp[i]=make([]int,n+1); dp[i][0]=1 }; for i:=1;i<=m;i++ { for j:=1;j<=n;j++ { dp[i][j]=dp[i-1][j]; if s[i-1]==t[j-1] { dp[i][j]+=dp[i-1][j-1] } } }; return dp[m][n] }
func main(){ fmt.Println(numDistinct("rabbbit","rabbit")) }
''',
"R": '''numDistinct <- function(s,t){ m<-nchar(s); n<-nchar(t); dp<-matrix(0,m+1,n+1); for(i in 0:m) dp[i+1,1]<-1; if(m>=1) for(i in 1:m) for(j in 1:n){ dp[i+1,j+1]<-dp[i,j+1]; if(substr(s,i,i)==substr(t,j,j)) dp[i+1,j+1]<-dp[i+1,j+1]+dp[i,j] }; dp[m+1,n+1] }
cat(numDistinct("rabbbit","rabbit"),"\\n")
''',
}))

# 203 Course Schedule II
L.append((203, "Course Schedule II", "Graphs", "Medium", 102,
"Return any topological ordering of courses, or empty array if impossible.",
{
"Python": '''def findOrder(n,pre):
    from collections import defaultdict,deque
    g=defaultdict(list); ind=[0]*n
    for a,b in pre: g[b].append(a); ind[a]+=1
    q=deque(i for i in range(n) if ind[i]==0); res=[]
    while q:
        x=q.popleft(); res.append(x)
        for y in g[x]:
            ind[y]-=1
            if ind[y]==0: q.append(y)
    return res if len(res)==n else []

if __name__=="__main__":
    print(findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
''',
"JavaScript": '''function findOrder(n,pre){const g=Array.from({length:n},()=>[]);const ind=new Array(n).fill(0);for(const [a,b] of pre){g[b].push(a);ind[a]++;}const q=[];for(let i=0;i<n;i++)if(ind[i]===0)q.push(i);const res=[];while(q.length){const x=q.shift();res.push(x);for(const y of g[x])if(--ind[y]===0)q.push(y);}return res.length===n?res:[];}
console.log(findOrder(4,[[1,0],[2,0],[3,1],[3,2]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] findOrder(int n,int[][] pre){List<List<Integer>> g=new ArrayList<>();for(int i=0;i<n;i++)g.add(new ArrayList<>());int[] ind=new int[n];for(int[] p:pre){g.get(p[1]).add(p[0]);ind[p[0]]++;}Deque<Integer> q=new ArrayDeque<>();for(int i=0;i<n;i++)if(ind[i]==0)q.add(i);int[] res=new int[n];int k=0;while(!q.isEmpty()){int x=q.poll();res[k++]=x;for(int y:g.get(x))if(--ind[y]==0)q.add(y);}return k==n?res:new int[0];}
  public static void main(String[]a){System.out.println(Arrays.toString(findOrder(4,new int[][]{{1,0},{2,0},{3,1},{3,2}})));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> findOrder(int n,vector<vector<int>> pre){vector<vector<int>> g(n);vector<int> ind(n,0);for(auto& p:pre){g[p[1]].push_back(p[0]);ind[p[0]]++;}queue<int> q;for(int i=0;i<n;i++) if(ind[i]==0)q.push(i);vector<int> res;while(!q.empty()){int x=q.front();q.pop();res.push_back(x);for(int y:g[x]) if(--ind[y]==0)q.push(y);}return (int)res.size()==n?res:vector<int>{};}
int main(){auto r=findOrder(4,{{1,0},{2,0},{3,1},{3,2}});for(int x:r)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func findOrder(n int,pre [][]int) []int { g:=make([][]int,n); ind:=make([]int,n); for _,p:=range pre { g[p[1]]=append(g[p[1]],p[0]); ind[p[0]]++ }; q:=[]int{}; for i:=0;i<n;i++ { if ind[i]==0 { q=append(q,i) } }; res:=[]int{}; for len(q)>0 { x:=q[0]; q=q[1:]; res=append(res,x); for _,y:=range g[x] { ind[y]--; if ind[y]==0 { q=append(q,y) } } }; if len(res)==n { return res }; return []int{} }
func main(){ fmt.Println(findOrder(4,[][]int{{1,0},{2,0},{3,1},{3,2}})) }
''',
"R": '''findOrder <- function(n,pre){ g<-vector("list",n); ind<-rep(0,n); for(p in pre){ g[[p[2]+1]]<-c(g[[p[2]+1]],p[1]+1); ind[p[1]+1]<-ind[p[1]+1]+1 }; q<-which(ind==0); res<-c(); while(length(q)>0){ x<-q[1]; q<-q[-1]; res<-c(res,x-1); for(y in g[[x]]){ ind[y]<-ind[y]-1; if(ind[y]==0) q<-c(q,y) } }; if(length(res)==n) res else c() }
cat(findOrder(4,list(c(1,0),c(2,0),c(3,1),c(3,2))),"\\n")
''',
}))

# 204 Graph Valid Tree
L.append((204, "Graph Valid Tree", "Graphs", "Medium", 102,
"Given n nodes and edges, determine if they form a tree (connected and no cycles).",
{
"Python": '''def validTree(n,edges):
    if len(edges)!=n-1: return False
    par=list(range(n))
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for a,b in edges:
        ra,rb=find(a),find(b)
        if ra==rb: return False
        par[ra]=rb
    return True

if __name__=="__main__":
    print(validTree(5,[[0,1],[0,2],[0,3],[1,4]]))
    print(validTree(5,[[0,1],[1,2],[2,3],[1,3],[1,4]]))
''',
"JavaScript": '''function validTree(n,edges){if(edges.length!==n-1)return false;const par=Array.from({length:n},(_,i)=>i);function find(x){while(par[x]!==x){par[x]=par[par[x]];x=par[x];}return x;}for(const [a,b] of edges){const ra=find(a),rb=find(b);if(ra===rb)return false;par[ra]=rb;}return true;}
console.log(validTree(5,[[0,1],[0,2],[0,3],[1,4]]));console.log(validTree(5,[[0,1],[1,2],[2,3],[1,3],[1,4]]));
''',
"Java": '''public class __CLASS__{
  static int[] P; static int find(int x){while(P[x]!=x){P[x]=P[P[x]];x=P[x];}return x;}
  static boolean validTree(int n,int[][] e){if(e.length!=n-1)return false;P=new int[n];for(int i=0;i<n;i++)P[i]=i;for(int[] x:e){int ra=find(x[0]),rb=find(x[1]);if(ra==rb)return false;P[ra]=rb;}return true;}
  public static void main(String[]a){System.out.println(validTree(5,new int[][]{{0,1},{0,2},{0,3},{1,4}}));System.out.println(validTree(5,new int[][]{{0,1},{1,2},{2,3},{1,3},{1,4}}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> P; int find(int x){while(P[x]!=x){P[x]=P[P[x]];x=P[x];}return x;}
bool validTree(int n,vector<vector<int>> e){if((int)e.size()!=n-1)return false;P.resize(n);iota(P.begin(),P.end(),0);for(auto& x:e){int ra=find(x[0]),rb=find(x[1]);if(ra==rb)return false;P[ra]=rb;}return true;}
int main(){cout<<boolalpha<<validTree(5,{{0,1},{0,2},{0,3},{1,4}})<<"\\n"<<validTree(5,{{0,1},{1,2},{2,3},{1,3},{1,4}})<<"\\n";}
''',
"Go": '''package main
import "fmt"
var P []int
func find(x int) int { for P[x]!=x { P[x]=P[P[x]]; x=P[x] }; return x }
func validTree(n int,e [][]int) bool { if len(e)!=n-1 { return false }; P=make([]int,n); for i:=range P { P[i]=i }; for _,x:=range e { ra:=find(x[0]); rb:=find(x[1]); if ra==rb { return false }; P[ra]=rb }; return true }
func main(){ fmt.Println(validTree(5,[][]int{{0,1},{0,2},{0,3},{1,4}})); fmt.Println(validTree(5,[][]int{{0,1},{1,2},{2,3},{1,3},{1,4}})) }
''',
"R": '''validTree <- function(n,edges){ if(length(edges)!=n-1) return(FALSE); par<-0:(n-1); find<-function(x){ while(par[x+1]!=x){ par[x+1]<<-par[par[x+1]+1]; x<-par[x+1] }; x }; for(e in edges){ ra<-find(e[1]); rb<-find(e[2]); if(ra==rb) return(FALSE); par[ra+1]<<-rb }; TRUE }
cat(validTree(5,list(c(0,1),c(0,2),c(0,3),c(1,4))),"\\n")
''',
}))

# 205 Course Schedule IV
L.append((205, "Course Schedule IV", "Graphs", "Medium", 103,
"Given prerequisites, answer queries: is course u a (transitive) prerequisite of v?",
{
"Python": '''def checkIfPrerequisite(n,pre,queries):
    reach=[[False]*n for _ in range(n)]
    from collections import defaultdict
    g=defaultdict(list); ind=[0]*n
    for a,b in pre: g[a].append(b); ind[b]+=1; reach[a][b]=True
    from collections import deque
    q=deque(i for i in range(n) if ind[i]==0); order=[]
    while q:
        x=q.popleft(); order.append(x)
        for y in g[x]:
            ind[y]-=1
            if ind[y]==0: q.append(y)
    for x in order:
        for y in g[x]:
            for k in range(n):
                if reach[k][x]: reach[k][y]=True
    return [reach[u][v] for u,v in queries]

if __name__=="__main__":
    print(checkIfPrerequisite(3,[[1,2],[1,0],[2,0]],[[1,0],[1,2]]))
''',
"JavaScript": '''function checkIfPrerequisite(n,pre,queries){const r=Array.from({length:n},()=>new Array(n).fill(false));const g=Array.from({length:n},()=>[]);const ind=new Array(n).fill(0);for(const [a,b] of pre){g[a].push(b);ind[b]++;r[a][b]=true;}const q=[];for(let i=0;i<n;i++)if(ind[i]===0)q.push(i);const order=[];while(q.length){const x=q.shift();order.push(x);for(const y of g[x])if(--ind[y]===0)q.push(y);}for(const x of order)for(const y of g[x])for(let k=0;k<n;k++)if(r[k][x])r[k][y]=true;return queries.map(([u,v])=>r[u][v]);}
console.log(checkIfPrerequisite(3,[[1,2],[1,0],[2,0]],[[1,0],[1,2]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static List<Boolean> checkIfPrerequisite(int n,int[][] pre,int[][] qs){boolean[][] r=new boolean[n][n];List<List<Integer>> g=new ArrayList<>();for(int i=0;i<n;i++)g.add(new ArrayList<>());int[] ind=new int[n];for(int[] p:pre){g.get(p[0]).add(p[1]);ind[p[1]]++;r[p[0]][p[1]]=true;}Deque<Integer> q=new ArrayDeque<>();for(int i=0;i<n;i++)if(ind[i]==0)q.add(i);List<Integer> order=new ArrayList<>();while(!q.isEmpty()){int x=q.poll();order.add(x);for(int y:g.get(x))if(--ind[y]==0)q.add(y);}for(int x:order)for(int y:g.get(x))for(int k=0;k<n;k++)if(r[k][x])r[k][y]=true;List<Boolean> out=new ArrayList<>();for(int[] qq:qs)out.add(r[qq[0]][qq[1]]);return out;}
  public static void main(String[]a){System.out.println(checkIfPrerequisite(3,new int[][]{{1,2},{1,0},{2,0}},new int[][]{{1,0},{1,2}}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<bool> checkIfPrerequisite(int n,vector<vector<int>> pre,vector<vector<int>> qs){vector<vector<bool>> r(n,vector<bool>(n,false));vector<vector<int>> g(n);vector<int> ind(n,0);for(auto& p:pre){g[p[0]].push_back(p[1]);ind[p[1]]++;r[p[0]][p[1]]=true;}queue<int> q;for(int i=0;i<n;i++) if(ind[i]==0)q.push(i);vector<int> order;while(!q.empty()){int x=q.front();q.pop();order.push_back(x);for(int y:g[x]) if(--ind[y]==0)q.push(y);}for(int x:order) for(int y:g[x]) for(int k=0;k<n;k++) if(r[k][x])r[k][y]=true;vector<bool> out;for(auto& qq:qs)out.push_back(r[qq[0]][qq[1]]);return out;}
int main(){auto r=checkIfPrerequisite(3,{{1,2},{1,0},{2,0}},{{1,0},{1,2}});for(bool b:r)cout<<b<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
func checkIfPrerequisite(n int,pre,qs [][]int) []bool { r:=make([][]bool,n); for i:=range r { r[i]=make([]bool,n) }; g:=make([][]int,n); ind:=make([]int,n); for _,p:=range pre { g[p[0]]=append(g[p[0]],p[1]); ind[p[1]]++; r[p[0]][p[1]]=true }; q:=[]int{}; for i:=0;i<n;i++ { if ind[i]==0 { q=append(q,i) } }; order:=[]int{}; for len(q)>0 { x:=q[0]; q=q[1:]; order=append(order,x); for _,y:=range g[x] { ind[y]--; if ind[y]==0 { q=append(q,y) } } }; for _,x:=range order { for _,y:=range g[x] { for k:=0;k<n;k++ { if r[k][x] { r[k][y]=true } } } }; out:=[]bool{}; for _,qq:=range qs { out=append(out,r[qq[0]][qq[1]]) }; return out }
func main(){ fmt.Println(checkIfPrerequisite(3,[][]int{{1,2},{1,0},{2,0}},[][]int{{1,0},{1,2}})) }
''',
"R": '''checkIfPrerequisite <- function(n,pre,qs){ r<-matrix(FALSE,n,n); for(p in pre) r[p[1]+1,p[2]+1]<-TRUE; for(k in 1:n) for(i in 1:n) for(j in 1:n) if(r[i,k]&&r[k,j]) r[i,j]<-TRUE; sapply(qs,function(q) r[q[1]+1,q[2]+1]) }
print(checkIfPrerequisite(3,list(c(1,2),c(1,0),c(2,0)),list(c(1,0),c(1,2))))
''',
}))

# 206 Number of Connected Components in an Undirected Graph
L.append((206, "Number of Connected Components In An Undirected Graph", "Graphs", "Medium", 103,
"Given n nodes and undirected edges, return the number of connected components.",
{
"Python": '''def countComponents(n,edges):
    par=list(range(n)); cnt=n
    def find(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for a,b in edges:
        ra,rb=find(a),find(b)
        if ra!=rb: par[ra]=rb; cnt-=1
    return cnt

if __name__=="__main__":
    print(countComponents(5,[[0,1],[1,2],[3,4]]))
    print(countComponents(5,[[0,1],[1,2],[2,3],[3,4]]))
''',
"JavaScript": '''function countComponents(n,edges){const par=Array.from({length:n},(_,i)=>i);let cnt=n;function find(x){while(par[x]!==x){par[x]=par[par[x]];x=par[x];}return x;}for(const [a,b] of edges){const ra=find(a),rb=find(b);if(ra!==rb){par[ra]=rb;cnt--;}}return cnt;}
console.log(countComponents(5,[[0,1],[1,2],[3,4]]));
''',
"Java": '''public class __CLASS__{
  static int[] P; static int find(int x){while(P[x]!=x){P[x]=P[P[x]];x=P[x];}return x;}
  static int countComponents(int n,int[][] e){P=new int[n];for(int i=0;i<n;i++)P[i]=i;int cnt=n;for(int[] x:e){int ra=find(x[0]),rb=find(x[1]);if(ra!=rb){P[ra]=rb;cnt--;}}return cnt;}
  public static void main(String[]a){System.out.println(countComponents(5,new int[][]{{0,1},{1,2},{3,4}}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
vector<int> P; int find(int x){while(P[x]!=x){P[x]=P[P[x]];x=P[x];}return x;}
int countComponents(int n,vector<vector<int>> e){P.resize(n);iota(P.begin(),P.end(),0);int cnt=n;for(auto& x:e){int ra=find(x[0]),rb=find(x[1]);if(ra!=rb){P[ra]=rb;cnt--;}}return cnt;}
int main(){cout<<countComponents(5,{{0,1},{1,2},{3,4}})<<"\\n";}
''',
"Go": '''package main
import "fmt"
var P []int
func find(x int) int { for P[x]!=x { P[x]=P[P[x]]; x=P[x] }; return x }
func countComponents(n int,e [][]int) int { P=make([]int,n); for i:=range P { P[i]=i }; cnt:=n; for _,x:=range e { ra:=find(x[0]); rb:=find(x[1]); if ra!=rb { P[ra]=rb; cnt-- } }; return cnt }
func main(){ fmt.Println(countComponents(5,[][]int{{0,1},{1,2},{3,4}})) }
''',
"R": '''countComponents <- function(n,edges){ par<-0:(n-1); cnt<-n; find<-function(x){ while(par[x+1]!=x){ par[x+1]<<-par[par[x+1]+1]; x<-par[x+1] }; x }; for(e in edges){ ra<-find(e[1]); rb<-find(e[2]); if(ra!=rb){ par[ra+1]<<-rb; cnt<<-cnt-1 } }; cnt }
cat(countComponents(5,list(c(0,1),c(1,2),c(3,4))),"\\n")
''',
}))

# 207 Decode String
L.append((207, "Decode String", "Stack", "Medium", 104,
"Decode a run-length-style string like \"3[a2[c]]\" -> \"accaccacc\".",
{
"Python": '''def decodeString(s):
    st=[]; cur=""; k=0
    for ch in s:
        if ch.isdigit(): k=k*10+int(ch)
        elif ch=='[': st.append((cur,k)); cur=""; k=0
        elif ch==']':
            pre,n=st.pop(); cur=pre+cur*n
        else: cur+=ch
    return cur

if __name__=="__main__":
    print(decodeString("3[a]2[bc]"))
    print(decodeString("3[a2[c]]"))
''',
"JavaScript": '''function decodeString(s){const st=[];let cur="",k=0;for(const ch of s){if(ch>='0'&&ch<='9')k=k*10+(ch.charCodeAt(0)-48);else if(ch==='['){st.push([cur,k]);cur="";k=0;}else if(ch===']'){const [pre,n]=st.pop();cur=pre+cur.repeat(n);}else cur+=ch;}return cur;}
console.log(decodeString("3[a]2[bc]"));console.log(decodeString("3[a2[c]]"));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static String decodeString(String s){Deque<Object[]> st=new ArrayDeque<>();StringBuilder cur=new StringBuilder();int k=0;for(char ch:s.toCharArray()){if(Character.isDigit(ch))k=k*10+(ch-'0');else if(ch=='['){st.push(new Object[]{cur.toString(),k});cur=new StringBuilder();k=0;}else if(ch==']'){Object[] x=st.pop();String pre=(String)x[0];int n=(int)x[1];StringBuilder nb=new StringBuilder(pre);for(int i=0;i<n;i++)nb.append(cur);cur=nb;}else cur.append(ch);}return cur.toString();}
  public static void main(String[]a){System.out.println(decodeString("3[a]2[bc]"));System.out.println(decodeString("3[a2[c]]"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
string decodeString(string s){vector<pair<string,int>> st;string cur;int k=0;for(char ch:s){if(isdigit(ch))k=k*10+(ch-'0');else if(ch=='['){st.push_back({cur,k});cur="";k=0;}else if(ch==']'){auto [pre,n]=st.back();st.pop_back();string nb=pre;for(int i=0;i<n;i++)nb+=cur;cur=nb;}else cur+=ch;}return cur;}
int main(){cout<<decodeString("3[a]2[bc]")<<"\\n"<<decodeString("3[a2[c]]")<<"\\n";}
''',
"Go": '''package main
import ("fmt"; "strings")
func decodeString(s string) string { type fr struct{ pre string; k int }; st:=[]fr{}; cur:=""; k:=0; for _,ch:=range s { if ch>='0'&&ch<='9' { k=k*10+int(ch-'0') } else if ch=='[' { st=append(st,fr{cur,k}); cur=""; k=0 } else if ch==']' { f:=st[len(st)-1]; st=st[:len(st)-1]; cur=f.pre+strings.Repeat(cur,f.k) } else { cur+=string(ch) } }; return cur }
func main(){ fmt.Println(decodeString("3[a]2[bc]")); fmt.Println(decodeString("3[a2[c]]")) }
''',
"R": '''decodeString <- function(s){ st<-list(); cur<-""; k<-0; for(ch in strsplit(s,"")[[1]]){ if(ch %in% as.character(0:9)) k<-k*10+as.integer(ch) else if(ch=="["){ st[[length(st)+1]]<-list(pre=cur,k=k); cur<-""; k<-0 } else if(ch=="]"){ f<-st[[length(st)]]; st[[length(st)]]<-NULL; cur<-paste0(f$pre,paste(rep(cur,f$k),collapse="")) } else cur<-paste0(cur,ch) }; cur }
cat(decodeString("3[a]2[bc]"),"\\n"); cat(decodeString("3[a2[c]]"),"\\n")
''',
}))

# 208 Maximum Frequency Stack
L.append((208, "Maximum Frequency Stack", "Stack", "Hard", 104,
"Push/pop a stack returning the most-frequent element (ties: most recent).",
{
"Python": '''from collections import defaultdict
class FreqStack:
    def __init__(s): s.f=defaultdict(int); s.g=defaultdict(list); s.maxf=0
    def push(s,v): s.f[v]+=1; s.maxf=max(s.maxf,s.f[v]); s.g[s.f[v]].append(v)
    def pop(s):
        v=s.g[s.maxf].pop(); s.f[v]-=1
        if not s.g[s.maxf]: s.maxf-=1
        return v

if __name__=="__main__":
    fs=FreqStack()
    for x in [5,7,5,7,4,5]: fs.push(x)
    print([fs.pop() for _ in range(4)])
''',
"JavaScript": '''class FreqStack{constructor(){this.f=new Map();this.g=new Map();this.maxf=0;}push(v){const c=(this.f.get(v)||0)+1;this.f.set(v,c);if(c>this.maxf)this.maxf=c;if(!this.g.has(c))this.g.set(c,[]);this.g.get(c).push(v);}pop(){const arr=this.g.get(this.maxf);const v=arr.pop();this.f.set(v,this.f.get(v)-1);if(arr.length===0)this.maxf--;return v;}}
const fs=new FreqStack();[5,7,5,7,4,5].forEach(x=>fs.push(x));console.log([fs.pop(),fs.pop(),fs.pop(),fs.pop()]);
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class FreqStack{Map<Integer,Integer> f=new HashMap<>();Map<Integer,Deque<Integer>> g=new HashMap<>();int maxf=0;
    void push(int v){int c=f.getOrDefault(v,0)+1;f.put(v,c);if(c>maxf)maxf=c;g.computeIfAbsent(c,k->new ArrayDeque<>()).push(v);}
    int pop(){Deque<Integer> d=g.get(maxf);int v=d.pop();f.put(v,f.get(v)-1);if(d.isEmpty())maxf--;return v;}}
  public static void main(String[]a){FreqStack fs=new FreqStack();for(int x:new int[]{5,7,5,7,4,5})fs.push(x);List<Integer> r=new ArrayList<>();for(int i=0;i<4;i++)r.add(fs.pop());System.out.println(r);}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct FreqStack{unordered_map<int,int> f;unordered_map<int,vector<int>> g;int maxf=0;
  void push(int v){f[v]++;maxf=max(maxf,f[v]);g[f[v]].push_back(v);}
  int pop(){int v=g[maxf].back();g[maxf].pop_back();f[v]--;if(g[maxf].empty())maxf--;return v;}};
int main(){FreqStack fs;for(int x:{5,7,5,7,4,5})fs.push(x);for(int i=0;i<4;i++)cout<<fs.pop()<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
type FreqStack struct { f map[int]int; g map[int][]int; maxf int }
func New() *FreqStack { return &FreqStack{f:map[int]int{},g:map[int][]int{}} }
func (s *FreqStack) Push(v int) { s.f[v]++; if s.f[v]>s.maxf { s.maxf=s.f[v] }; s.g[s.f[v]]=append(s.g[s.f[v]],v) }
func (s *FreqStack) Pop() int { arr:=s.g[s.maxf]; v:=arr[len(arr)-1]; s.g[s.maxf]=arr[:len(arr)-1]; s.f[v]--; if len(s.g[s.maxf])==0 { s.maxf-- }; return v }
func main(){ fs:=New(); for _,x:=range []int{5,7,5,7,4,5} { fs.Push(x) }; for i:=0;i<4;i++ { fmt.Print(fs.Pop()," ") }; fmt.Println() }
''',
"R": '''FreqStack <- function(){ f<-list(); g<-list(); maxf<-0; push<-function(v){ k<-as.character(v); c<-(if(is.null(f[[k]])) 0 else f[[k]])+1; f[[k]]<<-c; if(c>maxf) maxf<<-c; ck<-as.character(c); g[[ck]]<<-c(g[[ck]],v) }; pop<-function(){ ck<-as.character(maxf); arr<-g[[ck]]; v<-arr[length(arr)]; g[[ck]]<<-arr[-length(arr)]; f[[as.character(v)]]<<-f[[as.character(v)]]-1; if(length(g[[ck]])==0) maxf<<-maxf-1; v }; list(push=push,pop=pop) }
fs<-FreqStack(); for(x in c(5,7,5,7,4,5)) fs$push(x); for(i in 1:4) cat(fs$pop()," "); cat("\\n")
''',
}))

# 209 Hand of Straights
L.append((209, "Hand of Straights", "Greedy", "Medium", 105,
"Can hand be rearranged into groups of size W of consecutive cards?",
{
"Python": '''from collections import Counter
def isNStraightHand(h,W):
    if len(h)%W: return False
    c=Counter(h)
    for x in sorted(c):
        if c[x]>0:
            cnt=c[x]
            for k in range(W):
                if c[x+k]<cnt: return False
                c[x+k]-=cnt
    return True

if __name__=="__main__":
    print(isNStraightHand([1,2,3,6,2,3,4,7,8],3))
    print(isNStraightHand([1,2,3,4,5],4))
''',
"JavaScript": '''function isNStraightHand(h,W){if(h.length%W)return false;const c=new Map();for(const x of h)c.set(x,(c.get(x)||0)+1);const keys=[...c.keys()].sort((a,b)=>a-b);for(const x of keys){const cnt=c.get(x);if(cnt>0){for(let k=0;k<W;k++){const v=c.get(x+k)||0;if(v<cnt)return false;c.set(x+k,v-cnt);}}}return true;}
console.log(isNStraightHand([1,2,3,6,2,3,4,7,8],3));console.log(isNStraightHand([1,2,3,4,5],4));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static boolean isNStraightHand(int[] h,int W){if(h.length%W!=0)return false;TreeMap<Integer,Integer> c=new TreeMap<>();for(int x:h)c.merge(x,1,Integer::sum);for(int x:new ArrayList<>(c.keySet())){int cnt=c.getOrDefault(x,0);if(cnt>0){for(int k=0;k<W;k++){int v=c.getOrDefault(x+k,0);if(v<cnt)return false;if(v==cnt)c.remove(x+k);else c.put(x+k,v-cnt);}}}return true;}
  public static void main(String[]a){System.out.println(isNStraightHand(new int[]{1,2,3,6,2,3,4,7,8},3));System.out.println(isNStraightHand(new int[]{1,2,3,4,5},4));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool isNStraightHand(vector<int> h,int W){if((int)h.size()%W)return false;map<int,int> c;for(int x:h)c[x]++;for(auto& p:c){if(p.second>0){int cnt=p.second;for(int k=0;k<W;k++){if(c[p.first+k]<cnt)return false;c[p.first+k]-=cnt;}}}return true;}
int main(){cout<<boolalpha<<isNStraightHand({1,2,3,6,2,3,4,7,8},3)<<"\\n"<<isNStraightHand({1,2,3,4,5},4)<<"\\n";}
''',
"Go": '''package main
import ("fmt"; "sort")
func isNStraightHand(h []int,W int) bool { if len(h)%W!=0 { return false }; c:=map[int]int{}; for _,x:=range h { c[x]++ }; keys:=[]int{}; for k:=range c { keys=append(keys,k) }; sort.Ints(keys); for _,x:=range keys { cnt:=c[x]; if cnt>0 { for k:=0;k<W;k++ { if c[x+k]<cnt { return false }; c[x+k]-=cnt } } }; return true }
func main(){ fmt.Println(isNStraightHand([]int{1,2,3,6,2,3,4,7,8},3)); fmt.Println(isNStraightHand([]int{1,2,3,4,5},4)) }
''',
"R": '''isNStraightHand <- function(h,W){ if(length(h)%%W!=0) return(FALSE); c<-table(h); keys<-as.integer(names(c)); names(c)<-keys; ord<-order(keys); for(i in ord){ x<-keys[i]; cnt<-c[as.character(x)]; if(cnt>0){ for(k in 0:(W-1)){ key<-as.character(x+k); v<-if(is.na(c[key])) 0 else c[key]; if(v<cnt) return(FALSE); c[key]<<-v-cnt } } }; TRUE }
cat(isNStraightHand(c(1,2,3,6,2,3,4,7,8),3),"\\n")
''',
}))

# 210 Dota2 Senate
L.append((210, "Dota2 Senate", "Greedy", "Medium", 105,
"Senate string of 'R'/'D'. Each round senators ban earliest opponent. Return winning party.",
{
"Python": '''from collections import deque
def predictPartyVictory(s):
    R=deque(); D=deque(); n=len(s)
    for i,ch in enumerate(s): (R if ch=='R' else D).append(i)
    while R and D:
        r=R.popleft(); d=D.popleft()
        if r<d: R.append(r+n)
        else: D.append(d+n)
    return "Radiant" if R else "Dire"

if __name__=="__main__":
    print(predictPartyVictory("RD"))
    print(predictPartyVictory("RDD"))
''',
"JavaScript": '''function predictPartyVictory(s){const R=[],D=[];const n=s.length;for(let i=0;i<n;i++)(s[i]==='R'?R:D).push(i);while(R.length&&D.length){const r=R.shift(),d=D.shift();if(r<d)R.push(r+n);else D.push(d+n);}return R.length?"Radiant":"Dire";}
console.log(predictPartyVictory("RD"));console.log(predictPartyVictory("RDD"));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static String predictPartyVictory(String s){Deque<Integer> R=new ArrayDeque<>(),D=new ArrayDeque<>();int n=s.length();for(int i=0;i<n;i++)(s.charAt(i)=='R'?R:D).add(i);while(!R.isEmpty()&&!D.isEmpty()){int r=R.poll(),d=D.poll();if(r<d)R.add(r+n);else D.add(d+n);}return R.isEmpty()?"Dire":"Radiant";}
  public static void main(String[]a){System.out.println(predictPartyVictory("RD"));System.out.println(predictPartyVictory("RDD"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
string predictPartyVictory(string s){queue<int> R,D;int n=s.size();for(int i=0;i<n;i++) (s[i]=='R'?R:D).push(i);while(!R.empty()&&!D.empty()){int r=R.front();R.pop();int d=D.front();D.pop();if(r<d)R.push(r+n);else D.push(d+n);}return R.empty()?"Dire":"Radiant";}
int main(){cout<<predictPartyVictory("RD")<<"\\n"<<predictPartyVictory("RDD")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func predictPartyVictory(s string) string { R,D:=[]int{},[]int{}; n:=len(s); for i:=0;i<n;i++ { if s[i]=='R' { R=append(R,i) } else { D=append(D,i) } }; for len(R)>0 && len(D)>0 { r:=R[0]; R=R[1:]; d:=D[0]; D=D[1:]; if r<d { R=append(R,r+n) } else { D=append(D,d+n) } }; if len(R)>0 { return "Radiant" }; return "Dire" }
func main(){ fmt.Println(predictPartyVictory("RD")); fmt.Println(predictPartyVictory("RDD")) }
''',
"R": '''predictPartyVictory <- function(s){ ch<-strsplit(s,"")[[1]]; n<-length(ch); R<-which(ch=='R')-1; D<-which(ch=='D')-1; while(length(R)>0 && length(D)>0){ r<-R[1]; R<-R[-1]; d<-D[1]; D<-D[-1]; if(r<d) R<-c(R,r+n) else D<-c(D,d+n) }; if(length(R)>0) "Radiant" else "Dire" }
cat(predictPartyVictory("RD"),"\\n"); cat(predictPartyVictory("RDD"),"\\n")
''',
}))

write_lessons(L)
