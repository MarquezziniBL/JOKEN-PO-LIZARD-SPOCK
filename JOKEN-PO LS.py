from tkinter import *
from tkinter import messagebox as mb
import tkinter as tk
import customtkinter as ctk
from PIL import Image
import random

def start():
    
    def rules():
        rule_win = Toplevel()
        rule_win.title("REGRAS")
        rule_win.geometry("497x453")
        rule_win.resizable(False,False)
        rule_win["background"]="#224A6F"
        rule_win.iconbitmap("lagarto.ico")
        image = tk.PhotoImage(file="regras.png")
        
        tk.Label(rule_win, text="\tBem vindo ao Joken-po Lagarto Spock\n\tConfira as regras abaixo:",
                font=("arial",15), background="#224A6F").place(x=-10, y=1)
        
        tk.Label(rule_win, image=image).place(x=1, y=50)
        rule_win.mainloop()
    def victory(choice, comp_choice):
        
        placar_comp = score_comp["text"]
        placar_player= score_player["text"]
#player win        
        if choice == "ROCK" and comp_choice == "TESOURA":
            mb.showinfo("Vencedor","PEDRA ESMAGA TESOURA\n\nVitória: JOGADOR")
            placar_player += 1
        elif choice == "ROCK" and comp_choice == "LAGARTO":
            mb.showinfo("Vencedor","PEDRA ESMAGA LAGARTO\n\nVitória: JOGADOR")
            placar_player += 1
        elif choice == "PAPEL" and comp_choice == "ROCK":
            mb.showinfo("Vencedor","PAPEL EMBRULHA PEDRA\n\nVitória: JOGADOR")
            placar_player += 1
        elif choice == "PAPEL" and comp_choice == "SPOCK":
            mb.showinfo("Vencedor","PAPEL REFUTA SPOCK\n\nVitória: JOGADOR")
            placar_player += 1
        elif choice == "TESOURA" and comp_choice == "PAPEL":
            mb.showinfo("Vencedor","TESOURA CORTA PAPEL\n\nVitória: JOGADOR")
            placar_player += 1
        elif choice == "TESOURA" and comp_choice == "LAGARTO":
            mb.showinfo("Vencedor","TESOURA DECAPITA LAGARTO\n\nVitória: JOGADOR")
            placar_player += 1
        elif choice == "LAGARTO" and comp_choice == "PAPEL":
            mb.showinfo("Vencedor","LAGARTO COME PAPEL\n\nVitória: JOGADOR")
            placar_player += 1
        elif choice == "LAGARTO" and comp_choice == "SPOCK":
            mb.showinfo("Vencedor","LAGARTO ENVENENA SPOCK\n\nVitória: JOGADOR")
            placar_player += 1
        elif choice == "SPOCK" and comp_choice == "TESOURA":
            mb.showinfo("Vencedor","SPOCK ESMAGA TESOURA\n\nVitória: JOGADOR")
            placar_player += 1
        elif choice == "SPOCK" and comp_choice == "ROCK":
            mb.showinfo("Vencedor","SPOCK VAPORIZA PEDRA\n\nVitória: JOGADOR")
            placar_player += 1
