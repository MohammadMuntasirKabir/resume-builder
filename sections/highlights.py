"""Highlights section."""

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
HIGHLIGHTS = [
    "0.5+ years of professional experience",
    "3+ major projects at Xobotronix IT",
    "7+ AI automation tools used daily",
    "25+ technologies in active use",
    "Client-facing across 3+ concurrent projects",
    "Full-stack + ERP + AI agent development",
]


def build_highlights():
    items = []
    items.append(sec("HIGHLIGHTS"))
    items.append(Spacer(1, 2))
    for h in HIGHLIGHTS:
        items.append(P(f"• {h}", size=8, leading=11, color=BODY))
    return items
