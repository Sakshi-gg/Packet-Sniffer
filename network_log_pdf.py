import pandas as pd
from fpdf import FPDF

df = pd.read_csv("network_log.csv")

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "Network Traffic Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, f"Total Packets Captured: {len(df)}", ln=True)
pdf.ln(10)

pdf.set_font("Arial", "B", 12)
for col in df.columns:
    pdf.cell(45, 10, col, border=1)
pdf.ln()

pdf.set_font("Arial", size=10)
for _, row in df.iterrows():
    for item in row:
        pdf.cell(45, 10, str(item), border=1)
    pdf.ln()

pdf.output("Network_Report.pdf")
print("✅ PDF report saved as 'Report.pdf'.")
