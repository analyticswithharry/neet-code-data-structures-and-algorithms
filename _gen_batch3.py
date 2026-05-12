"""Batch 3: NeetCode lessons 36-60 with embedded question + working solution."""
from _lesson_writer import write_lessons

LESSONS = []

# ---- 036 Valid Anagram ----
LESSONS.append((36, "Valid Anagram", "Arrays and Hashing", "Easy", 18,
"""Given two strings s and t, return true if t is an anagram of s.

Example: s = "anagram", t = "nagaram" -> true""",
{
"Python":'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        d = {}
        for c in s: d[c] = d.get(c,0)+1
        for c in t:
            if d.get(c,0)==0: return False
            d[c]-=1
        return True

if __name__ == "__main__":
    print(Solution().isAnagram("anagram","nagaram"))
    print(Solution().isAnagram("rat","car"))
''',
"JavaScript":'''
var isAnagram = function(s, t) {
    if (s.length !== t.length) return false;
    const d = {};
    for (const c of s) d[c] = (d[c]||0)+1;
    for (const c of t) { if (!d[c]) return false; d[c]--; }
    return true;
};
console.log(isAnagram("anagram","nagaram"), isAnagram("rat","car"));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public boolean isAnagram(String s, String t) {
        if (s.length()!=t.length()) return false;
        int[] c = new int[26];
        for (int i=0;i<s.length();i++){ c[s.charAt(i)-'a']++; c[t.charAt(i)-'a']--; }
        for (int x: c) if (x!=0) return false;
        return true;
    }
    public static void main(String[] a){
        __CLASS__ s = new __CLASS__();
        System.out.println(s.isAnagram("anagram","nagaram"));
        System.out.println(s.isAnagram("rat","car"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size()!=t.size()) return false;
        int c[26] = {0};
        for (size_t i=0;i<s.size();++i){ c[s[i]-'a']++; c[t[i]-'a']--; }
        for (int x: c) if (x) return false;
        return true;
    }
};
int main(){ Solution s; cout<<s.isAnagram("anagram","nagaram")<<" "<<s.isAnagram("rat","car")<<endl; }
''',
"Go":'''
package main
import "fmt"
func isAnagram(s, t string) bool {
    if len(s)!=len(t){return false}
    var c [26]int
    for i:=0;i<len(s);i++ { c[s[i]-'a']++; c[t[i]-'a']-- }
    for _,x:=range c{ if x!=0 {return false} }
    return true
}
func main(){ fmt.Println(isAnagram("anagram","nagaram"), isAnagram("rat","car")) }
''',
"R":'''
isAnagram <- function(s, t) {
    if (nchar(s)!=nchar(t)) return(FALSE)
    a <- sort(strsplit(s,"")[[1]])
    b <- sort(strsplit(t,"")[[1]])
    all(a==b)
}
print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))
''',
}))

# ---- 037 Group Anagrams ----
LESSONS.append((37, "Group Anagrams", "Arrays and Hashing", "Medium", 18,
"""Given an array of strings strs, group the anagrams together.

Example: ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]""",
{
"Python":'''
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return list(d.values())

if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
''',
"JavaScript":'''
var groupAnagrams = function(strs) {
    const m = new Map();
    for (const s of strs) {
        const k = s.split("").sort().join("");
        if (!m.has(k)) m.set(k, []);
        m.get(k).push(s);
    }
    return [...m.values()];
};
console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> m = new HashMap<>();
        for (String s: strs) {
            char[] a = s.toCharArray(); Arrays.sort(a);
            String k = new String(a);
            m.computeIfAbsent(k, x -> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(m.values());
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().groupAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        for (auto& s: strs) { string k=s; sort(k.begin(),k.end()); m[k].push_back(s); }
        vector<vector<string>> r; for (auto& p: m) r.push_back(p.second); return r;
    }
};
int main(){ vector<string> v={"eat","tea","tan","ate","nat","bat"}; auto r=Solution().groupAnagrams(v);
    for(auto& g:r){ for(auto& s:g) cout<<s<<" "; cout<<"|"; } cout<<endl; }
''',
"Go":'''
package main
import ("fmt"; "sort"; "strings")
func groupAnagrams(strs []string) [][]string {
    m := map[string][]string{}
    for _,s := range strs {
        b := []byte(s); sort.Slice(b, func(i,j int) bool{return b[i]<b[j]})
        k := string(b); m[k] = append(m[k], s)
    }
    out := [][]string{}
    for _,v := range m { out = append(out, v) }
    _ = strings.Join
    return out
}
func main(){ fmt.Println(groupAnagrams([]string{"eat","tea","tan","ate","nat","bat"})) }
''',
"R":'''
groupAnagrams <- function(strs) {
    keys <- sapply(strs, function(s) paste(sort(strsplit(s,"")[[1]]), collapse=""))
    split(strs, keys)
}
print(groupAnagrams(c("eat","tea","tan","ate","nat","bat")))
''',
}))

# ---- 038 Top K Frequent Elements ----
LESSONS.append((38, "Top K Frequent Elements", "Arrays and Hashing", "Medium", 19,
"""Given an integer array nums and integer k, return the k most frequent elements.

Example: nums = [1,1,1,2,2,3], k = 2 -> [1,2]""",
{
"Python":'''
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        return [x for x,_ in Counter(nums).most_common(k)]

if __name__ == "__main__":
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))
''',
"JavaScript":'''
var topKFrequent = function(nums, k) {
    const m = new Map();
    for (const n of nums) m.set(n,(m.get(n)||0)+1);
    return [...m.entries()].sort((a,b)=>b[1]-a[1]).slice(0,k).map(e=>e[0]);
};
console.log(topKFrequent([1,1,1,2,2,3], 2));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> c = new HashMap<>();
        for (int n: nums) c.merge(n, 1, Integer::sum);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->b[1]-a[1]);
        for (var e: c.entrySet()) pq.add(new int[]{e.getKey(), e.getValue()});
        int[] r = new int[k];
        for (int i=0;i<k;i++) r[i] = pq.poll()[0];
        return r;
    }
    public static void main(String[] a){
        System.out.println(Arrays.toString(new __CLASS__().topKFrequent(new int[]{1,1,1,2,2,3}, 2)));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> c;
        for (int n: nums) c[n]++;
        vector<pair<int,int>> v(c.begin(), c.end());
        sort(v.begin(), v.end(), [](auto& a, auto& b){return a.second>b.second;});
        vector<int> r; for (int i=0;i<k;i++) r.push_back(v[i].first); return r;
    }
};
int main(){ vector<int> v={1,1,1,2,2,3}; for (int x: Solution().topKFrequent(v,2)) cout<<x<<" "; cout<<endl; }
''',
"Go":'''
package main
import ("fmt"; "sort")
func topKFrequent(nums []int, k int) []int {
    c := map[int]int{}
    for _,n := range nums { c[n]++ }
    type p struct{ v,f int }
    a := []p{}
    for v,f := range c { a = append(a, p{v,f}) }
    sort.Slice(a, func(i,j int) bool { return a[i].f > a[j].f })
    r := []int{}
    for i:=0;i<k;i++ { r = append(r, a[i].v) }
    return r
}
func main(){ fmt.Println(topKFrequent([]int{1,1,1,2,2,3}, 2)) }
''',
"R":'''
topKFrequent <- function(nums, k) {
    t <- sort(table(nums), decreasing=TRUE)
    as.integer(names(t)[1:k])
}
print(topKFrequent(c(1,1,1,2,2,3), 2))
''',
}))

# ---- 039 Product of Array Except Self ----
LESSONS.append((39, "Product of Array Except Self", "Arrays and Hashing", "Medium", 19,
"""Given nums, return an array where answer[i] is the product of all elements
except nums[i]. Must run in O(n) without division.

Example: [1,2,3,4] -> [24,12,8,6]""",
{
"Python":'''
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums); res = [1]*n
        left = 1
        for i in range(n): res[i] = left; left *= nums[i]
        right = 1
        for i in range(n-1,-1,-1): res[i] *= right; right *= nums[i]
        return res

if __name__ == "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))
''',
"JavaScript":'''
var productExceptSelf = function(nums) {
    const n = nums.length, r = new Array(n).fill(1);
    let left = 1;
    for (let i=0;i<n;i++){ r[i]=left; left*=nums[i]; }
    let right = 1;
    for (let i=n-1;i>=0;i--){ r[i]*=right; right*=nums[i]; }
    return r;
};
console.log(productExceptSelf([1,2,3,4]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length; int[] r = new int[n];
        int left = 1;
        for (int i=0;i<n;i++){ r[i]=left; left*=nums[i]; }
        int right = 1;
        for (int i=n-1;i>=0;i--){ r[i]*=right; right*=nums[i]; }
        return r;
    }
    public static void main(String[] a){
        System.out.println(Arrays.toString(new __CLASS__().productExceptSelf(new int[]{1,2,3,4})));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size(); vector<int> r(n,1);
        int left = 1;
        for (int i=0;i<n;i++){ r[i]=left; left*=nums[i]; }
        int right = 1;
        for (int i=n-1;i>=0;i--){ r[i]*=right; right*=nums[i]; }
        return r;
    }
};
int main(){ vector<int> v={1,2,3,4}; for (int x: Solution().productExceptSelf(v)) cout<<x<<" "; cout<<endl; }
''',
"Go":'''
package main
import "fmt"
func productExceptSelf(nums []int) []int {
    n := len(nums); r := make([]int, n)
    left := 1
    for i:=0;i<n;i++ { r[i]=left; left*=nums[i] }
    right := 1
    for i:=n-1;i>=0;i-- { r[i]*=right; right*=nums[i] }
    return r
}
func main(){ fmt.Println(productExceptSelf([]int{1,2,3,4})) }
''',
"R":'''
productExceptSelf <- function(nums) {
    n <- length(nums); r <- rep(1L, n); left <- 1
    for (i in seq_len(n)) { r[i] <- left; left <- left * nums[i] }
    right <- 1
    for (i in n:1) { r[i] <- r[i] * right; right <- right * nums[i] }
    r
}
print(productExceptSelf(c(1,2,3,4)))
''',
}))

# ---- 040 Longest Consecutive Sequence ----
LESSONS.append((40, "Longest Consecutive Sequence", "Arrays and Hashing", "Medium", 20,
"""Given an unsorted array, return the length of the longest consecutive
elements sequence in O(n).

Example: [100,4,200,1,3,2] -> 4 (sequence 1,2,3,4)""",
{
"Python":'''
class Solution:
    def longestConsecutive(self, nums):
        s = set(nums); best = 0
        for n in s:
            if n-1 not in s:
                cur = n; length = 1
                while cur+1 in s: cur+=1; length+=1
                best = max(best, length)
        return best

