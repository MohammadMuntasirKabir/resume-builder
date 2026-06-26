"""Header section: photo, name, title, location + social links."""

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle

from config import (
    CONTENT_W, DARK, MID, LINK_CLR, FB, FR, FO,
)

# ── Social links data ───────────────────────────────────────────
# (text, href_or_none, color)
SOCIAL_LINKS = [
    ("Dhaka, Bangladesh", None, MID),
    ("kabirmuntasir96@gmail.com", "mailto:kabirmuntasir96@gmail.com", LINK_CLR),
    ("GitHub", "https://github.com/MohammadMuntasirKabir", LINK_CLR),
    ("LinkedIn", "https://www.linkedin.com/in/mohammad-muntasir-kabir-642020381", LINK_CLR),
    ("Portfolio", "https://nextjs-personal-portfolio-zeta.vercel.app", LINK_CLR),
]


def P(text, size=8.5, leading=None, color=DARK, bold=False, italic=False, align=0, href=None):
    fn = FB if bold else (FO if italic else FR)
    ld = leading or size + 2.2
    from reportlab.lib.styles import ParagraphStyle
    s = ParagraphStyle("", fontName=fn, fontSize=size, leading=ld, textColor=color, alignment=align, spaceAfter=0)
    if href:
        text = f'<a href="{href}" color="#2563EB">{text}</a>'
    return Paragraph(text, s)


def build_header(photo):
    """Build the header: photo, name, title, location + social links."""
    from reportlab.platypus.flowables import Image as RLImage

    photo_obj = RLImage(photo, width=0.54 * inch, height=0.54 * inch)

    header_items = [
        Spacer(1, 5),
        photo_obj,
        Spacer(1, 3),
        P("Mohammad Muntasir Kabir", size=16, leading=19, color=DARK, bold=True, align=1),
        P("Software Engineer  ·  Full-Stack Developer  ·  AI Automation Specialist",
          size=8.5, leading=11.5, color=MID, align=1),
        Spacer(1, 2),
    ]

    # Build social links row
    social_cells = []
    for i, (text, href, color) in enumerate(SOCIAL_LINKS):
        if i > 0:
            social_cells.append(P("·", size=8, leading=11, color=MID, align=1))
        social_cells.append(P(text, size=8, leading=11, color=color, href=href))

    col_widths = [
        CONTENT_W * 0.18, CONTENT_W * 0.03,
        CONTENT_W * 0.24, CONTENT_W * 0.03,
        CONTENT_W * 0.13, CONTENT_W * 0.03,
        CONTENT_W * 0.16, CONTENT_W * 0.03,
        CONTENT_W * 0.20,
    ]

    social_table = Table([social_cells], colWidths=col_widths)
    header_items.append(social_table)
    header_items.append(Spacer(1, 5))

    header_table = Table([[item] for item in header_items], colWidths=[CONTENT_W])
    header_table.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 0.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
    ]))

    return header_table
