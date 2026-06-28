"""Education section."""

from reportlab.platypus import Paragraph, Spacer

from config import DARK, BODY, MID, ACCENT, FB, FR, FO


def P(text, size=8.5, leading=None, color=DARK, bold=False, italic=False, align=0, href=None):
    fn = FB if bold else (FO if italic else FR)
    ld = leading or size + 2.2
    from reportlab.lib.styles import ParagraphStyle
    s = ParagraphStyle("", fontName=fn, fontSize=size, leading=ld, textColor=color, alignment=align, spaceAfter=0)
    if href:
        text = f'<a href="{href}" color="#2563EB">{text}</a>'
    return Paragraph(text, s)


def sec(text):
    return P(text, size=10, leading=13, color=ACCENT, bold=True)


# ── Data ───────────────────────────────────────────────────────
DEGREE = "B.Sc. in Computer Science"
UNIVERSITY = "Brac University"
DURATION = "Jan 2021 – Jun 2026"
CGPA = "3.09"
COURSEWORK = [
    "Software Engineering",
    "Algorithms & Data Structures",
    "Database Systems",
    "Artificial Intelligence",
    "Compiler Design",
    "Operating Systems",
]


def build_education():
    items = []
    items.append(sec("EDUCATION"))
    items.append(Spacer(1, 2))
    items.append(P(DEGREE, size=9, leading=12, bold=True))
    items.append(P(UNIVERSITY, size=8.5, leading=11.5, color=MID))
    items.append(P(DURATION, size=8.5, leading=11.5, color=MID))
    items.append(P(f"CGPA: {CGPA}", size=8.5, leading=11.5, color=MID))
    items.append(Spacer(1, 3))
    items.append(P("Relevant Coursework:", size=8.5, leading=11.5, bold=True))
    for c in COURSEWORK:
        items.append(P(f"• {c}", size=8, leading=11, color=BODY))
    return items
