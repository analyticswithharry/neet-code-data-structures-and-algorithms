// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 059 -- Time Based Key Value Store
// Category   : Binary Search
// Difficulty : Medium
// Study Plan : Day 29
// =============================================================
//
// QUESTION:
//   Design a time-based key-value data structure that supports
//   set(key, value, timestamp) and get(key, timestamp), where get returns
//   the value with the largest timestamp <= the given timestamp.
// =============================================================

class TimeMap {
    constructor(){ this.d = new Map(); }
    set(k, v, t){
        if (!this.d.has(k)) this.d.set(k, []);
        this.d.get(k).push([t, v]);
    }
    get(k, t){
        if (!this.d.has(k)) return "";
        const a = this.d.get(k);
        let l = 0, r = a.length - 1, res = "";
        while (l <= r) {
            const m = (l+r) >> 1;
            if (a[m][0] <= t) { res = a[m][1]; l = m+1; } else r = m-1;
        }
        return res;
    }
}
const tm = new TimeMap(); tm.set("foo","bar",1);
console.log(tm.get("foo",1), tm.get("foo",3));
tm.set("foo","bar2",4);
console.log(tm.get("foo",4), tm.get("foo",5));
