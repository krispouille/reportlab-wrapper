from wrapper import Document, landscape, A4

output = 'pdf/'+__file__[:-3]+'.pdf'

# open a A4 document in landscapte and  with no paddings
pdf = Document(output, title='Configure a page', pagesize=landscape(A4))

# create a new page :
# set a background color
# override paddings from 0 to 10
# override pagesize from landscape to portrait
pdf.page(color='#336391', left=10, right=10, top=10, bottom=10, pagesize=A4)

# save and close
pdf.close()
