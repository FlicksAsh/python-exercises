def remove_first_and_last(content):
    return content[1:-1]



html = ['<h1>', "Some content", "more content", '</h1>']

print(remove_first_and_last(html))