if __name__ == "__main__":
    print(Solution().longestConsecutive([100,4,200,1,3,2]))
''',
"JavaScript":'''
var longestConsecutive = function(nums) {
    const s = new Set(nums); let best = 0;
    for (const n of s) {
        if (!s.has(n-1)) {
            let cur = n, len = 1;
            while (s.has(cur+1)) { cur++; len++; }
            best = Math.max(best, len);
        }
    }
    return best;
};
console.log(longestConsecutive([100,4,200,1,3,2]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int longestConsecutive(int[] nums) {
        Set<Integer> s = new HashSet<>();
        for (int n: nums) s.add(n);
        int best = 0;
        for (int n: s) if (!s.contains(n-1)) {
            int cur = n, len = 1;
            while (s.contains(cur+1)) { cur++; len++; }
            best = Math.max(best, len);
        }
        return best;
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().longestConsecutive(new int[]{100,4,200,1,3,2}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end()); int best = 0;
        for (int n: s) if (!s.count(n-1)) {
            int cur = n, len = 1;
            while (s.count(cur+1)) { cur++; len++; }
            best = max(best, len);
        }
        return best;
    }
};
int main(){ vector<int> v={100,4,200,1,3,2}; cout<<Solution().longestConsecutive(v)<<endl; }
''',
"Go":'''
package main
import "fmt"
func longestConsecutive(nums []int) int {
    s := map[int]bool{}
    for _,n := range nums { s[n] = true }
    best := 0
    for n := range s {
        if !s[n-1] {
            cur, l := n, 1
            for s[cur+1] { cur++; l++ }
            if l > best { best = l }
        }
    }
    return best
}
func main(){ fmt.Println(longestConsecutive([]int{100,4,200,1,3,2})) }
''',
"R":'''
longestConsecutive <- function(nums) {
    s <- unique(nums); best <- 0
    for (n in s) {
        if (!((n-1) %in% s)) {
            cur <- n; len <- 1
            while ((cur+1) %in% s) { cur <- cur+1; len <- len+1 }
            if (len > best) best <- len
        }
    }
    best
}
print(longestConsecutive(c(100,4,200,1,3,2)))
''',
}))

# ---- 041 Valid Palindrome ----
LESSONS.append((41, "Valid Palindrome", "Two Pointers", "Easy", 20,
"""Return true if s is a palindrome considering only alphanumeric chars
and ignoring case.

Example: "A man, a plan, a canal: Panama" -> true""",
{
"Python":'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            while i<j and not s[i].isalnum(): i+=1
            while i<j and not s[j].isalnum(): j-=1
            if s[i].lower() != s[j].lower(): return False
            i+=1; j-=1
        return True

if __name__ == "__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
''',
"JavaScript":'''
var isPalindrome = function(s) {
    const isAN = c => /[a-z0-9]/i.test(c);
    let i=0, j=s.length-1;
    while (i<j) {
        while (i<j && !isAN(s[i])) i++;
        while (i<j && !isAN(s[j])) j--;
        if (s[i].toLowerCase()!==s[j].toLowerCase()) return false;
        i++; j--;
    }
    return true;
};
console.log(isPalindrome("A man, a plan, a canal: Panama"), isPalindrome("race a car"));
''',
"Java":'''
public class __CLASS__ {
    public boolean isPalindrome(String s) {
        int i=0, j=s.length()-1;
        while (i<j) {
            while (i<j && !Character.isLetterOrDigit(s.charAt(i))) i++;
            while (i<j && !Character.isLetterOrDigit(s.charAt(j))) j--;
            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) return false;
            i++; j--;
        }
        return true;
    }
    public static void main(String[] a){
        __CLASS__ s = new __CLASS__();
        System.out.println(s.isPalindrome("A man, a plan, a canal: Panama"));
        System.out.println(s.isPalindrome("race a car"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool isPalindrome(string s) {
        int i=0, j=s.size()-1;
        while (i<j) {
            while (i<j && !isalnum((unsigned char)s[i])) i++;
            while (i<j && !isalnum((unsigned char)s[j])) j--;
            if (tolower((unsigned char)s[i]) != tolower((unsigned char)s[j])) return false;
            i++; j--;
        }
        return true;
    }
};
int main(){ Solution s; cout<<s.isPalindrome("A man, a plan, a canal: Panama")<<" "<<s.isPalindrome("race a car")<<endl; }
''',
"Go":'''
package main
import ("fmt"; "unicode")
func isPalindrome(s string) bool {
    r := []rune(s); i, j := 0, len(r)-1
    for i < j {
        for i<j && !unicode.IsLetter(r[i]) && !unicode.IsDigit(r[i]) { i++ }
        for i<j && !unicode.IsLetter(r[j]) && !unicode.IsDigit(r[j]) { j-- }
        if unicode.ToLower(r[i]) != unicode.ToLower(r[j]) { return false }
        i++; j--
    }
    return true
}
func main(){ fmt.Println(isPalindrome("A man, a plan, a canal: Panama"), isPalindrome("race a car")) }
''',
"R":'''
isPalindrome <- function(s) {
    s <- tolower(gsub("[^a-zA-Z0-9]", "", s))
    s == paste(rev(strsplit(s,"")[[1]]), collapse="")
}
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
''',
}))

# ---- 042 3Sum ----
LESSONS.append((42, "3Sum", "Two Pointers", "Medium", 21,
"""Given nums, return all unique triplets [a,b,c] such that a+b+c=0.

Example: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]""",
{
"Python":'''
class Solution:
    def threeSum(self, nums):
        nums.sort(); res = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]: continue
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s<0: l+=1
                elif s>0: r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]: l+=1
                    while l<r and nums[r]==nums[r-1]: r-=1
                    l+=1; r-=1
        return res

if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
''',
"JavaScript":'''
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
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums); List<List<Integer>> res = new ArrayList<>();
        for (int i=0;i<nums.length-2;i++) {
            if (i>0 && nums[i]==nums[i-1]) continue;
            int l=i+1, r=nums.length-1;
            while (l<r) {
                int s = nums[i]+nums[l]+nums[r];
                if (s<0) l++;
                else if (s>0) r--;
                else {
                    res.add(Arrays.asList(nums[i],nums[l],nums[r]));
                    while (l<r && nums[l]==nums[l+1]) l++;
                    while (l<r && nums[r]==nums[r-1]) r--;
                    l++; r--;
                }
            }
        }
        return res;
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().threeSum(new int[]{-1,0,1,2,-1,-4}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end()); vector<vector<int>> res;
        for (int i=0;i<(int)nums.size()-2;i++) {
            if (i>0 && nums[i]==nums[i-1]) continue;
            int l=i+1, r=nums.size()-1;
            while (l<r) {
                int s = nums[i]+nums[l]+nums[r];
                if (s<0) l++;
                else if (s>0) r--;
                else {
                    res.push_back({nums[i],nums[l],nums[r]});
                    while (l<r && nums[l]==nums[l+1]) l++;
                    while (l<r && nums[r]==nums[r-1]) r--;
                    l++; r--;
                }
            }
        }
        return res;
    }
};
int main(){ vector<int> v={-1,0,1,2,-1,-4}; for (auto& t: Solution().threeSum(v)) { for (int x: t) cout<<x<<" "; cout<<"|"; } cout<<endl; }
''',
"Go":'''
package main
import ("fmt"; "sort")
func threeSum(nums []int) [][]int {
    sort.Ints(nums); res := [][]int{}
    for i:=0; i<len(nums)-2; i++ {
        if i>0 && nums[i]==nums[i-1] { continue }
        l, r := i+1, len(nums)-1
        for l<r {
            s := nums[i]+nums[l]+nums[r]
            if s<0 { l++ } else if s>0 { r-- } else {
                res = append(res, []int{nums[i],nums[l],nums[r]})
                for l<r && nums[l]==nums[l+1] { l++ }
                for l<r && nums[r]==nums[r-1] { r-- }
                l++; r--
            }
        }
    }
    return res
}
func main(){ fmt.Println(threeSum([]int{-1,0,1,2,-1,-4})) }
''',
"R":'''
threeSum <- function(nums) {
    nums <- sort(nums); res <- list()
    n <- length(nums)
    for (i in seq_len(n-2)) {
        if (i>1 && nums[i]==nums[i-1]) next
        l <- i+1; r <- n
        while (l<r) {
            s <- nums[i]+nums[l]+nums[r]
            if (s<0) l <- l+1
            else if (s>0) r <- r-1
            else {
                res[[length(res)+1]] <- c(nums[i],nums[l],nums[r])
                while (l<r && nums[l]==nums[l+1]) l <- l+1
                while (l<r && nums[r]==nums[r-1]) r <- r-1
                l <- l+1; r <- r-1
            }
        }
    }
    res
}
print(threeSum(c(-1,0,1,2,-1,-4)))
''',
}))

