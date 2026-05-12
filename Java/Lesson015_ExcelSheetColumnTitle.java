// =============================================================
// MIT License | @analyticswithharry2026
// GitHub  : https://github.com/analyticswithharry
// YouTube : Analytics with Harry
// =============================================================
// Lesson     : 015 -- Excel Sheet Column Title
// Category   : Math and Geometry
// Difficulty : Easy
// Study Plan : Day 8
// =============================================================
//
// QUESTION:
//   Given an integer columnNumber, return its corresponding column title
//   as it appears in an Excel sheet.
//
//   Example:
//     1  -> A
//     28 -> AB
//     701 -> ZY
// =============================================================

public class Lesson015_ExcelSheetColumnTitle {
    public String convertToTitle(int n) {
        StringBuilder sb = new StringBuilder();
        while (n > 0) { n--; sb.append((char)('A' + n % 26)); n /= 26; }
        return sb.reverse().toString();
    }
    public static void main(String[] args) {
        Lesson015_ExcelSheetColumnTitle s = new Lesson015_ExcelSheetColumnTitle();
        System.out.println(s.convertToTitle(1) + " " + s.convertToTitle(28) + " " + s.convertToTitle(701));
    }
}
