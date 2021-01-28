import textwrap as tw
text = '123123 123 123'
data = 'this is\n\t\ta    text'

print(text)
'''
print(tw.wrap(text,width=4))
print(tw.fill(text, width=3))

print(tw.shorten(text, width=3, placeholder=')))'))
'''
print(data)
print(tw.dedent(data))
