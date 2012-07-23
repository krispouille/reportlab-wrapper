from wrapper.styles import COVER_TITLE, COVER_DOMAIN
from reportlab.platypus import Paragraph, Frame, Image, PageBreak, KeepTogether

def first_cover(pdf):
  pdf.rectangle(color='#336391',height='50%',top=0)
  pdf.rectangle(color='#e6eeee',height='50%',bottom=0)
  pdf.rectangle(color='#ffffff',width=260,height=322,left='center',top='center')
  pdf.text('Reportlab Toolkit',top='15%',left='center',style=COVER_TITLE)
  pdf.image('images/reportlab.gif', top='center', left='center')
  pdf.text('Wrapper',bottom='15%',left='center',style=COVER_DOMAIN)


def last_cover(pdf):
  pdf.padding(left=0,right=0,bottom=0,top=0)
  pdf.color('#e6eeee')
