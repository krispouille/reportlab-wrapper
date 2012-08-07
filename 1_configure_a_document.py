from wrapper import Document, landscape, A4

output = 'pdf/'+__file__[:-3]+'.pdf'

# Document extends class reportlab.pdfgen.canvas.Canvas

# example - Let's set an empty document :
# title    = "EMPTY_DOCUMENT" (default = '<Unknown>') 
# pagesize = landscape(A4)    (default = A4)
pdf = Document(output, title='EMPTY_DOCUMENT', pagesize=landscape(A4))

# save and close
pdf.close()
