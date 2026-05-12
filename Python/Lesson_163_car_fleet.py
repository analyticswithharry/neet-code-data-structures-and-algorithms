# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 163 -- Car Fleet
# Category   : Stack
# Difficulty : Medium
# Study Plan : Day 82
# =============================================================
#
# QUESTION:
#   Cars at positions head to target with given speeds. Cars cannot pass; slower car ahead caps faster car behind. Return number of fleets that arrive.
# =============================================================
def carFleet(target,pos,sp):
    cars=sorted(zip(pos,sp),reverse=True)
    fleets=0; lastT=0.0
    for p,s in cars:
        t=(target-p)/s
        if t>lastT:
            fleets+=1; lastT=t
    return fleets

if __name__=="__main__":
    print(carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
