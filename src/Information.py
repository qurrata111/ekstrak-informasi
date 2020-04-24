class Information:

    def __init__ (self):
        self.cases = 0
        self.date = "XX/XX/XXXX"
        self.sentence = "EMPTY"
        self.name_of_file = "NONE"

    def __init__ (self, cases, date, sentence, name_of_file):
        self.cases = cases
        self.date = date
        self.sentence = sentence 
        self.name_of_file = name_of_file 

    def set_cases (self, cases):
        self.cases = cases

    def set_date (self, date):
        self.date = date 

    def set_sentence (self, sentence):
        self.sentence = sentence 

    def set_name_of_file (self, name_of_file):
        self.name_of_file = name_of_file 

    def print_info(self):
        print("Waktu        :", self.date)
        print("Kasus        :", self.cases)
        print("Kalimat      :", self.sentence)
        print("Nama file    :", self.name_of_file)
        print()