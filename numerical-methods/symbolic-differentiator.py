class Token:

    def __init__(self,ttype,tvalue):
        self.ttype=ttype
        self.tvalue=tvalue


Token_list = []


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


""" write the pytests for the above (tests done) and also work on the parser and Evaluator func logic"""

class Parser:
    def __init__(self):
        self.current_label=current_label
        self.left_content=left_content
        self.right_content=right_content

    def consume(self,Token_List):
        while EOL!=True:
            





