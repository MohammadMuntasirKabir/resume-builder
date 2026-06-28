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
        "name": "AI Travel Planner",
        "date": "May – Jun 2026",
        "url": "https://github.com/MohammadMuntasirKabir/ai-travel-planner",
        "demo": "https://ai-travel-planner-azure-chi.vercel.app",
        "stack": "Next.js 16, React 19, Prisma, NextAuth 5, OpenRouter AI, @dnd-kit, react-globe.gl",
        "desc": "AI-powered travel planning with AI-generated itineraries, location suggestions, "
                "drag-and-drop trip organization, interactive globe view, and AI chat. "
                "68 tests, rate limiting, error boundaries, input validation.",
    },
    {
        "name": "HRMS System",
        "date": "May – Jun 2026",
        "url": "https://github.com/MohammadMuntasirKabir/hrms-system",
        "demo": "https://hrms-system-ogg4.onrender.com",
        "stack": "Laravel 13, Livewire 4, Flux UI, Spatie Permission, SQLite",
        "desc": "Human Resource Management System: employee management, recruitment workflows, "
                "payroll, 6-role access control, audit logging, dashboard analytics, API resources. "
                "209+ tests passing.",
    },
    {
        "name": "Event Planner Pro",
        "date": "May – Jun 2026",
        "url": "https://github.com/MohammadMuntasirKabir/event-planner-pro",
        "demo": "https://event-planner-pro-lac.vercel.app",
        "stack": "Next.js 16, Clerk, Prisma, Neon DB, Tailwind CSS",
        "desc": "Full-stack event management platform with event creation, attendee management, "
                "RSVP tracking, invite links, and polished dashboard. Rate limiting, input "
                "validation, error boundaries. 208 tests passing.",
    },
    {
        "name": "GymAI Dhaka",
        "date": "May – Jun 2026",
        "url": "https://github.com/MohammadMuntasirKabir/gymai-dhaka",
        "demo": "https://gym-ai-dhaka.vercel.app",
        "stack": "Vite, React 19, React Router, Neon DB, Tailwind CSS",
        "desc": "Gym partnership platform in Bangladesh. AI-generated personalized training plans, "
                "gym discovery, membership management, partner dashboards. Retry logic for AI API, "
                "form validation, error boundaries.",
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
        # Line 4: GitHub Repo + Live Demo — 1 space gap between
        items.append(Table(
            [[
                P("GitHub Repo", size=8, leading=11, color=LINK_CLR, href=proj["url"]),
                P(" Live Demo", size=8, leading=11, color=LINK_CLR, href=proj["demo"]),
            ]],
            colWidths=[RIGHT_W * 0.14, RIGHT_W * 0.14],
            style=INNER_TABLE_STYLE,
        ))

    return items
