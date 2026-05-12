"""Batch 8: lessons 161-185."""
from _lesson_writer import write_lessons

L = []

# 161 Pow x n
L.append((161, "Pow x n", "Math and Geometry", "Medium", 81,
"Implement pow(x, n) — x raised to the n-th power.",
{
"Python": '''def myPow(x,n):
    if n<0: x,n=1/x,-n
    r=1.0
    while n:
        if n&1: r*=x
        x*=x; n>>=1
    return r

if __name__=="__main__":
    print(round(myPow(2.0,10),5))
    print(round(myPow(2.1,3),5))
    print(round(myPow(2.0,-2),5))
''',
"JavaScript": '''function myPow(x,n){if(n<0){x=1/x;n=-n;}let r=1.0;while(n){if(n&1)r*=x;x*=x;n=Math.floor(n/2);}return r;}
console.log(myPow(2,10));console.log(myPow(2,-2));
''',
"Java": '''public class __CLASS__{
  static double myPow(double x,long n){if(n<0){x=1/x;n=-n;}double r=1.0;while(n>0){if((n&1)==1)r*=x;x*=x;n>>=1;}return r;}
  public static void main(String[]a){System.out.println(myPow(2.0,10));System.out.println(myPow(2.0,-2));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
double myPow(double x,long long n){if(n<0){x=1/x;n=-n;}double r=1.0;while(n){if(n&1)r*=x;x*=x;n>>=1;}return r;}
int main(){cout<<myPow(2.0,10)<<"\\n"<<myPow(2.0,-2)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func myPow(x float64,n int) float64 { if n<0 { x=1/x; n=-n }; r:=1.0; for n>0 { if n&1==1 { r*=x }; x*=x; n>>=1 }; return r }
func main(){ fmt.Println(myPow(2,10)); fmt.Println(myPow(2,-2)) }
''',
"R": '''myPow <- function(x,n){ if(n<0){ x<-1/x; n<--n }; r<-1.0; while(n>0){ if(bitwAnd(n,1)==1) r<-r*x; x<-x*x; n<-bitwShiftR(n,1) }; r }
cat(myPow(2,10),"\\n"); cat(myPow(2,-2),"\\n")
''',
}))

# 162 Multiply Strings
L.append((162, "Multiply Strings", "Math and Geometry", "Medium", 81,
"Given two non-negative integers as strings, return their product as a string. Do not use built-in big-int conversion.",
{
"Python": '''def mul(a,b):
    if a=="0" or b=="0": return "0"
    n,m=len(a),len(b); r=[0]*(n+m)
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            p=int(a[i])*int(b[j])
            s=p+r[i+j+1]
            r[i+j+1]=s%10
            r[i+j]+=s//10
    s="".join(map(str,r)).lstrip("0")
    return s or "0"

if __name__=="__main__":
    print(mul("123","456"))
''',
"JavaScript": '''function mul(a,b){if(a==="0"||b==="0")return "0";const n=a.length,m=b.length,r=new Array(n+m).fill(0);for(let i=n-1;i>=0;i--)for(let j=m-1;j>=0;j--){const p=(a.charCodeAt(i)-48)*(b.charCodeAt(j)-48);const s=p+r[i+j+1];r[i+j+1]=s%10;r[i+j]+=Math.floor(s/10);}return r.join("").replace(/^0+/,"")||"0";}
console.log(mul("123","456"));
''',
"Java": '''public class __CLASS__{
  static String mul(String a,String b){if(a.equals("0")||b.equals("0"))return "0";int n=a.length(),m=b.length();int[] r=new int[n+m];for(int i=n-1;i>=0;i--)for(int j=m-1;j>=0;j--){int p=(a.charAt(i)-'0')*(b.charAt(j)-'0');int s=p+r[i+j+1];r[i+j+1]=s%10;r[i+j]+=s/10;}StringBuilder sb=new StringBuilder();for(int v:r)sb.append(v);while(sb.length()>1 && sb.charAt(0)=='0')sb.deleteCharAt(0);return sb.toString();}
  public static void main(String[]a){System.out.println(mul("123","456"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
string mul(string a,string b){if(a=="0"||b=="0")return "0";int n=a.size(),m=b.size();vector<int> r(n+m,0);for(int i=n-1;i>=0;i--)for(int j=m-1;j>=0;j--){int p=(a[i]-'0')*(b[j]-'0');int s=p+r[i+j+1];r[i+j+1]=s%10;r[i+j]+=s/10;}string out;for(int v:r)out+=char('0'+v);size_t k=out.find_first_not_of('0');return k==string::npos?"0":out.substr(k);}
int main(){cout<<mul("123","456")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func mul(a,b string) string { if a=="0"||b=="0" { return "0" }; n,m:=len(a),len(b); r:=make([]int,n+m); for i:=n-1;i>=0;i-- { for j:=m-1;j>=0;j-- { p:=int(a[i]-'0')*int(b[j]-'0'); s:=p+r[i+j+1]; r[i+j+1]=s%10; r[i+j]+=s/10 } }; out:=""; for _,v:=range r { out+=string(rune('0'+v)) }; for len(out)>1 && out[0]=='0' { out=out[1:] }; return out }
func main(){ fmt.Println(mul("123","456")) }
''',
"R": '''mul <- function(a,b){ if(a=="0"||b=="0") return("0"); n<-nchar(a); m<-nchar(b); r<-rep(0,n+m); ca<-as.integer(charToRaw(a))-48; cb<-as.integer(charToRaw(b))-48; for(i in n:1) for(j in m:1){ p<-ca[i]*cb[j]; s<-p+r[i+j]; r[i+j]<-s%%10; r[i+j-1]<-r[i+j-1]+s%/%10 }; out<-paste(r,collapse=""); sub("^0+","",out) }
cat(mul("123","456"),"\\n")
''',
}))

# 163 Car Fleet
L.append((163, "Car Fleet", "Stack", "Medium", 82,
"Cars at positions head to target with given speeds. Cars cannot pass; slower car ahead caps faster car behind. Return number of fleets that arrive.",
{
"Python": '''def carFleet(target,pos,sp):
    cars=sorted(zip(pos,sp),reverse=True)
    fleets=0; lastT=0.0
    for p,s in cars:
        t=(target-p)/s
        if t>lastT:
            fleets+=1; lastT=t
    return fleets

if __name__=="__main__":
    print(carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
''',
"JavaScript": '''function carFleet(target,pos,sp){const cars=pos.map((p,i)=>[p,sp[i]]).sort((a,b)=>b[0]-a[0]);let f=0,lt=0;for(const [p,s] of cars){const t=(target-p)/s;if(t>lt){f++;lt=t;}}return f;}
console.log(carFleet(12,[10,8,0,5,3],[2,4,1,1,3]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int carFleet(int target,int[] pos,int[] sp){int n=pos.length;Integer[] idx=new Integer[n];for(int i=0;i<n;i++)idx[i]=i;Arrays.sort(idx,(a,b)->pos[b]-pos[a]);int f=0;double lt=0;for(int i:idx){double t=(double)(target-pos[i])/sp[i];if(t>lt){f++;lt=t;}}return f;}
  public static void main(String[]a){System.out.println(carFleet(12,new int[]{10,8,0,5,3},new int[]{2,4,1,1,3}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int carFleet(int target,vector<int> pos,vector<int> sp){int n=pos.size();vector<pair<int,int>> c;for(int i=0;i<n;i++)c.push_back({pos[i],sp[i]});sort(c.begin(),c.end(),greater<>());int f=0;double lt=0;for(auto& p:c){double t=(double)(target-p.first)/p.second;if(t>lt){f++;lt=t;}}return f;}
int main(){cout<<carFleet(12,{10,8,0,5,3},{2,4,1,1,3})<<"\\n";}
''',
"Go": '''package main
import ("fmt"; "sort")
func carFleet(target int,pos,sp []int) int { n:=len(pos); idx:=make([]int,n); for i:=range idx { idx[i]=i }; sort.Slice(idx,func(i,j int) bool { return pos[idx[i]]>pos[idx[j]] }); f:=0; lt:=0.0; for _,i:=range idx { t:=float64(target-pos[i])/float64(sp[i]); if t>lt { f++; lt=t } }; return f }
func main(){ fmt.Println(carFleet(12,[]int{10,8,0,5,3},[]int{2,4,1,1,3})) }
''',
"R": '''carFleet <- function(target,pos,sp){ o<-order(-pos); pos<-pos[o]; sp<-sp[o]; f<-0; lt<-0; for(i in seq_along(pos)){ t<-(target-pos[i])/sp[i]; if(t>lt){ f<-f+1; lt<-t } }; f }
cat(carFleet(12,c(10,8,0,5,3),c(2,4,1,1,3)),"\\n")
''',
}))

# 164 Simplify Path
L.append((164, "Simplify Path", "Stack", "Medium", 82,
"Given a Unix-style absolute path, return the simplified canonical path.",
{
"Python": '''def simplify(p):
    st=[]
    for part in p.split('/'):
        if part=='' or part=='.': continue
        if part=='..':
            if st: st.pop()
        else: st.append(part)
    return '/'+'/'.join(st)

if __name__=="__main__":
    print(simplify("/a/./b/../../c/"))
    print(simplify("/home//foo/"))
''',
"JavaScript": '''function simplify(p){const st=[];for(const part of p.split('/')){if(part===''||part==='.')continue;if(part==='..'){if(st.length)st.pop();}else st.push(part);}return '/'+st.join('/');}
console.log(simplify("/a/./b/../../c/"));console.log(simplify("/home//foo/"));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static String simplify(String p){Deque<String> st=new ArrayDeque<>();for(String part:p.split("/")){if(part.isEmpty()||part.equals("."))continue;if(part.equals("..")){if(!st.isEmpty())st.pop();}else st.push(part);}StringBuilder sb=new StringBuilder();Iterator<String> it=st.descendingIterator();while(it.hasNext()){sb.append('/').append(it.next());}return sb.length()==0?"/":sb.toString();}
  public static void main(String[]a){System.out.println(simplify("/a/./b/../../c/"));System.out.println(simplify("/home//foo/"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
string simplify(string p){vector<string> st;string cur;stringstream ss(p);string part;while(getline(ss,part,'/')){if(part==""||part==".")continue;if(part==".."){if(!st.empty())st.pop_back();}else st.push_back(part);}string out;for(auto& s:st) out+="/"+s;return out.empty()?"/":out;}
int main(){cout<<simplify("/a/./b/../../c/")<<"\\n"<<simplify("/home//foo/")<<"\\n";}
''',
"Go": '''package main
import ("fmt"; "strings")
func simplify(p string) string { st:=[]string{}; for _,part:=range strings.Split(p,"/") { if part==""||part=="." { continue }; if part==".." { if len(st)>0 { st=st[:len(st)-1] } } else { st=append(st,part) } }; return "/"+strings.Join(st,"/") }
func main(){ fmt.Println(simplify("/a/./b/../../c/")); fmt.Println(simplify("/home//foo/")) }
''',
"R": '''simplify <- function(p){ parts<-strsplit(p,"/")[[1]]; st<-c(); for(part in parts){ if(part==""||part==".") next; if(part==".."){ if(length(st)>0) st<-st[-length(st)] } else st<-c(st,part) }; paste0("/",paste(st,collapse="/")) }
cat(simplify("/a/./b/../../c/"),"\\n")
''',
}))

