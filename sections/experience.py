"""Professional Experience section."""

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
TITLE = "Software Developer Intern"
COMPANY = "Xobotronix IT — Dhaka, Bangladesh  |  Nov 2025 – May 2026"
BULLETS = [
    "Worked extensively with Odoo ERP — customizing 23+ modules, building workflows, "
    "and delivering client-facing solutions.",
    "Leveraged AI Automation tools (Claude Code, Codex, n8n, Zapier) to ship quality "
    "software in the shortest time possible.",
    "Built Xobo-Pharma digital pharmacy: AI Doctor Chat, appointments, eCommerce, "
    "inventory, accounting — fully automated order-to-invoice workflows.",
    "Built a Learning Management System (LMS) for ESS School and backend services "
    "for Whiteshell Hi-Tech.",
    "Actively involved in client communications across multiple projects, gathering "
    "requirements and translating them into technical deliverables.",
]


def build_experience():
    items = []
    items.append(sec("PROFESSIONAL EXPERIENCE"))
    items.append(Spacer(1, 2))
    items.append(P(TITLE, size=9.5, leading=12.5, bold=True))
    items.append(P(COMPANY, size=8.5, leading=11.5, italic=True, color=MID))
    for b in BULLETS:
        items.append(P(f"• {b}", size=8.5, leading=11.5, color=BODY))
    return items
