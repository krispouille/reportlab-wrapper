from wrapper import Document, A4

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

# create your own elements styles
h1    = pdf._text(font='Helvetica-Bold', size=20, color='#17365d')
p     = pdf._text(font='Times-Roman')
pre   = pdf._text(font='Courier',preformatted=True)
tbl   = pdf._table()
img   = pdf._image()

# start page applying a specific layout "firstCover"
pdf.page(layout=firstCover)

# change padding for next pages by setting all to 40 points
pdf.padding(left=20,right=20,top=20,bottom=20)

# start a page with :
#- no layout set
#- a background color #e6eeee
#- keeping the previous padding above: left = right = top = bottom = 40
#- a flow of text elements: h1 followed by p
pdf.page(
  h1('About This Document'),
  p('This document explains my attempt to wrap the current Reportlab Toolkit API in order to make PDFs easily.'),
  img('images/reportlab.gif'),
  color='#e6eeee'
)

# start page with :
#- no layout set
#- a background color #336391
#- overriding padding from 40 to 0
pdf.page(color='#336391',left=0,right=0,top=0,bottom=0)

# save and close document
pdf.close()
