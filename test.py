from wrapper.pdf      import Document, A4
from wrapper.styles   import p, h2, h3
from wrapper.layouts  import firstCover, lastCover

# output file
output = 'pdf/'+__file__[:-3]+'.pdf'

# Initialize PDF
pdf = Document(output, title='My Title Test', pagesize=A4)

# start page applying a specific layout "first_cover"
pdf.page(layout=firstCover)

# change paddings for next pages by setting all to 40 points
pdf.padding(left=40,right=40,top=40,bottom=40)

# start page applying no layout (defaults settings)
pdf.page(
  h2('About This Document'),
  p('This document explains my attempt to wrap the current Reportlab Toolkit API in order to make PDFs easily.'),
  h3('How it works')
)

# start page applying a layout "last_cover"
pdf.page(layout=lastCover)

# save and close document
pdf.close()