# ---- 043 Container With Most Water ----
LESSONS.append((43, "Container With Most Water", "Two Pointers", "Medium", 21,
"""Given heights, find two lines that with the x-axis form a container
holding the most water. Return the max area.

Example: [1,8,6,2,5,4,8,3,7] -> 49""",
{
"Python":'''
class Solution:
    def maxArea(self, h):
        i, j, best = 0, len(h)-1, 0
        while i<j:
            best = max(best, (j-i)*min(h[i],h[j]))
            if h[i] < h[j]: i+=1
            else: j-=1
        return best

if __name__ == "__main__":
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
''',
"JavaScript":'''
var maxArea = function(h) {
    let i=0, j=h.length-1, best=0;
    while (i<j) {
        best = Math.max(best, (j-i)*Math.min(h[i],h[j]));
        if (h[i]<h[j]) i++; else j--;
    }
    return best;
};
console.log(maxArea([1,8,6,2,5,4,8,3,7]));
''',
"Java":'''
public class __CLASS__ {
    public int maxArea(int[] h) {
        int i=0, j=h.length-1, best=0;
        while (i<j) {
            best = Math.max(best, (j-i)*Math.min(h[i],h[j]));
            if (h[i]<h[j]) i++; else j--;
        }
        return best;
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().maxArea(new int[]{1,8,6,2,5,4,8,3,7}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& h) {
        int i=0, j=h.size()-1, best=0;
        while (i<j) {
            best = max(best, (j-i)*min(h[i],h[j]));
            if (h[i]<h[j]) i++; else j--;
        }
        return best;
    }
};
int main(){ vector<int> v={1,8,6,2,5,4,8,3,7}; cout<<Solution().maxArea(v)<<endl; }
''',
"Go":'''
package main
import "fmt"
func maxArea(h []int) int {
    i, j, best := 0, len(h)-1, 0
    min := func(a,b int) int { if a<b {return a}; return b }
    for i<j {
        a := (j-i)*min(h[i],h[j])
        if a > best { best = a }
        if h[i]<h[j] { i++ } else { j-- }
    }
    return best
}
func main(){ fmt.Println(maxArea([]int{1,8,6,2,5,4,8,3,7})) }
''',
"R":'''
maxArea <- function(h) {
    i <- 1; j <- length(h); best <- 0
    while (i<j) {
        a <- (j-i)*min(h[i],h[j])
        if (a > best) best <- a
        if (h[i] < h[j]) i <- i+1 else j <- j-1
    }
    best
}
print(maxArea(c(1,8,6,2,5,4,8,3,7)))
''',
}))

# ---- 044 Trapping Rain Water ----
LESSONS.append((44, "Trapping Rain Water", "Two Pointers", "Hard", 22,
"""Given heights, compute how much water can be trapped after raining.

Example: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6""",
{
"Python":'''
class Solution:
    def trap(self, h):
        l, r = 0, len(h)-1; lm = rm = 0; ans = 0
        while l<r:
            if h[l] < h[r]:
                lm = max(lm, h[l]); ans += lm - h[l]; l+=1
            else:
                rm = max(rm, h[r]); ans += rm - h[r]; r-=1
        return ans

if __name__ == "__main__":
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
''',
"JavaScript":'''
var trap = function(h) {
    let l=0, r=h.length-1, lm=0, rm=0, ans=0;
    while (l<r) {
        if (h[l]<h[r]) { lm=Math.max(lm,h[l]); ans+=lm-h[l]; l++; }
        else { rm=Math.max(rm,h[r]); ans+=rm-h[r]; r--; }
    }
    return ans;
};
console.log(trap([0,1,0,2,1,0,1,3,2,1,2,1]));
''',
"Java":'''
public class __CLASS__ {
    public int trap(int[] h) {
        int l=0, r=h.length-1, lm=0, rm=0, ans=0;
        while (l<r) {
            if (h[l]<h[r]) { lm=Math.max(lm,h[l]); ans+=lm-h[l]; l++; }
            else { rm=Math.max(rm,h[r]); ans+=rm-h[r]; r--; }
        }
        return ans;
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().trap(new int[]{0,1,0,2,1,0,1,3,2,1,2,1}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int trap(vector<int>& h) {
        int l=0, r=h.size()-1, lm=0, rm=0, ans=0;
        while (l<r) {
            if (h[l]<h[r]) { lm=max(lm,h[l]); ans+=lm-h[l]; l++; }
            else { rm=max(rm,h[r]); ans+=rm-h[r]; r--; }
        }
        return ans;
    }
};
int main(){ vector<int> v={0,1,0,2,1,0,1,3,2,1,2,1}; cout<<Solution().trap(v)<<endl; }
''',
"Go":'''
package main
import "fmt"
func trap(h []int) int {
    l, r, lm, rm, ans := 0, len(h)-1, 0, 0, 0
    max := func(a,b int) int { if a>b {return a}; return b }
    for l<r {
        if h[l]<h[r] { lm = max(lm,h[l]); ans += lm-h[l]; l++ } else { rm = max(rm,h[r]); ans += rm-h[r]; r-- }
    }
    return ans
}
func main(){ fmt.Println(trap([]int{0,1,0,2,1,0,1,3,2,1,2,1})) }
''',
"R":'''
trap <- function(h) {
    l <- 1; r <- length(h); lm <- 0; rm <- 0; ans <- 0
    while (l<r) {
        if (h[l] < h[r]) { lm <- max(lm,h[l]); ans <- ans + lm - h[l]; l <- l+1 }
        else { rm <- max(rm,h[r]); ans <- ans + rm - h[r]; r <- r-1 }
    }
    ans
}
print(trap(c(0,1,0,2,1,0,1,3,2,1,2,1)))
''',
}))

# ---- 045 Best Time to Buy and Sell Stock ----
LESSONS.append((45, "Best Time to Buy and Sell Stock", "Sliding Window", "Easy", 22,
"""Given prices, return the maximum profit from a single buy/sell.

Example: [7,1,5,3,6,4] -> 5""",
{
"Python":'''
class Solution:
    def maxProfit(self, prices):
        lo = float("inf"); best = 0
        for p in prices:
            if p < lo: lo = p
            elif p - lo > best: best = p - lo
        return best

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
''',
"JavaScript":'''
var maxProfit = function(prices) {
    let lo = Infinity, best = 0;
    for (const p of prices) {
        if (p < lo) lo = p;
        else if (p - lo > best) best = p - lo;
    }
    return best;
};
console.log(maxProfit([7,1,5,3,6,4]));
''',
"Java":'''
public class __CLASS__ {
    public int maxProfit(int[] prices) {
        int lo = Integer.MAX_VALUE, best = 0;
        for (int p: prices) {
            if (p < lo) lo = p;
            else if (p - lo > best) best = p - lo;
        }
        return best;
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().maxProfit(new int[]{7,1,5,3,6,4}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lo = INT_MAX, best = 0;
        for (int p: prices) { if (p<lo) lo=p; else if (p-lo>best) best=p-lo; }
        return best;
    }
};
int main(){ vector<int> v={7,1,5,3,6,4}; cout<<Solution().maxProfit(v)<<endl; }
''',
"Go":'''
package main
import ("fmt"; "math")
func maxProfit(prices []int) int {
    lo := math.MaxInt32; best := 0
    for _,p := range prices {
        if p < lo { lo = p } else if p - lo > best { best = p - lo }
    }
    return best
}
func main(){ fmt.Println(maxProfit([]int{7,1,5,3,6,4})) }
''',
"R":'''
maxProfit <- function(prices) {
    lo <- Inf; best <- 0
    for (p in prices) {
        if (p < lo) lo <- p
        else if (p - lo > best) best <- p - lo
    }
    best
}
print(maxProfit(c(7,1,5,3,6,4)))
''',
}))

