from wrapper.pdf          import Document, A4
from reportlab.platypus   import Paragraph
from reportlab.lib.styles import ParagraphStyle

##### custom layouts #####

def firstCover(pdf):
  ''' Layout for the first page '''
  pdf.rectangle(color='#336391',height='50%',top=0)
  pdf.rectangle(color='#e6eeee',height='50%',bottom=0)
  pdf.rectangle(color='#ffffff',width=260,height=322,left='center',top='center')
  pdf.image('images/reportlab.gif', top='center', left='center')

def lastCover(pdf):
  ''' Layout for the last page '''
  pdf.padding(left=0,right=0,bottom=0,top=0)
  pdf.color('#e6eeee')


##### DOCUMENT #####

# output file
output = 'pdf/'+__file__[:-3]+'.pdf'

# initialize PDF
pdf = Document(output, title='Example')

# create your own text formats
h1 = pdf.style('h1', font='Helvetica-Bold', size=20, color='#17365d')
p  = pdf.style('p',  font='Times-Roman')

# start page applying a specific layout "firstCover"
pdf.page(layout=firstCover)

# change paddings for next pages by setting all to 40 points
pdf.padding(left=40,right=40,top=40,bottom=40)

# start page applying no layout (default settings)
pdf.page(
  h1('About This Document'),
  p('This document explains my attempt to wrap the current Reportlab Toolkit API in order to make PDFs easily.'),
  color='#e6eeee'
)

# start page with a background color and no padding
pdf.page(color='#336391',left=0,right=0,top=0,bottom=0)

# save and close document
pdf.close()
