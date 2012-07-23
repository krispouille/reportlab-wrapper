# Reportlab API Wrapper #

## Presentation ##
This project is an attempt to wrap the Reportlab current API in order to generate PDFs  easily.

## Getting started ##
1- Get the project from git:

$ git clone https://github.com/krispouille/reportlab-wrapper

2- In your project directory, create your python script for a test
```
from wrapper.pdf import Document, A4

# Initialize PDF
pdf = Document('test.php', 'MY_TITLE')

pdf.page(
  h2('MY_TITLE'),
  p('Help')
)

# save and close PDF
pdf.close()
```
