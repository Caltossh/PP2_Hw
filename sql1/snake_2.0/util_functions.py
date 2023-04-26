import re


def get_level(file_name):

    level_pattern = re.compile(r'level=(.*)')
    level = ''
    file_data = ''
    with open(file_name, 'r') as file:
        for line in file.readlines():
            file_data += line
    level = level_pattern.findall(file_data)

    try:
        return level[0]
    except IndexError as _ex:
        return 1

#get_level('./progress_data/beket_data.txt')


def get_map(file_name):
    map_pattern = re.compile(r'(\[{1}\d+.*\])')
    file_data = ''
    with open(file_name, 'r') as file:
        for line in file.readlines():
            file_data += line
    
    map_list = map_pattern.findall(file_data)
    row = ''
    output_map = []
    for map in map_list:
        #print(map)
        row = re.findall(pattern = r'\d.', string= map, flags = re.DOTALL)
        row = [int(float(i)) for i in row]
        output_map.append(row)
    return output_map
    
print(get_map('snake_2.0/progress_data/data.txt'))

def get_body_list(file_name):
    body_list_text = ''
    with open(file_name, 'r') as file:
        for line in file.readlines():
            if 'body_list' in line:
                body_list_text = line
    pattern = re.compile(r"\((.*?)\)")
    vectors = pattern.findall(body_list_text)
    output = []
    for vector in vectors:
        output.append(tuple([int(i) for i in re.split(", ", vector)]))
    return output

#get_body_list('./progress_data/beket_data.txt')