# ---- 046 Longest Substring Without Repeating Characters ----
LESSONS.append((46, "Longest Substring Without Repeating Characters", "Sliding Window", "Medium", 23,
"""Given a string, find the length of the longest substring without
repeating characters.

Example: "abcabcbb" -> 3""",
{
"Python":'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}; l = 0; best = 0
        for r,c in enumerate(s):
            if c in seen and seen[c] >= l: l = seen[c] + 1
            seen[c] = r
            best = max(best, r - l + 1)
        return best

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
''',
"JavaScript":'''
var lengthOfLongestSubstring = function(s) {
    const seen = {}; let l = 0, best = 0;
    for (let r=0;r<s.length;r++) {
        const c = s[r];
        if (seen[c] !== undefined && seen[c] >= l) l = seen[c] + 1;
        seen[c] = r;
        best = Math.max(best, r - l + 1);
    }
    return best;
};
console.log(lengthOfLongestSubstring("abcabcbb"), lengthOfLongestSubstring("bbbbb"));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int lengthOfLongestSubstring(String s) {
        Map<Character,Integer> seen = new HashMap<>();
        int l=0, best=0;
        for (int r=0;r<s.length();r++) {
            char c = s.charAt(r);
            if (seen.containsKey(c) && seen.get(c) >= l) l = seen.get(c)+1;
            seen.put(c, r);
            best = Math.max(best, r-l+1);
        }
        return best;
    }
    public static void main(String[] a){
        __CLASS__ s = new __CLASS__();
        System.out.println(s.lengthOfLongestSubstring("abcabcbb"));
        System.out.println(s.lengthOfLongestSubstring("bbbbb"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> seen; int l=0, best=0;
        for (int r=0;r<(int)s.size();r++) {
            auto it = seen.find(s[r]);
            if (it!=seen.end() && it->second>=l) l = it->second+1;
            seen[s[r]] = r;
            best = max(best, r-l+1);
        }
        return best;
    }
};
int main(){ Solution s; cout<<s.lengthOfLongestSubstring("abcabcbb")<<" "<<s.lengthOfLongestSubstring("bbbbb")<<endl; }
''',
"Go":'''
package main
import "fmt"
func lengthOfLongestSubstring(s string) int {
    seen := map[byte]int{}; l, best := 0, 0
    for r:=0;r<len(s);r++ {
        if v,ok := seen[s[r]]; ok && v >= l { l = v + 1 }
        seen[s[r]] = r
        if r-l+1 > best { best = r-l+1 }
    }
    return best
}
func main(){ fmt.Println(lengthOfLongestSubstring("abcabcbb"), lengthOfLongestSubstring("bbbbb")) }
''',
"R":'''
lengthOfLongestSubstring <- function(s) {
    chars <- strsplit(s,"")[[1]]; seen <- list(); l <- 1; best <- 0
    for (r in seq_along(chars)) {
        c <- chars[r]
        if (!is.null(seen[[c]]) && seen[[c]] >= l) l <- seen[[c]] + 1
        seen[[c]] <- r
        if (r - l + 1 > best) best <- r - l + 1
    }
    best
}
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
''',
}))

# ---- 047 Longest Repeating Character Replacement ----
LESSONS.append((47, "Longest Repeating Character Replacement", "Sliding Window", "Medium", 23,
"""Given a string s and integer k, you can change at most k characters.
Return length of the longest substring with all same characters.

Example: s="AABABBA", k=1 -> 4""",
{
"Python":'''
class Solution:
    def characterReplacement(self, s, k):
        cnt = {}; l = 0; best = 0; mf = 0
        for r,c in enumerate(s):
            cnt[c] = cnt.get(c,0)+1
            mf = max(mf, cnt[c])
            if r - l + 1 - mf > k:
                cnt[s[l]] -= 1; l += 1
            best = max(best, r - l + 1)
        return best

if __name__ == "__main__":
    print(Solution().characterReplacement("AABABBA", 1))
''',
"JavaScript":'''
var characterReplacement = function(s, k) {
    const cnt = {}; let l=0, best=0, mf=0;
    for (let r=0;r<s.length;r++) {
        cnt[s[r]] = (cnt[s[r]]||0)+1;
        mf = Math.max(mf, cnt[s[r]]);
        if (r - l + 1 - mf > k) { cnt[s[l]]--; l++; }
        best = Math.max(best, r - l + 1);
    }
    return best;
};
console.log(characterReplacement("AABABBA", 1));
''',
"Java":'''
public class __CLASS__ {
    public int characterReplacement(String s, int k) {
        int[] cnt = new int[26]; int l=0, best=0, mf=0;
        for (int r=0;r<s.length();r++) {
            cnt[s.charAt(r)-'A']++;
            mf = Math.max(mf, cnt[s.charAt(r)-'A']);
            if (r - l + 1 - mf > k) { cnt[s.charAt(l)-'A']--; l++; }
            best = Math.max(best, r - l + 1);
        }
        return best;
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().characterReplacement("AABABBA", 1));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int characterReplacement(string s, int k) {
        int cnt[26] = {0}; int l=0, best=0, mf=0;
        for (int r=0;r<(int)s.size();r++) {
            cnt[s[r]-'A']++;
            mf = max(mf, cnt[s[r]-'A']);
            if (r - l + 1 - mf > k) { cnt[s[l]-'A']--; l++; }
            best = max(best, r - l + 1);
        }
        return best;
    }
};
int main(){ cout<<Solution().characterReplacement("AABABBA", 1)<<endl; }
''',
"Go":'''
package main
import "fmt"
func characterReplacement(s string, k int) int {
    var cnt [26]int; l, best, mf := 0, 0, 0
    max := func(a,b int) int { if a>b {return a}; return b }
    for r:=0; r<len(s); r++ {
        cnt[s[r]-'A']++; mf = max(mf, cnt[s[r]-'A'])
        if r - l + 1 - mf > k { cnt[s[l]-'A']--; l++ }
        best = max(best, r - l + 1)
    }
    return best
}
func main(){ fmt.Println(characterReplacement("AABABBA", 1)) }
''',
"R":'''
characterReplacement <- function(s, k) {
    chars <- strsplit(s,"")[[1]]; cnt <- list(); l <- 1; best <- 0; mf <- 0
    for (r in seq_along(chars)) {
        c <- chars[r]
        cnt[[c]] <- if (is.null(cnt[[c]])) 1 else cnt[[c]] + 1
        if (cnt[[c]] > mf) mf <- cnt[[c]]
        if (r - l + 1 - mf > k) {
            cnt[[chars[l]]] <- cnt[[chars[l]]] - 1
            l <- l + 1
        }
        if (r - l + 1 > best) best <- r - l + 1
    }
    best
}
print(characterReplacement("AABABBA", 1))
''',
}))

# ---- 048 Permutation in String ----
LESSONS.append((48, "Permutation in String", "Sliding Window", "Medium", 24,
"""Given s1 and s2, return true if s2 contains a permutation of s1.

Example: s1="ab", s2="eidbaooo" -> true""",
{
"Python":'''
class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2): return False
        a = [0]*26; b = [0]*26
        for c in s1: a[ord(c)-97]+=1
        for i in range(len(s1)): b[ord(s2[i])-97]+=1
        if a==b: return True
        for i in range(len(s1), len(s2)):
            b[ord(s2[i])-97]+=1
            b[ord(s2[i-len(s1)])-97]-=1
            if a==b: return True
        return False

if __name__ == "__main__":
    print(Solution().checkInclusion("ab","eidbaooo"))
    print(Solution().checkInclusion("ab","eidboaoo"))
''',
"JavaScript":'''
var checkInclusion = function(s1, s2) {
    if (s1.length > s2.length) return false;
    const a = new Array(26).fill(0), b = new Array(26).fill(0);
    for (const c of s1) a[c.charCodeAt(0)-97]++;
    for (let i=0;i<s1.length;i++) b[s2.charCodeAt(i)-97]++;
    const eq = () => a.every((v,i)=>v===b[i]);
    if (eq()) return true;
    for (let i=s1.length;i<s2.length;i++) {
        b[s2.charCodeAt(i)-97]++;
        b[s2.charCodeAt(i-s1.length)-97]--;
        if (eq()) return true;
    }
    return false;
};
console.log(checkInclusion("ab","eidbaooo"), checkInclusion("ab","eidboaoo"));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length()>s2.length()) return false;
        int[] a = new int[26], b = new int[26];
        for (int i=0;i<s1.length();i++) { a[s1.charAt(i)-'a']++; b[s2.charAt(i)-'a']++; }
        if (Arrays.equals(a,b)) return true;
        for (int i=s1.length();i<s2.length();i++) {
            b[s2.charAt(i)-'a']++;
            b[s2.charAt(i-s1.length())-'a']--;
            if (Arrays.equals(a,b)) return true;
        }
        return false;
    }
    public static void main(String[] x){
        __CLASS__ s = new __CLASS__();
        System.out.println(s.checkInclusion("ab","eidbaooo"));
        System.out.println(s.checkInclusion("ab","eidboaoo"));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size()>s2.size()) return false;
        int a[26]={0}, b[26]={0};
        for (size_t i=0;i<s1.size();i++) { a[s1[i]-'a']++; b[s2[i]-'a']++; }
        auto eq = [&](){ for (int i=0;i<26;i++) if (a[i]!=b[i]) return false; return true; };
        if (eq()) return true;
        for (size_t i=s1.size();i<s2.size();i++) {
            b[s2[i]-'a']++;
            b[s2[i-s1.size()]-'a']--;
            if (eq()) return true;
        }
        return false;
    }
};
int main(){ Solution s; cout<<s.checkInclusion("ab","eidbaooo")<<" "<<s.checkInclusion("ab","eidboaoo")<<endl; }
''',
"Go":'''
package main
import "fmt"
func checkInclusion(s1, s2 string) bool {
    if len(s1) > len(s2) { return false }
    var a, b [26]int
    for i:=0;i<len(s1);i++ { a[s1[i]-'a']++; b[s2[i]-'a']++ }
    if a==b { return true }
    for i:=len(s1); i<len(s2); i++ {
        b[s2[i]-'a']++; b[s2[i-len(s1)]-'a']--
        if a==b { return true }
    }
    return false
}
func main(){ fmt.Println(checkInclusion("ab","eidbaooo"), checkInclusion("ab","eidboaoo")) }
''',
"R":'''
checkInclusion <- function(s1, s2) {
    if (nchar(s1) > nchar(s2)) return(FALSE)
    a <- table(factor(strsplit(s1,"")[[1]], levels=letters))
    n <- nchar(s1)
    for (i in 1:(nchar(s2)-n+1)) {
        sub <- substr(s2, i, i+n-1)
        b <- table(factor(strsplit(sub,"")[[1]], levels=letters))
        if (all(a==b)) return(TRUE)
    }
    FALSE
}
print(checkInclusion("ab","eidbaooo"))
print(checkInclusion("ab","eidboaoo"))
''',
}))

# ---- 049 Min Stack ----
LESSONS.append((49, "Min Stack", "Stack", "Medium", 24,
"""Design a stack supporting push, pop, top, and getMin in O(1).""",
{
"Python":'''
class MinStack:
    def __init__(self):
        self.s = []; self.m = []
    def push(self, val):
        self.s.append(val)
        self.m.append(val if not self.m else min(val, self.m[-1]))
    def pop(self): self.s.pop(); self.m.pop()
    def top(self): return self.s[-1]
    def getMin(self): return self.m[-1]

if __name__ == "__main__":
    s = MinStack(); s.push(-2); s.push(0); s.push(-3)
    print(s.getMin()); s.pop(); print(s.top()); print(s.getMin())
