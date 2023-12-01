import json
from os.path import isfile
from typing import List, Union


class InputHelper:
    def __init__(self, day):
        self.day = day

    def load_data(self, as_string=False, as_json=False) -> Union[List[str], str]:
        file_path = "../inputs/day{}.txt".format(self.day)

        if not isfile(path=file_path):
            print("File \"{}\" does not exist!\n".format(file_path))
            exit(1)

        handle = open(file=file_path, mode='rt', encoding='utf-8')

        if as_string:
            result = handle.read()
            handle.close()
            return result
        elif as_json:
            result = json.load(handle)
            handle.close()
            return result
        else:
            lines = []

            for line in handle:
                lines.append(line.rstrip())

            handle.close()

            return lines
