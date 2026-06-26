#!/usr/bin/env python3
"""
Resume Builder — index.py
=========================

Single-page ATS-friendly resume for Mohammad Muntasir Kabir.
Light theme: white + grey, dark text. 2-column grid. All links clickable.

Structure:
  config.py              — Shared constants (colors, fonts, dimensions, output path)
  sections/
    __init__.py
    header.py            — Photo, name, title, location + social links
    education.py         — Education (degree, university, CGPA, coursework)
    skills.py            — Technical Skills
    highlights.py        — Highlights / Key Facts
    summary.py           — Professional Summary
    experience.py        — Professional Experience
    projects.py          — Projects list
    left_column.py       — Shared left-column utilities (hr divider)
    right_column.py      — Shared right-column utilities

To modify a specific section of the resume, edit only the corresponding
file in the sections/ folder. Do NOT touch config.py unless you want to
change global styling (colors, margins, fonts, output path).
"""

import os
from io import BytesIO

from PIL import Image, ImageDraw
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import (
    HRFlowable,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

import config
from sections.header import build_header
from sections.education import build_education
from sections.skills import build_skills
from sections.highlights import build_highlights
from sections.summary import build_summary
from sections.experience import build_experience
from sections.projects import build_projects
from sections.left_column import hr


def make_round_photo(src, size_px):
    img = Image.open(src).convert("RGBA")
    w, h = img.size
    side = min(w, h)
    img = img.crop(((w - side) // 2, (h - side) // 2, (w + side) // 2, (h + side) // 2))
    img = img.resize((size_px, size_px), Image.LANCZOS)
    mask = Image.new("L", (size_px, size_px), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size_px, size_px), fill=255)
    img.putalpha(mask)
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf


def build():
    # ── Photo ────────────────────────────────────────────────────
    from reportlab.platypus.flowables import Image as RLImage

    photo_buf = make_round_photo(config.PHOTO_SRC, 62)

    # ── Header ───────────────────────────────────────────────────
    header_table = build_header(photo_buf)
    header_border = HRFlowable(
        width=config.CONTENT_W, thickness=1.2,
        color=config.DIVIDER, spaceAfter=5, spaceBefore=0,
    )

    # ── Left Column (sidebar) ───────────────────────────────────
    left_all = []
    left_all += build_education()
    left_all.append(Spacer(1, 5))
    left_all.append(hr())
    left_all += build_skills()
    left_all.append(Spacer(1, 5))
    left_all.append(hr())
    left_all += build_highlights()

    # ── Right Column (main content) ─────────────────────────────
    right_all = []
    right_all += build_summary()
    right_all.append(Spacer(1, 5))
    right_all.append(hr())
    right_all += build_experience()
    right_all.append(Spacer(1, 3))
    right_all.append(hr())
    right_all += build_projects()

    # ── Balance columns ──────────────────────────────────────────
    while len(left_all) < len(right_all):
        left_all.append(Spacer(1, 1))
    while len(right_all) < len(left_all):
        right_all.append(Spacer(1, 1))

    # ── Wrap columns in tables ───────────────────────────────────
    right_table = Table([[item] for item in right_all], colWidths=[config.RIGHT_W])
    right_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 0.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))

    left_table = Table([[item] for item in left_all], colWidths=[config.LEFT_W])
    left_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 0.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))

    body_table = Table([[left_table, right_table]], colWidths=[config.LEFT_W, config.RIGHT_W])
    body_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (0, -1), config.SIDE_BG),
        ("BACKGROUND", (1, 0), (1, -1), config.BG),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("LINEAFTER", (0, 0), (0, -1), 0.7, config.DIVIDER),
    ]))

    # ── Build PDF ────────────────────────────────────────────────
    doc = SimpleDocTemplate(
        config.OUTPUT,
        pagesize=LETTER,
        leftMargin=config.MARGIN,
        rightMargin=config.MARGIN,
        topMargin=config.MARGIN,
        bottomMargin=config.MARGIN,
        title="Mohammad Muntasir Kabir — Resume",
        author="Mohammad Muntasir Kabir",
    )
    doc.build([header_table, header_border, body_table])
    print(f"Resume: {config.OUTPUT}  ({os.path.getsize(config.OUTPUT) / 1024:.1f} KB)")


if __name__ == "__main__":
    build()