''',
"JavaScript":'''
class MinStack {
    constructor(){ this.s=[]; this.m=[]; }
    push(v){ this.s.push(v); this.m.push(this.m.length?Math.min(v,this.m[this.m.length-1]):v); }
    pop(){ this.s.pop(); this.m.pop(); }
    top(){ return this.s[this.s.length-1]; }
    getMin(){ return this.m[this.m.length-1]; }
}
const s = new MinStack(); s.push(-2); s.push(0); s.push(-3);
console.log(s.getMin()); s.pop(); console.log(s.top()); console.log(s.getMin());
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class MinStack {
        Deque<Integer> s = new ArrayDeque<>(), m = new ArrayDeque<>();
        public void push(int v){ s.push(v); m.push(m.isEmpty()?v:Math.min(v,m.peek())); }
        public void pop(){ s.pop(); m.pop(); }
        public int top(){ return s.peek(); }
        public int getMin(){ return m.peek(); }
    }
    public static void main(String[] a){
        MinStack s = new MinStack(); s.push(-2); s.push(0); s.push(-3);
        System.out.println(s.getMin()); s.pop();
        System.out.println(s.top()); System.out.println(s.getMin());
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class MinStack {
    stack<int> s, m;
public:
    void push(int v){ s.push(v); m.push(m.empty()?v:min(v,m.top())); }
    void pop(){ s.pop(); m.pop(); }
    int top(){ return s.top(); }
    int getMin(){ return m.top(); }
};
int main(){ MinStack s; s.push(-2); s.push(0); s.push(-3); cout<<s.getMin()<<" "; s.pop(); cout<<s.top()<<" "<<s.getMin()<<endl; }
''',
"Go":'''
package main
import "fmt"
type MinStack struct{ s, m []int }
func (st *MinStack) Push(v int){
    st.s = append(st.s, v)
    if len(st.m)==0 || v < st.m[len(st.m)-1] { st.m = append(st.m, v) } else { st.m = append(st.m, st.m[len(st.m)-1]) }
}
func (st *MinStack) Pop(){ st.s = st.s[:len(st.s)-1]; st.m = st.m[:len(st.m)-1] }
func (st *MinStack) Top() int { return st.s[len(st.s)-1] }
func (st *MinStack) GetMin() int { return st.m[len(st.m)-1] }
func main(){
    s := &MinStack{}; s.Push(-2); s.Push(0); s.Push(-3)
    fmt.Println(s.GetMin()); s.Pop(); fmt.Println(s.Top()); fmt.Println(s.GetMin())
}
''',
"R":'''
MinStack <- function() {
    s <- c(); m <- c()
    list(
        push = function(v){ s <<- c(s, v); m <<- c(m, if (length(m)==0) v else min(v, m[length(m)])) },
        pop  = function(){ s <<- s[-length(s)]; m <<- m[-length(m)] },
        top  = function() s[length(s)],
        getMin = function() m[length(m)]
    )
}
st <- MinStack(); st$push(-2); st$push(0); st$push(-3)
print(st$getMin()); st$pop(); print(st$top()); print(st$getMin())
''',
}))

# ---- 050 Evaluate Reverse Polish Notation ----
LESSONS.append((50, "Evaluate Reverse Polish Notation", "Stack", "Medium", 25,
"""Evaluate an arithmetic expression in Reverse Polish Notation.

Example: ["2","1","+","3","*"] -> 9""",
{
"Python":'''
class Solution:
    def evalRPN(self, tokens):
        st = []
        for t in tokens:
            if t in "+-*/":
                b = st.pop(); a = st.pop()
                if t=="+": st.append(a+b)
                elif t=="-": st.append(a-b)
                elif t=="*": st.append(a*b)
                else: st.append(int(a/b))
            else: st.append(int(t))
        return st[0]

if __name__ == "__main__":
    print(Solution().evalRPN(["2","1","+","3","*"]))
''',
"JavaScript":'''
var evalRPN = function(tokens) {
    const st = [];
    for (const t of tokens) {
        if ("+-*/".includes(t)) {
            const b = st.pop(), a = st.pop();
            if (t==="+") st.push(a+b);
            else if (t==="-") st.push(a-b);
            else if (t==="*") st.push(a*b);
            else st.push(Math.trunc(a/b));
        } else st.push(parseInt(t));
    }
    return st[0];
};
console.log(evalRPN(["2","1","+","3","*"]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int evalRPN(String[] tokens) {
        Deque<Integer> st = new ArrayDeque<>();
        for (String t: tokens) {
            if ("+-*/".contains(t) && t.length()==1) {
                int b = st.pop(), a = st.pop();
                switch (t.charAt(0)) {
                    case '+': st.push(a+b); break;
                    case '-': st.push(a-b); break;
                    case '*': st.push(a*b); break;
                    default:  st.push(a/b);
                }
            } else st.push(Integer.parseInt(t));
        }
        return st.pop();
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().evalRPN(new String[]{"2","1","+","3","*"}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for (auto& t: tokens) {
            if (t=="+"||t=="-"||t=="*"||t=="/") {
                int b = st.top(); st.pop(); int a = st.top(); st.pop();
                if (t=="+") st.push(a+b);
                else if (t=="-") st.push(a-b);
                else if (t=="*") st.push(a*b);
                else st.push(a/b);
            } else st.push(stoi(t));
        }
        return st.top();
    }
};
int main(){ vector<string> v={"2","1","+","3","*"}; cout<<Solution().evalRPN(v)<<endl; }
''',
"Go":'''
package main
import ("fmt"; "strconv")
func evalRPN(tokens []string) int {
    st := []int{}
    for _,t := range tokens {
        switch t {
        case "+","-","*","/":
            b := st[len(st)-1]; a := st[len(st)-2]; st = st[:len(st)-2]
            switch t {
            case "+": st = append(st, a+b)
            case "-": st = append(st, a-b)
            case "*": st = append(st, a*b)
            case "/": st = append(st, a/b)
            }
        default:
            n, _ := strconv.Atoi(t); st = append(st, n)
        }
    }
    return st[0]
}
func main(){ fmt.Println(evalRPN([]string{"2","1","+","3","*"})) }
''',
"R":'''
evalRPN <- function(tokens) {
    st <- c()
    for (t in tokens) {
        if (t %in% c("+","-","*","/")) {
            b <- st[length(st)]; a <- st[length(st)-1]; st <- st[-c(length(st)-1, length(st))]
            r <- switch(t, "+"=a+b, "-"=a-b, "*"=a*b, "/"=as.integer(a/b))
            st <- c(st, r)
        } else st <- c(st, as.integer(t))
    }
    st[1]
}
print(evalRPN(c("2","1","+","3","*")))
''',
}))

# ---- 051 Generate Parentheses ----
LESSONS.append((51, "Generate Parentheses", "Stack", "Medium", 25,
"""Given n, return all valid combinations of n pairs of parentheses.

Example: n=3 -> ["((()))","(()())","(())()","()(())","()()()"]""",
{
"Python":'''
class Solution:
    def generateParenthesis(self, n):
        res = []
        def bt(cur, o, c):
            if len(cur) == 2*n: res.append(cur); return
            if o < n: bt(cur+"(", o+1, c)
            if c < o: bt(cur+")", o, c+1)
        bt("", 0, 0)
        return res

if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
''',
"JavaScript":'''
var generateParenthesis = function(n) {
    const res = [];
    const bt = (cur, o, c) => {
        if (cur.length === 2*n) { res.push(cur); return; }
        if (o < n) bt(cur+"(", o+1, c);
        if (c < o) bt(cur+")", o, c+1);
    };
    bt("", 0, 0);
    return res;
};
console.log(generateParenthesis(3));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        bt(res, "", 0, 0, n);
        return res;
    }
    private void bt(List<String> r, String cur, int o, int c, int n) {
        if (cur.length()==2*n) { r.add(cur); return; }
        if (o<n) bt(r, cur+"(", o+1, c, n);
        if (c<o) bt(r, cur+")", o, c+1, n);
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().generateParenthesis(3));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
    void bt(vector<string>& r, string cur, int o, int c, int n) {
        if ((int)cur.size()==2*n) { r.push_back(cur); return; }
        if (o<n) bt(r, cur+"(", o+1, c, n);
        if (c<o) bt(r, cur+")", o, c+1, n);
    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> r; bt(r, "", 0, 0, n); return r;
    }
};
int main(){ for (auto& s: Solution().generateParenthesis(3)) cout<<s<<" "; cout<<endl; }
''',
"Go":'''
package main
import "fmt"
func generateParenthesis(n int) []string {
    res := []string{}
    var bt func(cur string, o, c int)
    bt = func(cur string, o, c int) {
        if len(cur) == 2*n { res = append(res, cur); return }
        if o < n { bt(cur+"(", o+1, c) }
        if c < o { bt(cur+")", o, c+1) }
    }
    bt("", 0, 0)
    return res
}
func main(){ fmt.Println(generateParenthesis(3)) }
''',
"R":'''
generateParenthesis <- function(n) {
    res <- c()
    bt <- function(cur, o, c) {
        if (nchar(cur) == 2*n) { res[[length(res)+1]] <<- cur; return() }
        if (o < n) bt(paste0(cur,"("), o+1, c)
        if (c < o) bt(paste0(cur,")"), o, c+1)
    }
    bt("", 0, 0)
    res
}
print(generateParenthesis(3))
''',
}))

# ---- 052 Daily Temperatures ----
LESSONS.append((52, "Daily Temperatures", "Stack", "Medium", 26,
"""Given temperatures, for each day return the number of days until a
warmer temperature, or 0 if none.

Example: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]""",
{
"Python":'''
class Solution:
    def dailyTemperatures(self, t):
        n = len(t); res = [0]*n; st = []
        for i,v in enumerate(t):
            while st and t[st[-1]] < v:
                j = st.pop(); res[j] = i - j
            st.append(i)
        return res

if __name__ == "__main__":
    print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
''',
"JavaScript":'''
var dailyTemperatures = function(t) {
    const n = t.length, res = new Array(n).fill(0), st = [];
    for (let i=0;i<n;i++) {
        while (st.length && t[st[st.length-1]] < t[i]) {
            const j = st.pop(); res[j] = i - j;
        }
        st.push(i);
    }
    return res;
};
console.log(dailyTemperatures([73,74,75,71,69,72,76,73]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int[] dailyTemperatures(int[] t) {
        int n = t.length; int[] res = new int[n];
        Deque<Integer> st = new ArrayDeque<>();
        for (int i=0;i<n;i++) {
            while (!st.isEmpty() && t[st.peek()] < t[i]) {
                int j = st.pop(); res[j] = i - j;
            }
            st.push(i);
        }
        return res;
    }
    public static void main(String[] a){
        System.out.println(Arrays.toString(new __CLASS__().dailyTemperatures(new int[]{73,74,75,71,69,72,76,73})));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& t) {
        int n = t.size(); vector<int> res(n,0); stack<int> st;
        for (int i=0;i<n;i++) {
            while (!st.empty() && t[st.top()] < t[i]) {
                int j = st.top(); st.pop(); res[j] = i - j;
            }
            st.push(i);
        }
        return res;
    }
};
int main(){ vector<int> v={73,74,75,71,69,72,76,73}; for (int x: Solution().dailyTemperatures(v)) cout<<x<<" "; cout<<endl; }
''',
"Go":'''
package main
import "fmt"
func dailyTemperatures(t []int) []int {
    n := len(t); res := make([]int, n); st := []int{}
    for i:=0;i<n;i++ {
        for len(st)>0 && t[st[len(st)-1]] < t[i] {
            j := st[len(st)-1]; st = st[:len(st)-1]; res[j] = i - j
        }
        st = append(st, i)
    }
    return res
}
func main(){ fmt.Println(dailyTemperatures([]int{73,74,75,71,69,72,76,73})) }
''',
"R":'''
dailyTemperatures <- function(t) {
    n <- length(t); res <- rep(0L, n); st <- c()
    for (i in seq_len(n)) {
        while (length(st)>0 && t[st[length(st)]] < t[i]) {
            j <- st[length(st)]; st <- st[-length(st)]; res[j] <- i - j
        }
        st <- c(st, i)
    }
    res
}
print(dailyTemperatures(c(73,74,75,71,69,72,76,73)))
''',
}))

# ---- 053 Car Fleet ----
LESSONS.append((53, "Car Fleet", "Stack", "Medium", 26,
"""Cars at given positions move toward target with given speeds. A car
that catches up forms a fleet. Return the number of fleets that arrive.

Example: target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3] -> 3""",
{
"Python":'''
class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        st = []
        for p,s in cars:
            t = (target - p) / s
            if not st or t > st[-1]: st.append(t)
        return len(st)

if __name__ == "__main__":
    print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
''',
"JavaScript":'''
var carFleet = function(target, position, speed) {
    const cars = position.map((p,i)=>[p,speed[i]]).sort((a,b)=>b[0]-a[0]);
    const st = [];
    for (const [p,s] of cars) {
        const t = (target - p) / s;
        if (!st.length || t > st[st.length-1]) st.push(t);
    }
    return st.length;
};
console.log(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Integer[] idx = new Integer[n];
        for (int i=0;i<n;i++) idx[i] = i;
        Arrays.sort(idx, (a,b) -> position[b] - position[a]);
        Deque<Double> st = new ArrayDeque<>();
        for (int i: idx) {
            double t = (double)(target - position[i]) / speed[i];
            if (st.isEmpty() || t > st.peek()) st.push(t);
        }
        return st.size();
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().carFleet(12, new int[]{10,8,0,5,3}, new int[]{2,4,1,1,3}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int,int>> cars(n);
        for (int i=0;i<n;i++) cars[i] = {position[i], speed[i]};
        sort(cars.begin(), cars.end(), greater<>());
        vector<double> st;
        for (auto& [p,s]: cars) {
            double t = (double)(target - p) / s;
            if (st.empty() || t > st.back()) st.push_back(t);
        }
        return st.size();
    }
};
int main(){ vector<int> p={10,8,0,5,3}, s={2,4,1,1,3}; cout<<Solution().carFleet(12, p, s)<<endl; }
''',
"Go":'''
package main
import ("fmt"; "sort")
func carFleet(target int, position, speed []int) int {
    n := len(position); idx := make([]int, n)
    for i := range idx { idx[i] = i }
    sort.Slice(idx, func(i, j int) bool { return position[idx[i]] > position[idx[j]] })
    st := []float64{}
    for _, i := range idx {
        t := float64(target-position[i]) / float64(speed[i])
        if len(st)==0 || t > st[len(st)-1] { st = append(st, t) }
    }
    return len(st)
}
func main(){ fmt.Println(carFleet(12, []int{10,8,0,5,3}, []int{2,4,1,1,3})) }
''',
"R":'''
carFleet <- function(target, position, speed) {
    o <- order(position, decreasing=TRUE)
    p <- position[o]; s <- speed[o]; st <- c()
    for (i in seq_along(p)) {
        t <- (target - p[i]) / s[i]
        if (length(st)==0 || t > st[length(st)]) st <- c(st, t)
    }
    length(st)
}
print(carFleet(12, c(10,8,0,5,3), c(2,4,1,1,3)))
''',
}))

# ---- 054 Largest Rectangle in Histogram ----
LESSONS.append((54, "Largest Rectangle in Histogram", "Stack", "Hard", 27,
"""Given heights of bars, find the area of the largest rectangle.

Example: [2,1,5,6,2,3] -> 10""",
{
"Python":'''
class Solution:
    def largestRectangleArea(self, h):
        st = []; best = 0
        h2 = h + [0]
        for i,v in enumerate(h2):
            start = i
            while st and st[-1][1] > v:
                idx, height = st.pop()
                best = max(best, height*(i-idx))
                start = idx
            st.append((start, v))
        return best

if __name__ == "__main__":
    print(Solution().largestRectangleArea([2,1,5,6,2,3]))
''',
"JavaScript":'''
var largestRectangleArea = function(h) {
    const st = []; let best = 0;
    const h2 = [...h, 0];
    for (let i=0;i<h2.length;i++) {
        let start = i;
        while (st.length && st[st.length-1][1] > h2[i]) {
            const [idx, ht] = st.pop();
            best = Math.max(best, ht*(i-idx));
            start = idx;
        }
        st.push([start, h2[i]]);
    }
    return best;
};
console.log(largestRectangleArea([2,1,5,6,2,3]));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    public int largestRectangleArea(int[] h) {
        Deque<int[]> st = new ArrayDeque<>(); int best = 0;
        int n = h.length;
        for (int i=0;i<=n;i++) {
            int v = (i==n) ? 0 : h[i];
            int start = i;
            while (!st.isEmpty() && st.peek()[1] > v) {
                int[] top = st.pop();
                best = Math.max(best, top[1] * (i - top[0]));
                start = top[0];
            }
            st.push(new int[]{start, v});
        }
        return best;
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().largestRectangleArea(new int[]{2,1,5,6,2,3}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int largestRectangleArea(vector<int>& h) {
        stack<pair<int,int>> st; int best = 0; int n = h.size();
        for (int i=0;i<=n;i++) {
            int v = (i==n) ? 0 : h[i];
            int start = i;
            while (!st.empty() && st.top().second > v) {
                auto [idx, ht] = st.top(); st.pop();
                best = max(best, ht*(i-idx));
                start = idx;
            }
            st.push({start, v});
        }
        return best;
    }
};
int main(){ vector<int> v={2,1,5,6,2,3}; cout<<Solution().largestRectangleArea(v)<<endl; }
''',
"Go":'''
package main
import "fmt"
func largestRectangleArea(h []int) int {
    type p struct{ i, v int }
    st := []p{}; best := 0; n := len(h)
    max := func(a,b int) int { if a>b {return a}; return b }
    for i:=0;i<=n;i++ {
        var v int; if i==n { v = 0 } else { v = h[i] }
        start := i
        for len(st)>0 && st[len(st)-1].v > v {
            top := st[len(st)-1]; st = st[:len(st)-1]
            best = max(best, top.v*(i-top.i))
            start = top.i
        }
        st = append(st, p{start, v})
    }
    return best
}
func main(){ fmt.Println(largestRectangleArea([]int{2,1,5,6,2,3})) }
''',
"R":'''
largestRectangleArea <- function(h) {
    st_i <- c(); st_v <- c(); best <- 0
    h2 <- c(h, 0)
    for (i in seq_along(h2)) {
        start <- i
        while (length(st_v) > 0 && st_v[length(st_v)] > h2[i]) {
            idx <- st_i[length(st_i)]; ht <- st_v[length(st_v)]
            st_i <- st_i[-length(st_i)]; st_v <- st_v[-length(st_v)]
            best <- max(best, ht*(i-idx))
            start <- idx
        }
        st_i <- c(st_i, start); st_v <- c(st_v, h2[i])
    }
    best
}
print(largestRectangleArea(c(2,1,5,6,2,3)))
''',
}))

# ---- 055 Search a 2D Matrix ----
LESSONS.append((55, "Search a 2D Matrix", "Binary Search", "Medium", 27,
"""Given an m x n matrix sorted row-wise (and each row's first > prev row's last),
search for target.

Example: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 -> true""",
{
"Python":'''
class Solution:
    def searchMatrix(self, m, target):
        if not m or not m[0]: return False
        rows, cols = len(m), len(m[0])
        l, r = 0, rows*cols - 1
        while l <= r:
            mid = (l+r)//2
            v = m[mid//cols][mid%cols]
            if v == target: return True
            if v < target: l = mid+1
            else: r = mid-1
        return False

if __name__ == "__main__":
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
''',
"JavaScript":'''
var searchMatrix = function(m, target) {
    if (!m.length || !m[0].length) return false;
    const rows = m.length, cols = m[0].length;
    let l = 0, r = rows*cols - 1;
    while (l <= r) {
        const mid = (l+r) >> 1;
        const v = m[Math.floor(mid/cols)][mid%cols];
        if (v === target) return true;
        if (v < target) l = mid+1; else r = mid-1;
    }
    return false;
};
console.log(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3));
console.log(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13));
''',
"Java":'''
public class __CLASS__ {
    public boolean searchMatrix(int[][] m, int target) {
        if (m.length==0 || m[0].length==0) return false;
        int rows = m.length, cols = m[0].length;
        int l = 0, r = rows*cols - 1;
        while (l <= r) {
            int mid = (l+r)/2;
            int v = m[mid/cols][mid%cols];
            if (v == target) return true;
            if (v < target) l = mid+1; else r = mid-1;
        }
        return false;
    }
    public static void main(String[] a){
        int[][] m = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
        __CLASS__ s = new __CLASS__();
        System.out.println(s.searchMatrix(m, 3));
        System.out.println(s.searchMatrix(m, 13));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& m, int target) {
        if (m.empty() || m[0].empty()) return false;
        int rows = m.size(), cols = m[0].size();
        int l = 0, r = rows*cols - 1;
        while (l <= r) {
            int mid = (l+r)/2;
            int v = m[mid/cols][mid%cols];
            if (v == target) return true;
            if (v < target) l = mid+1; else r = mid-1;
        }
        return false;
    }
};
int main(){ vector<vector<int>> m = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    cout<<Solution().searchMatrix(m,3)<<" "<<Solution().searchMatrix(m,13)<<endl; }
''',
"Go":'''
package main
import "fmt"
func searchMatrix(m [][]int, target int) bool {
    if len(m)==0 || len(m[0])==0 { return false }
    rows, cols := len(m), len(m[0])
    l, r := 0, rows*cols - 1
    for l <= r {
        mid := (l+r)/2
        v := m[mid/cols][mid%cols]
        if v == target { return true }
        if v < target { l = mid+1 } else { r = mid-1 }
    }
    return false
}
func main(){
    m := [][]int{{1,3,5,7},{10,11,16,20},{23,30,34,60}}
    fmt.Println(searchMatrix(m, 3), searchMatrix(m, 13))
}
''',
"R":'''
searchMatrix <- function(m, target) {
    if (length(m)==0) return(FALSE)
    rows <- nrow(m); cols <- ncol(m)
    l <- 0; r <- rows*cols - 1
    while (l <= r) {
        mid <- (l+r) %/% 2
        rr <- mid %/% cols + 1; cc <- mid %% cols + 1
        v <- m[rr, cc]
        if (v == target) return(TRUE)
        if (v < target) l <- mid+1 else r <- mid-1
    }
    FALSE
}
m <- matrix(c(1,3,5,7,10,11,16,20,23,30,34,60), nrow=3, byrow=TRUE)
print(searchMatrix(m, 3))
print(searchMatrix(m, 13))
''',
}))

# ---- 056 Koko Eating Bananas ----
LESSONS.append((56, "Koko Eating Bananas", "Binary Search", "Medium", 28,
"""Koko eats bananas at speed k per hour. Given piles and h hours,
return the minimum k such that she finishes within h hours.

Example: piles=[3,6,7,11], h=8 -> 4""",
{
"Python":'''
import math
class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        while l < r:
            mid = (l+r)//2
            hrs = sum(math.ceil(p/mid) for p in piles)
            if hrs <= h: r = mid
            else: l = mid+1
        return l

if __name__ == "__main__":
    print(Solution().minEatingSpeed([3,6,7,11], 8))
''',
"JavaScript":'''
var minEatingSpeed = function(piles, h) {
    let l = 1, r = Math.max(...piles);
    while (l < r) {
        const mid = (l+r) >> 1;
        let hrs = 0;
        for (const p of piles) hrs += Math.ceil(p/mid);
        if (hrs <= h) r = mid; else l = mid+1;
    }
    return l;
};
console.log(minEatingSpeed([3,6,7,11], 8));
''',
"Java":'''
public class __CLASS__ {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = 0;
        for (int p: piles) r = Math.max(r, p);
        while (l < r) {
            int mid = l + (r-l)/2;
            long hrs = 0;
            for (int p: piles) hrs += (p + mid - 1) / mid;
            if (hrs <= h) r = mid; else l = mid+1;
        }
        return l;
    }
    public static void main(String[] a){
        System.out.println(new __CLASS__().minEatingSpeed(new int[]{3,6,7,11}, 8));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1, r = *max_element(piles.begin(), piles.end());
        while (l < r) {
            int mid = l + (r-l)/2;
            long long hrs = 0;
            for (int p: piles) hrs += (p + mid - 1) / mid;
            if (hrs <= h) r = mid; else l = mid+1;
        }
        return l;
    }
};
int main(){ vector<int> v={3,6,7,11}; cout<<Solution().minEatingSpeed(v, 8)<<endl; }
''',
"Go":'''
package main
import "fmt"
func minEatingSpeed(piles []int, h int) int {
    l, r := 1, 0
    for _, p := range piles { if p > r { r = p } }
    for l < r {
        mid := (l+r)/2
        hrs := 0
        for _, p := range piles { hrs += (p + mid - 1) / mid }
        if hrs <= h { r = mid } else { l = mid+1 }
    }
    return l
}
func main(){ fmt.Println(minEatingSpeed([]int{3,6,7,11}, 8)) }
''',
"R":'''
minEatingSpeed <- function(piles, h) {
    l <- 1; r <- max(piles)
    while (l < r) {
        mid <- (l+r) %/% 2
        hrs <- sum(ceiling(piles / mid))
        if (hrs <= h) r <- mid else l <- mid + 1
    }
    l
}
print(minEatingSpeed(c(3,6,7,11), 8))
''',
}))

# ---- 057 Find Minimum in Rotated Sorted Array ----
LESSONS.append((57, "Find Minimum in Rotated Sorted Array", "Binary Search", "Medium", 28,
"""Given a rotated sorted array of unique elements, return its minimum.

Example: [3,4,5,1,2] -> 1""",
{
"Python":'''
class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]: l = mid+1
            else: r = mid
        return nums[l]

