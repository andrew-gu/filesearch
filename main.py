from pathlib import Path
from shutil import copyfile

p = Path()
search_setting = str()
search_value = str()
search_action = str()
def input_path():
    global p
    p = Path(input())
    if p.exists() == False:
        print('ERROR')
        input_path()

def input_settings():
    search_param = input()
    global search_setting, search_value
    search_setting = search_param[0]
    if search_setting not in ['N','E','S']:
        print('ERROR')
        input_actions()
    try:
        search_param[2]          
    except IndexError:
        print('ERROR')
        input_settings()
    search_value = search_param[2:]
    if search_param[1] == ' ':
        if search_setting == 'N':
            pass
        elif search_setting == 'E':
            if search_value[0] == '.':
                search_value = search_value[1:]
        elif search_setting == 'S':
            try:
                search_value = int(search_value)
            except ValueError:
                print('ERROR')
                input_settings()
        else:
            print('ERROR')
            input_settings()

def input_actions():
    global search_action
    search_action = input()
    if search_action not in ['P','F','D','T']:
        print('ERROR')
        input_actions()

def browse_folders(path):
    for i in path.iterdir():
        if i.is_dir():
            browse_folders(i)
        elif i.is_file():
            execute_search(i)

def search_name(f):
    if (f.name.split('.')[0]) == search_value:
        execute_action(f)

def search_ext(f):
    if search_value in (f.suffixes):
        execute_action(f)

def search_size(f):
    if f.stat().st_size >= search_value:
        execute_action(f)
def execute_search(f):
    if search_setting == 'N':
        search_name(f)
    elif search_setting == 'E':
        search_ext(f)
    elif search_setting == 'S':
        search_size(f)

def execute_action(f):
    if search_action == 'P':
        print(f)
    if search_action == 'F':
        print(f)
        print(f.open().readline())
    if search_action =='D':
        print(f)
        copyfile(str(p),str(p)+'.dup')
    if search_action == 'T':
        print(f)
        f.touch()

def main():
    input_path()
    input_settings()
    input_actions()
    browse_folders(p)

if __name__ == '__main__':
    main()
