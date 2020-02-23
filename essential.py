import urllib.request
import twhandle
import json
import os.path
import os


def search_tweet(q, api_reference):
    if not os.path.isfile(f'cache/{q}.json'):
        url = twhandle.augment(api_reference, {'q': q})
        data = urllib.request.urlopen(url).read()
        js = json.loads(data)
        os.makedirs(f'cache')
        with open(f'cache/{q}.json', 'w') as outfile:
            json.dump(js, outfile)
        return js
    else:
        with open(f'cache/{q}.json', 'r') as file:
            js = json.load(file)
        return js


def json_navigate(obj_elem):
    while True:
        if isinstance(obj_elem, (list, dict, tuple)):
            if isinstance(obj_elem, (list, tuple)):
                ind_l = list(range(len(obj_elem)))
            else:
                ind_l = list(obj_elem.keys())
        elif obj_elem is None:
            print('\n\n──> Nothing here...\n')
            return
        else:
            print(f'\n\n──> {obj_elem}\n')
            return
        for i, each in enumerate(obj_elem):
            if not isinstance(each, (list, tuple, dict)):
                print(f'├── [{i}|{obj_elem[ind_l[i]].__class__.__name__}] ──── {each}')
            else:
                print(f'├── [{i}|{obj_elem[ind_l[i]].__class__.__name__}] ──── /.')
        value = input('\nEnter an index of element or press "b" to move back: ')
        os.system('cls' if os.name == 'nt' else 'clear')
        if value == 'h':
            return
        else:
            value = int(value)
        json_navigate(obj_elem[ind_l[value]])


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