if __name__ == "__main__":
    print(Solution().findMin([3,4,5,1,2]))
    print(Solution().findMin([4,5,6,7,0,1,2]))
''',
"JavaScript":'''
var findMin = function(nums) {
    let l = 0, r = nums.length - 1;
    while (l < r) {
        const mid = (l+r) >> 1;
        if (nums[mid] > nums[r]) l = mid+1; else r = mid;
    }
    return nums[l];
};
console.log(findMin([3,4,5,1,2]), findMin([4,5,6,7,0,1,2]));
''',
"Java":'''
public class __CLASS__ {
    public int findMin(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = (l+r)/2;
            if (nums[mid] > nums[r]) l = mid+1; else r = mid;
        }
        return nums[l];
    }
    public static void main(String[] a){
        __CLASS__ s = new __CLASS__();
        System.out.println(s.findMin(new int[]{3,4,5,1,2}));
        System.out.println(s.findMin(new int[]{4,5,6,7,0,1,2}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r) {
            int mid = (l+r)/2;
            if (nums[mid] > nums[r]) l = mid+1; else r = mid;
        }
        return nums[l];
    }
};
int main(){ vector<int> v={3,4,5,1,2}, w={4,5,6,7,0,1,2}; cout<<Solution().findMin(v)<<" "<<Solution().findMin(w)<<endl; }
''',
"Go":'''
package main
import "fmt"
func findMin(nums []int) int {
    l, r := 0, len(nums)-1
    for l < r {
        mid := (l+r)/2
        if nums[mid] > nums[r] { l = mid+1 } else { r = mid }
    }
    return nums[l]
}
func main(){ fmt.Println(findMin([]int{3,4,5,1,2}), findMin([]int{4,5,6,7,0,1,2})) }
''',
"R":'''
findMin <- function(nums) {
    l <- 1; r <- length(nums)
    while (l < r) {
        mid <- (l+r) %/% 2
        if (nums[mid] > nums[r]) l <- mid+1 else r <- mid
    }
    nums[l]
}
print(findMin(c(3,4,5,1,2)))
print(findMin(c(4,5,6,7,0,1,2)))
''',
}))

# ---- 058 Search in Rotated Sorted Array ----
LESSONS.append((58, "Search in Rotated Sorted Array", "Binary Search", "Medium", 29,
"""Search target in a rotated sorted array of unique values.
Return its index, or -1 if not found.

Example: nums=[4,5,6,7,0,1,2], target=0 -> 4""",
{
"Python":'''
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target: return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]: r = mid-1
                else: l = mid+1
            else:
                if nums[mid] < target <= nums[r]: l = mid+1
                else: r = mid-1
        return -1