# 165 Jump Game
L.append((165, "Jump Game", "Greedy", "Medium", 83,
"Each element is max jump length from that position. Return true iff you can reach the last index from index 0.",
{
"Python": '''def canJump(a):
    r=0
    for i,v in enumerate(a):
        if i>r: return False
        r=max(r,i+v)
    return True

if __name__=="__main__":
    print(canJump([2,3,1,1,4]))
    print(canJump([3,2,1,0,4]))
''',
"JavaScript": '''function canJump(a){let r=0;for(let i=0;i<a.length;i++){if(i>r)return false;r=Math.max(r,i+a[i]);}return true;}
console.log(canJump([2,3,1,1,4]));console.log(canJump([3,2,1,0,4]));
''',
"Java": '''public class __CLASS__{
  static boolean canJump(int[] a){int r=0;for(int i=0;i<a.length;i++){if(i>r)return false;r=Math.max(r,i+a[i]);}return true;}
  public static void main(String[]x){System.out.println(canJump(new int[]{2,3,1,1,4}));System.out.println(canJump(new int[]{3,2,1,0,4}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool canJump(vector<int> a){int r=0;for(int i=0;i<(int)a.size();i++){if(i>r)return false;r=max(r,i+a[i]);}return true;}
int main(){cout<<boolalpha<<canJump({2,3,1,1,4})<<"\\n"<<canJump({3,2,1,0,4})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func canJump(a []int) bool { r:=0; for i,v:=range a { if i>r { return false }; if i+v>r { r=i+v } }; return true }
func main(){ fmt.Println(canJump([]int{2,3,1,1,4})); fmt.Println(canJump([]int{3,2,1,0,4})) }
''',
"R": '''canJump <- function(a){ r<-0; for(i in seq_along(a)){ if((i-1)>r) return(FALSE); r<-max(r,(i-1)+a[i]) }; TRUE }
cat(canJump(c(2,3,1,1,4)),"\\n"); cat(canJump(c(3,2,1,0,4)),"\\n")
''',
}))

# 166 Jump Game II
L.append((166, "Jump Game II", "Greedy", "Medium", 83,
"Return the minimum number of jumps to reach the last index. Assume reachable.",
{
"Python": '''def jump(a):
    j=0; cur=0; far=0
    for i in range(len(a)-1):
        far=max(far,i+a[i])
        if i==cur:
            j+=1; cur=far
    return j

if __name__=="__main__":
    print(jump([2,3,1,1,4]))
    print(jump([2,3,0,1,4]))
''',
"JavaScript": '''function jump(a){let j=0,cur=0,far=0;for(let i=0;i<a.length-1;i++){far=Math.max(far,i+a[i]);if(i===cur){j++;cur=far;}}return j;}
console.log(jump([2,3,1,1,4]));console.log(jump([2,3,0,1,4]));
''',
"Java": '''public class __CLASS__{
  static int jump(int[] a){int j=0,cur=0,far=0;for(int i=0;i<a.length-1;i++){far=Math.max(far,i+a[i]);if(i==cur){j++;cur=far;}}return j;}
  public static void main(String[]x){System.out.println(jump(new int[]{2,3,1,1,4}));System.out.println(jump(new int[]{2,3,0,1,4}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int jump(vector<int> a){int j=0,cur=0,far=0;for(int i=0;i<(int)a.size()-1;i++){far=max(far,i+a[i]);if(i==cur){j++;cur=far;}}return j;}
int main(){cout<<jump({2,3,1,1,4})<<"\\n"<<jump({2,3,0,1,4})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func jump(a []int) int { j,cur,far:=0,0,0; for i:=0;i<len(a)-1;i++ { if i+a[i]>far { far=i+a[i] }; if i==cur { j++; cur=far } }; return j }
func main(){ fmt.Println(jump([]int{2,3,1,1,4})); fmt.Println(jump([]int{2,3,0,1,4})) }
''',
"R": '''jump <- function(a){ j<-0; cur<-0; far<-0; n<-length(a); for(i in 1:(n-1)){ far<-max(far,(i-1)+a[i]); if((i-1)==cur){ j<-j+1; cur<-far } }; j }
cat(jump(c(2,3,1,1,4)),"\\n"); cat(jump(c(2,3,0,1,4)),"\\n")
''',
}))

# 167 Coin Change
L.append((167, "Coin Change", "1-D Dynamic Programming", "Medium", 84,
"Fewest coins needed to make up amount; coins are unlimited. Return -1 if impossible.",
{
"Python": '''def coinChange(coins,amt):
    INF=float('inf'); dp=[0]+[INF]*amt
    for a in range(1,amt+1):
        for c in coins:
            if c<=a: dp[a]=min(dp[a],dp[a-c]+1)
    return -1 if dp[amt]==INF else dp[amt]

if __name__=="__main__":
    print(coinChange([1,2,5],11))
    print(coinChange([2],3))
''',
"JavaScript": '''function coinChange(coins,amt){const INF=1e9;const dp=new Array(amt+1).fill(INF);dp[0]=0;for(let a=1;a<=amt;a++)for(const c of coins)if(c<=a)dp[a]=Math.min(dp[a],dp[a-c]+1);return dp[amt]===INF?-1:dp[amt];}
console.log(coinChange([1,2,5],11));console.log(coinChange([2],3));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int coinChange(int[] coins,int amt){int INF=Integer.MAX_VALUE/2;int[] dp=new int[amt+1];Arrays.fill(dp,INF);dp[0]=0;for(int a=1;a<=amt;a++)for(int c:coins)if(c<=a)dp[a]=Math.min(dp[a],dp[a-c]+1);return dp[amt]>=INF?-1:dp[amt];}
  public static void main(String[]a){System.out.println(coinChange(new int[]{1,2,5},11));System.out.println(coinChange(new int[]{2},3));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int coinChange(vector<int> coins,int amt){int INF=1e9;vector<int> dp(amt+1,INF);dp[0]=0;for(int a=1;a<=amt;a++)for(int c:coins) if(c<=a) dp[a]=min(dp[a],dp[a-c]+1);return dp[amt]>=INF?-1:dp[amt];}
int main(){cout<<coinChange({1,2,5},11)<<"\\n"<<coinChange({2},3)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func coinChange(coins []int,amt int) int { INF:=1<<30; dp:=make([]int,amt+1); for i:=range dp { dp[i]=INF }; dp[0]=0; for a:=1;a<=amt;a++ { for _,c:=range coins { if c<=a && dp[a-c]+1<dp[a] { dp[a]=dp[a-c]+1 } } }; if dp[amt]>=INF { return -1 }; return dp[amt] }
func main(){ fmt.Println(coinChange([]int{1,2,5},11)); fmt.Println(coinChange([]int{2},3)) }
''',
"R": '''coinChange <- function(coins,amt){ INF<-1e9; dp<-rep(INF,amt+1); dp[1]<-0; if(amt>=1) for(a in 1:amt){ for(c in coins) if(c<=a) dp[a+1]<-min(dp[a+1],dp[a-c+1]+1) }; if(dp[amt+1]>=INF) -1 else dp[amt+1] }
cat(coinChange(c(1,2,5),11),"\\n"); cat(coinChange(c(2),3),"\\n")
''',
}))

# 168 Maximum Product Subarray
L.append((168, "Maximum Product Subarray", "1-D Dynamic Programming", "Medium", 84,
"Find a contiguous subarray with the largest product.",
{
"Python": '''def maxProduct(a):
    mx=mn=res=a[0]
    for v in a[1:]:
        if v<0: mx,mn=mn,mx
        mx=max(v,mx*v); mn=min(v,mn*v)
        res=max(res,mx)
    return res

if __name__=="__main__":
    print(maxProduct([2,3,-2,4]))
    print(maxProduct([-2,0,-1]))
''',
"JavaScript": '''function maxProduct(a){let mx=a[0],mn=a[0],res=a[0];for(let i=1;i<a.length;i++){const v=a[i];if(v<0){[mx,mn]=[mn,mx];}mx=Math.max(v,mx*v);mn=Math.min(v,mn*v);res=Math.max(res,mx);}return res;}
console.log(maxProduct([2,3,-2,4]));console.log(maxProduct([-2,0,-1]));
''',
"Java": '''public class __CLASS__{
  static int maxProduct(int[] a){int mx=a[0],mn=a[0],res=a[0];for(int i=1;i<a.length;i++){int v=a[i];if(v<0){int t=mx;mx=mn;mn=t;}mx=Math.max(v,mx*v);mn=Math.min(v,mn*v);res=Math.max(res,mx);}return res;}
  public static void main(String[]x){System.out.println(maxProduct(new int[]{2,3,-2,4}));System.out.println(maxProduct(new int[]{-2,0,-1}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int maxProduct(vector<int> a){int mx=a[0],mn=a[0],res=a[0];for(int i=1;i<(int)a.size();i++){int v=a[i];if(v<0)swap(mx,mn);mx=max(v,mx*v);mn=min(v,mn*v);res=max(res,mx);}return res;}
int main(){cout<<maxProduct({2,3,-2,4})<<"\\n"<<maxProduct({-2,0,-1})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func maxProduct(a []int) int { mx,mn,res:=a[0],a[0],a[0]; for i:=1;i<len(a);i++ { v:=a[i]; if v<0 { mx,mn=mn,mx }; if v>mx*v { mx=v } else { mx=mx*v }; if v<mn*v { mn=v } else { mn=mn*v }; if mx>res { res=mx } }; return res }
func main(){ fmt.Println(maxProduct([]int{2,3,-2,4})); fmt.Println(maxProduct([]int{-2,0,-1})) }
''',
"R": '''maxProduct <- function(a){ mx<-a[1]; mn<-a[1]; res<-a[1]; if(length(a)>=2) for(i in 2:length(a)){ v<-a[i]; if(v<0){ t<-mx; mx<-mn; mn<-t }; mx<-max(v,mx*v); mn<-min(v,mn*v); res<-max(res,mx) }; res }
cat(maxProduct(c(2,3,-2,4)),"\\n")
''',
}))

