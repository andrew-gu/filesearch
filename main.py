from pathlib import Path
import shutil
'''-------------input-------------'''
def input_path():
    p = Path(input())
    if not p.exists():
        print('ERROR1')
        input_path()
    return p
def input_attributes()->list:
    search_att = input()
    setting = str()
    val = str()
    if search_att[0] not in ['N','E','S'] and not search_att[1] == ' ':
        print('ERROR2')
        input_attributes()
    setting = search_att[0]
    val = search_att[2:]
    if search_att[0] == 'S':
        try:
            val = int(search_att[2:])
        except TypeError:
            print('ERROR3')
            input_attributes()
    return [setting,val]

def input_action()->str:
    search_act = input()
    if search_act not in ['P','F','D','T']:
        print('ERROR4')
        input_action()
    return search_act
'''----------action handling--------------'''
def find_name(val:str,act:str,p:Path):
    for i in p.iterdir():
        if i.is_dir():
            find_name(val,act,i)
        else:
            try:
                if val == i.name[0:i.name.index('.')]:
                    act_handler(i,act)
                else:
                    continue
            except ValueError:
                continue            
def find_ext(val:str,act:str,p:Path):
    if val[0] == '.':
        val = val[1:]
    for i in p.iterdir():
        if i.is_dir():
            find_ext(val,act,i)
        else:
            if val == i.suffix[1:]:
                act_handler(i,act)
            else:
                continue
def find_size(val:int,act:str,p:Path):
    for i in p.iterdir():
        if i.is_dir():
            find_size(val,act,i)
        else:
            if i.stat().st_size >= val:
                act_handler(i,act)
            else:
                continue
def act_open(p):
    print(p.open().readline())
def act_copy(p):
    shutil.copy(str(p),str(p.with_name(p.name + '.dup')))
def act_touch(p):
    p.touch()
def act_handler(p,act:str):
    print(p)
    if act == 'F':
        act_open(p)
    elif act == 'D':
        act_copy(p)
    elif act == 'T':
        act_touch(p)
def search_handler(attr: list, act:str, p:Path):
    if attr[0] == 'N':
        find_name(attr[1],act,p)
    elif attr[0] == 'E':
        find_ext(attr[1],act,p)
    elif attr[0] == 'S':
        find_size(attr[1],act,p)
def main():
    p = input_path()
    a = input_attributes()
    act = input_action()
    search_handler(a,act,p)
if __name__ == '__main__':
    main()
