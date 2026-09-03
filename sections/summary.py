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
    "Client-focused Software Engineer with 6 months of professional experience "
    "in international client communication, requirement gathering, and translating "
    "business needs into technical solutions. B.Sc. in CSE with strong command of "
    "full-stack web development (React, Next.js, Laravel, WordPress) and AI automation "
    "tools. Proven ability to manage cross-functional projects, deliver client-facing "
    "products, and build long-term relationships with stakeholders across multiple "
    "industries including healthcare, education, and HR management."
)


def build_summary():
    items = []
    items.append(sec("PROFESSIONAL SUMMARY"))
    items.append(Spacer(1, 2))
    items.append(P(SUMMARY, size=8.5, leading=11.5, color=BODY))
    return items
