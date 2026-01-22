from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import csv, statistics

csv_file = "sampledata.csv"
pdf_file = "automated_report.pdf"

with open(csv_file, newline='') as f:
    data = [row for row in csv.reader(f) if row]

scores = [int(r[1]) for r in data[1:] if len(r) > 1 and r[1].isdigit()]

doc = SimpleDocTemplate(
    pdf_file,
    pagesize=A4,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Title"],
    textColor=colors.darkblue,
    alignment=1  # Center
)

stat_style = ParagraphStyle(
    "StatStyle",
    parent=styles["Normal"],
    fontSize=11,
    spaceAfter=6
)

story = [
    Paragraph("AUTOMATED REPORT GENERATION", title_style),
    Spacer(1, 20),
    Paragraph("Summary Statistics", styles["Heading2"]),
    Spacer(1, 10),
    Paragraph(f"• Average Score : <b>{statistics.mean(scores):.2f}</b>", stat_style),
    Paragraph(f"• Highest Score : <b>{max(scores)}</b>", stat_style),
    Paragraph(f"• Lowest Score : <b>{min(scores)}</b>", stat_style),
    Spacer(1, 20),
    Paragraph("Detailed Data", styles["Heading2"]),
    Spacer(1, 10)
]

table = Table(data, hAlign="CENTER")
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#4F81BD")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("ALIGN", (1,1), (-1,-1), "CENTER"),
    ("FONT", (0,0), (-1,0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0,0), (-1,0), 10),
    ("BACKGROUND", (0,1), (-1,-1), colors.whitesmoke),
    ("GRID", (0,0), (-1,-1), 1, colors.grey),
]))

story.append(table)
doc.build(story)

print("PDF Report Generated Successfully")
