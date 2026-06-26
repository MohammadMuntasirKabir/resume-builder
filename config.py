"""Shared configuration and styling constants for the resume builder."""

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch

# ── Output ─────────────────────────────────────────────────────
OUTPUT = "/home/rownak/projects/resume-builder/Mohammad_Muntasir_Kabir_Resume.pdf"
PHOTO_SRC = "/home/rownak/Pictures/Screenshot_20260620_182059.png"

# ── Page Layout ────────────────────────────────────────────────
PAGE_W, PAGE_H = LETTER
MARGIN = 0.32 * inch
CONTENT_W = PAGE_W - 2 * MARGIN

LEFT_W = 1.85 * inch
RIGHT_W = CONTENT_W - LEFT_W

# ── Colors ─────────────────────────────────────────────────────
BG = white
SIDE_BG = HexColor("#F3F4F6")
DIVIDER = HexColor("#D1D5DB")
ACCENT = HexColor("#2563EB")
DARK = HexColor("#111827")
BODY = HexColor("#1F2937")
MID = HexColor("#4B5563")
LINK_CLR = HexColor("#2563EB")

# ── Fonts ──────────────────────────────────────────────────────
FB = "Helvetica-Bold"
FR = "Helvetica"
FO = "Helvetica-Oblique"
