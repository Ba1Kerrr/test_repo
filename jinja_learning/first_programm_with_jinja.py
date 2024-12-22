#first_jinja_example
from jinja2 import Template
name = input("Enter your name: ")
tmp = Template("Hello {{ name }}")
msg = tmp.render(name=name)
print(msg)
