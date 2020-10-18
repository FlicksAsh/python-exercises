def remove_first_and_last(list_to_clean):
    _, *content, _ = list_to_clean
    return content


html = ['<h1>', "Some content", "more content", '</h1>']

print(remove_first_and_last(html))