// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 053 -- Car Fleet
// Category   : Stack
// Difficulty : Medium
// Study Plan : Day 26
// =============================================================
//
// QUESTION:
//   Cars at given positions move toward target with given speeds. A car
//   that catches up forms a fleet. Return the number of fleets that arrive.
//
//   Example: target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3] -> 3
// =============================================================

var carFleet = function(target, position, speed) {
    const cars = position.map((p,i)=>[p,speed[i]]).sort((a,b)=>b[0]-a[0]);
    const st = [];
    for (const [p,s] of cars) {
        const t = (target - p) / s;
        if (!st.length || t > st[st.length-1]) st.push(t);
    }
    return st.length;
};
console.log(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]));
