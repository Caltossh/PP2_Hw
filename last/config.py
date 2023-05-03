from configparser import ConfigParser

def config(filename="./db_config.ini", section="postgresql"):
    parser = ConfigParser()

    parser.read(filename)
    
    db = {}
    if parser.has_section(section=section):
        params = parser.items(section=section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the filename {filename} file')
    
    return db