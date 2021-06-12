def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}<{0}>'.format(tag,msg))

    return wrap_text


tag1 = html_tag('h1')

print(tag1)

