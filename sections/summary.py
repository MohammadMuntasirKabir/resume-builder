"""Professional Summary section."""

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
SUMMARY = (
    "I'm Rownak (Mohammad Muntasir Kabir), a Software Developer Intern at Xobotronix IT in "
    "Dhaka, currently completing my B.Sc. in Computer Science at Brac University (CGPA 3.09). "
    "I build full-stack web applications with React, Next.js 16, and Laravel 13, and I'm "
    "especially drawn to AI-assisted development — using Claude Code, Codex, n8n, and Zapier to "
    "ship reliable software fast. At Xobotronix I've customized 23+ Odoo ERP modules and built "
    "client-facing products like Xobo-Pharma (an AI-powered digital pharmacy) and learning "
    "management systems. I care about writing tested, maintainable code, owning features end to "
    "end, and turning messy business requirements into clean technical deliverables."
)


def build_summary():
    items = []
    items.append(sec("PROFESSIONAL SUMMARY"))
    items.append(Spacer(1, 2))
    items.append(P(SUMMARY, size=8.5, leading=11.5, color=BODY))
    return items