# 169 Coin Change II
L.append((169, "Coin Change II", "2-D Dynamic Programming", "Medium", 85,
"Number of distinct combinations of coins (unlimited) summing to amount.",
{
"Python": '''def change(amt,coins):
    dp=[0]*(amt+1); dp[0]=1
    for c in coins:
        for a in range(c,amt+1):
            dp[a]+=dp[a-c]
    return dp[amt]

if __name__=="__main__":
    print(change(5,[1,2,5]))
    print(change(3,[2]))
''',
"JavaScript": '''function change(amt,coins){const dp=new Array(amt+1).fill(0);dp[0]=1;for(const c of coins)for(let a=c;a<=amt;a++)dp[a]+=dp[a-c];return dp[amt];}
console.log(change(5,[1,2,5]));console.log(change(3,[2]));
''',
"Java": '''public class __CLASS__{
  static int change(int amt,int[] coins){int[] dp=new int[amt+1];dp[0]=1;for(int c:coins)for(int a=c;a<=amt;a++)dp[a]+=dp[a-c];return dp[amt];}
  public static void main(String[]a){System.out.println(change(5,new int[]{1,2,5}));System.out.println(change(3,new int[]{2}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int change(int amt,vector<int> coins){vector<long long> dp(amt+1,0);dp[0]=1;for(int c:coins) for(int a=c;a<=amt;a++) dp[a]+=dp[a-c];return (int)dp[amt];}
int main(){cout<<change(5,{1,2,5})<<"\\n"<<change(3,{2})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func change(amt int,coins []int) int { dp:=make([]int,amt+1); dp[0]=1; for _,c:=range coins { for a:=c; a<=amt; a++ { dp[a]+=dp[a-c] } }; return dp[amt] }
func main(){ fmt.Println(change(5,[]int{1,2,5})); fmt.Println(change(3,[]int{2})) }
''',
"R": '''change <- function(amt,coins){ dp<-rep(0,amt+1); dp[1]<-1; for(c in coins) if(c<=amt) for(a in c:amt) dp[a+1]<-dp[a+1]+dp[a-c+1]; dp[amt+1] }
cat(change(5,c(1,2,5)),"\\n"); cat(change(3,c(2)),"\\n")
''',
}))

# 170 Target Sum
L.append((170, "Target Sum", "2-D Dynamic Programming", "Medium", 85,
"Assign + or - to each number so the sum equals target. Return number of ways.",
{
"Python": '''def findTargetSumWays(nums,target):
    from collections import defaultdict
    dp={0:1}
    for n in nums:
        nd=defaultdict(int)
        for s,c in dp.items():
            nd[s+n]+=c; nd[s-n]+=c
        dp=nd
    return dp.get(target,0)

if __name__=="__main__":
    print(findTargetSumWays([1,1,1,1,1],3))
''',
"JavaScript": '''function findTargetSumWays(nums,target){let dp=new Map([[0,1]]);for(const n of nums){const nd=new Map();for(const [s,c] of dp){nd.set(s+n,(nd.get(s+n)||0)+c);nd.set(s-n,(nd.get(s-n)||0)+c);}dp=nd;}return dp.get(target)||0;}
console.log(findTargetSumWays([1,1,1,1,1],3));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int findTargetSumWays(int[] nums,int target){Map<Integer,Integer> dp=new HashMap<>();dp.put(0,1);for(int n:nums){Map<Integer,Integer> nd=new HashMap<>();for(var e:dp.entrySet()){nd.merge(e.getKey()+n,e.getValue(),Integer::sum);nd.merge(e.getKey()-n,e.getValue(),Integer::sum);}dp=nd;}return dp.getOrDefault(target,0);}
  public static void main(String[]a){System.out.println(findTargetSumWays(new int[]{1,1,1,1,1},3));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int findTargetSumWays(vector<int> nums,int target){unordered_map<int,int> dp;dp[0]=1;for(int n:nums){unordered_map<int,int> nd;for(auto& p:dp){nd[p.first+n]+=p.second;nd[p.first-n]+=p.second;}dp=nd;}return dp.count(target)?dp[target]:0;}
int main(){cout<<findTargetSumWays({1,1,1,1,1},3)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func findTargetSumWays(nums []int,target int) int { dp:=map[int]int{0:1}; for _,n:=range nums { nd:=map[int]int{}; for s,c:=range dp { nd[s+n]+=c; nd[s-n]+=c }; dp=nd }; return dp[target] }
func main(){ fmt.Println(findTargetSumWays([]int{1,1,1,1,1},3)) }
''',
"R": '''findTargetSumWays <- function(nums,target){ dp<-list(); dp[[as.character(0)]]<-1; for(n in nums){ nd<-list(); for(k in names(dp)){ s<-as.integer(k); v<-dp[[k]]; ka<-as.character(s+n); kb<-as.character(s-n); nd[[ka]]<-(if(is.null(nd[[ka]])) 0 else nd[[ka]])+v; nd[[kb]]<-(if(is.null(nd[[kb]])) 0 else nd[[kb]])+v }; dp<-nd }; v<-dp[[as.character(target)]]; if(is.null(v)) 0 else v }
cat(findTargetSumWays(c(1,1,1,1,1),3),"\\n")
''',
}))

# 171 Partition to K Equal Sum Subsets
L.append((171, "Partition to K Equal Sum Subsets", "Backtracking", "Medium", 86,
"Determine if nums can be partitioned into k subsets with equal sum.",
{
"Python": '''def canPartitionKSubsets(nums,k):
    s=sum(nums)
    if s%k: return False
    target=s//k; nums.sort(reverse=True)
    if nums[0]>target: return False
    buckets=[0]*k
    def bt(i):
        if i==len(nums): return True
        for j in range(k):
            if buckets[j]+nums[i]<=target:
                buckets[j]+=nums[i]
                if bt(i+1): return True
                buckets[j]-=nums[i]
            if buckets[j]==0: break
        return False
    return bt(0)

if __name__=="__main__":
    print(canPartitionKSubsets([4,3,2,3,5,2,1],4))
''',
"JavaScript": '''function canPartitionKSubsets(nums,k){const s=nums.reduce((a,b)=>a+b,0);if(s%k)return false;const t=s/k;nums.sort((a,b)=>b-a);if(nums[0]>t)return false;const b=new Array(k).fill(0);function bt(i){if(i===nums.length)return true;for(let j=0;j<k;j++){if(b[j]+nums[i]<=t){b[j]+=nums[i];if(bt(i+1))return true;b[j]-=nums[i];}if(b[j]===0)break;}return false;}return bt(0);}
console.log(canPartitionKSubsets([4,3,2,3,5,2,1],4));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int[] b; static int t; static int K; static int[] N;
  static boolean bt(int i){if(i==N.length)return true;for(int j=0;j<K;j++){if(b[j]+N[i]<=t){b[j]+=N[i];if(bt(i+1))return true;b[j]-=N[i];}if(b[j]==0)break;}return false;}
  static boolean canPartitionKSubsets(int[] nums,int k){int s=0;for(int v:nums)s+=v;if(s%k!=0)return false;t=s/k;Arrays.sort(nums);for(int i=0,j=nums.length-1;i<j;i++,j--){int x=nums[i];nums[i]=nums[j];nums[j]=x;}if(nums[0]>t)return false;b=new int[k];K=k;N=nums;return bt(0);}
  public static void main(String[]a){System.out.println(canPartitionKSubsets(new int[]{4,3,2,3,5,2,1},4));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int t,K; vector<int> N,B;
bool bt(int i){if(i==(int)N.size())return true;for(int j=0;j<K;j++){if(B[j]+N[i]<=t){B[j]+=N[i];if(bt(i+1))return true;B[j]-=N[i];}if(B[j]==0)break;}return false;}
bool canPartitionKSubsets(vector<int> nums,int k){int s=0;for(int v:nums)s+=v;if(s%k)return false;t=s/k;sort(nums.begin(),nums.end(),greater<>());if(nums[0]>t)return false;K=k;N=nums;B.assign(k,0);return bt(0);}
int main(){cout<<boolalpha<<canPartitionKSubsets({4,3,2,3,5,2,1},4)<<"\\n";}
''',
"Go": '''package main
import ("fmt"; "sort")
var (T,K int; N,B []int)
func bt(i int) bool { if i==len(N) { return true }; for j:=0;j<K;j++ { if B[j]+N[i]<=T { B[j]+=N[i]; if bt(i+1) { return true }; B[j]-=N[i] }; if B[j]==0 { break } }; return false }
func canPartitionKSubsets(nums []int,k int) bool { s:=0; for _,v:=range nums { s+=v }; if s%k!=0 { return false }; T=s/k; sort.Sort(sort.Reverse(sort.IntSlice(nums))); if nums[0]>T { return false }; K=k; N=nums; B=make([]int,k); return bt(0) }
func main(){ fmt.Println(canPartitionKSubsets([]int{4,3,2,3,5,2,1},4)) }
''',
"R": '''canPartitionKSubsets <- function(nums,k){ s<-sum(nums); if(s%%k!=0) return(FALSE); t<-s/k; nums<-sort(nums,decreasing=TRUE); if(nums[1]>t) return(FALSE); b<-rep(0,k); bt<-function(i){ if(i>length(nums)) return(TRUE); for(j in 1:k){ if(b[j]+nums[i]<=t){ b[j]<<-b[j]+nums[i]; if(bt(i+1)) return(TRUE); b[j]<<-b[j]-nums[i] }; if(b[j]==0) break }; FALSE }; bt(1) }
cat(canPartitionKSubsets(c(4,3,2,3,5,2,1),4),"\\n")
''',
}))

