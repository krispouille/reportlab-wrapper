from wrapper.pdf      import Document, A4, landscape, portrait
from wrapper.styles   import p, h2, h3, table
from wrapper.layouts  import first_cover, last_cover

pdf = Document('test.pdf', title='My Title Test', pagesize=A4)

pdf.page(layout=first_cover)

pdf.padding(left=40,right=40,top=40,bottom=40)

pdf.page(
  h2('About This Document'),
  p('This document is an attempt for me to wrap the current Reportlab Toolkit API in order to make PDFs easily.')
)

pdf.page(layout=last_cover)
pdf.close()
