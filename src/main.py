from textnode import TextNode, TextType
from htmlnode import HTMLNode
from copystatic import copy_static
import os, os.path,shutil
from generatepage import generate_page
from generatepagesrecursive import generate_pages_recursive
import sys


def main():
    #a=TextNode("Hello World!",TextType.NORMAL,"www.facebook.com")
    #print(a)

    #node = HTMLNode(tag="div", value="Hello", props={"class": "container"})
    #print(node)  # Since you don't have a __str__ method, this will use __repr__

    basepath = "/"

    if len(sys.argv) >1 :
        basepath = sys.argv[1]


    source = "static"
    destination = "docs"

    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination, exist_ok= True)
    copy_static(source, destination)
    print(f"static files copied!")

    #markdown_path = "content/index.md"
    #template_path = "template.html"
    #dest_path = "public/index.html"

    #generate_page(markdown_path, template_path, dest_path)
    #print(f"index page generated!")

    dir_path_content = "content"
    template_path = "template.html"
    dest_dir_path = "docs"


    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)








    

if __name__ == "__main__":
    main()

