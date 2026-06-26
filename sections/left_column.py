"""Shared utilities for left-column sections."""

from reportlab.lib.colors import HexColor
from reportlab.platypus import HRFlowable


def hr():
    return HRFlowable(width="100%", thickness=0.5, color=HexColor("#D1D5DB"), spaceAfter=2, spaceBefore=1)
