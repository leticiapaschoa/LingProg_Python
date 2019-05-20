from tkinter import *
import requests
import json

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
  
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
  
        self.titulo = Label(self.container1, text="Informe os dados do curso :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()
  
        self.lblidCurso = Label(self.container2, text="ID Curso:", font=self.fonte, width=10)
        self.lblidCurso.pack(side=LEFT)
  
        self.txtidCurso = Entry(self.container2)
        self.txtidCurso["width"] = 10
        self.txtidCurso["font"] = self.fonte
        self.txtidCurso.pack(side=LEFT)
  
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarCurso
        self.btnBuscar.pack(side=RIGHT)
  
        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
  
        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT) 
    
    
  
        self.lblDuracao= Label(self.container6, text="Duração:", font=self.fonte, width=10)
        self.lblDuracao.pack(side=LEFT)
  
        self.txtDuracao = Entry(self.container6)
        self.txtDuracao["width"] = 25
        self.txtDuracao["font"] = self.fonte
        self.txtDuracao.pack(side=LEFT)
  
        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirCurso
        self.bntInsert.pack (side=LEFT)
  
        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarCurso
        self.bntAlterar.pack (side=LEFT)
  
        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirCurso
        self.bntExcluir.pack(side=LEFT)
  
        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
  
  
    def inserirCurso(self):
          
        nome = self.txtnome.get()
        duracao = self.txtDuracao.get()

        data = {
                 'ativo': True,                    
                 'duracao': int(duracao), 
                 'nome': nome                    
               }                
        
        headers = {
                    'Content-Type': 'application/json',
                  }

        req = requests.post(url = 'http://localhost:5000/flask/api/cursos', headers = headers, data = json.dumps(data))  
        
        if req.ok:
            self.txtidCurso.delete(0, END)
            self.txtnome.delete(0, END)
            self.txtDuracao.delete(0, END)
        else:
            self.lblmsg["text"] = 'Erro ao consultar API'
  
    def alterarCurso(self):
        nome = self.txtnome.get()
        duracao = self.txtDuracao.get()
        curso = self.txtidCurso.get()

        data = {
                 'ativo': True,                    
                 'duracao': int(duracao), 
                 'nome': nome                    
               }                
        
        headers = {
                    'Content-Type': 'application/json',
                  }

        req = requests.put(url = 'http://localhost:5000/flask/api/cursos/'+ curso, headers = headers, data = json.dumps(data))  
        
        if req.ok:
            self.txtidCurso.delete(0, END)
            self.txtnome.delete(0, END)
            self.txtDuracao.delete(0, END)
        else:
            self.lblmsg["text"] = 'Erro ao consultar API'
  
  
  
    def excluirCurso(self):
        idCurso = self.txtidCurso.get()  
        req = requests.delete('http://localhost:5000/flask/api/cursos/'+idCurso)   
        
        if req.ok:
            self.txtidCurso.delete(0, END)
            self.txtnome.delete(0, END)
            self.txtDuracao.delete(0, END)
        else:
            self.lblmsg["text"] = 'Erro ao consultar a API'
  
    def buscarCurso(self):
        idCurso = self.txtidCurso.get()
        req = requests.get('http://localhost:5000/flask/api/cursos/'+idCurso)   
        
        if req.ok:
            dados = req.json()         

            self.txtnome.delete(0, END)
            self.txtDuracao.delete(0, END)

            self.txtnome.insert(INSERT, dados['curso'][0]['nome'])            
            self.txtDuracao.insert(INSERT, dados['curso'][0]['duracao'])
        else:
              self.lblmsg["text"] = 'Erro ao consultar a API'


root = Tk()
Application(root)
root.mainloop()