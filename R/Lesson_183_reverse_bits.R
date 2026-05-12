# =============================================================
# MIT License | @analyticswithharry2026
# GitHub  : https://github.com/analyticswithharry
# YouTube : Analytics with Harry
# =============================================================
# Lesson     : 183 -- Reverse Bits
# Category   : Bit Manipulation
# Difficulty : Easy
# Study Plan : Day 92
# =============================================================
#
# QUESTION:
#   Reverse bits of a given 32-bit unsigned integer.
# =============================================================
reverseBits <- function(n){ r<-0; for(i in 1:32){ r<-bitwOr(bitwShiftL(r,1), bitwAnd(n,1)); n<-bitwShiftR(n,1) }; r }
cat(reverseBits(43261596),"\n")
