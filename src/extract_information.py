from bm import *
from kmp import *
from regex import *
from load_txt import *
from kasus_waktu import *
from Information import *

# menyimpan ke dalam list of information
def extract_information(folder, keyword, algorithm):
    files = get_file_name(folder) # menyimpan list of file
    texts = [] # menyimpan kalimat
    for file in files:
        texts.append(break_into_sentence(file))
    found = -999
    i = 0
    infos = [] # menyimpan list of information
    # mencari kemunculan keyword dalam kalimat
    for text in texts:
        for sentence in text:
            if algorithm.lower() == "kmp":
                found = kmp_match(sentence, keyword)
                if found != -999:
                    cases = find_cases(sentence, kmp_match(sentence, keyword))
                    date = find_tanggal(sentence, find_tanggal(texts[i][2],""))
                    file_name = files[i]
                    info = Information(cases, date, sentence, file_name)
                    infos.append(info)
            elif algorithm.lower() == "bm":
                found = bm_match(sentence, keyword)
                if found != -999:
                    cases = find_cases(sentence, bm_match(sentence, keyword))
                    date = find_tanggal(sentence, find_tanggal(texts[i][2],""))
                    file_name = files[i]
                    info = Information(cases, date, sentence, file_name)
                    infos.append(info)
            elif algorithm.lower() == "regex":
                found = regex_match(sentence, keyword)
                if found != -999:
                    cases = find_cases(sentence, regex_match(sentence, keyword))
                    date = find_tanggal(sentence, find_tanggal(texts[i][2],""))
                    file_name = files[i]
                    info = Information(cases, date, sentence, file_name)
                    infos.append(info)
        i += 1
    return infos