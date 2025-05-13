from generatepage import generate_page
import os,os.path
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    
    source_contents = os.listdir(dir_path_content)
    for item  in source_contents:
        source_path = os.path.join(dir_path_content,item)
        dest_filename = item.replace('.md', '.html')
        dest_path = os.path.join(dest_dir_path, dest_filename)
        if os.path.isfile(source_path) and item.endswith(".md"):
            os.makedirs(os.path.dirname(dest_path), exist_ok= True)
            generate_page(source_path, template_path,dest_path, basepath)
        elif os.path.isdir(source_path):
            new_dest_dir = os.path.join(dest_dir_path,item)
            os.makedirs(new_dest_dir, exist_ok= True)
            generate_pages_recursive(source_path, template_path,new_dest_dir, basepath)





