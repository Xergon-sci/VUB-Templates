# VUB-Templates
This package contains templates for VUB-styled reports. With these templates, reports can be generated through code. See [here](#-usage) how to do that.

## Installation
The easiest way to install is directly from GitHub trough pip:
```
pip install git+https://github.com/Xergon-sci/VUB-Templates.git
```

## Usage
First, an instance of the template is made. Then, the document can be constructed as pleased. See the example below. If changes or small additions are wanted, the [fpdf2 documentation](https://pyfpdf.github.io/fpdf2/index.html) can be consulted.

```python
from templates import Report

# Make an instance from a template, it automatically generates a front page.
rep = Report('Dynamic reporting', 'With VUB-Templates in python.', 'Michiel Jacobs', 'Faculteit Wetenschappen en Bio-ingenieurswetenschappen')

# Add a Page
rep.add_page()

# Show off
rep.head1('Head 1')
rep.head2('Head 2')
rep.head3('Head 3')
rep.text('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.''')
rep.image('/VUB-Templates/demo/img/dioxin-835806_640.png', w=100)

# Table
data = (
    ('First name', 'Last name', 'Score', 'Comment'),
    ('Jeff', 'Bezas', '10/20', 'Does not deliver...'),
    ('Elon', 'Mesk', '19/20', ''),
    ('Bill', 'Doors', '17/20', ''),
    ('Isaac', 'Oldton', '16/20', 'Not in this class?'),
)

rep.table(data, 4)

# Save the template
rep.output('demo.pdf')
```
The output of this code can be observerd [here](https://github.com/Xergon-sci/VUB-Templates/blob/a298f0aa3fca896870d3a2dc880d523027a22073/demo/demo.pdf).

<img src="https://github.com/Xergon-sci/Alchemical-DFT/blob/2c7c9aa24005a819518583fcd064387650d3af22/alchemicalDFT/static/media/vub_rgb.png" width="500">