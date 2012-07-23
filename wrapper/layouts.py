from wrapper.styles import COVER_TITLE_1, COVER_TITLE_2
from reportlab.platypus import Paragraph, Frame, Image, PageBreak, KeepTogether

def firstCover(pdf):
  ''' Settings to apply to the current (first) page '''

  pdf.rectangle(color='#336391',height='50%',top=0)
  pdf.rectangle(color='#e6eeee',height='50%',bottom=0)
  pdf.rectangle(color='#ffffff',width=260,height=322,left='center',top='center')
  pdf.text('Reportlab Toolkit',top='15%',left='center',style=COVER_TITLE_1)
  pdf.image('images/reportlab.gif', top='center', left='center')
  pdf.text('Wrapper',bottom='15%',left='center',style=COVER_TITLE_2)


def lastCover(pdf):
  ''' Settings to apply to the current (last) page '''

  pdf.padding(left=0,right=0,bottom=0,top=0)
  pdf.color('#e6eeee')
