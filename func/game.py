import sqlite3
import json
import random

conn = sqlite3.connect('data/kr_korean.db')
c = conn.cursor()
datapath = "data/filter.json"

class word_relay:
    def __init__(self, enteredword):
        self.enterdword = enteredword
    
    def get_last_word(self):
        return self.enterdword[-1]
    
    def format_word(self, givenword):
        if "-" in givenword:
            givenword = givenword.replace("-", "")
        
        if len(givenword) < 2:
            pass
        else:
            return givenword
    
    def return_new_words(self):
        last_word = self.get_last_word()
        c.execute("SELECT word FROM kr WHERE part = '명사' AND word LIKE ?", (last_word + "%",))
        res = c.fetchall()
        #listify the result
        reslist = []
        for i in res:
            filteredword = self.format_word(i[0])
            if filteredword != None:
                reslist.append(filteredword)
        
        return reslist
    
    def choose_word(self):
        list_of_words = self.return_new_words()
        if len(list_of_words) == 0:
            return None
        else:
            #remove dupe words
            with open(datapath) as f:
                data = json.load(f)
                f.close()
            
            for i in data["used_words"]:
                if i in list_of_words:
                    list_of_words.remove(i)
            
            #get a random word from list_of_words
            random_word = random.choice(list_of_words)

            with open(datapath, "w") as f:
                data["used_words"].append(random_word)
                json.dump(data, f, indent=2)
                f.close()

            return random_word
    
def add_word(word):
    with open(datapath) as f:
        data = json.load(f)
        f.close()
    
    if word in data["used_words"]:
        return False
    else:
        data["used_words"].append(word)
        with open(datapath, "w") as f:
            json.dump(data, f, indent=2)
            f.close()
        return True

def remove_word(word):
    with open(datapath) as f:
        data = json.load(f)
        f.close()
    
    if word in data["used_words"]:
        data["used_words"].remove(word)
        with open(datapath, "w") as f:
            json.dump(data, f, indent=2)
            f.close()
        return True
    else:
        return False

def reset_game():
    what_i_want = {"used_words": []}
    with open(datapath, "w") as f:
        json.dump(what_i_want, f, indent=2)
        f.close()