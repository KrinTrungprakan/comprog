import random

class thaigen:
    def __init__(self):
        self.lastpos = None
        self.thc = thc
        
    def get(self):
        consonant = random.choice(self.thc)
        self.lastpos = consonant[0]
        return consonant[0]
    
    def get_answer(self):
        for consonant in self.thc:
            if consonant.startswith(self.lastpos):
                split_entry = consonant
                return [split_entry[0], split_entry[1], *split_entry[2:].split()]
            
    
    def dont_ask_this(self, cons):
      #removes the consonant from thc so that it won't be asked again
      #look for the consonant cons in thc 
      for line in self.thc:
          if cons in line:
              #print("removing "+cons)
              self.thc.remove(line)

            
    def howmany(self):
         count = len(self.thc)
         return count
    
    def reset(self):

        self.thc = ["กMgor gai", "ขHkho khai", "ฃHkho khuat (not used)",

"คLkho khwai","ฅLkho khon (not used)", "ฆLkho rakhang", "งMngo ngu",

"จHjoor jaan","ฉHcho ching","ชMcho chang", "ซLso so", "ฌLso cheer",

"ญLyo ying", "ฎMdo chada","ฏMto patak", "ฐHtho than","ฑLtho montho",

"ฒLtho phuthao","ณLno nen","ดMdo dek","ตMto tao","ถHtho thung",

"ทLtho thahan","ธLtho thong","นLno nu","บMbo baimai","ปMpo pla",

"ผHpho phueng","ฝHfo fa","พLpho phan","ฟLfo fan","ภLpho sam-phao",

"มLmo ma","ยLyo yak","รLro rua","ลLlo ling","วLwo waen","ศHso sala",

"ษHso rusi","สHso suea","หHho hip","ฬLlo chula","อMo ang",

"ฮLho nokhuk"]
    
         
thc = [
    "กMgor gai",
    "ขHkho khai",
    "ฃHkho khuat (not used)",
    "คLkho khwai",
    "ฅLkho khon (not used)",
    "ฆLkho rakhang",
    "งMngo ngu",
    "จHjoor jaan",
    "ฉHcho ching",
    "ชMcho chang",
    "ซLso so",
    "ฌLso cheer",
    "ญLyo ying",
    "ฎMdo chada",
    "ฏMto patak",
    "ฐHtho than",
    "ฑLtho montho",
    "ฒLtho phuthao",
    "ณLno nen",
    "ดMdo dek",
    "ตMto tao",
    "ถHtho thung",
    "ทLtho thahan",
    "ธLtho thong",
    "นLno nu",
    "บMbo baimai",
    "ปMpo pla",
    "ผHpho phueng",
    "ฝHfo fa",
    "พLpho phan",
    "ฟLfo fan",
    "ภLpho sam-phao",
    "มLmo ma",
    "ยLyo yak",
    "รLro rua",
    "ลLlo ling",
    "วLwo waen",
    "ศHso sala",
    "ษHso rusi",
    "สHso suea",
    "หHho hip",
    "ฬLlo chula",
    "อMo ang",
    "ฮLho nokhuk"
]

gen = thaigen()
consonant = gen.get()
print("Random consonant:", consonant)
print("Answer:", gen.get_answer())
gen.dont_ask_this(consonant)
print(gen.howmany())
gen.reset()
print(gen.howmany())