# 172 N Queens
L.append((172, "N Queens", "Backtracking", "Hard", 86,
"Place n queens on n×n board so none attack each other; return the count of distinct solutions.",
{
"Python": '''def totalNQueens(n):
    cnt=[0]; cols=set(); d1=set(); d2=set()
    def bt(r):
        if r==n: cnt[0]+=1; return
        for c in range(n):
            if c in cols or r-c in d1 or r+c in d2: continue
            cols.add(c); d1.add(r-c); d2.add(r+c)
            bt(r+1)
            cols.remove(c); d1.remove(r-c); d2.remove(r+c)
    bt(0); return cnt[0]

if __name__=="__main__":
    print(totalNQueens(4))
    print(totalNQueens(6))
''',
"JavaScript": '''function totalNQueens(n){let cnt=0;const cols=new Set(),d1=new Set(),d2=new Set();function bt(r){if(r===n){cnt++;return;}for(let c=0;c<n;c++){if(cols.has(c)||d1.has(r-c)||d2.has(r+c))continue;cols.add(c);d1.add(r-c);d2.add(r+c);bt(r+1);cols.delete(c);d1.delete(r-c);d2.delete(r+c);}}bt(0);return cnt;}
console.log(totalNQueens(4));console.log(totalNQueens(6));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int cnt; static int N; static Set<Integer> cols,d1,d2;
  static void bt(int r){if(r==N){cnt++;return;}for(int c=0;c<N;c++){if(cols.contains(c)||d1.contains(r-c)||d2.contains(r+c))continue;cols.add(c);d1.add(r-c);d2.add(r+c);bt(r+1);cols.remove(c);d1.remove(r-c);d2.remove(r+c);}}
  static int totalNQueens(int n){cnt=0;N=n;cols=new HashSet<>();d1=new HashSet<>();d2=new HashSet<>();bt(0);return cnt;}
  public static void main(String[]a){System.out.println(totalNQueens(4));System.out.println(totalNQueens(6));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int CNT,N; set<int> COLS,D1,D2;
void bt(int r){if(r==N){CNT++;return;}for(int c=0;c<N;c++){if(COLS.count(c)||D1.count(r-c)||D2.count(r+c))continue;COLS.insert(c);D1.insert(r-c);D2.insert(r+c);bt(r+1);COLS.erase(c);D1.erase(r-c);D2.erase(r+c);}}
int totalNQueens(int n){CNT=0;N=n;COLS.clear();D1.clear();D2.clear();bt(0);return CNT;}
int main(){cout<<totalNQueens(4)<<"\\n"<<totalNQueens(6)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func totalNQueens(n int) int { cnt:=0; cols:=map[int]bool{}; d1:=map[int]bool{}; d2:=map[int]bool{}; var bt func(r int); bt=func(r int){ if r==n { cnt++; return }; for c:=0;c<n;c++ { if cols[c]||d1[r-c]||d2[r+c] { continue }; cols[c]=true; d1[r-c]=true; d2[r+c]=true; bt(r+1); delete(cols,c); delete(d1,r-c); delete(d2,r+c) } }; bt(0); return cnt }
func main(){ fmt.Println(totalNQueens(4)); fmt.Println(totalNQueens(6)) }
''',
"R": '''totalNQueens <- function(n){ cnt<-0; cols<-c(); d1<-c(); d2<-c(); bt<-function(r){ if(r>n){ cnt<<-cnt+1; return() }; for(c in 1:n){ if((c %in% cols) || ((r-c) %in% d1) || ((r+c) %in% d2)) next; cols<<-c(cols,c); d1<<-c(d1,r-c); d2<<-c(d2,r+c); bt(r+1); cols<<-cols[-length(cols)]; d1<<-d1[-length(d1)]; d2<<-d2[-length(d2)] } }; bt(1); cnt }
cat(totalNQueens(4),"\\n")
''',
}))

# 173 Pacific Atlantic Water Flow
L.append((173, "Pacific Atlantic Water Flow", "Graphs", "Medium", 87,
"Return cells from which water can flow to both Pacific (top/left) and Atlantic (bottom/right).",
{
"Python": '''def pacificAtlantic(h):
    if not h: return []
    R,C=len(h),len(h[0])
    pac=[[False]*C for _ in range(R)]; atl=[[False]*C for _ in range(R)]
    def dfs(r,c,seen):
        seen[r][c]=True
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<R and 0<=nc<C and not seen[nr][nc] and h[nr][nc]>=h[r][c]:
                dfs(nr,nc,seen)
    for c in range(C):
        dfs(0,c,pac); dfs(R-1,c,atl)
    for r in range(R):
        dfs(r,0,pac); dfs(r,C-1,atl)
    return [[r,c] for r in range(R) for c in range(C) if pac[r][c] and atl[r][c]]

if __name__=="__main__":
    print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
''',
"JavaScript": '''function pacificAtlantic(h){if(!h.length)return[];const R=h.length,C=h[0].length;const pac=Array.from({length:R},()=>new Array(C).fill(false));const atl=Array.from({length:R},()=>new Array(C).fill(false));function dfs(r,c,seen){seen[r][c]=true;for(const [dr,dc] of [[1,0],[-1,0],[0,1],[0,-1]]){const nr=r+dr,nc=c+dc;if(nr>=0&&nr<R&&nc>=0&&nc<C&&!seen[nr][nc]&&h[nr][nc]>=h[r][c])dfs(nr,nc,seen);}}for(let c=0;c<C;c++){dfs(0,c,pac);dfs(R-1,c,atl);}for(let r=0;r<R;r++){dfs(r,0,pac);dfs(r,C-1,atl);}const res=[];for(let r=0;r<R;r++)for(let c=0;c<C;c++)if(pac[r][c]&&atl[r][c])res.push([r,c]);return res;}
console.log(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]).length);
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int R,C; static int[][] H; static int[][] DIR={{1,0},{-1,0},{0,1},{0,-1}};
  static void dfs(int r,int c,boolean[][] s){s[r][c]=true;for(int[] d:DIR){int nr=r+d[0],nc=c+d[1];if(nr>=0&&nr<R&&nc>=0&&nc<C&&!s[nr][nc]&&H[nr][nc]>=H[r][c])dfs(nr,nc,s);}}
  static List<int[]> pacificAtlantic(int[][] h){R=h.length;C=h[0].length;H=h;boolean[][] pac=new boolean[R][C],atl=new boolean[R][C];for(int c=0;c<C;c++){dfs(0,c,pac);dfs(R-1,c,atl);}for(int r=0;r<R;r++){dfs(r,0,pac);dfs(r,C-1,atl);}List<int[]> res=new ArrayList<>();for(int r=0;r<R;r++)for(int c=0;c<C;c++)if(pac[r][c]&&atl[r][c])res.add(new int[]{r,c});return res;}
  public static void main(String[]a){System.out.println(pacificAtlantic(new int[][]{{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}}).size());}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int R,C; vector<vector<int>> H; int DIR[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
void dfs(int r,int c,vector<vector<bool>>& s){s[r][c]=true;for(auto& d:DIR){int nr=r+d[0],nc=c+d[1];if(nr>=0&&nr<R&&nc>=0&&nc<C&&!s[nr][nc]&&H[nr][nc]>=H[r][c])dfs(nr,nc,s);}}
vector<vector<int>> pacificAtlantic(vector<vector<int>> h){R=h.size();C=h[0].size();H=h;vector<vector<bool>> pac(R,vector<bool>(C,false)),atl(R,vector<bool>(C,false));for(int c=0;c<C;c++){dfs(0,c,pac);dfs(R-1,c,atl);}for(int r=0;r<R;r++){dfs(r,0,pac);dfs(r,C-1,atl);}vector<vector<int>> res;for(int r=0;r<R;r++)for(int c=0;c<C;c++)if(pac[r][c]&&atl[r][c])res.push_back({r,c});return res;}
int main(){cout<<pacificAtlantic({{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}}).size()<<"\\n";}
''',
"Go": '''package main
import "fmt"
func pacificAtlantic(h [][]int) [][]int { if len(h)==0 { return nil }; R,C:=len(h),len(h[0]); pac:=make([][]bool,R); atl:=make([][]bool,R); for i:=range pac { pac[i]=make([]bool,C); atl[i]=make([]bool,C) }; var dfs func(r,c int,s [][]bool); dfs=func(r,c int,s [][]bool){ s[r][c]=true; for _,d:=range [4][2]int{{1,0},{-1,0},{0,1},{0,-1}} { nr,nc:=r+d[0],c+d[1]; if nr>=0 && nr<R && nc>=0 && nc<C && !s[nr][nc] && h[nr][nc]>=h[r][c] { dfs(nr,nc,s) } } }; for c:=0;c<C;c++ { dfs(0,c,pac); dfs(R-1,c,atl) }; for r:=0;r<R;r++ { dfs(r,0,pac); dfs(r,C-1,atl) }; var res [][]int; for r:=0;r<R;r++ { for c:=0;c<C;c++ { if pac[r][c] && atl[r][c] { res=append(res,[]int{r,c}) } } }; return res }
func main(){ fmt.Println(len(pacificAtlantic([][]int{{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}}))) }
''',
"R": '''pacificAtlantic <- function(h){ R<-length(h); C<-length(h[[1]]); pac<-matrix(FALSE,R,C); atl<-matrix(FALSE,R,C); dfs<-function(r,c,seen){ seen[r,c]<-TRUE; for(d in list(c(1,0),c(-1,0),c(0,1),c(0,-1))){ nr<-r+d[1]; nc<-c+d[2]; if(nr>=1&&nr<=R&&nc>=1&&nc<=C&&!seen[nr,nc]&&h[[nr]][nc]>=h[[r]][c]) seen<-dfs(nr,nc,seen) }; seen }; for(c in 1:C){ pac<-dfs(1,c,pac); atl<-dfs(R,c,atl) }; for(r in 1:R){ pac<-dfs(r,1,pac); atl<-dfs(r,C,atl) }; res<-list(); for(r in 1:R) for(c in 1:C) if(pac[r,c]&&atl[r,c]) res[[length(res)+1]]<-c(r-1,c-1); res }
cat(length(pacificAtlantic(list(c(1,2,2,3,5),c(3,2,3,4,4),c(2,4,5,3,1),c(6,7,1,4,5),c(5,1,1,2,4)))),"\\n")
''',
}))

