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
        EOC=False # how do I check when EOC {End of Characters} ==True 
        while EOC != True:
            char=linput[lposition]
            rposition+=1
            if (char.isdigit()):
                peek_value=linput[rposition] """ Use peek value to check forward 1 step and if the 1 step is a digit grab 
                                                 a chunk of rposition:rposition+2 and loop through to pick the digits and concatenate to char"""
                if(peek_value.isdigit()):
                    chunk=[]
                    chunk=linput[rposition:rposition+2]
                    for i in range(len(chunk)):
                        if(chunk[i].isdigit()):
                            char+=chunk[i] #concatenation
                        else:
                            break;  
                lposition+=1 # incrememnt for lposition 
                token=Token("integer",char)
                token_list.append(token)        
                else:
                  # no more digits to grab
                    token=Token("integer",char) # Next step: add to token list and increment lposition
                    token_list.append(token)
            elif(char.isalpha()):
                token=Token("identifier",char)
                token_list.append(token)
                lposition+=1
            elif(char=="+") or (char=="-") or (char=="*"):
                token=Token("symbol",char)
                token_list.append(token)
                lposition+=1
            """ create the if statement to determine EOC {End of Characters} """
            if (lposition==len(linput)) and (rposition>len(linput)):
                EOC=True


""" write the pytests for the above and also work on the parser and rule logic"""



