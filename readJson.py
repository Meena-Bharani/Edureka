import json
from dotenv import load_dotenv
load_dotenv()
path = os.getenv('PATH')

class read_json_example:
    def read_json_data_1(path):
        _data = json.load(open(path))
        data = json.loads(json.dumps(_data))
        print(data["name"])
        for i in data['languages']:
            print(i)

    def read_json_data_2(path):
        _data = open(path,'r')
        # json to python
        data = json.load(_data)
        print(data['name'])
        for i in data['languages']:
            print(i)

    def read_json_data_3(path):
        with open(path) as _data:
            data = json.load(_data)
            print(data['name'])
if __name__=='__main__':
    # courses = {"name": "meena", "languages": ["Python", "Java", "SQL"]}
    ex = read_json_example.read_json_data_3(path)