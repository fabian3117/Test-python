# from fpdf import FPDF
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# pdf.cell(200, 10, txt="Go Be Great!", ln=1, align="C")
# pdf.output("./sample_demo.pdf")
import sys

from consumer.consumer import Consumer

consumer=Consumer(sys.argv[1])
consumer.star_read()