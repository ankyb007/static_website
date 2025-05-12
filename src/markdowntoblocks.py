def markdown_to_blocks(text):

    final =[]
    result =text.split("\n\n")

    for i in result:
        if i == "":
            continue
        final.append(i.strip())
    return final
    #res=list(map(lambda x:x.strip(), result))
    #final = filter(lambda x:x.strip(),res)
    #return list(final)