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
        if not os.path.isdir('cache'):
            os.makedirs(f'cache')
        with open(f'cache/{q}.json', 'w') as outfile:
            json.dump(js, outfile)
        return js
    else:
        with open(f'cache/{q}.json', 'r') as file:
            js = json.load(file)
        return js


def json_navigate(obj_elm):
    while True:
        output_list = []
        if isinstance(obj_elm, (list, dict, tuple)):
            if isinstance(obj_elm, (list, tuple)):
                ind_l = list(range(len(obj_elm)))
            else:
                ind_l = list(obj_elm.keys())
        elif obj_elm is None:
            print('\n\n──> Nothing here...\n')
            return
        else:
            print(f'\n\n──> {obj_elm}\n')
            return
        for i, each in enumerate(obj_elm):
            if not isinstance(each, (list, tuple, dict)):
                output_list.append((f'├── [{i}|{obj_elm[ind_l[i]].__class__.__name__}] ──── {each}', 1))
            else:
                output_list.append((f'├── [{i}|{obj_elm[ind_l[i]].__class__.__name__}]/', 0))
        output_list.sort(key=lambda x: x[-1])
        for elm in output_list:
            print(elm[0])
        value = input('\nEnter an index of element or press "h" to move back: ')
        os.system('cls' if os.name == 'nt' else 'clear')
        if value == 'h':
            return
        else:
            value = int(value)
        json_navigate(obj_elm[ind_l[value]])


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
