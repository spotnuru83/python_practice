

def write_lines_to_file(lines, to_file):
    with open(to_file,"w") as file:
        file.writelines(lines) 
