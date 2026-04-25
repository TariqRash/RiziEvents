from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Inches, Pt


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "deliverables" / "RiziEvents-Technical-Documentation.docx"


def ensure_styles(document: Document) -> None:
    normal = document.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(10.5)

    if "CodeBlock" not in document.styles:
        style = document.styles.add_style("CodeBlock", WD_STYLE_TYPE.PARAGRAPH)
        style.font.name = "Courier New"
        style.font.size = Pt(8.5)
        pf = style.paragraph_format
        pf.left_indent = Inches(0.25)
        pf.right_indent = Inches(0.25)
        pf.space_before = Pt(3)
        pf.space_after = Pt(3)


def add_markdown(document: Document, path: Path) -> None:
    in_code = False
    code_lang = ""

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()

        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lang = line[3:].strip()
                if code_lang:
                    document.add_paragraph(code_lang.upper(), style="Intense Quote")
            else:
                in_code = False
                code_lang = ""
            continue

        if in_code:
            document.add_paragraph(line or " ", style="CodeBlock")
            continue

        if not line.strip():
            document.add_paragraph("")
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            level = min(len(heading.group(1)), 4)
            document.add_heading(heading.group(2).strip(), level=level)
            continue

        if re.match(r"^\d+\.\s+", line):
            document.add_paragraph(re.sub(r"^\d+\.\s+", "", line), style="List Number")
            continue

        if line.startswith("- "):
            document.add_paragraph(line[2:], style="List Bullet")
            continue

        document.add_paragraph(line)


def add_diagram_section(document: Document, title: str, path: Path) -> None:
    document.add_heading(title, level=2)
    document.add_paragraph("Mermaid source:")
    document.add_paragraph(path.read_text(encoding="utf-8").strip(), style="CodeBlock")


def main() -> None:
    document = Document()
    ensure_styles(document)

    section = document.sections[0]
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

    document.add_heading("RiziEvents Technical Documentation", level=0)
    document.add_paragraph("Reduced MVP submission package for the Holberton phase-three review.")

    add_markdown(document, ROOT / "docs" / "technical-documentation.md")

    document.add_page_break()
    add_markdown(document, ROOT / "docs" / "api-spec.md")

    document.add_page_break()
    add_markdown(document, ROOT / "docs" / "scm-qa-plan.md")

    document.add_page_break()
    add_markdown(document, ROOT / "docs" / "technical-justifications.md")

    document.add_page_break()
    add_diagram_section(document, "System Architecture Diagram", ROOT / "docs" / "diagrams" / "system-architecture.mmd")
    add_diagram_section(document, "Database ER Diagram", ROOT / "docs" / "diagrams" / "database-er.mmd")
    add_diagram_section(document, "Sequence Diagram: Create and Publish Event", ROOT / "docs" / "diagrams" / "sequence-create-publish.mmd")
    add_diagram_section(document, "Sequence Diagram: Guest Registration", ROOT / "docs" / "diagrams" / "sequence-guest-registration.mmd")
    add_diagram_section(document, "Sequence Diagram: Offline Check-in", ROOT / "docs" / "diagrams" / "sequence-offline-checkin.mmd")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    document.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