#pc win
        elif comp_choice == "ROCK" and choice == "TESOURA":
            mb.showinfo("Vencedor","PEDRA ESMAGA TESOURA\n\nVitória: COMPUTADOR")
            placar_comp += 1
        elif comp_choice == "ROCK" and choice == "LAGARTO":
            mb.showinfo("Vencedor","PEDRA ESMAGA LAGARTO\n\nVitória: COMPUTADOR")
            placar_comp += 1
        elif comp_choice == "PAPEL" and choice == "ROCK":
            mb.showinfo("Vencedor","PAPEL EMBRULHA PEDRA\n\nVitória: COMPUTADOR")
            placar_comp += 1
        elif comp_choice == "PAPEL" and choice == "SPOCK":
            mb.showinfo("Vencedor","PAPEL REFUTA SPOCK\n\nVitória: COMPUTADOR")
            placar_comp += 1
        elif comp_choice == "TESOURA" and choice == "PAPEL":
            mb.showinfo("Vencedor","TESOURA CORTA PAPEL\n\nVitória: COMPUTADOR")
            placar_comp += 1
        elif comp_choice == "TESOURA" and choice == "LAGARTO":
            mb.showinfo("Vencedor","TESOURA DECAPITA LAGARTO\n\nVitória: COMPUTADOR")
            placar_comp += 1
        elif comp_choice == "LAGARTO" and choice == "PAPEL":
            mb.showinfo("Vencedor","LAGARTO COME PAPEL\n\nVitória: COMPUTADOR")
            placar_comp += 1
        elif comp_choice == "LAGARTO" and choice == "SPOCK":
            mb.showinfo("Vencedor","LAGARTO ENVENENA SPOCK\n\nVitória: COMPUTADOR")
            placar_comp += 1
        elif comp_choice == "SPOCK" and choice == "TESOURA":
            mb.showinfo("Vencedor","SPOCK ESMAGA TESOURA\n\nVitória: COMPUTADOR")
            placar_comp += 1
        elif comp_choice == "SPOCK" and choice == "ROCK":
            mb.showinfo("Vencedor","SPOCK VAPORIZA PEDRA\n\nVitória: COMPUTADOR")
            placar_comp += 1
            
        else:
            mb.showinfo("Vencedor","EMPATE")  
            
        score_comp.config(text= placar_comp) 
        score_player.config(text= placar_player)   

    def escolhas():
        escolha = esc.get()
        
        imagem_player = ""
        imagem_comp = ""
        choose = ""
        
        if escolha == 0:
            mb.showwarning("ERRO","Escolha uma opção!")
        elif escolha == 1:
            choose = "ROCK"
            imagem_player = ctk.CTkImage(Image.open("pedra.png"), size=(70,70))
        elif escolha == 2:
            choose = "PAPEL"
            imagem_player = ctk.CTkImage(Image.open("papel.png"), size=(70,70))
        elif escolha == 3:
            choose = "TESOURA"
            imagem_player = ctk.CTkImage(Image.open("tesoura.png"), size=(70,70))
        elif escolha == 4:
            choose = "LAGARTO"
            imagem_player = ctk.CTkImage(Image.open("lizard.png"), size=(70,70))
        elif escolha == 5:
            choose = "SPOCK"
            imagem_player = ctk.CTkImage(Image.open("spock.png"), size=(70,70))
        
        L = ["ROCK", "PAPEL", "TESOURA", "LAGARTO", "SPOCK"]
        comp_choose = random.choice(L)
        
        if comp_choose == "ROCK":
            imagem_comp = ctk.CTkImage(Image.open("pedra.png"), size=(70,70))
        elif comp_choose == "PAPEL":
            imagem_comp = ctk.CTkImage(Image.open("papel.png"), size=(70,70))
        elif comp_choose == "TESOURA":
            imagem_comp = ctk.CTkImage(Image.open("tesoura.png"), size=(70,70))
        elif comp_choose == "LAGARTO":
            imagem_comp = ctk.CTkImage(Image.open("lizard.png"), size=(70,70))
        elif comp_choose == "SPOCK":
            imagem_comp = ctk.CTkImage(Image.open("spock.png"), size=(70,70))
        
        escolha_jogador.configure(image = imagem_player)
        escolha_pc.configure(image = imagem_comp)
        
        return victory(choose, comp_choose)   
    
    
    app = Tk()
    app.title("JOKEN-PO LS")
    app.geometry("300x450")
    app.resizable(False,False)
    app.iconbitmap("lagarto.ico")
    app["background"]="#224A6F"
    esc = IntVar()
    
    play_bt = ctk.CTkImage(Image.open("play_bt.png"), size=(80,50))
    logo = ctk.CTkImage(Image.open("logo2.png"),size=(230,200))
    
    jko = ctk.CTkLabel(app,image=logo, bg_color="#224A6F",text="")
    jko.place(x=40, y=-20)
    
#Info player
    player = tk.Label(app, text= "JOGADOR",font=("arial",11,"bold"), background="#224A6F")
    player.place(x=30,y=160)
    
    score_player = tk.Label(app, background="#224A6F", text= 0,font=("arial",11,"bold"))
    score_player.place(x=60,y=180)
    
    label_escolha_jogador = ctk.CTkFrame(app,bg_color="#224A6F",fg_color="white",width=80, height=80, corner_radius=10)
    label_escolha_jogador.place(x=30, y= 200)
        
    escolha_jogador = ctk.CTkLabel(label_escolha_jogador, bg_color="white", text="")
    escolha_jogador.place(x=5,y=5)

#VERSUS    
    versus = tk.Label(app, text="X",font=("arial",40), background="#224A6F")
    versus.place(x=130, y= 200)

#Info comp    
    comp = tk.Label(app, text= "COMPUTADOR",font=("arial",11,"bold"), background="#224A6F")
    comp.place(x=175,y=160) 
       
    score_comp = tk.Label(app, background="#224A6F", text= 0,font=("arial",11,"bold"))
    score_comp.place(x=225,y=180)

    label_escolha_pc = ctk.CTkFrame(app, bg_color="#224A6F",fg_color="white",width=80, height=80, corner_radius=10)
    label_escolha_pc.place(x=190, y= 200)
    
    escolha_pc = ctk.CTkLabel(label_escolha_pc, bg_color="white",  text="")
    escolha_pc.place(x=5,y=5)
    
#RadioButtons
    rock = tk.Radiobutton(app,text="PEDRA",font=("arial",10,"bold"), background="#224A6F",variable=esc,value=1)
    rock.place(x=75,y=290)
    
    paper = tk.Radiobutton(app,text="PAPEL",font=("arial",10,"bold"), background="#224A6F",variable=esc,value=2)
    paper.place(x=75,y=310)
    
    scissor  = tk.Radiobutton(app,text="TESOURA",font=("arial",10,"bold"), background="#224A6F",variable=esc,value=3)
    scissor.place(x=145,y=290)
    
    lizard  = tk.Radiobutton(app,text="LAGARTO",font=("arial",10,"bold"), background="#224A6F",variable=esc,value=4)
    lizard.place(x=145,y=310)
    
    spock  = tk.Radiobutton(app,text="SPOCK",font=("arial",10,"bold"), background="#224A6F",variable=esc,value=5)
    spock.place(x=120,y=330)
# Action buttons    
    bt_start = ctk.CTkButton(app,image= play_bt,text="",bg_color="#224A6F",fg_color="white",hover_color="#F07E2B",
                             corner_radius=10,command=escolhas)
    bt_start.place(x=75, y=360)

    bt_regras = ctk.CTkButton(app,text="REGRAS",bg_color="#224A6F",font=("arial",10, "bold"), hover_color="#F07E2B",
                              width=10, command=rules)
    bt_regras.place(x=5, y=415)    
    
    app.mainloop()



start()


