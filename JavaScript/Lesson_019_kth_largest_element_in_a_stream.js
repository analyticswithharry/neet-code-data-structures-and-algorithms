// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 019 -- Kth Largest Element In a Stream
// Category   : Heap Priority Queue
// Difficulty : Easy
// Study Plan : Day 10
// =============================================================
//
// QUESTION:
//   Design a class to find the kth largest element in a stream. Implement:
//     KthLargest(int k, int[] nums)
//     add(val) -> returns the element representing the kth largest in the stream.
//
//   Example:
//     k=3, nums=[4,5,8,2]
//     add(3) -> 4; add(5) -> 5; add(10) -> 5; add(9) -> 8; add(4) -> 8
// =============================================================

// min-heap of size k
class KthLargest {
    constructor(k, nums) { this.k = k; this.h = []; for (const n of nums) this.add(n); }
    add(val) {
        if (this.h.length < this.k) { this._push(val); }
        else if (val > this.h[0]) { this.h[0] = val; this._down(0); }
        return this.h[0];
    }
    _push(v) { this.h.push(v); this._up(this.h.length - 1); }
    _up(i) { while (i > 0) { const p = (i-1)>>1; if (this.h[p] > this.h[i]) { [this.h[p],this.h[i]]=[this.h[i],this.h[p]]; i = p; } else break; } }
    _down(i) { const n = this.h.length; while (true) { const l=2*i+1, r=2*i+2; let s=i;
        if (l<n && this.h[l]<this.h[s]) s=l; if (r<n && this.h[r]<this.h[s]) s=r;
        if (s===i) break; [this.h[s],this.h[i]]=[this.h[i],this.h[s]]; i=s; } }
}
const kl = new KthLargest(3, [4,5,8,2]);
console.log([3,5,10,9,4].map(x => kl.add(x)));
