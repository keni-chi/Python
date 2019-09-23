import re
import glob


def read_file(file_path):
    test_data = open(file_path, "r")
    lines = test_data.readlines()
    test_data.close()
    return lines


def get_file_path_list():
    file_path_list = glob.glob('./input/*.py')
    return file_path_list


def camel_to_word(camel):
    word_list = [x for x in re.split('([a-z]+)([A-Z][a-z0-9]+)|([A-Z][a-z0-9]+)', camel) if x != None and x != '']
    return word_list


def snake_to_word(snake):
    word_list = snake.split('_')
    print(word_list)
    return word_list


def make_word_list(target):
    file_path_list = get_file_path_list()
    
    for file_path in file_path_list:
        lines = read_file(file_path)

        matching_str = target + ' '
        method_list = []
        for line in lines:
            if matching_str in line:
                line = line.replace(matching_str, '')
                line =  line.split('(')[0]
                line = line.replace(' ', '')
                line = line.replace('__', '')
                if target == 'class':
                    method_list.extend(camel_to_word(line))
                elif target == 'def':
                    method_list.extend(snake_to_word(line))
                else:
                    pass

        words = '\n'.join(method_list)

        file_name = file_path.split('/')[2]
        file_name = file_name.split('.')[0]

        output_name = './output/' + file_name + '_' + target + '.txt'
        with open(output_name, 'wt') as f:
            f.write(words)


def main():
    make_word_list('class')
    make_word_list('def')


if __name__ == '__main__':
    main()
