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
import java.util.*;
public class Lesson171_PartitionToKEqualSumSubsets{
  static int[] b; static int t; static int K; static int[] N;
  static boolean bt(int i){if(i==N.length)return true;for(int j=0;j<K;j++){if(b[j]+N[i]<=t){b[j]+=N[i];if(bt(i+1))return true;b[j]-=N[i];}if(b[j]==0)break;}return false;}
  static boolean canPartitionKSubsets(int[] nums,int k){int s=0;for(int v:nums)s+=v;if(s%k!=0)return false;t=s/k;Arrays.sort(nums);for(int i=0,j=nums.length-1;i<j;i++,j--){int x=nums[i];nums[i]=nums[j];nums[j]=x;}if(nums[0]>t)return false;b=new int[k];K=k;N=nums;return bt(0);}
  public static void main(String[]a){System.out.println(canPartitionKSubsets(new int[]{4,3,2,3,5,2,1},4));}
}