# 174 Surrounded Regions
L.append((174, "Surrounded Regions", "Graphs", "Medium", 87,
"Capture all 'O' regions surrounded by 'X' (regions touching the border are not captured).",
{
"Python": '''def solve(b):
    if not b: return
    R,C=len(b),len(b[0])
    def dfs(r,c):
        if r<0 or r>=R or c<0 or c>=C or b[r][c]!='O': return
        b[r][c]='S'
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)
    for r in range(R):
        dfs(r,0); dfs(r,C-1)
    for c in range(C):
        dfs(0,c); dfs(R-1,c)
    for r in range(R):
        for c in range(C):
            b[r][c]='O' if b[r][c]=='S' else 'X'

if __name__=="__main__":
    g=[['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
    solve(g); print(g)
''',
"JavaScript": '''function solve(b){if(!b.length)return;const R=b.length,C=b[0].length;function dfs(r,c){if(r<0||r>=R||c<0||c>=C||b[r][c]!=='O')return;b[r][c]='S';dfs(r+1,c);dfs(r-1,c);dfs(r,c+1);dfs(r,c-1);}for(let r=0;r<R;r++){dfs(r,0);dfs(r,C-1);}for(let c=0;c<C;c++){dfs(0,c);dfs(R-1,c);}for(let r=0;r<R;r++)for(let c=0;c<C;c++)b[r][c]=b[r][c]==='S'?'O':'X';}
const g=[['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']];solve(g);console.log(g);
''',
"Java": '''public class __CLASS__{
  static int R,C; static char[][] B;
  static void dfs(int r,int c){if(r<0||r>=R||c<0||c>=C||B[r][c]!='O')return;B[r][c]='S';dfs(r+1,c);dfs(r-1,c);dfs(r,c+1);dfs(r,c-1);}
  static void solve(char[][] b){R=b.length;C=b[0].length;B=b;for(int r=0;r<R;r++){dfs(r,0);dfs(r,C-1);}for(int c=0;c<C;c++){dfs(0,c);dfs(R-1,c);}for(int r=0;r<R;r++)for(int c=0;c<C;c++)b[r][c]=b[r][c]=='S'?'O':'X';}
  public static void main(String[]a){char[][] g={{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}};solve(g);for(char[] row:g){for(char x:row)System.out.print(x);System.out.println();}}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int R,C; vector<vector<char>> B;
void dfs(int r,int c){if(r<0||r>=R||c<0||c>=C||B[r][c]!='O')return;B[r][c]='S';dfs(r+1,c);dfs(r-1,c);dfs(r,c+1);dfs(r,c-1);}
void solve(vector<vector<char>>& b){R=b.size();C=b[0].size();B=b;for(int r=0;r<R;r++){dfs(r,0);dfs(r,C-1);}for(int c=0;c<C;c++){dfs(0,c);dfs(R-1,c);}for(int r=0;r<R;r++)for(int c=0;c<C;c++)b[r][c]=B[r][c]=='S'?'O':'X';}
int main(){vector<vector<char>> g={{'X','X','X','X'},{'X','O','O','X'},{'X','X','O','X'},{'X','O','X','X'}};solve(g);for(auto& r:g){for(char x:r)cout<<x;cout<<"\\n";}}
''',
"Go": '''package main
import "fmt"
func solve(b [][]byte){ if len(b)==0 { return }; R,C:=len(b),len(b[0]); var dfs func(r,c int); dfs=func(r,c int){ if r<0||r>=R||c<0||c>=C||b[r][c]!='O' { return }; b[r][c]='S'; dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1) }; for r:=0;r<R;r++ { dfs(r,0); dfs(r,C-1) }; for c:=0;c<C;c++ { dfs(0,c); dfs(R-1,c) }; for r:=0;r<R;r++ { for c:=0;c<C;c++ { if b[r][c]=='S' { b[r][c]='O' } else { b[r][c]='X' } } } }
func main(){ g:=[][]byte{[]byte("XXXX"),[]byte("XOOX"),[]byte("XXOX"),[]byte("XOXX")}; solve(g); for _,r:=range g { fmt.Println(string(r)) } }
''',
"R": '''solve_regions <- function(b){ R<-length(b); C<-nchar(b[[1]]); m<-do.call(rbind,lapply(b,function(s) strsplit(s,"")[[1]])); dfs<-function(r,c){ if(r<1||r>R||c<1||c>C||m[r,c]!='O') return(); m[r,c]<<-'S'; dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1) }; for(r in 1:R){ dfs(r,1); dfs(r,C) }; for(c in 1:C){ dfs(1,c); dfs(R,c) }; m[m=='O']<-'X'; m[m=='S']<-'O'; apply(m,1,paste,collapse="") }
print(solve_regions(c("XXXX","XOOX","XXOX","XOXX")))
''',
}))

# 175 Validate BST
L.append((175, "Validate Binary Search Tree", "Trees", "Medium", 88,
"Determine if a binary tree is a valid BST.",
{
"Python": '''class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def isValidBST(root):
    def rec(n,lo,hi):
        if not n: return True
        if not(lo<n.v<hi): return False
        return rec(n.l,lo,n.v) and rec(n.r,n.v,hi)
    return rec(root,float('-inf'),float('inf'))

if __name__=="__main__":
    r=N(2,N(1),N(3))
    print(isValidBST(r))
    r2=N(5,N(1),N(4,N(3),N(6)))
    print(isValidBST(r2))
''',
"JavaScript": '''class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function isValidBST(n,lo=-Infinity,hi=Infinity){if(!n)return true;if(!(n.v>lo&&n.v<hi))return false;return isValidBST(n.l,lo,n.v)&&isValidBST(n.r,n.v,hi);}
console.log(isValidBST(new N(2,new N(1),new N(3))));
console.log(isValidBST(new N(5,new N(1),new N(4,new N(3),new N(6)))));
''',
"Java": '''public class __CLASS__{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static boolean rec(N n,long lo,long hi){if(n==null)return true;if(n.v<=lo||n.v>=hi)return false;return rec(n.l,lo,n.v)&&rec(n.r,n.v,hi);}
  static boolean isValidBST(N r){return rec(r,Long.MIN_VALUE,Long.MAX_VALUE);}
  public static void main(String[]a){N r=new N(2);r.l=new N(1);r.r=new N(3);System.out.println(isValidBST(r));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct N{int v;N*l=0;N*r=0;N(int v):v(v){}};
bool rec(N* n,long lo,long hi){if(!n)return true;if(n->v<=lo||n->v>=hi)return false;return rec(n->l,lo,n->v)&&rec(n->r,n->v,hi);}
bool isValidBST(N* r){return rec(r,LLONG_MIN,LLONG_MAX);}
int main(){N r(2),a(1),b(3);r.l=&a;r.r=&b;cout<<boolalpha<<isValidBST(&r)<<"\\n";}
''',
"Go": '''package main
import ("fmt"; "math")
type N struct{ V int; L,R *N }
func rec(n *N,lo,hi float64) bool { if n==nil { return true }; v:=float64(n.V); if v<=lo||v>=hi { return false }; return rec(n.L,lo,v) && rec(n.R,v,hi) }
func isValidBST(r *N) bool { return rec(r,math.Inf(-1),math.Inf(1)) }
func main(){ r:=&N{V:2,L:&N{V:1},R:&N{V:3}}; fmt.Println(isValidBST(r)) }
''',
"R": '''isValidBST <- function(n,lo=-Inf,hi=Inf){ if(is.null(n)) return(TRUE); if(!(n$v>lo && n$v<hi)) return(FALSE); isValidBST(n$l,lo,n$v) && isValidBST(n$r,n$v,hi) }
n <- function(v,l=NULL,r=NULL) list(v=v,l=l,r=r)
cat(isValidBST(n(2,n(1),n(3))),"\\n")
''',
}))

# 176 Kth Smallest in BST
L.append((176, "Kth Smallest Element In a Bst", "Trees", "Medium", 88,
"Return the kth smallest value in a BST (1-indexed).",
{
"Python": '''class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def kth(root,k):
    st=[]; cur=root
    while cur or st:
        while cur: st.append(cur); cur=cur.l
        cur=st.pop(); k-=1
        if k==0: return cur.v
        cur=cur.r

if __name__=="__main__":
    r=N(3,N(1,None,N(2)),N(4))
    print(kth(r,1))
    print(kth(r,3))
''',
"JavaScript": '''class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function kth(root,k){const st=[];let cur=root;while(cur||st.length){while(cur){st.push(cur);cur=cur.l;}cur=st.pop();if(--k===0)return cur.v;cur=cur.r;}}
const r=new N(3,new N(1,null,new N(2)),new N(4));
console.log(kth(r,1));console.log(kth(r,3));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static int kth(N r,int k){Deque<N> st=new ArrayDeque<>();N cur=r;while(cur!=null||!st.isEmpty()){while(cur!=null){st.push(cur);cur=cur.l;}cur=st.pop();if(--k==0)return cur.v;cur=cur.r;}return -1;}
  public static void main(String[]a){N r=new N(3);r.l=new N(1);r.l.r=new N(2);r.r=new N(4);System.out.println(kth(r,1));System.out.println(kth(r,3));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct N{int v;N*l=0;N*r=0;N(int v):v(v){}};
int kth(N* r,int k){stack<N*> st;N* cur=r;while(cur||!st.empty()){while(cur){st.push(cur);cur=cur->l;}cur=st.top();st.pop();if(--k==0)return cur->v;cur=cur->r;}return -1;}
int main(){N r(3),a(1),b(2),c(4);r.l=&a;a.r=&b;r.r=&c;cout<<kth(&r,1)<<"\\n"<<kth(&r,3)<<"\\n";}
''',
"Go": '''package main
import "fmt"
type N struct{ V int; L,R *N }
func kth(r *N,k int) int { st:=[]*N{}; cur:=r; for cur!=nil || len(st)>0 { for cur!=nil { st=append(st,cur); cur=cur.L }; cur=st[len(st)-1]; st=st[:len(st)-1]; k--; if k==0 { return cur.V }; cur=cur.R }; return -1 }
func main(){ r:=&N{V:3,L:&N{V:1,R:&N{V:2}},R:&N{V:4}}; fmt.Println(kth(r,1)); fmt.Println(kth(r,3)) }
''',
"R": '''kth <- function(root,k){ st<-list(); cur<-root; while(!is.null(cur)||length(st)>0){ while(!is.null(cur)){ st[[length(st)+1]]<-cur; cur<-cur$l }; cur<-st[[length(st)]]; st[[length(st)]]<-NULL; k<-k-1; if(k==0) return(cur$v); cur<-cur$r } }
n <- function(v,l=NULL,r=NULL) list(v=v,l=l,r=r)
cat(kth(n(3,n(1,NULL,n(2)),n(4)),1),"\\n")
''',
}))

