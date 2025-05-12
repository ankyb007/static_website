import re
def extract_title(markdown):
    res =[line[1:].strip() for line in markdown.split("\n") if re.match(r"^#[^#].*",line)]
    if res:
        return(res[0])
        
    raise Exception("L1 Header not found")

