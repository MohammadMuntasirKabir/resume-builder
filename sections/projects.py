"""Projects section."""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle

from config import RIGHT_W, DARK, BODY, MID, ACCENT, LINK_CLR, FB, FR, FO


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
PROJECTS = [
    {
        "name": "HRMS System",
        "date": "May – Jun 2026",
        "url": "https://github.com/MohammadMuntasirKabir/hrms-system",
        "demo": "https://hrms-system-prod.vercel.app/",
        "stack": "Laravel 13, Livewire 4, PostgreSQL, Spatie Permission",
        "desc": "Full-stack HR Management System with multi-company support, payroll, "
                "recruitment workflows, 6-role access control, and dashboard analytics. "
                "Delivered for client deployment with 209+ tests.",
    },
    {
        "name": "Stilla Furniture",
        "date": "Jul – Aug 2026",
        "url": "https://github.com/MohammadMuntasirKabir/stilla-furniture",
        "demo": None,
        "stack": "WordPress, Docker, Custom Theme, Stripe, SEO",
        "desc": "Scandinavian furniture storefront with custom WordPress theme, "
                "shopping cart, Stripe payments, authentication, and SEO optimization.",
    },
]

INNER_TABLE_STYLE = TableStyle([
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
])


def build_projects():
    items = []
    items.append(sec("PROJECTS"))
    items.append(Spacer(1, 2))

    for i, proj in enumerate(PROJECTS):
        if i > 0:
            items.append(Spacer(1, 3))

        # Line 1: Project name (left) + Date (right) — same line
        items.append(Table(
            [[
                P(proj["name"], size=9.5, leading=12.5, bold=True, color=DARK),
                P(proj["date"], size=8.5, leading=11.5, color=MID, align=2),
            ]],
            colWidths=[RIGHT_W * 0.70, RIGHT_W * 0.30],
            style=INNER_TABLE_STYLE,
        ))
        # Line 2: Technologies
        items.append(P(proj["stack"], size=8, leading=11, italic=True, color=MID))
        # Line 3: Description
        items.append(P(proj["desc"], size=8.5, leading=11.5, color=BODY))
        # Line 4: Full URLs for print
        link_cells = []
        if proj.get("url"):
            link_cells.append(P(proj["url"], size=7.5, leading=10, color=LINK_CLR, href=proj["url"]))
        if proj.get("demo"):
            if link_cells:
                link_cells.append(P("  ·  ", size=7.5, leading=10, color=MID))
            link_cells.append(P(proj["demo"], size=7.5, leading=10, color=LINK_CLR, href=proj["demo"]))
        if link_cells:
            items.append(Table([link_cells], colWidths=[RIGHT_W * 0.95], style=INNER_TABLE_STYLE))

    return items
