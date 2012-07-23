from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table
from reportlab.platypus.tables import TableStyle
from reportlab.lib.enums import TA_RIGHT

def p(text):
  return Paragraph(text,DEFAULT)

def h2(text):
  return Paragraph(text,H2)

def h3(text):
  return Paragraph(text,H3)

def table(datas):
  return Table(datas,style=DEFAULT_TABLE)

DEFAULT = ParagraphStyle('default',
  fontName = 'Times-Roman',#Helvetica
  fontSize = 13,
  leading  = 15.6,
  spaceAfter = 6
)
H2 = ParagraphStyle('H2',
  fontName  = 'Helvetica-Bold',
  fontSize  = 20,
  textColor = '#17365d',
  leading  = 24,
  spaceAfter = 6,
)
H3 = ParagraphStyle('H3',
  fontName   = 'Helvetica-Bold',
  fontSize   = 15,
  textColor  = '#336391',
  spaceAfter = 30
)
DEFAULT_TABLE = TableStyle([
  ('ALIGN', (0,0), (-1,-1), 'LEFT'),
  ('VALIGN', (0,0), (-1,-1), 'TOP'),
  ('LEFTPADDING', (0,0), (-1,-1), 0),
  ('RIGHTPADDING', (0,0), (-1,-1), 0),
 # ('TOPPADDING', (0,0), (-1,-1), 0),
 # ('BOTTOMPADDING', (0,0), (-1,-1), 0),
])
COVER_TITLE_1  = ParagraphStyle('cover_title_1', 
  fontSize  = 50, 
  leading   = 62, 
  textColor = '#ffffff'
) 
COVER_TITLE_2 = ParagraphStyle('cover_title_2', 
  fontName  = 'Helvetica-Bold',
  fontSize  = 40, 
  leading   = 52, 
  textColor = '#990000'
) 
