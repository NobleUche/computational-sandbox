import pytest 

class Token:

    def __init__(self,ttype,tvalue):
        self.ttype=ttype
        self.tvalue=tvalue




class Lexer:
    def __init__(self,linput):
        self.linput=linput
        self.lposition=0
        self.rposition=0

    def Next_Token(self):
        while self.lposition<len(self.linput):
            char=self.linput[self.lposition]
            self.rposition+=1
            if (char.isdigit()):
                if(self.rposition<len(self.linput)):
                    peek_value=self.linput[self.rposition]
                    if(peek_value.isdigit()):
                        chunk=[]
                        chunk=self.linput[self.rposition:self.rposition+2]
                        for i in range(len(chunk)):
                            if(chunk[i].isdigit()):
                                char+=chunk[i] #concatenation
                            else:
                                break;  
                        self.lposition+=1 # incrememnt for lposition 
                        token=Token("integer",char)
                        token_list.append(token)        
                    else:
                        token=Token("integer",char) # Next step: add to token list and increment lposition
                        token_list.append(token)
                        self.lposition+=1
                else:
                    break
            elif(char.isalpha()):
                token=Token("identifier",char)
                token_list.append(token)
                self.lposition+=1
            elif(char=="+") or (char=="-") or (char=="*") or (char=="="):
                token=Token("symbol",char)
                token_list.append(token)
                self.lposition+=1
            else:
                self.lposition+=1 # incrememnt for lposition
            """ create the if statement to determine EOC {End of Characters} """


token_list = []

def func():
    dfile="2x+3y=45"
    lexer=Lexer(dfile)
    lexer.Next_Token()

def test_func():
    func()
    assert len(token_list) == 7
    assert token_list[0].ttype == "integer"
    assert token_list[0].tvalue == "2"
    assert token_list[6].ttype == "integer"
    assert token_list[6].tvalue =="45"