from jinja2 import Template
# t=Template("hello {{something}}!")
# t.render(something="word")
x=[]
for n in range(10):
    x.append(n)

u=Template("count: {0}".format(x))
u.render()