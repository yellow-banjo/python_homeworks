def converter(file_name):
    input_data = read_data(file_name)
    if input_data == ['']:
        raise ValueError('File is empty')

    feature = input_data.pop(0).split(',')
    for i, x in enumerate(feature):
        if x == '':
            feature[i] = 'feature ' + str(i)
    jsons = []
    for data in input_data:
        jsons.append(convert(feature, data))
    write_data(jsons)


def convert(feature, data):
    json = {}
    data = data.split(',')
    for key, x in zip(feature, data):
        if x == '':
            json[key] = 'null'
        else:
            json[key] = x
    return json


def read_data(file_name):
    with open(file_name) as file:
        data = file.read().splitlines()
    return data


def write_data(data):
    with open("output.json", 'w') as file:
        file.write('[\n')
        for i, d in enumerate(data):
            file.write(' {\n')
            for idx, (key, value) in enumerate(d.items()):
                if idx == len(d) - 1:
                    file.write(f'   {key}: {value}\n')
                else:
                    file.write(f'   {key}: {value},\n')
            if i == len(data) - 1:
                file.write(' }\n')
            else:
                file.write(' },\n')
        file.write(']\n')


def main():
    converter("input.csv")


if __name__ == '__main__':
    main()
