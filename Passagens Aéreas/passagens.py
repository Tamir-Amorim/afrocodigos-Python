class PassagensAereaManager():
    
    passagens_compradas =[]
    
    def adicionar_passagem (self, passagem):
        self.passagens_compradas.append(passagem)
        
        
    
class Passagem():   
    
    def __init__(self, origem, desnito, preço):
        
        self.origem = origem
        self.desnito = desnito
        self.preço = preço
        
    def __repr__(self):
        return f"{self.origem} -> {self.desnito} R${self.preço}"