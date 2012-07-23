# Reportlab API Wrapper #

## Presentation ##
This project is an attempt to wrap the Reportlab current API in order to generate PDFs  easily.

## Getting started ##
1- Get the project from git:

$ git clone https://github.com/krispouille/reportlab-wrapper

2- In your project directory, create your python script for a test

```python
from wrapper.pdf import Document, A4
from wrapper.styles import h2, p

# Initialize PDF
pdf = Document('test.pdf', 'Lipsum')

pdf.page(
  h2('What is Lorem Lipsum ?'),
  p('''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.''')
)

# save and close PDF
pdf.close()
```
