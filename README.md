# Reportlab API Wrapper #

## Presentation ##
This project is an attempt to wrap the Reportlab current API in order to generate PDFs  easily.

## Getting started ##
1- Get the project from git:

$ git clone https://github.com/krispouille/reportlab-wrapper

2- In your project directory, create your python script for a test

```python
from wrapper.pdf          import Document, A4
from reportlab.platypus   import Paragraph
from reportlab.lib.styles import ParagraphStyle


##### custom styles #####

def h1(text):
  ''' returns a Paragraph formatted as a title '''
  return Paragraph(text, ParagraphStyle('h1',
    fontName   = 'Helvetica-Bold',
    fontSize   = 20,
    textColor  = '#17365d',
    leading    = 24,
    spaceAfter = 6
  ))


def p(text):
   ''' returns a Paragraph to be added to a page '''
   return Paragraph(text, ParagraphStyle('p',
     fontName   = 'Times-Roman',
     fontSize   = 13,
     leading    = 15.6,
     spaceAfter = 6
   ))                  
 
##### custom layouts #####
 
def firstCover(pdf):
  ''' Layout for the first page '''
  pdf.rectangle(color='#336391',height='50%',top=0)
  pdf.rectangle(color='#e6eeee',height='50%',bottom=0)
  pdf.rectangle(color='#ffffff',width=260,height=322,left='center',top='center')
  pdf.image('images/reportlab.gif', top='center', left='center')
 
##### DOCUMENT #####

# initialize PDF
pdf = Document('example.pdf', title='Example')

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
 
# start page applying a layout "lastCover"
pdf.page(color='#336391',left=0,right=0,top=0,bottom=0)
 
# save and close document
pdf.close()
```
