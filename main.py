from pydoc import text
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from view import *

co0 = "#000000" #preto
co1 = "#feffff" #branca
co2 = "#4fa882" #verde
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e06636" #profit
co6 = "#038cfc" #azul
co7 = "#ef5350" #vermelho
co8 = "#008000" # + verde
co9 = "#e9edf5" # skyblue

janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)


frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat') #relief definir efeito 3D
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW) #sticky define a direção, indicando o lado


#Label Cima
app_nome = Label(frame_cima,text='Formulário de Tarefas', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)


#funcao inserir
def inserir():
    
    global tree
    
    titulo = e_titulo.get()
    descricao = e_descricao.get()
    ativo = e_ativo.get()
    dt_alteracao = e_alteracao.get()
    dt_cadastro = e_cadastro.get()
    
    lista = [titulo, descricao, ativo, dt_alteracao, dt_cadastro]
    
    if titulo == '':
        messagebox.showerror('Erro', 'O titulo não pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
        e_titulo.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_ativo.delete(0, 'end')
        e_alteracao.delete(0, 'end')
        e_cadastro.delete(0, 'end')
    for widget in frame_direita.winfo_children():
        widget.destroy()
    mostrar()    


# funcao atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        
        valor_id = tree_lista[0]
        
        e_titulo.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_ativo.delete(0, 'end')
        e_alteracao.delete(0, 'end')
        e_cadastro.delete(0, 'end')
        
        e_titulo.insert(0, tree_lista[1])
        e_descricao.insert(0, tree_lista[2])
        e_ativo.insert(0, tree_lista[3])
        e_alteracao.insert(0, tree_lista[4])
        e_cadastro.insert(0, tree_lista[5])
        
    
        def update():
            titulo = e_titulo.get()
            descricao = e_descricao.get()
            ativo = e_ativo.get()
            dt_alteracao = e_alteracao.get()
            dt_cadastro = e_cadastro.get()
            
            lista = [titulo, descricao, ativo, dt_alteracao, dt_cadastro, valor_id]
            
            if titulo == '':
                messagebox.showerror('Erro', 'O nome não pode ser vazio')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')
                e_titulo.delete(0, 'end')
                e_descricao.delete(0, 'end')
                e_ativo.delete(0, 'end')
                e_alteracao.delete(0, 'end')
                e_cadastro.delete(0, 'end')
            for widget in frame_direita.winfo_children():
                widget.destroy()
                
            mostrar()    
            
        # botao Confirmar
        b_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=110, y=340)    
                
        
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


#funcao deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']
        
        valor_id = [tree_lista[0]]
        
        deletar_info(valor_id)
        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')
        
        for widget in frame_direita.winfo_children():
            widget.destroy()
        
        mostrar()
        
    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

#Configurando Frame baixo

#titulo
l_titulo = Label(frame_baixo,text='Título *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_titulo.place(x=10, y=10)
e_titulo = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_titulo.place(x=15, y=40)

# descricao
l_descricao = Label(frame_baixo,text='Descrição *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_descricao.place(x=10, y=70)
e_descricao = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_descricao.place(x=15, y=100)

# Ativo
l_ativo = Label(frame_baixo,text='Ativo *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_ativo.place(x=10, y=130)
e_ativo = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_ativo.place(x=15, y=160)

# Data do Cadastro
l_cadastro = Label(frame_baixo,text='Data de Cadastro *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cadastro.place(x=15, y=190)
e_cadastro = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
e_cadastro.place(x=15, y=220)

# Data da Alteração
l_alteracao = Label(frame_baixo,text='Data da Alteração *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_alteracao.place(x=160, y=190)
e_alteracao = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2)
e_alteracao.place(x=160, y=220)

# botao inserir
b_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=300)

# botao atualizar
b_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=300)

# botao Deletar
b_deletar= Button(frame_baixo,command=deletar, text='Deletar', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=200, y=300)

#Frame Direita

lista = [[1,'Joao', 'TESTE', 'SIM', "12/19/1990", '12/02/2022']]

def mostrar():
    
    global tree
    
    lista = mostrar_info()

    #lista cabeçario
    tabela_head = ['ID', 'Titulo', 'Descrição', 'Ativo', 'Data de Cadastro', 'Data de Alteração']

    #criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","center","center"] #orientação do texto
    h=[30,170,140,60,150,150] #tamanho dos campos titulos
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1
        
    for item in lista:
        tree.insert('', 'end', values=item)
mostrar()

janela.mainloop()