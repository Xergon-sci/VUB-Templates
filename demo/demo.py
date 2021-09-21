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