if __name__ == "__main__":
    print(Solution().search([4,5,6,7,0,1,2], 0))
    print(Solution().search([4,5,6,7,0,1,2], 3))
''',
"JavaScript":'''
var search = function(nums, target) {
    let l = 0, r = nums.length - 1;
    while (l <= r) {
        const mid = (l+r) >> 1;
        if (nums[mid] === target) return mid;
        if (nums[l] <= nums[mid]) {
            if (nums[l] <= target && target < nums[mid]) r = mid-1;
            else l = mid+1;
        } else {
            if (nums[mid] < target && target <= nums[r]) l = mid+1;
            else r = mid-1;
        }
    }
    return -1;
};
console.log(search([4,5,6,7,0,1,2], 0), search([4,5,6,7,0,1,2], 3));
''',
"Java":'''
public class __CLASS__ {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = (l+r)/2;
            if (nums[mid] == target) return mid;
            if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target < nums[mid]) r = mid-1;
                else l = mid+1;
            } else {
                if (nums[mid] < target && target <= nums[r]) l = mid+1;
                else r = mid-1;
            }
        }
        return -1;
    }
    public static void main(String[] a){
        __CLASS__ s = new __CLASS__();
        System.out.println(s.search(new int[]{4,5,6,7,0,1,2}, 0));
        System.out.println(s.search(new int[]{4,5,6,7,0,1,2}, 3));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = (l+r)/2;
            if (nums[mid] == target) return mid;
            if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target < nums[mid]) r = mid-1;
                else l = mid+1;
            } else {
                if (nums[mid] < target && target <= nums[r]) l = mid+1;
                else r = mid-1;
            }
        }
        return -1;
    }
};
int main(){ vector<int> v={4,5,6,7,0,1,2}; cout<<Solution().search(v,0)<<" "<<Solution().search(v,3)<<endl; }
''',
"Go":'''
package main
import "fmt"
func search(nums []int, target int) int {
    l, r := 0, len(nums)-1
    for l <= r {
        mid := (l+r)/2
        if nums[mid] == target { return mid }
        if nums[l] <= nums[mid] {
            if nums[l] <= target && target < nums[mid] { r = mid-1 } else { l = mid+1 }
        } else {
            if nums[mid] < target && target <= nums[r] { l = mid+1 } else { r = mid-1 }
        }
    }
    return -1
}
func main(){ fmt.Println(search([]int{4,5,6,7,0,1,2}, 0), search([]int{4,5,6,7,0,1,2}, 3)) }
''',
"R":'''
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
''',
}))

# ---- 059 Time Based Key-Value Store ----
LESSONS.append((59, "Time Based Key Value Store", "Binary Search", "Medium", 29,
"""Design a time-based key-value data structure that supports
set(key, value, timestamp) and get(key, timestamp), where get returns
the value with the largest timestamp <= the given timestamp.""",
{
"Python":'''
from bisect import bisect_right
class TimeMap:
    def __init__(self): self.d = {}
    def set(self, k, v, t):
        self.d.setdefault(k, []).append((t, v))
    def get(self, k, t):
        if k not in self.d: return ""
        arr = self.d[k]
        i = bisect_right(arr, (t, chr(127)))
        return arr[i-1][1] if i else ""

if __name__ == "__main__":
    tm = TimeMap(); tm.set("foo","bar",1)
    print(tm.get("foo",1)); print(tm.get("foo",3))
    tm.set("foo","bar2",4); print(tm.get("foo",4)); print(tm.get("foo",5))
