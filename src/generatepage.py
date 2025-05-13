from markdowntohtmlnode import markdown_to_html_node
from extracttitle import extract_title
import os, os.path

def generate_page(from_path, template_path, dest_path,  basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        markdown_content = file.read()
        print(markdown_content)
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    title = extract_title(markdown_content)

    with open(template_path,'r') as file2:
        template_content = file2.read()
        print(template_content)
    updated_content = template_content.replace("{{ Title }}", title)
    updated_content = updated_content.replace("{{ Content }}", html_content)
    updated_content = updated_content.replace('href="/', f'href="{basepath}')
    updated_content = updated_content.replace('src="/', f'src="{basepath}')
    


    os.makedirs(os.path.dirname(dest_path), exist_ok= True)
    
    with open(dest_path, 'w') as dest_file:
        dest_file.write(updated_content)

    


    

    
    

    