# 177 Word Break
L.append((177, "Word Break", "1-D Dynamic Programming", "Medium", 89,
"Determine if string s can be segmented into words from the given dictionary.",
{
"Python": '''def wordBreak(s,wd):
    w=set(wd); n=len(s); dp=[False]*(n+1); dp[0]=True
    for i in range(1,n+1):
        for j in range(i):
            if dp[j] and s[j:i] in w:
                dp[i]=True; break
    return dp[n]

if __name__=="__main__":
    print(wordBreak("leetcode",["leet","code"]))
    print(wordBreak("applepenapple",["apple","pen"]))
    print(wordBreak("catsandog",["cats","dog","sand","and","cat"]))
''',
"JavaScript": '''function wordBreak(s,wd){const w=new Set(wd);const n=s.length;const dp=new Array(n+1).fill(false);dp[0]=true;for(let i=1;i<=n;i++)for(let j=0;j<i;j++)if(dp[j]&&w.has(s.substring(j,i))){dp[i]=true;break;}return dp[n];}
console.log(wordBreak("leetcode",["leet","code"]));console.log(wordBreak("catsandog",["cats","dog","sand","and","cat"]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static boolean wordBreak(String s,List<String> wd){Set<String> w=new HashSet<>(wd);int n=s.length();boolean[] dp=new boolean[n+1];dp[0]=true;for(int i=1;i<=n;i++)for(int j=0;j<i;j++)if(dp[j]&&w.contains(s.substring(j,i))){dp[i]=true;break;}return dp[n];}
  public static void main(String[]a){System.out.println(wordBreak("leetcode",Arrays.asList("leet","code")));System.out.println(wordBreak("catsandog",Arrays.asList("cats","dog","sand","and","cat")));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool wordBreak(string s,vector<string> wd){unordered_set<string> w(wd.begin(),wd.end());int n=s.size();vector<bool> dp(n+1,false);dp[0]=true;for(int i=1;i<=n;i++)for(int j=0;j<i;j++)if(dp[j]&&w.count(s.substr(j,i-j))){dp[i]=true;break;}return dp[n];}
int main(){cout<<boolalpha<<wordBreak("leetcode",{"leet","code"})<<"\\n"<<wordBreak("catsandog",{"cats","dog","sand","and","cat"})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func wordBreak(s string,wd []string) bool { w:=map[string]bool{}; for _,x:=range wd { w[x]=true }; n:=len(s); dp:=make([]bool,n+1); dp[0]=true; for i:=1;i<=n;i++ { for j:=0;j<i;j++ { if dp[j] && w[s[j:i]] { dp[i]=true; break } } }; return dp[n] }
func main(){ fmt.Println(wordBreak("leetcode",[]string{"leet","code"})); fmt.Println(wordBreak("catsandog",[]string{"cats","dog","sand","and","cat"})) }
''',
"R": '''wordBreak <- function(s,wd){ w<-as.list(wd); names(w)<-wd; n<-nchar(s); dp<-c(TRUE,rep(FALSE,n)); for(i in 1:n) for(j in 0:(i-1)) if(dp[j+1] && !is.null(w[[substr(s,j+1,i)]])){ dp[i+1]<-TRUE; break }; dp[n+1] }
cat(wordBreak("leetcode",c("leet","code")),"\\n")
''',
}))

# 178 Longest Increasing Subsequence
L.append((178, "Longest Increasing Subsequence", "1-D Dynamic Programming", "Medium", 89,
"Length of the longest strictly-increasing subsequence.",
{
"Python": '''from bisect import bisect_left
def LIS(a):
    tail=[]
    for x in a:
        i=bisect_left(tail,x)
        if i==len(tail): tail.append(x)
        else: tail[i]=x
    return len(tail)

if __name__=="__main__":
    print(LIS([10,9,2,5,3,7,101,18]))
    print(LIS([0,1,0,3,2,3]))
''',
"JavaScript": '''function LIS(a){const t=[];for(const x of a){let lo=0,hi=t.length;while(lo<hi){const m=(lo+hi)>>1;if(t[m]<x)lo=m+1;else hi=m;}t[lo]=x;}return t.length;}
console.log(LIS([10,9,2,5,3,7,101,18]));console.log(LIS([0,1,0,3,2,3]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int LIS(int[] a){List<Integer> t=new ArrayList<>();for(int x:a){int lo=0,hi=t.size();while(lo<hi){int m=(lo+hi)>>>1;if(t.get(m)<x)lo=m+1;else hi=m;}if(lo==t.size())t.add(x);else t.set(lo,x);}return t.size();}
  public static void main(String[]a){System.out.println(LIS(new int[]{10,9,2,5,3,7,101,18}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int LIS(vector<int> a){vector<int> t;for(int x:a){auto it=lower_bound(t.begin(),t.end(),x);if(it==t.end())t.push_back(x);else *it=x;}return t.size();}
int main(){cout<<LIS({10,9,2,5,3,7,101,18})<<"\\n"<<LIS({0,1,0,3,2,3})<<"\\n";}
''',
"Go": '''package main
import ("fmt"; "sort")
func LIS(a []int) int { t:=[]int{}; for _,x:=range a { i:=sort.SearchInts(t,x); if i==len(t) { t=append(t,x) } else { t[i]=x } }; return len(t) }
func main(){ fmt.Println(LIS([]int{10,9,2,5,3,7,101,18})); fmt.Println(LIS([]int{0,1,0,3,2,3})) }
''',
"R": '''LIS <- function(a){ t<-c(); for(x in a){ i<-findInterval(x-1,t)+1; if(i>length(t)) t<-c(t,x) else t[i]<-x }; length(t) }
cat(LIS(c(10,9,2,5,3,7,101,18)),"\\n")
''',
}))

# 179 Construct Binary Tree from Preorder and Inorder
L.append((179, "Construct Binary Tree From Preorder And Inorder Traversal", "Trees", "Medium", 90,
"Given preorder and inorder traversals (no duplicates), reconstruct the binary tree.",
{
"Python": '''class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def build(pre,ino):
    idx={v:i for i,v in enumerate(ino)}
    it=iter(pre)
    def rec(lo,hi):
        if lo>hi: return None
        v=next(it); k=idx[v]
        n=N(v); n.l=rec(lo,k-1); n.r=rec(k+1,hi); return n
    return rec(0,len(ino)-1)

def pre_order(n):
    if not n: return []
    return [n.v]+pre_order(n.l)+pre_order(n.r)

if __name__=="__main__":
    r=build([3,9,20,15,7],[9,3,15,20,7])
    print(pre_order(r))
''',
"JavaScript": '''class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function build(pre,ino){const idx=new Map();ino.forEach((v,i)=>idx.set(v,i));let p=0;function rec(lo,hi){if(lo>hi)return null;const v=pre[p++];const k=idx.get(v);const n=new N(v);n.l=rec(lo,k-1);n.r=rec(k+1,hi);return n;}return rec(0,ino.length-1);}
function pre_order(n){if(!n)return [];return [n.v,...pre_order(n.l),...pre_order(n.r)];}
console.log(pre_order(build([3,9,20,15,7],[9,3,15,20,7])));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static int p; static int[] PRE; static Map<Integer,Integer> IDX;
  static N rec(int lo,int hi){if(lo>hi)return null;int v=PRE[p++];int k=IDX.get(v);N n=new N(v);n.l=rec(lo,k-1);n.r=rec(k+1,hi);return n;}
  static N build(int[] pre,int[] ino){p=0;PRE=pre;IDX=new HashMap<>();for(int i=0;i<ino.length;i++)IDX.put(ino[i],i);return rec(0,ino.length-1);}
  static List<Integer> pre_order(N n){List<Integer> r=new ArrayList<>();if(n==null)return r;r.add(n.v);r.addAll(pre_order(n.l));r.addAll(pre_order(n.r));return r;}
  public static void main(String[]a){System.out.println(pre_order(build(new int[]{3,9,20,15,7},new int[]{9,3,15,20,7})));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct N{int v;N*l=0;N*r=0;N(int v):v(v){}};
int P; vector<int> PRE; unordered_map<int,int> IDX;
N* rec(int lo,int hi){if(lo>hi)return 0;int v=PRE[P++];int k=IDX[v];N* n=new N(v);n->l=rec(lo,k-1);n->r=rec(k+1,hi);return n;}
N* build(vector<int> pre,vector<int> ino){P=0;PRE=pre;IDX.clear();for(int i=0;i<(int)ino.size();i++)IDX[ino[i]]=i;return rec(0,ino.size()-1);}
void pre_order(N* n,vector<int>& r){if(!n)return;r.push_back(n->v);pre_order(n->l,r);pre_order(n->r,r);}
int main(){auto t=build({3,9,20,15,7},{9,3,15,20,7});vector<int> r;pre_order(t,r);for(int x:r)cout<<x<<" ";cout<<"\\n";}
''',
"Go": '''package main
import "fmt"
type N struct{ V int; L,R *N }
var P int; var PRE []int; var IDX map[int]int
func rec(lo,hi int) *N { if lo>hi { return nil }; v:=PRE[P]; P++; k:=IDX[v]; n:=&N{V:v}; n.L=rec(lo,k-1); n.R=rec(k+1,hi); return n }
func build(pre,ino []int) *N { P=0; PRE=pre; IDX=map[int]int{}; for i,v:=range ino { IDX[v]=i }; return rec(0,len(ino)-1) }
func pre(n *N,r *[]int){ if n==nil { return }; *r=append(*r,n.V); pre(n.L,r); pre(n.R,r) }
func main(){ t:=build([]int{3,9,20,15,7},[]int{9,3,15,20,7}); var r []int; pre(t,&r); fmt.Println(r) }
''',
"R": '''build <- function(pre,ino){ idx<-setNames(seq_along(ino)-1,ino); p<-1; rec<-function(lo,hi){ if(lo>hi) return(NULL); v<-pre[p]; p<<-p+1; k<-idx[[as.character(v)]]; list(v=v,l=rec(lo,k-1),r=rec(k+1,hi)) }; rec(0,length(ino)-1) }
pre_order <- function(n){ if(is.null(n)) return(c()); c(n$v,pre_order(n$l),pre_order(n$r)) }
cat(pre_order(build(c(3,9,20,15,7),c(9,3,15,20,7))),"\\n")
''',
}))

