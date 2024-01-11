# mengembalikan type data dict type argument di awali dengan **
def create_div(tag,text,**atribute):
    html = f"<{tag} class= \"{" "}\">"
    for key,value in atribute.items():
        html + f"{key} {value}"
    html = html + f"{text}</{tag}>" # full tag html
    return html

div = create_div("div","Porfolio")
print(div)
div_peendidikan = create_div("div","Pendidikan",style="black")
print(div_peendidikan)