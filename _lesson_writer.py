"""Shared writer for NeetCode lesson batches with embedded question + solution."""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
LANG_EXT = {"Python":"py","JavaScript":"js","Java":"java","CPP":"cpp","Go":"go","R":"R"}
COMMENT  = {"Python":"#","JavaScript":"//","Java":"//","CPP":"//","Go":"//","R":"#"}
CPP_PORTABLE = ("#include <vector>\n#include <string>\n#include <iostream>\n"
                "#include <stack>\n#include <queue>\n#include <unordered_map>\n"
                "#include <unordered_set>\n#include <map>\n#include <set>\n"
                "#include <algorithm>\n#include <climits>\n#include <numeric>\n"
                "#include <functional>\n#include <cmath>")

def slug(t):
    s = re.sub(r"[^a-zA-Z0-9 ]", " ", t).strip().lower()
    return re.sub(r"\s+", "_", s)

def java_class(num, t):
    parts = re.sub(r"[^a-zA-Z0-9 ]", " ", t).split()
    return f"Lesson{num:03d}_" + "".join(p.capitalize() for p in parts)

def header(lang, num, title, cat, diff, day, question):
    c = COMMENT[lang]
    lines = [
        f"{c} =============================================================",
        f"{c} MIT License | @analyticswithharry2026",
        f"{c} GitHub  : https://github.com/analyticswithharry",
        f"{c} YouTube : Analytics with Harry",
        f"{c} =============================================================",
        f"{c} Lesson     : {num:03d} -- {title}",
        f"{c} Category   : {cat}",
        f"{c} Difficulty : {diff}",
        f"{c} Study Plan : Day {day}",
        f"{c} =============================================================",
        f"{c}",
        f"{c} QUESTION:",
    ]
    for line in question.strip().splitlines():
        lines.append(f"{c}   {line}".rstrip())
    lines.append(f"{c} =============================================================")
    lines.append("")
    return "\n".join(lines)

def fname(lang, num, title):
    if lang == "Java": return f"{java_class(num,title)}.java"
    return f"Lesson_{num:03d}_{slug(title)}.{LANG_EXT[lang]}"

def write_lessons(lessons):
    """lessons: list of (num, title, cat, diff, day, question, {lang: body})"""
    print(f"Writing {len(lessons)} lessons x 6 langs = {len(lessons)*6} files...")
    for num, title, cat, diff, day, q, codes in lessons:
        for lang in LANG_EXT:
            body = codes[lang].replace("__CLASS__", java_class(num, title))
            if lang == "CPP":
                body = body.replace("#include <bits/stdc++.h>", CPP_PORTABLE)
            prefix = "//go:build ignore\n\n" if lang == "Go" else ""
            content = prefix + header(lang, num, title, cat, diff, day, q) + body
            if not content.endswith("\n"): content += "\n"
            d = os.path.join(ROOT, lang); os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, fname(lang, num, title)), "w") as f:
                f.write(content)
    print("Done.")
