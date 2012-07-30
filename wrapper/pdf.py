from reportlab.pdfgen import canvas
from reportlab.platypus import Frame, Paragraph, Image
from reportlab.lib.utils import ImageReader, simpleSplit
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import cm,inch
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import pagesizes
from reportlab.lib.colors import HexColor

landscape = pagesizes.landscape
portrait  = pagesizes.portrait
A4        = pagesizes.A4

class Document(canvas.Canvas):

  def __init__(self, filename, title=None, pagesize=None):
    ''' extends/initialize canvas '''
    
    title = '<Unknown>' if title==None else title
    size  = A4 if pagesize==None else pagesize
     
    canvas.Canvas.__init__(self, filename, pagesize=size)

    self.setTitle(title)
    self.pageCount          = 0

    self.pagesize           = size
    self.width, self.height = self.pagesize
    
    self.x                  = 0
    self.y                  = 0
    self.left               = 0
    self.right              = 0
    self.top                = 0
    self.bottom             = 0


  def placement(self, width=0, height=0, left=0, bottom=0, top=None, right=None):
    '''
    returns (x,y) position for an element depending on :
    - width   = int | '0-100%'
    - height  = int | '0-100%'
    - left    = int | 'center' | '0-100%'
    - bottom  = int | 'center' | '0-100%'
    - top     = int | 'center' | '0-100%'
    - right   = int | 'center' | '0-100%'
    '''
    x = y = 0

    width  = checkPercent(width, self.width)
    left   = checkPercent(left, self.width)
    right  = checkPercent(right, self.width)
    height = checkPercent(height, self.height)
    top    = checkPercent(top, self.height)
    bottom = checkPercent(bottom, self.height)
    
    if left=='center' or right=='center':
      x = self.width/2-width/2
    else:
      x = left
      x = x if right==None else self.width-width-right

    if top=='center' or bottom=='center':
      y = self.height/2-height/2
    else:
      y = bottom
      y = y if top==None else self.height-height-top
    
    return (x,y)

  def padding(self,bottom=None,top=None,left=None,right=None):
    ''' edit paddings '''

    bottom = bottom if bottom!=None else self.bottom
    top    = top    if top!=None    else self.top
    left   = left   if left!=None   else self.left
    right  = right  if right!=None  else self.right
    
    tx = left-self.left
    ty = bottom-self.bottom
    x  = tx if tx!=0 else left
    y  = ty if ty!=0 else bottom
    
    self.bottom = bottom
    self.top    = top
    self.left   = left
    self.right  = right
    self.width  = self.pagesize[0]-self.left-self.right
    self.height = self.pagesize[1]-self.bottom-self.top

    #print self.width,self.height,tx, ty
    self.translate(tx,ty)
    

  def page(self,*args,**config):
    ''' 
    Configure  a new page in the PDF
    Merge the defaults page configuration with the new one
    Apply all changes to this new page
    '''
    def _page(c):
      ''' sub-function to handle display of a page'''

      if self.pageCount > 0 : 
        self.showPage()
        self.translate(self.left,self.bottom)
      self.setPageSize(self.pagesize)

      color  = c.pop('color') if 'color' in c else None
      layout = c.pop('layout') if 'layout' in c else None

      self.padding(**c)

      self.pageCount = self.pageCount + 1
      if color: self.color(color)
      if layout: layout(self)
 
    story = list(args)
    
    if 'pagesize' in config:
      self.pagesize = config.pop('pagesize')
      self.width,self.height = self.pagesize
    
    if len(story)==0:
      _page(config)
    else:
      while(story):
        _page(dict(config))
        self.frame(story)

  def image(self, filename, width=None, height=None, left=0, bottom=0, top=None, right=None, mask=None, preserveAspectRatio=False, anchor='c'):
    ''' add an image to canvas '''
    
    self.saveState()
    image  = ImageReader(filename)
    width  = image.getSize()[0] if width==None  else width
    height = image.getSize()[1] if height==None else height
    
    width  = checkPercent(width, self.width)
    height = checkPercent(height, self.height)

    x, y = self.placement(width, height, left, bottom, top, right)
    self.drawImage(image, x, y, width, height, mask, preserveAspectRatio, anchor)
    self.restoreState()

  def text(self, text, width=None, height=None, left=0, bottom=0, top=None, right=None, style=None):
    ''' add a text/paragraph to canvas '''

    self.saveState()
    style  = getSampleStyleSheet()['Normal'] if style==None else style
    p      = Paragraph(text,style)
    width  = checkPercent(width, self.width)
    height = checkPercent(height, self.height)
    width  = stringWidth(p.getPlainText(),style.fontName, style.fontSize)+1 if width==None else width
    height = style.leading*len(simpleSplit(p.getPlainText(), style.fontName, style.fontSize, width)) if height==None else height

    width = self.width if width > self.width else width

    width, height = p.wrap(width, height)
    x,y = self.placement(width, height, left, bottom, top, right)

    p.drawOn(self,x,y)
    self.restoreState()


  def rectangle(self,width='100%',height='100%',left=0,bottom=0,top=None,right=None,color='#eeeeee'):
    ''' draw a rectangle  '''

    self.saveState()
    self.setFillColor(HexColor(color))
    width  = checkPercent(width, self.width)
    height = checkPercent(height, self.height)
    x,y = self.placement(width,height,left,bottom,top,right)
    self.rect(x,y,width,height,stroke=0,fill=1)
    self.restoreState()

  def color(self, c):
    ''' set a background color to a page  '''
    
    self.rectangle(color=c,width='100%',height='100%')

  def line(self,width='100%',height=1,left=None,bottom=None,top=None,right=None,color='#000'):
    ''' draw a line '''

    self.rectangle(width,height,left,bottom,top,right,color)
  
  def frame(self,story,width='100%',height='100%',left=0,bottom=0,top=None,right=None):
    ''' create a zone that will contain flowable elements '''

    self.saveState()
    
    width  = checkPercent(width, self.width)
    height = checkPercent(height, self.height)
    x,y    = self.placement(width,height,left,bottom,top,right)
    f      = Frame(x,y,width,height)
    f.addFromList(story,self)
    self.restoreState()

  def close(self):
    ''' close current page and save the document '''
    
    self.showPage()
    self.save()


  def style(self, name,font='Helvetica',size=13,letterSpacing=None,color='#000000',marginTop=0,marginBottom=6):
    ''' returns a function that will create a formatted text  '''

    letterSpacing=size*1.2 if letterSpacing==None else letterSpacing
    
    def callBack(text):
      return Paragraph(text, ParagraphStyle(name,
       fontName=font,
       fontSize=size,
       leading=letterSpacing,
       textColor=color,
       spaceBefore=marginTop,
       spaceAfter=marginBottom
      ))
    
    return callBack
    
def checkPercent(string, reference):
  ''' 
  for a given percentage in string (formatted as 'xx%') and an integer as reference,
  it returns the integer value. Examples :
  print checkPercent('10%',100) returns 10 (good format "xx%")
  print checkPercent(1200,100)  returns 1200 (bad format)
  '''

  if string==None: return string
  try:
    return int(string)
  except:
    value = string[:-1]
    if string[-1]=='%' and value.isdigit() and int(value) in range(101):
      return reference*int(value)/100
    else:
      return string
