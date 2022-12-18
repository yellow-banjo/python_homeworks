import csv
import json


def converter(file_name):
    input_data = read_data(file_name)
    if input_data == [[]]:
        raise ValueError('File is empty')

    feature = input_data.pop(0)
    for i, x in enumerate(feature):
        if x == '':
            feature[i] = 'feature ' + str(i)
    jsons = []
    for data in input_data:
        jsons.append(convert(feature, data))
    write_data(jsons)


def convert(feature, data):
    json_ = {}
    for key, x in zip(feature, data):
        if x == '':
            json_[key] = 'null'
        else:
            json_[key] = x
    return json_


def read_data(file_name):
    data = []
    with open(file_name) as file:
        cur = csv.reader(file)
        for i in cur:
            data.append(i)
    return data


def write_data(data):
    with open("output.json", "w") as file:
        file.write(json.dumps(data, indent=1))


def main():
    converter("input.csv")


if __name__ == '__main__':
    main()
