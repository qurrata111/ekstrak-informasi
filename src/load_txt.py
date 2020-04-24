import os
def break_into_sentence(name_file):
    list_of_sentence = []
    sentence = ""
    file = open(name_file, 'r')
    char = ""
    while (True):
        prev_char = char
        char = file.read(1)
        sentence += char
        if (char == ' ' and prev_char == ".") or char == '\n':
            sentence = sentence.replace('\n','')
            sentence += '\n'
            list_of_sentence.append(sentence)
            sentence = ""
        if not char:
            break
    file.close
    return list_of_sentence

def get_file_name(folder):
    list_file_name = []
    for dirname, _, filenames in os.walk(folder):
        for filename in filenames:
            list_file_name.append(os.path.join(dirname,filename))
    return list_file_name