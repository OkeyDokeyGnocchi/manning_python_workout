# XML Generator
#  - Create a function myxml()
#    - Should take three arguments
#      - tag name: first argument creates opening and closing tags
#        - myxml('foo') -> <foo></foo>
#      - input text: second argument is text between the tags
#        - myxml('foo'. 'bar') -> <foo>bar</foo>
#      - tag attributes: third argument is name-value pairs to modify opening tag
#        - myxml('foo', 'bar', a=1, b=2, c=3) -> <foo a="1" b="2" c="3">bar</foo>
#    - Should return a string with xml-like elements based on input

def myxml(tag_name, inner_text="", **modifiers):
    mod_string = ""
    for k,v in modifiers.items():
        mod_string += f' {k}="{str(v)}"'
    return f'<{tag_name}{mod_string}>{inner_text}</{tag_name}>'

if __name__ == '__main__':
    print(myxml('foo', 'bar', a=1, b=2, c=3))
    print(myxml('foo'))