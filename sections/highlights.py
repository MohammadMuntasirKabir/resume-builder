"""Core Competencies section — tailored for Client Relationship Executive role."""

from reportlab.platypus import Paragraph, Spacer

from config import DARK, BODY, ACCENT, FB, FR, FO


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
COMPETENCIES = [
    "Client Communication",
    "Requirement Gathering",
    "Stakeholder Management",
    "English Fluency",
    "Cross-functional Collaboration",
    "Technical Consulting",
]


def build_highlights():
    items = []
    items.append(sec("CORE COMPETENCIES"))
    items.append(Spacer(1, 2))
    for c in COMPETENCIES:
        items.append(P(f"• {c}", size=8.5, leading=11.5, color=BODY))
    return items
