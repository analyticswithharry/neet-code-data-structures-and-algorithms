"""Regenerate README.md lesson catalog table with all 250 entries x 6 language links."""
import os, re, glob

ROOT = os.path.dirname(os.path.abspath(__file__))

# Map num -> (title, category, difficulty, day, py_name, java_name)
lessons = {}

for path in sorted(glob.glob(os.path.join(ROOT, "python", "Lesson_*.py"))):
    fname = os.path.basename(path)
    m = re.match(r"Lesson_(\d{3})_(.+)\.py$", fname)
    if not m: continue
    num = int(m.group(1)); slug = m.group(2)
    with open(path) as f:
        head = [next(f) for _ in range(10)]
    title = re.search(r"-- (.+)$", head[5].strip()).group(1)
    cat = head[6].split(":",1)[1].strip()
    diff = head[7].split(":",1)[1].strip()
    day = head[8].split("Day",1)[1].strip()
    lessons[num] = (title, cat, diff, day, slug)

# Find java filename per number
java_map = {}
for path in sorted(glob.glob(os.path.join(ROOT, "java", "Lesson*.java"))):
    fname = os.path.basename(path)
    m = re.match(r"Lesson(\d{3})_(.+)\.java$", fname)
    if m:
        java_map[int(m.group(1))] = fname

# Build table
header = (
    "| #   | Title | Category | Difficulty | Day | Python | JS | Java | C++ | Go | R |\n"
    "| --- | ----- | -------- | ---------- | --- | ------ | -- | ---- | --- | -- | - |\n"
)
rows = []
for num in sorted(lessons):
    title, cat, diff, day, slug = lessons[num]
    py = f"python/Lesson_{num:03d}_{slug}.py"
    js = f"javascript/Lesson_{num:03d}_{slug}.js"
    jv_name = java_map.get(num, "")
    jv = f"java/{jv_name}" if jv_name else ""
    cp = f"cpp/Lesson_{num:03d}_{slug}.cpp"
    go = f"go/Lesson_{num:03d}_{slug}.go"
    rl = f"r/Lesson_{num:03d}_{slug}.R"
    def lk(label, p):
        return f"[{label}]({p})" if p else "—"
    rows.append(
        f"| {num:03d} | {title} | {cat} | {diff} | {day} | "
        f"{lk('py', py)} | {lk('js', js)} | {lk('java', jv)} | "
        f"{lk('cpp', cp)} | {lk('go', go)} | {lk('R', rl)} |"
    )

table = header + "\n".join(rows) + "\n"

# Read README and replace table region (lines containing "| #" header through next "---" or blank section)
readme_path = os.path.join(ROOT, "README.md")
with open(readme_path) as f:
    text = f.read()

# Find existing table block (starts at "| #   | Title" and ends before "> More lessons" or "---")
pattern = re.compile(r"\| #\s+\| Title.*?(?=\n>|\n---|\n## )", re.DOTALL)
new_text, n = pattern.subn(table.rstrip() + "\n\n", text)
if n == 0:
    # Append before Study Plan
    new_text = text.replace("## Study Plan", "## Lesson Catalog\n\n" + table + "\n---\n\n## Study Plan", 1)

with open(readme_path, "w") as f:
    f.write(new_text)

print(f"Wrote {len(rows)} table rows to README.md")
