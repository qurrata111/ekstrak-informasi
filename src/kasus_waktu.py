import re

def find_jam (sentence):
    results = []
    for match in re.finditer(r'(([0-9]|0[0-9]|1[0-9]|2[0-3])(?:.|:)([0-5][0-9]) ?([AaPpWw][MmIi][BbTt](?:|[Aa])))',sentence.upper()):
        results.append(match.group(0))
    for match in re.finditer(r'^([0-9]|0[0-9]|1[0-9]|2[0-3])(?:.|:)[0-5][0-9]',sentence.lower()):
        results.append(match.group(0)) 
    print(results)
    if len(results) != 0:
        for res in results:
            return res + " "
        return "" 
    else:
        return ""
def find_hari (sentence):
    results = re.findall(r'(?:Senin|Monday|Selasa|Tuesday|Rabu|Wednesday|Kamis|Thursday|Jumat|Friday|Sabtu|Saturday|Minggu|Sunday)',sentence)
    results = sorted(results,key=None,reverse=True)
    if len(results) != 0:
        for res in results:
            return res + " "
        return ""
    else:
        return ""

def find_bulan (sentence):
    res = re.findall(r'\d{0,2}\s{0,1}(?:Januari|January|Jan|February|Februari|Feb|Maret|March|Mar|April|Apr|May|Mei|June|Jun|Juni|July|Jul|Agustus|August|Agu|Aug|September|Sep|October|Oktober|Oct|Okt|November|Nov|Desember|December|Des|Dec)\s{0,1}\d{0,2},{0,1}\s{0,1}\d{0,4}', sentence)
    results = sorted(res,key=None,reverse=True)
    if len(results) != 0:
        for res in results:
            return res + " "
        return ''
    else:
        return ''
  
def find_tgl (sentence):
    results = re.findall(r'\d{1,2}/\d{1,2}/\d{1,4}|\d{1,4}/\d{1,2}/\d{1,2}|\d{1,2}-\d{1,2}-\d{1,4}|\d{1,4}-\d{1,2}-\d{1,2}',sentence.lower())
    results = sorted(results,key=None,reverse=True)
    if len(results) != 0:
        for res in results:
            return res + " "
        return ""
    else:
        return ""

def find_tanggal (sentence, news_date_update):
    news_date = news_date_update
    jam = find_jam(sentence)
    hari = find_hari(sentence)
    bulan = find_bulan(sentence)
    tanggal = find_tgl(sentence)
    date = hari + bulan + tanggal + jam
    if date != "" and len(date.replace(" ","")) > 3:
        return date
    else:
        return news_date

def find_cases (sentence, idx_keyword):
    cases = re.findall(r'\b\d+\b', sentence.lower()) # menyimpan semua angka
    # print(cases)
    cases_idx = [] # menyimpan idx kemunculan
    idx = 0
    if len(cases) != 0:
        if len(cases) == 1:
            return cases[0]
        else :
            for match in re.finditer(r'\b\d+\b', sentence.lower()):
                start, end = match.span()
                cases_idx.append(start)
            # print(cases_idx)
            deltas = []
            for case_idx in cases_idx: # memasukkan selisih angka terdekat dengan keyword
                deltas.append(abs(case_idx-idx_keyword))
            print(deltas)
            # mencari delta[i] terkecil
            min = deltas[0]
            for i in range (len(deltas)):
                if deltas[i] < min:
                    min = deltas[i]
                    idx = i
            # print(cases[idx])
            return cases[idx]
    return "0"
        