# 180 House Robber III
L.append((180, "House Robber III", "Trees", "Medium", 90,
"Houses arranged as a binary tree; cannot rob two directly-linked houses. Return max amount.",
{
"Python": '''class N:
    def __init__(s,v,l=None,r=None): s.v=v; s.l=l; s.r=r
def rob(root):
    def rec(n):
        if not n: return (0,0)
        l=rec(n.l); r=rec(n.r)
        with_n=n.v+l[1]+r[1]
        wo_n=max(l)+max(r)
        return (with_n,wo_n)
    return max(rec(root))

if __name__=="__main__":
    r=N(3,N(2,None,N(3)),N(3,None,N(1)))
    print(rob(r))
''',
"JavaScript": '''class N{constructor(v,l=null,r=null){this.v=v;this.l=l;this.r=r;}}
function rob(root){function rec(n){if(!n)return [0,0];const l=rec(n.l),r=rec(n.r);return [n.v+l[1]+r[1], Math.max(l[0],l[1])+Math.max(r[0],r[1])];}return Math.max(...rec(root));}
console.log(rob(new N(3,new N(2,null,new N(3)),new N(3,null,new N(1)))));
''',
"Java": '''public class __CLASS__{
  static class N{int v;N l,r;N(int v){this.v=v;}}
  static int[] rec(N n){if(n==null)return new int[]{0,0};int[] l=rec(n.l),r=rec(n.r);return new int[]{n.v+l[1]+r[1],Math.max(l[0],l[1])+Math.max(r[0],r[1])};}
  static int rob(N r){int[] x=rec(r);return Math.max(x[0],x[1]);}
  public static void main(String[]a){N r=new N(3);r.l=new N(2);r.l.r=new N(3);r.r=new N(3);r.r.r=new N(1);System.out.println(rob(r));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
struct N{int v;N*l=0;N*r=0;N(int v):v(v){}};
pair<int,int> rec(N* n){if(!n)return {0,0};auto l=rec(n->l);auto r=rec(n->r);return {n->v+l.second+r.second,max(l.first,l.second)+max(r.first,r.second)};}
int rob(N* r){auto x=rec(r);return max(x.first,x.second);}
int main(){N r(3),a(2),b(3),c(3),d(1);r.l=&a;a.r=&b;r.r=&c;c.r=&d;cout<<rob(&r)<<"\\n";}
''',
"Go": '''package main
import "fmt"
type N struct{ V int; L,R *N }
func rec(n *N) (int,int) { if n==nil { return 0,0 }; la,lb:=rec(n.L); ra,rb:=rec(n.R); return n.V+lb+rb, max2(la,lb)+max2(ra,rb) }
func max2(a,b int) int { if a>b { return a }; return b }
func rob(r *N) int { a,b:=rec(r); return max2(a,b) }
func main(){ r:=&N{V:3,L:&N{V:2,R:&N{V:3}},R:&N{V:3,R:&N{V:1}}}; fmt.Println(rob(r)) }
''',
"R": '''rob <- function(root){ rec<-function(n){ if(is.null(n)) return(c(0,0)); l<-rec(n$l); r<-rec(n$r); c(n$v+l[2]+r[2], max(l)+max(r)) }; max(rec(root)) }
n <- function(v,l=NULL,r=NULL) list(v=v,l=l,r=r)
cat(rob(n(3,n(2,NULL,n(3)),n(3,NULL,n(1)))),"\\n")
''',
}))

# 181 Open The Lock
L.append((181, "Open The Lock", "Graphs", "Medium", 91,
"4-wheel lock starts at '0000'. Each move turns a wheel +/-1. Avoid deadends. Return min moves to reach target or -1.",
{
"Python": '''from collections import deque
def openLock(deadends,target):
    dead=set(deadends)
    if "0000" in dead: return -1
    if target=="0000": return 0
    seen={"0000"}; q=deque([("0000",0)])
    while q:
        s,d=q.popleft()
        for i in range(4):
            for delta in (-1,1):
                ns=s[:i]+str((int(s[i])+delta)%10)+s[i+1:]
                if ns==target: return d+1
                if ns not in seen and ns not in dead:
                    seen.add(ns); q.append((ns,d+1))
    return -1

if __name__=="__main__":
    print(openLock(["0201","0101","0102","1212","2002"],"0202"))
''',
"JavaScript": '''function openLock(dead,target){const D=new Set(dead);if(D.has("0000"))return -1;if(target==="0000")return 0;const seen=new Set(["0000"]);let q=[["0000",0]];while(q.length){const [s,d]=q.shift();for(let i=0;i<4;i++)for(const x of [-1,1]){const c=(parseInt(s[i])+x+10)%10;const ns=s.substring(0,i)+c+s.substring(i+1);if(ns===target)return d+1;if(!seen.has(ns)&&!D.has(ns)){seen.add(ns);q.push([ns,d+1]);}}}return -1;}
console.log(openLock(["0201","0101","0102","1212","2002"],"0202"));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static int openLock(String[] dead,String target){Set<String> D=new HashSet<>(Arrays.asList(dead));if(D.contains("0000"))return -1;if(target.equals("0000"))return 0;Set<String> seen=new HashSet<>();seen.add("0000");Deque<String> q=new ArrayDeque<>();q.add("0000");int d=0;while(!q.isEmpty()){d++;int sz=q.size();for(int k=0;k<sz;k++){String s=q.poll();for(int i=0;i<4;i++)for(int x:new int[]{-1,1}){char[] a=s.toCharArray();a[i]=(char)('0'+((a[i]-'0'+x+10)%10));String ns=new String(a);if(ns.equals(target))return d;if(!seen.contains(ns)&&!D.contains(ns)){seen.add(ns);q.add(ns);}}}}return -1;}
  public static void main(String[]a){System.out.println(openLock(new String[]{"0201","0101","0102","1212","2002"},"0202"));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int openLock(vector<string> dead,string target){unordered_set<string> D(dead.begin(),dead.end());if(D.count("0000"))return -1;if(target=="0000")return 0;unordered_set<string> seen={"0000"};queue<string> q;q.push("0000");int d=0;while(!q.empty()){d++;int sz=q.size();while(sz--){string s=q.front();q.pop();for(int i=0;i<4;i++) for(int x:{-1,1}){string ns=s;ns[i]='0'+((ns[i]-'0'+x+10)%10);if(ns==target)return d;if(!seen.count(ns)&&!D.count(ns)){seen.insert(ns);q.push(ns);}}}}return -1;}
int main(){cout<<openLock({"0201","0101","0102","1212","2002"},"0202")<<"\\n";}
''',
"Go": '''package main
import "fmt"
func openLock(dead []string,target string) int { D:=map[string]bool{}; for _,x:=range dead { D[x]=true }; if D["0000"] { return -1 }; if target=="0000" { return 0 }; seen:=map[string]bool{"0000":true}; q:=[]string{"0000"}; d:=0; for len(q)>0 { d++; sz:=len(q); for k:=0;k<sz;k++ { s:=q[0]; q=q[1:]; for i:=0;i<4;i++ { for _,x:=range []int{-1,1} { b:=[]byte(s); b[i]=byte('0'+((int(b[i]-'0')+x+10)%10)); ns:=string(b); if ns==target { return d }; if !seen[ns]&&!D[ns] { seen[ns]=true; q=append(q,ns) } } } } }; return -1 }
func main(){ fmt.Println(openLock([]string{"0201","0101","0102","1212","2002"},"0202")) }
''',
"R": '''openLock <- function(dead,target){ D<-dead; if("0000"%in%D) return(-1); if(target=="0000") return(0); seen<-"0000"; q<-list(c("0000",0)); while(length(q)>0){ x<-q[[1]]; q[[1]]<-NULL; s<-x[1]; d<-as.integer(x[2]); for(i in 1:4) for(delta in c(-1,1)){ ch<-as.integer(substr(s,i,i)); nc<-(ch+delta+10)%%10; ns<-paste0(substr(s,1,i-1),nc,substr(s,i+1,4)); if(ns==target) return(d+1); if(!(ns%in%seen)&&!(ns%in%D)){ seen<-c(seen,ns); q[[length(q)+1]]<-c(ns,as.character(d+1)) } } }; -1 }
cat(openLock(c("0201","0101","0102","1212","2002"),"0202"),"\\n")
''',
}))

