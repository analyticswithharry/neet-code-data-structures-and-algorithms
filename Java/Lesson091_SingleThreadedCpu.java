// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 091 -- Single Threaded CPU
// Category   : Heap Priority Queue
// Difficulty : Medium
// Study Plan : Day 46
// =============================================================
//
// QUESTION:
//   You have tasks[i] = [enqueueTime, processingTime]. CPU picks the task with shortest processing time available; ties broken by index. Return order of indices.
// =============================================================

import java.util.*;
public class Lesson091_SingleThreadedCpu {
    public int[] getOrder(int[][] tasks){
        Integer[] idx = new Integer[tasks.length];
        for (int i=0;i<idx.length;i++) idx[i]=i;
        Arrays.sort(idx,(a,b)->tasks[a][0]-tasks[b][0]);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[0]!=b[0]?a[0]-b[0]:a[1]-b[1]);
        long t=0; int i=0; int[] res = new int[tasks.length]; int k=0;
        while (i<idx.length || !pq.isEmpty()){
            if (pq.isEmpty()) t = Math.max(t, tasks[idx[i]][0]);
            while (i<idx.length && tasks[idx[i]][0]<=t){ pq.add(new int[]{tasks[idx[i]][1], idx[i]}); i++; }
            int[] x = pq.poll(); t += x[0]; res[k++] = x[1];
        }
        return res;
    }
    public static void main(String[] a){
        System.out.println(Arrays.toString(new Lesson091_SingleThreadedCpu().getOrder(new int[][]{{1,2},{2,4},{3,2},{4,1}})));
    }
}
