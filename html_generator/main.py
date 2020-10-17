def html_generator(title, heading_type):
    html = f"<h{heading_type}>{title}</h{heading_type}>"
    return html 

print(html_generator("Rocking the Sway", 1))