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
def reverseBits(n):
    r=0
    for _ in range(32):
        r=(r<<1)|(n&1); n>>=1
    return r

if __name__=="__main__":
    print(reverseBits(0b00000010100101000001111010011100))
