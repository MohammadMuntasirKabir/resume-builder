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
    "I am a Software Engineer, AI Automation Specialist and Full-Stack Developer "
    "with expertise in full-stack web development using React, NextJS, Laravel, and modern JavaScript. "
    "Furthermore, I am proficient in leveraging AI-powered development tools, including "
    "Claude Code, Codex, n8n, Zapier, Opencode, Openclaw, Hermes Agent and more, "
    "to accelerate development while maintaining software quality. "
    "I also have 6 months of professional experience in Software Development where "
    "I customized and implemented ODOO ERP solutions with enhancements across 23+ modules "
    "and developed client-focused business workflows with the aid of AI Automation. "
    "Moreover, I have also learned about and improved on client communication,  "
    "requirements analysis, and translating business objectives into scalable technical "
    "solutions while managing multiple concurrent projects in a fast-paced and time-contrained environment."
)


def build_summary():
    items = []
    items.append(sec("PROFESSIONAL SUMMARY"))
    items.append(Spacer(1, 2))
    items.append(P(SUMMARY, size=8.5, leading=11.5, color=BODY))
    return items