# 182 Course Schedule
L.append((182, "Course Schedule", "Graphs", "Medium", 91,
"Given prerequisites pairs, can all courses be finished (no cycle)?",
{
"Python": '''def canFinish(n,pre):
    from collections import defaultdict,deque
    g=defaultdict(list); ind=[0]*n
    for a,b in pre: g[b].append(a); ind[a]+=1
    q=deque(i for i in range(n) if ind[i]==0); cnt=0
    while q:
        x=q.popleft(); cnt+=1
        for y in g[x]:
            ind[y]-=1
            if ind[y]==0: q.append(y)
    return cnt==n

if __name__=="__main__":
    print(canFinish(2,[[1,0]]))
    print(canFinish(2,[[1,0],[0,1]]))
''',
"JavaScript": '''function canFinish(n,pre){const g=Array.from({length:n},()=>[]);const ind=new Array(n).fill(0);for(const [a,b] of pre){g[b].push(a);ind[a]++;}const q=[];for(let i=0;i<n;i++)if(ind[i]===0)q.push(i);let cnt=0;while(q.length){const x=q.shift();cnt++;for(const y of g[x])if(--ind[y]===0)q.push(y);}return cnt===n;}
console.log(canFinish(2,[[1,0]]));console.log(canFinish(2,[[1,0],[0,1]]));
''',
"Java": '''import java.util.*;
public class __CLASS__{
  static boolean canFinish(int n,int[][] pre){List<List<Integer>> g=new ArrayList<>();for(int i=0;i<n;i++)g.add(new ArrayList<>());int[] ind=new int[n];for(int[] p:pre){g.get(p[1]).add(p[0]);ind[p[0]]++;}Deque<Integer> q=new ArrayDeque<>();for(int i=0;i<n;i++)if(ind[i]==0)q.add(i);int cnt=0;while(!q.isEmpty()){int x=q.poll();cnt++;for(int y:g.get(x))if(--ind[y]==0)q.add(y);}return cnt==n;}
  public static void main(String[]a){System.out.println(canFinish(2,new int[][]{{1,0}}));System.out.println(canFinish(2,new int[][]{{1,0},{0,1}}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool canFinish(int n,vector<vector<int>> pre){vector<vector<int>> g(n);vector<int> ind(n,0);for(auto& p:pre){g[p[1]].push_back(p[0]);ind[p[0]]++;}queue<int> q;for(int i=0;i<n;i++) if(ind[i]==0)q.push(i);int cnt=0;while(!q.empty()){int x=q.front();q.pop();cnt++;for(int y:g[x]) if(--ind[y]==0)q.push(y);}return cnt==n;}
int main(){cout<<boolalpha<<canFinish(2,{{1,0}})<<"\\n"<<canFinish(2,{{1,0},{0,1}})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func canFinish(n int,pre [][]int) bool { g:=make([][]int,n); ind:=make([]int,n); for _,p:=range pre { g[p[1]]=append(g[p[1]],p[0]); ind[p[0]]++ }; q:=[]int{}; for i:=0;i<n;i++ { if ind[i]==0 { q=append(q,i) } }; cnt:=0; for len(q)>0 { x:=q[0]; q=q[1:]; cnt++; for _,y:=range g[x] { ind[y]--; if ind[y]==0 { q=append(q,y) } } }; return cnt==n }
func main(){ fmt.Println(canFinish(2,[][]int{{1,0}})); fmt.Println(canFinish(2,[][]int{{1,0},{0,1}})) }
''',
"R": '''canFinish <- function(n,pre){ g<-vector("list",n); ind<-rep(0,n); for(p in pre){ g[[p[2]+1]]<-c(g[[p[2]+1]],p[1]+1); ind[p[1]+1]<-ind[p[1]+1]+1 }; q<-which(ind==0); cnt<-0; while(length(q)>0){ x<-q[1]; q<-q[-1]; cnt<-cnt+1; for(y in g[[x]]){ ind[y]<-ind[y]-1; if(ind[y]==0) q<-c(q,y) } }; cnt==n }
cat(canFinish(2,list(c(1,0))),"\\n"); cat(canFinish(2,list(c(1,0),c(0,1))),"\\n")
''',
}))

# 183 Reverse Bits
L.append((183, "Reverse Bits", "Bit Manipulation", "Easy", 92,
"Reverse bits of a given 32-bit unsigned integer.",
{
"Python": '''def reverseBits(n):
    r=0
    for _ in range(32):
        r=(r<<1)|(n&1); n>>=1
    return r

if __name__=="__main__":
    print(reverseBits(0b00000010100101000001111010011100))
''',
"JavaScript": '''function reverseBits(n){let r=0;for(let i=0;i<32;i++){r=(r<<1)|(n&1);n>>>=1;}return r>>>0;}
console.log(reverseBits(0b00000010100101000001111010011100));
''',
"Java": '''public class __CLASS__{
  static int reverseBits(int n){int r=0;for(int i=0;i<32;i++){r=(r<<1)|(n&1);n>>>=1;}return r;}
  public static void main(String[]a){System.out.println(reverseBits(0b00000010100101000001111010011100));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
uint32_t reverseBits(uint32_t n){uint32_t r=0;for(int i=0;i<32;i++){r=(r<<1)|(n&1);n>>=1;}return r;}
int main(){cout<<reverseBits(0b00000010100101000001111010011100)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func reverseBits(n uint32) uint32 { var r uint32; for i:=0;i<32;i++ { r=(r<<1)|(n&1); n>>=1 }; return r }
func main(){ fmt.Println(reverseBits(43261596)) }
''',
"R": '''reverseBits <- function(n){ r<-0; for(i in 1:32){ r<-bitwOr(bitwShiftL(r,1), bitwAnd(n,1)); n<-bitwShiftR(n,1) }; r }
cat(reverseBits(43261596),"\\n")
''',
}))

# 184 Missing Number
L.append((184, "Missing Number", "Bit Manipulation", "Easy", 92,
"Array contains n distinct numbers from [0,n]. Return the missing one.",
{
"Python": '''def missing(a):
    x=len(a)
    for i,v in enumerate(a):
        x^=i^v
    return x

if __name__=="__main__":
    print(missing([3,0,1]))
    print(missing([9,6,4,2,3,5,7,0,1]))
''',
"JavaScript": '''function missing(a){let x=a.length;for(let i=0;i<a.length;i++){x^=i^a[i];}return x;}
console.log(missing([3,0,1]));console.log(missing([9,6,4,2,3,5,7,0,1]));
''',
"Java": '''public class __CLASS__{
  static int missing(int[] a){int x=a.length;for(int i=0;i<a.length;i++)x^=i^a[i];return x;}
  public static void main(String[]a){System.out.println(missing(new int[]{3,0,1}));System.out.println(missing(new int[]{9,6,4,2,3,5,7,0,1}));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
int missing(vector<int> a){int x=a.size();for(int i=0;i<(int)a.size();i++)x^=i^a[i];return x;}
int main(){cout<<missing({3,0,1})<<"\\n"<<missing({9,6,4,2,3,5,7,0,1})<<"\\n";}
''',
"Go": '''package main
import "fmt"
func missing(a []int) int { x:=len(a); for i,v:=range a { x^=i^v }; return x }
func main(){ fmt.Println(missing([]int{3,0,1})); fmt.Println(missing([]int{9,6,4,2,3,5,7,0,1})) }
''',
"R": '''missing_num <- function(a){ x<-length(a); for(i in seq_along(a)) x<-bitwXor(x,bitwXor(i-1,a[i])); x }
cat(missing_num(c(3,0,1)),"\\n"); cat(missing_num(c(9,6,4,2,3,5,7,0,1)),"\\n")
''',
}))

# 185 Jump Game VII
L.append((185, "Jump Game VII", "Greedy", "Medium", 93,
"Binary string s. Start at 0; can jump from i to any j with i+minJump<=j<=i+maxJump and s[j]='0'. Reach last index?",
{
"Python": '''def canReach(s,mn,mx):
    n=len(s)
    if s[-1]!='0' or s[0]!='0': return False
    pre=[0]*(n+1); reach=[False]*n; reach[0]=True; pre[1]=1
    for i in range(1,n):
        if s[i]=='0':
            lo=max(0,i-mx); hi=i-mn
            if lo<=hi:
                if pre[hi+1]-pre[lo]>0: reach[i]=True
        pre[i+1]=pre[i]+(1 if reach[i] else 0)
    return reach[n-1]

if __name__=="__main__":
    print(canReach("011010",2,3))
    print(canReach("01101110",2,3))
''',
"JavaScript": '''function canReach(s,mn,mx){const n=s.length;if(s[n-1]!=='0'||s[0]!=='0')return false;const pre=new Array(n+1).fill(0);const r=new Array(n).fill(false);r[0]=true;pre[1]=1;for(let i=1;i<n;i++){if(s[i]==='0'){const lo=Math.max(0,i-mx),hi=i-mn;if(lo<=hi && pre[hi+1]-pre[lo]>0) r[i]=true;}pre[i+1]=pre[i]+(r[i]?1:0);}return r[n-1];}
console.log(canReach("011010",2,3));console.log(canReach("01101110",2,3));
''',
"Java": '''public class __CLASS__{
  static boolean canReach(String s,int mn,int mx){int n=s.length();if(s.charAt(n-1)!='0'||s.charAt(0)!='0')return false;int[] pre=new int[n+1];boolean[] r=new boolean[n];r[0]=true;pre[1]=1;for(int i=1;i<n;i++){if(s.charAt(i)=='0'){int lo=Math.max(0,i-mx),hi=i-mn;if(lo<=hi && pre[hi+1]-pre[lo]>0) r[i]=true;}pre[i+1]=pre[i]+(r[i]?1:0);}return r[n-1];}
  public static void main(String[]a){System.out.println(canReach("011010",2,3));System.out.println(canReach("01101110",2,3));}
}
''',
"CPP": '''#include <bits/stdc++.h>
using namespace std;
bool canReach(string s,int mn,int mx){int n=s.size();if(s.back()!='0'||s[0]!='0')return false;vector<int> pre(n+1,0);vector<bool> r(n,false);r[0]=true;pre[1]=1;for(int i=1;i<n;i++){if(s[i]=='0'){int lo=max(0,i-mx),hi=i-mn;if(lo<=hi && pre[hi+1]-pre[lo]>0) r[i]=true;}pre[i+1]=pre[i]+(r[i]?1:0);}return r[n-1];}
int main(){cout<<boolalpha<<canReach("011010",2,3)<<"\\n"<<canReach("01101110",2,3)<<"\\n";}
''',
"Go": '''package main
import "fmt"
func canReach(s string,mn,mx int) bool { n:=len(s); if s[n-1]!='0'||s[0]!='0' { return false }; pre:=make([]int,n+1); r:=make([]bool,n); r[0]=true; pre[1]=1; for i:=1;i<n;i++ { if s[i]=='0' { lo:=i-mx; if lo<0 { lo=0 }; hi:=i-mn; if lo<=hi && pre[hi+1]-pre[lo]>0 { r[i]=true } }; v:=0; if r[i] { v=1 }; pre[i+1]=pre[i]+v }; return r[n-1] }
func main(){ fmt.Println(canReach("011010",2,3)); fmt.Println(canReach("01101110",2,3)) }
''',
"R": '''canReach <- function(s,mn,mx){ n<-nchar(s); ch<-strsplit(s,"")[[1]]; if(ch[n]!='0'||ch[1]!='0') return(FALSE); pre<-rep(0,n+1); r<-rep(FALSE,n); r[1]<-TRUE; pre[2]<-1; for(i in 2:n){ if(ch[i]=='0'){ lo<-max(0,i-1-mx); hi<-i-1-mn; if(lo<=hi && pre[hi+2]-pre[lo+1]>0) r[i]<-TRUE }; pre[i+1]<-pre[i]+(if(r[i]) 1 else 0) }; r[n] }
cat(canReach("011010",2,3),"\\n")
''',
}))

write_lessons(L)
