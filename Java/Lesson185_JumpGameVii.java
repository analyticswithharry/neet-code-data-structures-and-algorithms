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
public class Lesson185_JumpGameVii{
  static boolean canReach(String s,int mn,int mx){int n=s.length();if(s.charAt(n-1)!='0'||s.charAt(0)!='0')return false;int[] pre=new int[n+1];boolean[] r=new boolean[n];r[0]=true;pre[1]=1;for(int i=1;i<n;i++){if(s.charAt(i)=='0'){int lo=Math.max(0,i-mx),hi=i-mn;if(lo<=hi && pre[hi+1]-pre[lo]>0) r[i]=true;}pre[i+1]=pre[i]+(r[i]?1:0);}return r[n-1];}
  public static void main(String[]a){System.out.println(canReach("011010",2,3));System.out.println(canReach("01101110",2,3));}
}
