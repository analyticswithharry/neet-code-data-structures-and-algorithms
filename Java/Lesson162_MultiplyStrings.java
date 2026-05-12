// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 162 -- Multiply Strings
// Category   : Math and Geometry
// Difficulty : Medium
// Study Plan : Day 81
// =============================================================
//
// QUESTION:
//   Given two non-negative integers as strings, return their product as a string. Do not use built-in big-int conversion.
// =============================================================
public class Lesson162_MultiplyStrings{
  static String mul(String a,String b){if(a.equals("0")||b.equals("0"))return "0";int n=a.length(),m=b.length();int[] r=new int[n+m];for(int i=n-1;i>=0;i--)for(int j=m-1;j>=0;j--){int p=(a.charAt(i)-'0')*(b.charAt(j)-'0');int s=p+r[i+j+1];r[i+j+1]=s%10;r[i+j]+=s/10;}StringBuilder sb=new StringBuilder();for(int v:r)sb.append(v);while(sb.length()>1 && sb.charAt(0)=='0')sb.deleteCharAt(0);return sb.toString();}
  public static void main(String[]a){System.out.println(mul("123","456"));}
}
