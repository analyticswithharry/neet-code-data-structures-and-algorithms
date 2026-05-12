// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 207 -- Decode String
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 104
// =============================================================
//
// QUESTION:
//   Decode a run-length-style string like "3[a2[c]]" -> "accaccacc".
// =============================================================
import java.util.*;
public class Lesson207_DecodeString{
  static String decodeString(String s){Deque<Object[]> st=new ArrayDeque<>();StringBuilder cur=new StringBuilder();int k=0;for(char ch:s.toCharArray()){if(Character.isDigit(ch))k=k*10+(ch-'0');else if(ch=='['){st.push(new Object[]{cur.toString(),k});cur=new StringBuilder();k=0;}else if(ch==']'){Object[] x=st.pop();String pre=(String)x[0];int n=(int)x[1];StringBuilder nb=new StringBuilder(pre);for(int i=0;i<n;i++)nb.append(cur);cur=nb;}else cur.append(ch);}return cur.toString();}
  public static void main(String[]a){System.out.println(decodeString("3[a]2[bc]"));System.out.println(decodeString("3[a2[c]]"));}
}
