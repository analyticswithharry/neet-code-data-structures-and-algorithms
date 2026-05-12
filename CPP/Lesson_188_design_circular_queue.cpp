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
#include <vector>
#include <string>
#include <iostream>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <numeric>
#include <functional>
#include <cmath>
using namespace std;
struct CQ{vector<int> a;int k,h=0,c=0;CQ(int k):a(k),k(k){}
  bool enQueue(int v){if(c==k)return false;a[(h+c)%k]=v;c++;return true;}
  bool deQueue(){if(c==0)return false;h=(h+1)%k;c--;return true;}
  int Front(){return c==0?-1:a[h];}
  int Rear(){return c==0?-1:a[(h+c-1)%k];}
  bool isEmpty(){return c==0;}
  bool isFull(){return c==k;}};
int main(){CQ q(3);cout<<q.enQueue(1)<<q.enQueue(2)<<q.enQueue(3)<<q.enQueue(4)<<"\n";cout<<q.Rear()<<" "<<q.isFull()<<" "<<q.deQueue()<<" "<<q.enQueue(4)<<" "<<q.Rear()<<"\n";}
