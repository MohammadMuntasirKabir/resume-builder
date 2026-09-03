"""Technical Skills section."""

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
SKILL_GROUPS = [
    ("Client Relations", "Requirement Gathering, Stakeholder Communication, Project Scoping"),
    ("Web Development", "React, Next.js, Laravel, Vue.js, Tailwind CSS, Node.js"),
    ("Languages", "Python, JavaScript, TypeScript, PHP, C/C++, C#, .NET"),
    ("SEO & Marketing", "SEO Frameworks, Digital Marketing, Google Analytics"),
    ("Databases & Cloud", "PostgreSQL, MySQL, MongoDB, Firebase, Docker, Git"),
    ("AI & ERP", "Claude Code, Codex, n8n, Zapier, Odoo ERP, REST APIs"),
]


def build_skills():
    items = []
    items.append(sec("TECHNICAL SKILLS"))
    items.append(Spacer(1, 2))
    for lbl, val in SKILL_GROUPS:
        items.append(P(f"<b>{lbl}:</b> {val}", size=8, leading=11, color=BODY))
    return items
