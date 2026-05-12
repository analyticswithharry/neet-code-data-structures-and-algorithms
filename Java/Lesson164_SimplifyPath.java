// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 164 -- Simplify Path
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 82
// =============================================================
//
// QUESTION:
//   Given a Unix-style absolute path, return the simplified canonical path.
// =============================================================
import java.util.*;
public class Lesson164_SimplifyPath{
  static String simplify(String p){Deque<String> st=new ArrayDeque<>();for(String part:p.split("/")){if(part.isEmpty()||part.equals("."))continue;if(part.equals("..")){if(!st.isEmpty())st.pop();}else st.push(part);}StringBuilder sb=new StringBuilder();Iterator<String> it=st.descendingIterator();while(it.hasNext()){sb.append('/').append(it.next());}return sb.length()==0?"/":sb.toString();}
  public static void main(String[]a){System.out.println(simplify("/a/./b/../../c/"));System.out.println(simplify("/home//foo/"));}
}
