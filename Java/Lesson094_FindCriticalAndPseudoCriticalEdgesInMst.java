// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 094 -- Find Critical and Pseudo Critical Edges in MST
// Category   : Advanced Graphs
// Difficulty : Hard
// Study Plan : Day 47
// =============================================================
//
// QUESTION:
//   Given n nodes and weighted edges, find indices of critical and pseudo-critical edges in any MST.
// =============================================================

import java.util.*;
public class Lesson094_FindCriticalAndPseudoCriticalEdgesInMst {
    static class DSU { int[] p,r; int cnt;
        DSU(int n){ p=new int[n]; r=new int[n]; cnt=n; for(int i=0;i<n;i++) p[i]=i; }
        int f(int x){ while(p[x]!=x){p[x]=p[p[x]]; x=p[x];} return x; }
        boolean u(int a,int b){ a=f(a); b=f(b); if(a==b) return false;
            if(r[a]<r[b]){int t=a;a=b;b=t;} p[b]=a; if(r[a]==r[b]) r[a]++; cnt--; return true; }
    }
    int n; int[][] E;
    int kruskal(int skip, int force){
        DSU d=new DSU(n); int w=0;
        if (force>=0){ if(!d.u(E[force][0],E[force][1])) return Integer.MAX_VALUE; w+=E[force][2]; }
        for (int i=0;i<E.length;i++){ if(i==skip) continue; if(d.u(E[i][0],E[i][1])) w+=E[i][2]; }
        return d.cnt==1 ? w : Integer.MAX_VALUE;
    }
    public List<List<Integer>> findCriticalAndPseudoCriticalEdges(int n, int[][] edges){
        this.n=n; int[][] e=new int[edges.length][4];
        for (int i=0;i<edges.length;i++){ e[i][0]=edges[i][0]; e[i][1]=edges[i][1]; e[i][2]=edges[i][2]; e[i][3]=i; }
        Arrays.sort(e,(a,b)->a[2]-b[2]); E=e;
        int base=kruskal(-1,-1);
        List<Integer> crit=new ArrayList<>(), pseu=new ArrayList<>();
        for (int i=0;i<e.length;i++){
            if (kruskal(i,-1) > base) crit.add(e[i][3]);
            else if (kruskal(-1,i) == base) pseu.add(e[i][3]);
        }
        return Arrays.asList(crit, pseu);
    }
    public static void main(String[] a){
        System.out.println(new Lesson094_FindCriticalAndPseudoCriticalEdgesInMst().findCriticalAndPseudoCriticalEdges(5, new int[][]{{0,1,1},{1,2,1},{2,3,2},{0,3,2},{0,4,3},{3,4,3},{1,4,6}}));
    }
}