''',
"JavaScript":'''
class TimeMap {
    constructor(){ this.d = new Map(); }
    set(k, v, t){
        if (!this.d.has(k)) this.d.set(k, []);
        this.d.get(k).push([t, v]);
    }
    get(k, t){
        if (!this.d.has(k)) return "";
        const a = this.d.get(k);
        let l = 0, r = a.length - 1, res = "";
        while (l <= r) {
            const m = (l+r) >> 1;
            if (a[m][0] <= t) { res = a[m][1]; l = m+1; } else r = m-1;
        }
        return res;
    }
}
const tm = new TimeMap(); tm.set("foo","bar",1);
console.log(tm.get("foo",1), tm.get("foo",3));
tm.set("foo","bar2",4);
console.log(tm.get("foo",4), tm.get("foo",5));
''',
"Java":'''
import java.util.*;
public class __CLASS__ {
    static class TimeMap {
        Map<String, List<int[]>> ts = new HashMap<>();
        Map<String, List<String>> vs = new HashMap<>();
        public void set(String k, String v, int t){
            ts.computeIfAbsent(k, x -> new ArrayList<>()).add(new int[]{t});
            vs.computeIfAbsent(k, x -> new ArrayList<>()).add(v);
        }
        public String get(String k, int t){
            if (!ts.containsKey(k)) return "";
            List<int[]> a = ts.get(k); List<String> b = vs.get(k);
            int l = 0, r = a.size()-1; String res = "";
            while (l <= r) {
                int m = (l+r)/2;
                if (a.get(m)[0] <= t) { res = b.get(m); l = m+1; } else r = m-1;
            }
            return res;
        }
    }
    public static void main(String[] a){
        TimeMap tm = new TimeMap(); tm.set("foo","bar",1);
        System.out.println(tm.get("foo",1)); System.out.println(tm.get("foo",3));
        tm.set("foo","bar2",4);
        System.out.println(tm.get("foo",4)); System.out.println(tm.get("foo",5));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class TimeMap {
    unordered_map<string, vector<pair<int,string>>> d;
public:
    void set(string k, string v, int t){ d[k].push_back({t, v}); }
    string get(string k, int t){
        if (!d.count(k)) return "";
        auto& a = d[k];
        int l=0, r=a.size()-1; string res = "";
        while (l<=r) {
            int m = (l+r)/2;
            if (a[m].first <= t) { res = a[m].second; l = m+1; } else r = m-1;
        }
        return res;
    }
};
int main(){ TimeMap tm; tm.set("foo","bar",1);
    cout<<tm.get("foo",1)<<" "<<tm.get("foo",3)<<endl;
    tm.set("foo","bar2",4);
    cout<<tm.get("foo",4)<<" "<<tm.get("foo",5)<<endl; }
''',
"Go":'''
package main
import "fmt"
type entry struct{ t int; v string }
type TimeMap struct{ d map[string][]entry }
func New() *TimeMap { return &TimeMap{d: map[string][]entry{}} }
func (m *TimeMap) Set(k, v string, t int) { m.d[k] = append(m.d[k], entry{t, v}) }
func (m *TimeMap) Get(k string, t int) string {
    a, ok := m.d[k]; if !ok { return "" }
    l, r, res := 0, len(a)-1, ""
    for l <= r {
        mid := (l+r)/2
        if a[mid].t <= t { res = a[mid].v; l = mid+1 } else { r = mid-1 }
    }
    return res
}
func main(){
    tm := New(); tm.Set("foo","bar",1)
    fmt.Println(tm.Get("foo",1), tm.Get("foo",3))
    tm.Set("foo","bar2",4)
    fmt.Println(tm.Get("foo",4), tm.Get("foo",5))
}
''',
"R":'''
TimeMap <- function() {
    d <- list()
    list(
        set = function(k, v, t){
            if (is.null(d[[k]])) d[[k]] <<- list(t=integer(), v=character())
            d[[k]]$t <<- c(d[[k]]$t, t); d[[k]]$v <<- c(d[[k]]$v, v)
        },
        get = function(k, t){
            if (is.null(d[[k]])) return("")
            ts <- d[[k]]$t; vs <- d[[k]]$v
            ok <- which(ts <= t)
            if (length(ok)==0) "" else vs[max(ok)]
        }
    )
}
tm <- TimeMap(); tm$set("foo","bar",1)
print(tm$get("foo",1)); print(tm$get("foo",3))
tm$set("foo","bar2",4)
print(tm$get("foo",4)); print(tm$get("foo",5))
''',
}))

# ---- 060 Median of Two Sorted Arrays ----
LESSONS.append((60, "Median of Two Sorted Arrays", "Binary Search", "Hard", 30,
"""Given two sorted arrays nums1 and nums2, return the median of the
combined sorted array. Run in O(log(min(m,n))).

Example: [1,3], [2] -> 2.0""",
{
"Python":'''
class Solution:
    def findMedianSortedArrays(self, a, b):
        if len(a) > len(b): a, b = b, a
        m, n = len(a), len(b); half = (m+n+1)//2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo+hi)//2; j = half - i
            la = a[i-1] if i>0 else float("-inf")
            ra = a[i] if i<m else float("inf")
            lb = b[j-1] if j>0 else float("-inf")
            rb = b[j] if j<n else float("inf")
            if la <= rb and lb <= ra:
                if (m+n) % 2: return float(max(la, lb))
                return (max(la, lb) + min(ra, rb)) / 2.0
            elif la > rb: hi = i-1
            else: lo = i+1
        return 0.0

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,3], [2]))
    print(Solution().findMedianSortedArrays([1,2], [3,4]))
''',
"JavaScript":'''
var findMedianSortedArrays = function(a, b) {
    if (a.length > b.length) [a, b] = [b, a];
    const m = a.length, n = b.length, half = ((m+n+1) >> 1);
    let lo = 0, hi = m;
    while (lo <= hi) {
        const i = (lo+hi) >> 1, j = half - i;
        const la = i>0 ? a[i-1] : -Infinity;
        const ra = i<m ? a[i]   :  Infinity;
        const lb = j>0 ? b[j-1] : -Infinity;
        const rb = j<n ? b[j]   :  Infinity;
        if (la <= rb && lb <= ra) {
            if ((m+n) % 2) return Math.max(la, lb);
            return (Math.max(la, lb) + Math.min(ra, rb)) / 2;
        } else if (la > rb) hi = i-1;
        else lo = i+1;
    }
    return 0;
};
console.log(findMedianSortedArrays([1,3], [2]));
console.log(findMedianSortedArrays([1,2], [3,4]));
''',
"Java":'''
public class __CLASS__ {
    public double findMedianSortedArrays(int[] a, int[] b) {
        if (a.length > b.length) { int[] t = a; a = b; b = t; }
        int m = a.length, n = b.length, half = (m+n+1)/2;
        int lo = 0, hi = m;
        while (lo <= hi) {
            int i = (lo+hi)/2, j = half - i;
            int la = i>0 ? a[i-1] : Integer.MIN_VALUE;
            int ra = i<m ? a[i]   : Integer.MAX_VALUE;
            int lb = j>0 ? b[j-1] : Integer.MIN_VALUE;
            int rb = j<n ? b[j]   : Integer.MAX_VALUE;
            if (la <= rb && lb <= ra) {
                if ((m+n) % 2 == 1) return Math.max(la, lb);
                return (Math.max(la, lb) + Math.min(ra, rb)) / 2.0;
            } else if (la > rb) hi = i-1;
            else lo = i+1;
        }
        return 0.0;
    }
    public static void main(String[] a){
        __CLASS__ s = new __CLASS__();
        System.out.println(s.findMedianSortedArrays(new int[]{1,3}, new int[]{2}));
        System.out.println(s.findMedianSortedArrays(new int[]{1,2}, new int[]{3,4}));
    }
}
''',
"CPP":'''
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    double findMedianSortedArrays(vector<int>& a, vector<int>& b) {
        if (a.size() > b.size()) swap(a, b);
        int m = a.size(), n = b.size(), half = (m+n+1)/2;
        int lo = 0, hi = m;
        while (lo <= hi) {
            int i = (lo+hi)/2, j = half - i;
            int la = i>0 ? a[i-1] : INT_MIN;
            int ra = i<m ? a[i]   : INT_MAX;
            int lb = j>0 ? b[j-1] : INT_MIN;
            int rb = j<n ? b[j]   : INT_MAX;
            if (la <= rb && lb <= ra) {
                if ((m+n) % 2) return max(la, lb);
                return (max(la, lb) + min(ra, rb)) / 2.0;
            } else if (la > rb) hi = i-1;
            else lo = i+1;
        }
        return 0.0;
    }
};
int main(){ vector<int> a={1,3}, b={2}, c={1,2}, d={3,4};
    cout<<Solution().findMedianSortedArrays(a,b)<<" "<<Solution().findMedianSortedArrays(c,d)<<endl; }
''',
"Go":'''
package main
import ("fmt"; "math")
func findMedianSortedArrays(a, b []int) float64 {
    if len(a) > len(b) { a, b = b, a }
    m, n := len(a), len(b); half := (m+n+1)/2
    lo, hi := 0, m
    max := func(x,y int) int { if x>y {return x}; return y }
    min := func(x,y int) int { if x<y {return x}; return y }
    for lo <= hi {
        i := (lo+hi)/2; j := half - i
        la := math.MinInt32; if i>0 { la = a[i-1] }
        ra := math.MaxInt32; if i<m { ra = a[i] }
        lb := math.MinInt32; if j>0 { lb = b[j-1] }
        rb := math.MaxInt32; if j<n { rb = b[j] }
        if la <= rb && lb <= ra {
            if (m+n) % 2 == 1 { return float64(max(la, lb)) }
            return float64(max(la, lb) + min(ra, rb)) / 2.0
        } else if la > rb { hi = i-1 } else { lo = i+1 }
    }
    return 0
}
func main(){
    fmt.Println(findMedianSortedArrays([]int{1,3}, []int{2}))
    fmt.Println(findMedianSortedArrays([]int{1,2}, []int{3,4}))
}
''',
"R":'''
findMedianSortedArrays <- function(a, b) {
    c <- sort(c(a, b)); n <- length(c)
    if (n %% 2 == 1) c[(n+1) %/% 2]
    else (c[n/2] + c[n/2 + 1]) / 2
}
print(findMedianSortedArrays(c(1,3), c(2)))
print(findMedianSortedArrays(c(1,2), c(3,4)))
''',
}))

if __name__ == "__main__":
    from _lesson_writer import write_lessons
    write_lessons(LESSONS)
