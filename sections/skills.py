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
    ("Languages", "Python, JavaScript, TypeScript, PHP, HTML5, CSS3"),
    ("Frameworks", "React, Next.js, Laravel, Livewire, Vue.js, Tailwind CSS, Node.js, Express"),
    ("CMS", "WordPress, Custom Theme & Plugin Development"),
    ("State Mgmt", "Redux, Zustand"),
    ("Databases", "PostgreSQL, MySQL, SQLite, MongoDB, Firebase, Supabase"),
    ("ERP", "Odoo ERP"),
    ("AI Automation", "Claude Code, Codex, OpenCode, PI, Zapier, n8n, OpenClaw, Hermes Agent"),
    ("DevOps & Cloud", "Git, GitHub, GitLab, Docker, GraphQL, REST APIs"),
    ("Auth & Payments", "NextAuth 5, Clerk, Neon Auth, Better Auth"),
    ("Other", "Figma, MCP, LLMs, Prisma"),
]


def build_skills():
    items = []
    items.append(sec("TECHNICAL SKILLS"))
    items.append(Spacer(1, 2))
    for lbl, val in SKILL_GROUPS:
        items.append(P(f"<b>{lbl}:</b> {val}", size=8, leading=11, color=BODY))
    return items
