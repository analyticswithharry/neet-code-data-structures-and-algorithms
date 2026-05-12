// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 188 -- Design Circular Queue
// Category   : Linked List
// Difficulty : Medium
// Study Plan : Day 94
// =============================================================
//
// QUESTION:
//   Implement a fixed-size circular queue with enQueue/deQueue/Front/Rear/isEmpty/isFull.
// =============================================================
public class Lesson188_DesignCircularQueue{
  static class CQ{int[] a;int k,h,c;CQ(int k){a=new int[k];this.k=k;}
    boolean enQueue(int v){if(c==k)return false;a[(h+c)%k]=v;c++;return true;}
    boolean deQueue(){if(c==0)return false;h=(h+1)%k;c--;return true;}
    int Front(){return c==0?-1:a[h];}
    int Rear(){return c==0?-1:a[(h+c-1)%k];}
    boolean isEmpty(){return c==0;}
    boolean isFull(){return c==k;}}
  public static void main(String[]a){CQ q=new CQ(3);System.out.println(q.enQueue(1)+","+q.enQueue(2)+","+q.enQueue(3)+","+q.enQueue(4));System.out.println(q.Rear()+","+q.isFull()+","+q.deQueue()+","+q.enQueue(4)+","+q.Rear());}
}
