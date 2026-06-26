# Resume Builder

ATS-friendly resume generator for **Mohammad Muntasir Kabir** using Python + ReportLab.

## Overview

Generates a clean, two-column PDF resume with:
- Header with photo, name, title, and social links
- Left column: Education, Technical Skills, Highlights
- Right column: Professional Summary, Experience, Projects
- Light theme (white + grey) optimized for ATS parsing

## Project Structure

```
config.py              — Shared constants (colors, fonts, dimensions, output path)
index.py               — Main entry point; assembles and builds the PDF
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
```

## Usage

### Prerequisites

```bash
pip install reportlab Pillow
```

### Generate Resume

```bash
python index.py
```

Output: `Mohammad_Muntasir_Kabir_Resume.pdf`

### Configuration

Edit `config.py` to change colors, fonts, margins, output path, or photo source. To modify content, edit the corresponding file in `sections/`.

## Output

The generated PDF is automatically copied to the portfolio's `public/` folder for direct download:
`nextjs-personal-portfolio/public/Mohammad_Muntasir_Kabir_Resume.pdf`
