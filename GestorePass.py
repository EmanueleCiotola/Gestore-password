from tkinter import *
import urllib.request
from urllib.request import urlopen
from random import *
import os
import csv
import ctypes
from threading import Timer

Connessione= "Online"

TestoFile=[]
DocumentoDecifrato=[]
c= 3
alfabeto= "AbcDeFGHilmNoPQrStuvZaBCdEfghIL"
conta= 3
RicaricaScrollOppureNo= True
ScrollPosizioneUno= 0
ScrollPosizioneDue= 0
errore1= "Negativo"
errore2= "Negativo"
errore3= "Negativo"
FileOrdineAlfabeticoDecriptato= []
ContatoreInformazioni= 0
ContaRimuovi= 0
Label1= ""
Label2= ""
Label3= ""
TimerVisAccountSpecifico= "Timer account specifico rimozione"

TrovaDocumenti1= os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documenti')
Trova= TrovaDocumenti1 + "\\PassGet"
TrovaDocumenti1+= "\\PassGet\\GestorePassword"
TrovaDocumenti= TrovaDocumenti1 + "\\CriptazioneCred.txt"
Icona= TrovaDocumenti1 + "\\IconaGestionePasswordLight.png"
#Icona= TrovaDocumenti1 + "\\IconaGestionePasswordDark.png"
IconaBottoneCerca= TrovaDocumenti1 + "\\BottonePngCerca.png"
IconaBottoneModifica= TrovaDocumenti1 + "\\BottonePngModifica.png"
try:
    FileCredenziali= open(TrovaDocumenti, "a")
    FileCredenziali.close()
except:
    os.makedirs(TrovaDocumenti1)
    FileCredenziali= open(TrovaDocumenti, "a")
    FileCredenziali.close()
    os.chdir(Trova)
    FILE_ATTRIBUTE_HIDDEN= 0x02
    file= ctypes.windll.kernel32.SetFileAttributesW(r'GestorePassword',
                                                    FILE_ATTRIBUTE_HIDDEN)
window = Tk()
window.title("Gestore Password")
window.resizable(False, False)
window.configure(background="#FDFDFD")
try:
    FileCredenziali= open(TrovaDocumenti, "a")
    FileCredenziali.close()
except:
    os.makedirs(TrovaDocumenti1)
    FileCredenziali= open(TrovaDocumenti, "a")
    FileCredenziali.close()

FileCredenziali= open(TrovaDocumenti, "r").readlines()
try:
    FileCredenziali[0] == ""
    window.geometry("313x152")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (313/2))
    y_cordinate = int((screen_height/2) - (152/2))
    window.geometry("{}x{}+{}+{}".format(313, 152, x_cordinate, y_cordinate - 100))
    RoL= "l"
except:
    window.geometry("313x212")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (313/2))
    y_cordinate = int((screen_height/2) - (212/2))
    window.geometry("{}x{}+{}+{}".format(313, 212, x_cordinate, y_cordinate - 100))
    RoL= "r"
try:
    window.iconphoto(False, PhotoImage(file=Icona))
except:
    try:
        with urlopen('https://www.google.it') as up:
            Connessione= "Online"
    except BaseException as ex:
        Connessione= "Offline"
    if Connessione == "Online":
        os.chdir(TrovaDocumenti1)
        urllib.request.urlretrieve("https://i.ibb.co/hyhdy3X/Icona-Gestione-Password-Light.png", "IconaGestionePasswordLight.png")
        #urllib.request.urlretrieve("https://i.ibb.co/CPWRD0g/Icona-Gestione-Password-Piccola.png", "IconaGestionePasswordDark.jpg")
        window.iconphoto(False, PhotoImage(file=Icona))
try:
    ImmagineBottoneCerca= PhotoImage(file= IconaBottoneCerca)
except:
    try:
        with urlopen('https://www.google.it') as up:
            Connessione= "Online"
    except BaseException as ex:
        Connessione= "Offline"
    if Connessione == "Online":
        os.chdir(TrovaDocumenti1)
        urllib.request.urlretrieve("https://i.ibb.co/jzyhkJH/Bottone-Png-Cerca.png", "BottonePngCerca.png")
        ImmagineBottoneCerca= PhotoImage(file=IconaBottoneCerca)
try:
    ImmagineBottoneModifica= PhotoImage(file= IconaBottoneModifica)
except:
    try:
        with urlopen('https://www.google.it') as up:
            Connessione= "Online"
    except BaseException as ex:
        Connessione= "Offline"
    if Connessione == "Online":
        os.chdir(TrovaDocumenti1)
        urllib.request.urlretrieve("https://i.ibb.co/hRrk0bq/Bottone-Modifica-Credenziali-Png.png", "BottonePngModifica.png")
        ImmagineBottoneModifica= PhotoImage(file=IconaBottoneModifica)
        
if Connessione == "Online":
    cl= 0
    alfabeto= "AbcDeFGHilmNoPQrStuvZaBCdEfghIL"
    BottoneConfermaNonPremere= "Premi"
    NonCambiarePass= "Cambia"
    TastoIndietroAvanti1o2= 0
    BottoneAggiungiOppureAggiungiAltroOppureHoCapito= "Aggiungi"

    SchermataLogRegErr= Frame(window, bg="#FDFDFD")
    SchermataPrincipale= Frame(window, bg="#FDFDFD")    

    ###########################
    SchermataVisualizzazioneCredenziali= Frame(SchermataPrincipale, bg="#FDFDFD")
    SchermataVisualizzazioneCredenzialiVuota= Frame(SchermataPrincipale, bg="#FDFDFD")
    ###########################
    SchermataPrincipaleMenù= Frame(SchermataPrincipale, bg="#F3F3F3")
    SchermataPrincipaleElementi= Frame(SchermataPrincipale, bg="#FDFDFD")

    SchermataAggiungiAccount= Frame(SchermataPrincipaleElementi, bg="#FDFDFD")
    SchermataCercaAccount= Frame(SchermataPrincipaleElementi, bg="#FDFDFD")
    SchermataImpostazioni= Frame(SchermataPrincipaleElementi, bg="#FDFDFD")
    SchermataInformazioni= Frame(SchermataPrincipaleElementi, bg="#FDFDFD")
    
    SchermataImporta= Frame(SchermataPrincipaleElementi, bg="#FDFDFD")
    SchermataCambiaPassAccesso= Frame(SchermataPrincipaleElementi, bg="#FDFDFD")
    SchermataVisualizzazioneSpecifica= Frame(SchermataPrincipaleElementi, bg="#FDFDFD")

    ###########################
    SchermataVisualizzazioneCredenziali.grid(row=1, column=0)
    ###########################
    SchermataPrincipaleMenù.grid(row=0, column=0)
    SchermataPrincipaleElementi.grid(row=1, column=0, pady=70, sticky="n")
    
    def ConfermaRegistrazione():
        window.focus()
        global cl
        global alfabeto
        c= 0
        try:
            ScrittaErroreErrata.grid_remove()
        except:
            None
        try:
            ScrittaErroreVuoto.grid_remove()
        except:
            None
        try:
            ScrittaErroreDiverse.grid_remove()
        except:
            None
        VerificaLogReg= "Okay"
        if RoL == "l":
            FileCredenziali= open(TrovaDocumenti, "r").readlines()
            contacl= 1
            FraseDecifrata= ""
            ListaDecriptazione= []
            MessaggioCifrato= FileCredenziali[0]
            chiavecifratura= FileCredenziali[1]
            chiavecifratura= chiavecifratura.replace("]", "")
            NumeroChiave= alfabeto.index(chiavecifratura[1])
            chiavecifratura= chiavecifratura.replace("[" + chiavecifratura[1] + " ", "")
            cl= 0
            for x in range(11):
                chiavecifratura= chiavecifratura.replace(alfabeto[NumeroChiave], str(cl))
                if str(alfabeto[NumeroChiave]) not in chiavecifratura:
                    NumeroChiave+= 1
                    cl+= 1
            cl= 0
            while contacl != len(chiavecifratura):
                if chiavecifratura[contacl] == " ":
                    ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                    cl= contacl
                contacl+= 1
            ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
            cl= 0
            while cl != len(MessaggioCifrato) - 1:
                cp= ListaDecriptazione.index(cl)
                FraseDecifrata+= MessaggioCifrato[cp]
                cl+= 1
            if InserisciPassword.get() != FraseDecifrata and InserisciPassword.get() != "":
                window.geometry("313x173")
                ScrittaErroreErrata.grid(row=3, column=1)#
                InserisciPassword.focus()
                VerificaLogReg= "l"
            elif InserisciPassword.get() == "":
                window.geometry("313x173")
                ScrittaErroreVuoto.grid(row=3, column=1)#
                InserisciPassword.focus()
                VerificaLogReg= "l"
        elif RoL == "r":
            c= 0
            c2= 0
            for x in InserisciPassword.get():
                if x == " ":
                    c+= 1
            for x in InserisciPassword2.get():
                if x == " ":
                    c2+= 1
            if len(InserisciPassword.get()) == c and c > 0 and len(InserisciPassword2.get()) == c2 and c2 > 0:
                window.geometry("313x234")
                ScrittaErroreErrata.grid(row=5, column=1)#
                InserisciPassword.focus()
                VerificaLogReg= "r"
            elif InserisciPassword.get() != InserisciPassword2.get():
                window.geometry("313x234")
                ScrittaErroreDiverse.grid(row=5, column=1)#
                InserisciPassword.focus()
                VerificaLogReg= "r"
            elif InserisciPassword.get() == "" or InserisciPassword2.get() == "":
                window.geometry("313x234")
                ScrittaErroreVuoto.grid(row=5, column=1)#
                InserisciPassword.focus()
                VerificaLogReg= "r"
            else:
                MessaggioCifrato= []
                frase= InserisciPassword.get()
                while len(MessaggioCifrato) != len(frase):
                        numero= randint(0, len(frase)-1)
                        if numero not in MessaggioCifrato:
                            MessaggioCifrato.append(numero)
                chiavecifratura= str(MessaggioCifrato)
                while cl != len(frase):
                    cp= MessaggioCifrato.index(cl)
                    MessaggioCifrato[cp]= frase[cl]
                    cl+= 1
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index(",")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaVirgola*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index(" ")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnBuco*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index("[")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaQuadraA*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index("]")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaQuadraB*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index("'")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnApostrofo*/-+"
                    except:
                        break
                chiavecifratura= chiavecifratura.replace(",", "")
                MessaggioCifrato= str(MessaggioCifrato)
                MessaggioCifrato= MessaggioCifrato.replace("'", "")
                MessaggioCifrato= MessaggioCifrato.replace(",", "")
                MessaggioCifrato= MessaggioCifrato.replace(" ", "")
                MessaggioCifrato= MessaggioCifrato.replace("[", "")
                MessaggioCifrato= MessaggioCifrato.replace("]", "")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaVirgola*/-+", ",")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnBuco*/-+", " ")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaQuadraA*/-+", "[")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaQuadraB*/-+", "]")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnApostrofo*/-+", "'")

                chiavecifratura= chiavecifratura.replace("[", "")
                chiavecifratura= chiavecifratura.replace("]", "")
                cl= 0
                NumeroChiaveIniziale= randint(0,20)
                NumeroChiave= NumeroChiaveIniziale
                for x in range(11):
                    chiavecifratura= chiavecifratura.replace(str(cl), alfabeto[NumeroChiave])
                    if str(cl) not in chiavecifratura:
                        NumeroChiave+= 1
                        cl+= 1
                chiavecifratura= "[" + alfabeto[NumeroChiaveIniziale] + " " + chiavecifratura + "]"
                FileCredenziali= open(TrovaDocumenti, "a")
                FileCredenziali.write(MessaggioCifrato + "\n" + chiavecifratura + "\n\n")
                FileCredenziali.close()       
        if VerificaLogReg == "Okay":
            window.geometry("898x500")#Inizio
            global BottoneConfermaNonPremere
            BottoneConfermaNonPremere= "NonPremere"
            SchermataLogRegErr.grid_remove()
            SchermataPrincipale.grid(row=0, column=0)
            global screen_width
            global screen_height
            x_cordinate = int((screen_width/2) - (898/2))
            y_cordinate = int((screen_height/2) - (500/2))
            window.geometry("{}x{}+{}+{}".format(898, 500, x_cordinate, y_cordinate))
    ###########################
    def VisualizzaTutteLeCredenziali():
        lista= frame.grid_slaves()
        for elemento in lista:
           elemento.destroy()
        TestoFile=[]
        DocumentoDecifrato=[]
        c= 3
        alfabeto= "AbcDeFGHilmNoPQrStuvZaBCdEfghIL"
        conta= 3
        file= open(TrovaDocumenti, 'r').readlines()
        file1= open("CriptazioneCred_Preparazione.txt","a")
        while conta < len(file) - 2:
            menospazio= file[c]
            menospazio= menospazio[0:-1]
            menospaziochiave= file[c + 1]
            menospaziochiave= menospaziochiave[0:-1]
            cl= 0
            contacl= 1
            FraseDecifrata= ""
            ListaDecriptazione= []
            MessaggioCifrato= menospazio
            chiavecifratura= menospaziochiave
            chiavecifratura= chiavecifratura.replace("]", "")
            NumeroChiave= alfabeto.index(chiavecifratura[1])
            chiavecifratura= chiavecifratura.replace("[" + chiavecifratura[1] + " ", "")
            cl= 0
            for x in range(11):
                chiavecifratura= chiavecifratura.replace(alfabeto[NumeroChiave], str(cl))
                if str(alfabeto[NumeroChiave]) not in chiavecifratura:
                    NumeroChiave+= 1
                    cl+= 1
            cl= 0
            while contacl != len(chiavecifratura):
                if chiavecifratura[contacl] == " ":
                    ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                    cl= contacl
                contacl+= 1
            ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
            cl= 0
            while cl != len(MessaggioCifrato):
                cp= ListaDecriptazione.index(cl)
                FraseDecifrata+= MessaggioCifrato[cp]
                cl+= 1
                
            file1.write(FraseDecifrata + "\n")
            c+= 7
            conta+= 7
        file1.close()

        with open('CriptazioneCred_Preparazione.txt', 'r') as r:
            for line in sorted(r):
                TestoFile.append(line[0:-1])

        os.unlink("CriptazioneCred_Preparazione.txt")

        c= 3
        c1= 0
        while c < (len(file) - 1):
            c1= 0
            while c1 < 3:
                menospazio= file[c]
                menospazio= menospazio[0:-1]
                menospaziochiave= file[c + 1]
                menospaziochiave= menospaziochiave[0:-1]
                cl= 0
                contacl= 1
                FraseDecifrata= ""
                ListaDecriptazione= []
                MessaggioCifrato= menospazio
                chiavecifratura= menospaziochiave
                chiavecifratura= chiavecifratura.replace("]", "")
                NumeroChiave= alfabeto.index(chiavecifratura[1])
                chiavecifratura= chiavecifratura.replace("[" + chiavecifratura[1] + " ", "")
                cl= 0
                for x in range(11):
                    chiavecifratura= chiavecifratura.replace(alfabeto[NumeroChiave], str(cl))
                    if str(alfabeto[NumeroChiave]) not in chiavecifratura:
                        NumeroChiave+= 1
                        cl+= 1
                cl= 0
                while contacl != len(chiavecifratura):
                    if chiavecifratura[contacl] == " ":
                        ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                        cl= contacl
                    contacl+= 1
                ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                cl= 0
                while cl != len(MessaggioCifrato):
                    cp= ListaDecriptazione.index(cl)
                    FraseDecifrata+= MessaggioCifrato[cp]
                    cl+= 1
                    
                DocumentoDecifrato.append(FraseDecifrata)
                c+= 2
                c1+= 1
            c+= 1

        FileOrdineAlfabeticoDecriptato= []
        c= 0
        while c < len(TestoFile):
            Posizione= DocumentoDecifrato.index(TestoFile[c])
            Testo= ""
            Testo+= DocumentoDecifrato[Posizione] + "\n" + DocumentoDecifrato[Posizione+1] + "\n" + DocumentoDecifrato[Posizione+ 2] + "\n"
            FileOrdineAlfabeticoDecriptato.append(DocumentoDecifrato[Posizione] + "\n")
            FileOrdineAlfabeticoDecriptato.append(DocumentoDecifrato[Posizione+1] + "\n")
            FileOrdineAlfabeticoDecriptato.append(DocumentoDecifrato[Posizione+ 2] + "\n")
            c+= 1
        ###########################
        ContatoreFunzioneBottoni= 0
        list_languages= []
        while ContatoreFunzioneBottoni < len(FileOrdineAlfabeticoDecriptato):
                if ContatoreFunzioneBottoni % 3 == 0:
                        list_languages.append(FileOrdineAlfabeticoDecriptato[ContatoreFunzioneBottoni])
                ContatoreFunzioneBottoni+= 1
        ###########################
        if FileOrdineAlfabeticoDecriptato != []:
            var= 1
            for language in list_languages:
                btn= Button(frame,
                            text="Modifica",
                            activebackground="#FDFDFD",
                            fg="#616161",
                            bg="#FDFDFD",
                            relief="flat",
                            bd=0,
                            width=10,
                            height=2,
                            takefocus= False,
                            command=lambda lan=language:show_lan(lan))
                btn.grid(row=var,column=3)
                var+= 1
            x= 0
            y= 1
            CoC= 0
            while x < len(FileOrdineAlfabeticoDecriptato):
                if CoC == 0:
                    CambiaTesto= FileOrdineAlfabeticoDecriptato[x][0:-1]
                    EntryVisScroll= Entry(frame,
                                          relief="groove",
                                          bd=0,
                                          justify=CENTER, #Non so se mi piace
                                          disabledforeground="black",
                                          disabledbackground="#FDFDFD",
                                          width=26,
                                          bg="#F3F3F3",
                                          font="helvetica 13")
                    EntryVisScroll.grid(row=y, column=0, pady=3)
                    EntryVisScroll.insert(0, CambiaTesto)
                    EntryVisScroll.config(state=DISABLED)
                elif CoC == 1:
                    CambiaTesto1= FileOrdineAlfabeticoDecriptato[x][0:-1]
                    if CambiaTesto1 == "None":
                        CambiaTesto1= "Nessuna mail inserita."
                    EntryVisScroll= Entry(frame,
                                        relief="groove",
                                        bd=0,
                                        justify=CENTER, #Non so se mi piace
                                        disabledforeground="black",
                                        disabledbackground="#FDFDFD",
                                        width=26,
                                        bg="#F3F3F3",
                                        font="helvetica 13")
                    EntryVisScroll.grid(row=y, column=1, pady=3)
                    EntryVisScroll.insert(0, CambiaTesto1)
                    EntryVisScroll.config(state=DISABLED)
                else:
                    CoC= -1
                    CambiaTesto2= FileOrdineAlfabeticoDecriptato[x][0:-1]
                    EntryVisScroll= Entry(frame,
                                        relief="groove",
                                        bd=0,
                                        justify=CENTER, #Non so se mi piace
                                        disabledforeground="black",
                                        disabledbackground="#FDFDFD",
                                        width=26,
                                        bg="#F3F3F3",
                                        font="helvetica 13")
                    EntryVisScroll.grid(row=y, column=2, pady=48)
                    EntryVisScroll.insert(0, CambiaTesto2)
                    EntryVisScroll.config(state=DISABLED)
                    y+= 1
                    LabelSpazioVis= Label(frame, bg="#FDFDFD", text="")
                    LabelSpazioVis.grid(row=y, column=0, columnspan=2)
                    if x == len(FileOrdineAlfabeticoDecriptato) - 1:
                        LabelSpazioVis.grid_remove()
                CoC+= 1
                x+= 1
                
            v= 1
            l= 0
            while l < len(FileOrdineAlfabeticoDecriptato):
                CanvSotto= Canvas(frame,
                                bg="#F3F3F3",
                                bd=0,
                                height=3,
                                width=878,
                                highlightbackground="#FDFDFD")
                CanvSopra= Canvas(frame,
                                bg="#F3F3F3",
                                bd=0,
                                height=3,
                                width=878,
                                highlightbackground="#FDFDFD")
                CanvSotto.grid(row=v, column=0, columnspan=4, sticky="s", pady=0)
                CanvSopra.grid(row=v+1, column=0, columnspan=4, sticky="n", pady=0)
                l+= 3
                v+= 1  
        else:
            ScrittaNessunAccountInseritoVis= Label(frame,
                                                   text="Nessun account inserito.",
                                                   font="helvetica 14",
                                                   bg="#FDFDFD",
                                                   fg="#616161")
            ScrittaNessunAccountInseritoVis.grid(padx=343, pady=190, sticky="n")
            global RicaricaScrollOppureNo
            if RicaricaScrollOppureNo == False:
                canvas.yview_scroll(-1000, "units")
                RicaricaScrollOppureNo= True
            try:
                BottoneEsportaPassword.config(state=DISABLED)
                BottoneEliminaTutto.config(state=DISABLED)
            except:
                None
    ###########################
    def AggiungiNuovoAccountMenù():
        listadisabled= frame.grid_slaves()
        for elemento in listadisabled:
           elemento.config(state=DISABLED)
        for elementocolorecarattere in listadisabled:
           try:
                elementocolorecarattere.config(disabledforeground="SystemDisabledText")
           except:
                None
        global ScrollPosizioneUno
        global ScrollPosizioneDue
        ScrollPosizioneUno= myscrollbar.get()[0]
        ScrollPosizioneDue= myscrollbar.get()[1]
        myscrollbar.set(0, 1)
        myscrollbar.config(command=False)
        SchermataPrincipaleElementi.grid(row=1, column=0, pady=70, sticky="n")
        SchermataAggiungiAccount.grid(row=0, column=0)
        InserisciNome.focus()
        BottoneGest.config(state=DISABLED)
        AggiungiBottone.config(state=DISABLED)
        CercaBottone.config(state=DISABLED)
        ImpostazioniBottone.config(state=DISABLED)
        InfoBottone.config(state=DISABLED)
    def BottoneHomeAggiungi():
        window.focus()
        global ScrollPosizioneUno
        global ScrollPosizioneDue
        myscrollbar.set(ScrollPosizioneUno, ScrollPosizioneDue)
        myscrollbar.config(command=canvas.yview)
        SchermataPrincipaleElementi.grid_remove()
        global BottoneAggiungiOppureAggiungiAltroOppureHoCapito
        BottoneAggiungiOppureAggiungiAltroOppureHoCapito= "Aggiungi"
        try:
            BottoneRiscriviCredenziali.grid_remove()
            BottoneConfermaCredenziali.grid(padx=5, pady=10)
        except:
            None
        try:
            BottoneAltreCredenziali.grid_remove()
            ScrittaAccountNuovoAggiuntoConferma.grid_remove()
            BottoneConfermaCredenziali.grid(padx=5, pady=10)
        except:
            None
        InserisciNome.config(state=NORMAL)
        InserisciMail.config(state=NORMAL)
        InserisciPass.config(state=NORMAL)
        InserisciNome.delete (0, END)
        InserisciMail.delete (0, END)
        InserisciPass.delete (0, END)

        SchermataAggiungiAccount.grid_remove()
        BottoneGest.config(state=NORMAL)
        AggiungiBottone.config(state=NORMAL)
        CercaBottone.config(state=NORMAL)
        ImpostazioniBottone.config(state=NORMAL)
        InfoBottone.config(state=NORMAL)    
        VisualizzaTutteLeCredenziali()
    def ConfermaNuovoAccount():
        global errore1
        global errore2
        global errore3
        errore1= "Negativo"
        errore2= "Negativo"
        errore3= "Negativo"
        nomenonvalido= "Nome non valido!"
        nomenoninserito= "Devi inserire un nome!"
        nomeusato= "Nome servizio già in uso!"
        mailnonvalida= "Mail non valida!"
        passnonvalida= "Password non valida!"
        passnoninserita= "Inserisci una password!"
        c= 0
        for x in InserisciNome.get():
            if x == " ":
                c+= 1    
        if len(InserisciNome.get()) == c and c > 0:
            caso1= 1
            errore1= "Positivo"
        if InserisciNome.get() == "":
            caso1= 2
            errore1= "Positivo"

        global TrovaDocumenti
        global TrovaDocumenti1
        global FileOrdineAlfabeticoDecriptato
        FileCredenziali= open(TrovaDocumenti, "r").readlines()
        c= 3
        while c < len(FileCredenziali):
            menospazio= FileCredenziali[c]
            menospazio= menospazio[0:-1]
            menospaziochiave= FileCredenziali[c + 1]
            menospaziochiave= menospaziochiave[0:-1]
            global cl
            cl= 0
            global alfabeto
            contacl= 1
            FraseDecifrata= ""
            ListaDecriptazione= []
            MessaggioCifrato= menospazio
            chiavecifratura= menospaziochiave
            chiavecifratura= chiavecifratura.replace("]", "")
            NumeroChiave= alfabeto.index(chiavecifratura[1])
            chiavecifratura= chiavecifratura.replace("[" + chiavecifratura[1] + " ", "")
            cl= 0
            for x in range(11):
                chiavecifratura= chiavecifratura.replace(alfabeto[NumeroChiave], str(cl))
                if str(alfabeto[NumeroChiave]) not in chiavecifratura:
                    NumeroChiave+= 1
                    cl+= 1
            cl= 0
            while contacl != len(chiavecifratura):
                if chiavecifratura[contacl] == " ":
                    ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                    cl= contacl
                contacl+= 1
            ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
            cl= 0
            while cl != len(MessaggioCifrato):
                cp= ListaDecriptazione.index(cl)
                FraseDecifrata+= MessaggioCifrato[cp]
                cl+= 1
            if InserisciNome.get() == FraseDecifrata:
                caso1= 3
                errore1= "Positivo"
            c+= 7
            
        if InserisciMail.get() != "":
            try:
                InserisciMail.get().index("@")
                try:
                    InserisciMail.get().index(".com")
                except:
                    InserisciMail.get().index(".it")
            except:
                errore2= "Positivo"
        c= 0
        for x in InserisciPass.get():
            if x == " ":
                c+= 1     
        if len(InserisciPass.get()) == c and c > 0:
            caso3= 1
            errore3= "Positivo"
        if InserisciPass.get() == "":
            caso3= 2
            errore3= "Positivo"
            
        if errore1 == "Positivo":
            if caso1 == 1:
                testoerrore1= nomenonvalido
            if caso1 == 2:
                testoerrore1= nomenoninserito
            if caso1 == 3:
                testoerrore1= nomeusato
            InserisciNome.delete (0, END)
            InserisciNome.insert (0, testoerrore1)
        if errore2 == "Positivo":
            InserisciMail.delete (0, END)
            InserisciMail.insert (0, mailnonvalida)
        if errore3 == "Positivo":
            if caso3 == 1:
                testoerrore3= passnonvalida
            if caso3 == 2:
                testoerrore3= passnoninserita    
            InserisciPass.delete (0, END)
            InserisciPass.insert (0, testoerrore3)

        if errore1 == "Positivo" or errore2 == "Positivo" or errore3 == "Positivo":
            global BottoneAggiungiOppureAggiungiAltroOppureHoCapito
            BottoneAggiungiOppureAggiungiAltroOppureHoCapito= "HoCapito"
            BottoneConfermaCredenziali.grid_remove()
            ScrittaIntroduzioneNuovo.focus()
            BottoneRiscriviCredenziali.grid(row=7, column=0, pady=10, padx=5)
            InserisciNome.config(state=DISABLED)
            InserisciMail.config(state=DISABLED)
            InserisciPass.config(state=DISABLED)
        else:
            BottoneAggiungiOppureAggiungiAltroOppureHoCapito= "AggiungiAltro"
            FileCredenziali= open(TrovaDocumenti, "a")
            contatoretraduzione= 1
            while contatoretraduzione <= 3:
                cl= 0
                MessaggioCifrato= []
                if contatoretraduzione == 1:
                    frase= InserisciNome.get()
                if contatoretraduzione == 2:
                    if InserisciMail.get() == "":
                        frase= "None"
                    else:
                        frase= InserisciMail.get()
                if contatoretraduzione == 3:
                    frase= InserisciPass.get()
                while len(MessaggioCifrato) != len(frase):
                    numero= randint(0, len(frase)-1)
                    if numero not in MessaggioCifrato:
                        MessaggioCifrato.append(numero)
                chiavecifratura= str(MessaggioCifrato)
                while cl != len(frase):
                    cp= MessaggioCifrato.index(cl)
                    MessaggioCifrato[cp]= frase[cl]
                    cl+= 1
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index(",")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaVirgola*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index(" ")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnBuco*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index("[")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaQuadraA*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index("]")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaQuadraB*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index("'")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnApostrofo*/-+"
                    except:
                        break
                chiavecifratura= chiavecifratura.replace(",", "")
                MessaggioCifrato= str(MessaggioCifrato)
                MessaggioCifrato= MessaggioCifrato.replace("'", "")
                MessaggioCifrato= MessaggioCifrato.replace(",", "")
                MessaggioCifrato= MessaggioCifrato.replace(" ", "")
                MessaggioCifrato= MessaggioCifrato.replace("[", "")
                MessaggioCifrato= MessaggioCifrato.replace("]", "")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaVirgola*/-+", ",")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnBuco*/-+", " ")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaQuadraA*/-+", "[")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaQuadraB*/-+", "]")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnApostrofo*/-+", "'")

                chiavecifratura= chiavecifratura.replace("[", "")
                chiavecifratura= chiavecifratura.replace("]", "")
                cl= 0
                NumeroChiaveIniziale= randint(0,20)
                NumeroChiave= NumeroChiaveIniziale
                for x in range(11):
                    chiavecifratura= chiavecifratura.replace(str(cl), alfabeto[NumeroChiave])
                    if str(cl) not in chiavecifratura:
                        NumeroChiave+= 1
                        cl+= 1
                chiavecifratura= "[" + alfabeto[NumeroChiaveIniziale] + " " + chiavecifratura + "]"
                FileCredenziali.write(MessaggioCifrato + "\n" + chiavecifratura + "\n")
                contatoretraduzione+= 1
            FileCredenziali.write("\n")
            FileCredenziali.close()
            BottoneConfermaCredenziali.grid_remove()
            InserisciNome.config(state=DISABLED)
            InserisciMail.config(state=DISABLED)
            InserisciPass.config(state=DISABLED)
            BottoneEsportaPassword.config(state=NORMAL)
            ScrittaIntroduzioneNuovo.focus()
            ScrittaAccountNuovoAggiuntoConferma.grid(row=7, column=0, pady=0, padx=5)
            BottoneAltreCredenziali.grid(padx=5, pady=10)
            BottoneEsportaPassword.config(state=NORMAL)
            BottoneEliminaTutto.config(state=NORMAL)
    def NuoveCredenziali():
        InserisciNome.focus()
        global BottoneAggiungiOppureAggiungiAltroOppureHoCapito
        BottoneAggiungiOppureAggiungiAltroOppureHoCapito= "Aggiungi"
        ScrittaAccountNuovoAggiuntoConferma.grid_remove()
        BottoneAltreCredenziali.grid_remove()
        InserisciNome.config(state=NORMAL)
        InserisciMail.config(state=NORMAL)
        InserisciPass.config(state=NORMAL)
        InserisciNome.delete (0, END)
        InserisciMail.delete (0, END)
        InserisciPass.delete (0, END)
        BottoneConfermaCredenziali.grid(padx=5, pady=10)
    def ConfermaRiscriviNuovoAccount():
        global BottoneAggiungiOppureAggiungiAltroOppureHoCapito
        BottoneAggiungiOppureAggiungiAltroOppureHoCapito= "Aggiungi"
        global errore1
        global errore2
        global errore3
        BottoneRiscriviCredenziali.grid_remove()
        BottoneConfermaCredenziali.grid(pady=10, padx=5)
        InserisciNome.config(state=NORMAL)
        InserisciMail.config(state=NORMAL)
        InserisciPass.config(state=NORMAL)
        if errore3 == "Positivo":
            InserisciPass.delete (0, END)
            InserisciPass.focus()
        if errore2 == "Positivo":
            InserisciMail.delete (0, END)
            InserisciMail.focus()
        if errore1 == "Positivo":
            InserisciNome.delete (0, END)
            InserisciNome.focus()
    def RicaricaAccountVisComando():
        FrameAttualeRimozione= str(SchermataPrincipaleElementi.grid_slaves())
        if FrameAttualeRimozione == "[<tkinter.Frame object .!frame2.!frame4.!frame2>]":
            SchermataPrincipaleElementi.grid_remove()
            CercaAccEntry.delete(0, END)
            SchermataCercaAccount.grid_remove()
            SchermataPrincipale.focus()
            AggiungiBottone.config(state=NORMAL)
            CercaBottone.config(state=NORMAL)
            ImpostazioniBottone.config(state=NORMAL)
            InfoBottone.config(state=NORMAL)
        elif FrameAttualeRimozione == "[<tkinter.Frame object .!frame2.!frame4.!frame4>]":
            global ScrollPosizioneUno
            global ScrollPosizioneDue
            myscrollbar.set(ScrollPosizioneUno, ScrollPosizioneDue)
            myscrollbar.config(command=canvas.yview)
            SchermataPrincipaleElementi.grid_remove()
            SchermataInformazioni.grid_remove()
            SchermataPrincipale.focus()
            AggiungiBottone.config(state=NORMAL)
            CercaBottone.config(state=NORMAL)
            ImpostazioniBottone.config(state=NORMAL)
            InfoBottone.config(state=NORMAL)
            VisualizzaTutteLeCredenziali()
        else:
            VisualizzaTutteLeCredenziali()
    def ImpostazioniSchermataGenerale():
        listadisabled= frame.grid_slaves()
        for elemento in listadisabled:
           elemento.config(state=DISABLED)
        for elementocolorecarattere in listadisabled:
           try:
                elementocolorecarattere.config(disabledforeground="SystemDisabledText")
           except:
                None
        global ScrollPosizioneUno
        global ScrollPosizioneDue
        ScrollPosizioneUno= myscrollbar.get()[0]
        ScrollPosizioneDue= myscrollbar.get()[1]
        myscrollbar.set(0, 1)
        myscrollbar.config(command=False)
        SchermataPrincipaleElementi.grid(row=1, column=0, pady=70, sticky="n")
        SchermataImpostazioni.grid()
        ScrittaImposta.focus()
        BottoneGest.config(state=DISABLED)
        AggiungiBottone.config(state=DISABLED)
        CercaBottone.config(state=DISABLED)
        ImpostazioniBottone.config(state=DISABLED)
        InfoBottone.config(state=DISABLED)
    def HomeDaImposta():
        window.focus()
        global ScrollPosizioneUno
        global ScrollPosizioneDue
        myscrollbar.set(ScrollPosizioneUno, ScrollPosizioneDue)
        myscrollbar.config(command=canvas.yview)
        SchermataPrincipaleElementi.grid_remove()
        SchermataImpostazioni.grid_remove()
        SchermataPrincipale.focus()
        FileCredenziali= open(TrovaDocumenti, "r").readlines()
        BottoneGest.config(state=NORMAL)
        AggiungiBottone.config(state=NORMAL)
        CercaBottone.config(state=NORMAL)
        ImpostazioniBottone.config(state=NORMAL)
        InfoBottone.config(state=NORMAL)
        VisualizzaTutteLeCredenziali()
    def EsportaComando():
        BottoneEsportaPassword.config(state=DISABLED)
        Focus= window.focus_get()
        if BottoneEsportaPassword == Focus:
            BottoneImportaPassword.focus()
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        desktop+= "\Password Gestore.csv"
        with open(desktop, 'w', newline= '', encoding="ISO-8859-1") as csv_file:
            csv_writer= csv.writer(csv_file, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['name', 'url', 'username', 'password'])
            FileCredenziali= open(TrovaDocumenti, "r").readlines()
            y= len(FileCredenziali) - 5
            c= 3
            while y > 0:
                contatore= 0
                while contatore < 3:
                    contatore+= 1
                    menospazio= FileCredenziali[c]
                    menospazio= menospazio[0:-1]
                    menospaziochiave= FileCredenziali[c + 1]
                    menospaziochiave= menospaziochiave[0:-1]
                    cl= 0
                    alfabeto= "AbcDeFGHilmNoPQrStuvZaBCdEfghIL"
                    contacl= 1
                    FraseDecifrata= ""
                    ListaDecriptazione= []
                    MessaggioCifrato= menospazio
                    chiavecifratura= menospaziochiave
                    chiavecifratura= chiavecifratura.replace("]", "")
                    NumeroChiave= alfabeto.index(chiavecifratura[1])
                    chiavecifratura= chiavecifratura.replace("[" + chiavecifratura[1] + " ", "")
                    cl= 0
                    for x in range(11):
                        chiavecifratura= chiavecifratura.replace(alfabeto[NumeroChiave], str(cl))
                        if str(alfabeto[NumeroChiave]) not in chiavecifratura:
                            NumeroChiave+= 1
                            cl+= 1
                    cl= 0
                    while contacl != len(chiavecifratura):
                        if chiavecifratura[contacl] == " ":
                            ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                            cl= contacl
                        contacl+= 1
                    ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                    cl= 0
                    while cl != len(MessaggioCifrato):
                        cp= ListaDecriptazione.index(cl)
                        FraseDecifrata+= MessaggioCifrato[cp]
                        cl+= 1
                    if contatore == 1:
                        NomeServizio= FraseDecifrata
                    elif contatore == 2:
                        if FraseDecifrata != "None":
                            Mail= FraseDecifrata
                        else:
                            Mail= ""
                    else:
                        Password= FraseDecifrata
                    c+= 2
                csv_writer.writerow([NomeServizio,"", Mail, Password])
                y-= 7
                c+= 1
    def ImportaComando():
        CercaAccountDaListaImporta.config(state=NORMAL)
        CercaAccountDaListaImporta.delete (0, END)
        CercaAccountDaListaImporta.focus()
        SchermataImpostazioni.grid_remove()
        SchermataImporta.grid()
    def MenuImportaComando():
        window.focus()
        global TastoIndietroAvanti1o2
        TastoIndietroAvanti1o2= 0
        try:
            CredenzialiImportate.grid_remove()
        except:
            None
        try:
            CredenzialiErroreImportazioneFileNonValido.grid_remove()
        except:
            None
        try:
            CredenzialiErroreImportazione.grid_remove()
        except:
            None
        try:
            BottoneImportaNuoveCredenziali.grid_remove()
            BottoneImportaCred.grid()
        except:
            None
        SchermataImporta.grid_remove()
        SchermataImpostazioni.grid()
        FileCredenziali= open(TrovaDocumenti, "r").readlines()
    def ImportaAltreCredenzialiComando():
        global TastoIndietroAvanti1o2
        TastoIndietroAvanti1o2+= 1
        try:
            CredenzialiImportate.grid_remove()
        except:
            None
        try:
            CredenzialiErroreImportazioneFileNonValido.grid_remove()
        except:
            None
        try:
            CredenzialiErroreImportazione.grid_remove()
        except:
            None
        BottoneImportaNuoveCredenziali.grid_remove()
        BottoneImportaCred.grid()
        CercaAccountDaListaImporta.config(state=NORMAL)
        CercaAccountDaListaImporta.delete (0, END)
        CercaAccountDaListaImporta.focus()
    def ImportaCredenzialiComando():
        global TastoIndietroAvanti1o2
        TastoIndietroAvanti1o2+= 1
        ScrittaImportaIntroduzione.focus()
        try:
            BottoneImportaCred.grid_remove()
            BottoneImportaNuoveCredenziali.grid(row=4, column=0, padx=20, pady=10)
            CercaAccountDaListaImporta.config(state=DISABLED)
            Desktop= os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            FileCsvPerImportazione= Desktop + "\\" + CercaAccountDaListaImporta.get() + ".csv"
            cl= 0
            global alfabeto
            with open(FileCsvPerImportazione, newline="") as filecsv:
                Lettore= csv.reader(filecsv, delimiter=",", quotechar="\'")
                try:
                    Dati= [(Linea[0], Linea[2], Linea[3]) for Linea in Lettore]
                    z= 1
                    while z < len(Dati):
                        NumeroNomeUguale= 1
                        Error= "Assente"
                        Tupla= Dati[z]
                        Nome= Tupla[0]
                        Mail= Tupla[1]
                        Password= Tupla[2]
                        c= 0
                        for x in Nome:
                            if x == " ":
                                c+= 1    
                        if len(Nome) == c and c > 0:
                            Error= "Presente"
                        if Nome == "":
                            Error= "Presente"
                        FileCredenziali= open(TrovaDocumenti, "r").readlines()
                        c= 3
                        while c < len(FileCredenziali):
                            menospazio= FileCredenziali[c]
                            menospazio= menospazio[0:-1]
                            menospaziochiave= FileCredenziali[c + 1]
                            menospaziochiave= menospaziochiave[0:-1]
                            cl= 0
                            contacl= 1
                            FraseDecifrata= ""
                            ListaDecriptazione= []
                            MessaggioCifrato= menospazio
                            chiavecifratura= menospaziochiave
                            chiavecifratura= chiavecifratura.replace("]", "")
                            NumeroChiave= alfabeto.index(chiavecifratura[1])
                            chiavecifratura= chiavecifratura.replace("[" + chiavecifratura[1] + " ", "")
                            cl= 0
                            for x in range(11):
                                chiavecifratura= chiavecifratura.replace(alfabeto[NumeroChiave], str(cl))
                                if str(alfabeto[NumeroChiave]) not in chiavecifratura:
                                    NumeroChiave+= 1
                                    cl+= 1
                            cl= 0
                            while contacl != len(chiavecifratura):
                                if chiavecifratura[contacl] == " ":
                                    ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                                    cl= contacl
                                contacl+= 1
                            ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                            cl= 0
                            while cl != len(MessaggioCifrato):
                                cp= ListaDecriptazione.index(cl)
                                FraseDecifrata+= MessaggioCifrato[cp]
                                cl+= 1
                            if Nome == FraseDecifrata:
                                Error= "Presente" #Qui taglia tutti quelli uguali. Potrei cambiarne il nome in nome (numero volte in cui è già uscito)
                            c+= 7
                            
                        if Mail != "":
                            try:
                                Mail.index("@")
                                try:
                                    Mail.index(".com")
                                except:
                                    Mail.index(".it")
                            except:
                                Mail= ""

                        c= 0
                        for x in Password:
                            if x == " ":
                                c+= 1     
                        if len(Password) == c and c > 0:
                            Error= "Presente"
                        if Password == "":
                            Error= "Presente"
                            
                        if Error == "Assente":
                            ControlZ= 0
                            while ControlZ < 3:
                                ControlZ+= 1
                                FileCredenziali= open(TrovaDocumenti, "a")
                                cl= 0
                                MessaggioCifrato= []
                                if ControlZ == 1:
                                    frase= Nome
                                if ControlZ == 2:
                                    if Mail == "":
                                        frase= "None"
                                    else:
                                        frase= Mail
                                if ControlZ == 3:
                                    frase= Password
                                while len(MessaggioCifrato) != len(frase):
                                    numero= randint(0, len(frase)-1)
                                    if numero not in MessaggioCifrato:
                                        MessaggioCifrato.append(numero)
                                chiavecifratura= str(MessaggioCifrato)
                                while cl != len(frase):
                                    cp= MessaggioCifrato.index(cl)
                                    MessaggioCifrato[cp]= frase[cl]
                                    cl+= 1
                                while 0 == 0:
                                    try:
                                        cp= MessaggioCifrato.index(",")
                                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaVirgola*/-+"
                                    except:
                                        break
                                while 0 == 0:
                                    try:
                                        cp= MessaggioCifrato.index(" ")
                                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnBuco*/-+"
                                    except:
                                        break
                                while 0 == 0:
                                    try:
                                        cp= MessaggioCifrato.index("[")
                                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaQuadraA*/-+"
                                    except:
                                        break
                                while 0 == 0:
                                    try:
                                        cp= MessaggioCifrato.index("]")
                                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaQuadraB*/-+"
                                    except:
                                        break
                                while 0 == 0:
                                    try:
                                        cp= MessaggioCifrato.index("'")
                                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnApostrofo*/-+"
                                    except:
                                        break
                                chiavecifratura= chiavecifratura.replace(",", "")
                                MessaggioCifrato= str(MessaggioCifrato)
                                MessaggioCifrato= MessaggioCifrato.replace("'", "")
                                MessaggioCifrato= MessaggioCifrato.replace(",", "")
                                MessaggioCifrato= MessaggioCifrato.replace(" ", "")
                                MessaggioCifrato= MessaggioCifrato.replace("[", "")
                                MessaggioCifrato= MessaggioCifrato.replace("]", "")
                                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaVirgola*/-+", ",")
                                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnBuco*/-+", " ")
                                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaQuadraA*/-+", "[")
                                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaQuadraB*/-+", "]")
                                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnApostrofo*/-+", "'")

                                chiavecifratura= chiavecifratura.replace("[", "")
                                chiavecifratura= chiavecifratura.replace("]", "")
                                cl= 0
                                NumeroChiaveIniziale= randint(0,20)
                                NumeroChiave= NumeroChiaveIniziale
                                for x in range(11):
                                    chiavecifratura= chiavecifratura.replace(str(cl), alfabeto[NumeroChiave])
                                    if str(cl) not in chiavecifratura:
                                        NumeroChiave+= 1
                                        cl+= 1
                                chiavecifratura= "[" + alfabeto[NumeroChiaveIniziale] + " " + chiavecifratura + "]"
                                FileCredenziali.write(MessaggioCifrato + "\n" + chiavecifratura + "\n")    
                                FileCredenziali.close()

                            FileCredenziali= open(TrovaDocumenti, "a")
                            FileCredenziali.write("\n")
                            FileCredenziali.close()
                        else:
                            None
                        z+= 1
                    CredenzialiImportate.grid(row=3, column=0, padx=20, pady=0)
                    ScrittaImportaIntroduzione.focus_set()
                    BottoneEsportaPassword.config(state=NORMAL)
                    BottoneEliminaTutto.config(state=NORMAL)
                except:
                    CredenzialiErroreImportazioneFileNonValido.grid(row=3, column=0, padx=20, pady=0)
        except FileNotFoundError:
            CredenzialiErroreImportazione.grid(row=3, column=0, padx=20, pady=0)
    def TempoScaduto():
        BottoneEliminaTuttoConferma.grid_remove()
        BottoneEliminaTutto.grid()
        Focus2= window.focus_get()
        if BottoneEliminaTuttoConferma == Focus2:
            BottoneEliminaTutto.focus()
    def EliminaTutteCredenzialiFile():
        timer= Timer(2, TempoScaduto)
        timer.start()
        BottoneEliminaTutto.grid_remove()
        BottoneEliminaTuttoConferma.grid(padx=15, pady=5)
        Focus1= window.focus_get()
        if BottoneEliminaTutto == Focus1:
            BottoneEliminaTuttoConferma.focus()
    def EliminaTutteCredenzialiFileConferma():
        window.focus()
        VerificaScrollPresenzaCredenziali1= open(TrovaDocumenti, "r").readlines()
        if len(VerificaScrollPresenzaCredenziali1) > 24:
            global RicaricaScrollOppureNo
            RicaricaScrollOppureNo= False
        BottoneEliminaTuttoConferma.grid_remove()
        BottoneEliminaTutto.grid()
        BottoneEliminaTutto.config(state=DISABLED)
        BottoneEsportaPassword.config(state=DISABLED)
        file1= open(TrovaDocumenti, "r").readlines()
        PasswordAccesso= file1[0]
        ChiavePassAccesso= file1[1]
        os.remove(TrovaDocumenti)
        FileCredenziali= open(TrovaDocumenti, "a")
        FileCredenziali.write(PasswordAccesso + ChiavePassAccesso + "\n")
        FileCredenziali.close()
    def ModificaPassAccesso():
        InserisciPassword1Mod.delete(0, END)
        InserisciPassword2Mod.delete(0, END)
        SchermataImpostazioni.grid_remove()
        SchermataCambiaPassAccesso.grid()
        InserisciPassword1Mod.focus()
    def BottoneMenuModifica():
        global NonCambiarePass
        NonCambiarePass= "Cambia"
        SchermataCambiaPassAccesso.grid_remove()
        SchermataImpostazioni.grid()
        ScrittaImposta.focus()
        InserisciPassword1Mod.config(state=NORMAL)
        InserisciPassword2Mod.config(state=NORMAL)
        BottoneConfermaMod.grid()
        try:
            ScrittaErroreErrataMod.grid_remove()
        except:
            None
        try:
            ScrittaErroreDiverseMod.grid_remove()
        except:
            None
        try:
            ScrittaErroreVuotoMod.grid_remove()
        except:
            None
        try:
            PassModificataScrittaMod.grid_remove()
        except:
            None
    def ConfermaModificaPass():
        ScrittaIntroduzioneLogInMod.focus()
        try:
            ScrittaErroreErrataMod.grid_remove()
        except:
            None
        try:
            ScrittaErroreDiverseMod.grid_remove()
        except:
            None
        try:
            ScrittaErroreVuotoMod.grid_remove()
        except:
            None
        global cl
        global alfabeto
        cl= 0
        c= 0
        c2= 0
        x= 0
        for x in InserisciPassword1Mod.get():
            if x == " ":
                c+= 1
        x= 0
        for x in InserisciPassword2Mod.get():
            if x == " ":
                c2+= 1
        if len(InserisciPassword1Mod.get()) == c and c > 0 and len(InserisciPassword2Mod.get()) == c2 and c2 > 0:
            ScrittaErroreErrataMod.grid(row=5, column=0, pady=5)#
            InserisciPassword1Mod.focus()
        elif InserisciPassword1Mod.get() != InserisciPassword2Mod.get():
            ScrittaErroreDiverseMod.grid(row=5, column=0, pady=5)#
            InserisciPassword1Mod.focus()
        elif InserisciPassword1Mod.get() == "" or InserisciPassword2Mod.get() == "":
            ScrittaErroreVuotoMod.grid(row=5, column=0, pady=5)#
            InserisciPassword1Mod.focus()
        else:
            global NonCambiarePass
            NonCambiarePass= "NonCambiare"
            os.rename(TrovaDocumenti, "CriptazioneCred_Modifica.txt")
            MessaggioCifrato= []
            frase= InserisciPassword1Mod.get()
            while len(MessaggioCifrato) != len(frase):
                    numero= randint(0, len(frase)-1)
                    if numero not in MessaggioCifrato:
                        MessaggioCifrato.append(numero)
            chiavecifratura= str(MessaggioCifrato)
            while cl != len(frase):
                cp= MessaggioCifrato.index(cl)
                MessaggioCifrato[cp]= frase[cl]
                cl+= 1
            while 0 == 0:
                try:
                    cp= MessaggioCifrato.index(",")
                    MessaggioCifrato[cp]= "+-/*QuiCiVaUnaVirgola*/-+"
                except:
                    break
            while 0 == 0:
                try:
                    cp= MessaggioCifrato.index(" ")
                    MessaggioCifrato[cp]= "+-/*QuiCiVaUnBuco*/-+"
                except:
                    break
            while 0 == 0:
                try:
                    cp= MessaggioCifrato.index("[")
                    MessaggioCifrato[cp]= "+-/*QuiCiVaUnaQuadraA*/-+"
                except:
                    break
            while 0 == 0:
                try:
                    cp= MessaggioCifrato.index("]")
                    MessaggioCifrato[cp]= "+-/*QuiCiVaUnaQuadraB*/-+"
                except:
                    break
            while 0 == 0:
                try:
                    cp= MessaggioCifrato.index("'")
                    MessaggioCifrato[cp]= "+-/*QuiCiVaUnApostrofo*/-+"
                except:
                    break
            chiavecifratura= chiavecifratura.replace(",", "")
            MessaggioCifrato= str(MessaggioCifrato)
            MessaggioCifrato= MessaggioCifrato.replace("'", "")
            MessaggioCifrato= MessaggioCifrato.replace(",", "")
            MessaggioCifrato= MessaggioCifrato.replace(" ", "")
            MessaggioCifrato= MessaggioCifrato.replace("[", "")
            MessaggioCifrato= MessaggioCifrato.replace("]", "")
            MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaVirgola*/-+", ",")
            MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnBuco*/-+", " ")
            MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaQuadraA*/-+", "[")
            MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaQuadraB*/-+", "]")
            MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnApostrofo*/-+", "'")

            chiavecifratura= chiavecifratura.replace("[", "")
            chiavecifratura= chiavecifratura.replace("]", "")
            cl= 0
            NumeroChiaveIniziale= randint(0,20)
            NumeroChiave= NumeroChiaveIniziale
            for x in range(11):
                chiavecifratura= chiavecifratura.replace(str(cl), alfabeto[NumeroChiave])
                if str(cl) not in chiavecifratura:
                    NumeroChiave+= 1
                    cl+= 1
            chiavecifratura= "[" + alfabeto[NumeroChiaveIniziale] + " " + chiavecifratura + "]"
            file= open(TrovaDocumenti, "a")
            file.write(MessaggioCifrato + "\n" + chiavecifratura + "\n\n")
            file1=open("CriptazioneCred_Modifica.txt", "r").readlines() 
            x= 3
            while x < len(file1):
                file.write(file1[x])
                x+= 1
            os.remove("CriptazioneCred_Modifica.txt")
            file.close()

            PassModificataScrittaMod.grid(row=5, column=0, pady=5)
            PassModificataScrittaMod.focus()

            InserisciPassword1Mod.config(state=DISABLED)
            InserisciPassword2Mod.config(state=DISABLED)
            BottoneConfermaMod.grid_remove()
    def InformazioniSchermataAppari():
        listadisabled= frame.grid_slaves()
        for elemento in listadisabled:
           elemento.config(state=DISABLED)
        for elementocolorecarattere in listadisabled:
           try:
                elementocolorecarattere.config(disabledforeground="SystemDisabledText")
           except:
                None
        global ScrollPosizioneUno
        global ScrollPosizioneDue
        ScrollPosizioneUno= myscrollbar.get()[0]
        ScrollPosizioneDue= myscrollbar.get()[1]
        myscrollbar.set(0, 1)
        myscrollbar.config(command=False)
        SchermataPrincipaleElementi.grid(row=1, column=0, pady=70, sticky="n")
        SchermataInformazioni.grid()
        SchermataInformazioni.focus()
        AggiungiBottone.config(state=DISABLED)
        CercaBottone.config(state=DISABLED)
        ImpostazioniBottone.config(state=DISABLED)
        InfoBottone.config(state=DISABLED)
        global ContatoreInformazioni
        ContatoreInformazioni= 0
        BottoneIndietro.config(state=DISABLED)
        ScrittaTitoloInfoEsporta.grid(row=0, pady=5)
        ScrittaInfoEsporta.grid(row=1, pady=13, padx=11)
        try:
            ScrittaTitoloInfoImporta.grid_remove()
            ScrittaInfoImporta.grid_remove()
            SpazioBottoniInfo.itemconfig(BottoniInfoCerchio2, fill="#FDFDFD")
        except:
            None
        try:
            ScrittaTitoloInfoGenerale.grid_remove()
            ScrittaInfoGenerale.grid_remove()
            ScrittaFineEmanueleCiotola.grid_remove()
            SpazioBottoniInfo.itemconfig(BottoniInfoCerchio3, fill="#FDFDFD")
        except:
            None
    def InfoAvantiComando():
        global ContatoreInformazioni
        ContatoreInformazioni+= 1
        if ContatoreInformazioni == 1:
            ScrittaTitoloInfoEsporta.grid_remove()
            ScrittaInfoEsporta.grid_remove()
            ScrittaTitoloInfoImporta.grid(row=0, pady=5)
            ScrittaInfoImporta.grid(row=1, pady=13, padx=7)
            SpazioBottoniInfo.itemconfig(BottoniInfoCerchio2, fill="#F3F3F3")
            BottoneIndietro.config(state=NORMAL)
        elif ContatoreInformazioni == 2:
            ScrittaTitoloInfoImporta.grid_remove()
            ScrittaInfoImporta.grid_remove()
            ScrittaTitoloInfoGenerale.grid(row=0, pady=5)
            ScrittaInfoGenerale.grid(row=1, pady=10, padx=6)
            ScrittaFineEmanueleCiotola.grid(row=2, pady=9, padx=5)
            SpazioBottoniInfo.itemconfig(BottoniInfoCerchio3, fill="#F3F3F3")
        elif ContatoreInformazioni == 3:
            global ScrollPosizioneUno
            global ScrollPosizioneDue
            myscrollbar.set(ScrollPosizioneUno, ScrollPosizioneDue)
            myscrollbar.config(command=canvas.yview)
            SchermataPrincipaleElementi.grid_remove()
            SchermataInformazioni.grid_remove()
            SchermataPrincipale.focus()
            AggiungiBottone.config(state=NORMAL)
            CercaBottone.config(state=NORMAL)
            ImpostazioniBottone.config(state=NORMAL)
            InfoBottone.config(state=NORMAL)
            ScrittaTitoloInfoGenerale.grid_remove()
            ScrittaInfoGenerale.grid_remove()
            ScrittaFineEmanueleCiotola.grid_remove()
            SpazioBottoniInfo.itemconfig(BottoniInfoCerchio2, fill="#FDFDFD")
            SpazioBottoniInfo.itemconfig(BottoniInfoCerchio3, fill="#FDFDFD")
            VisualizzaTutteLeCredenziali()
    def InfoIndietroComando():
        global ContatoreInformazioni
        ContatoreInformazioni-= 1
        if ContatoreInformazioni == 0:
            BottoneIndietro.config(state=DISABLED)
            FocusInfo= window.focus_get()
            if FocusInfo == BottoneIndietro:
                BottoneAvanti.focus()
            ScrittaTitoloInfoImporta.grid_remove()
            ScrittaInfoImporta.grid_remove()
            ScrittaTitoloInfoEsporta.grid(row=0, pady=5)
            ScrittaInfoEsporta.grid(row=1, pady=13, padx=11)
            SpazioBottoniInfo.itemconfig(BottoniInfoCerchio2, fill="#FDFDFD")
        elif ContatoreInformazioni == 1:
            ScrittaTitoloInfoGenerale.grid_remove()
            ScrittaInfoGenerale.grid_remove()
            ScrittaFineEmanueleCiotola.grid_remove()
            ScrittaTitoloInfoImporta.grid(row=0, pady=5)
            ScrittaInfoImporta.grid(row=1, pady=13, padx=7)
            SpazioBottoniInfo.itemconfig(BottoniInfoCerchio3, fill="#FDFDFD")
    def CercaAccount():
        SchermataPrincipaleElementi.grid(row=1, column=0, pady=0, sticky="n")
        try:
            CercaErroreNonTrovato.grid_remove()
        except:
            None
        try:
            CercaErroreNonScritto.grid_remove()
        except:
            None
        AggiungiBottone.config(state=DISABLED)
        CercaBottone.config(state=DISABLED)
        ImpostazioniBottone.config(state=DISABLED)
        InfoBottone.config(state=DISABLED)
        SchermataCercaAccount.grid()
        CercaAccEntry.focus()
        CercaAccEntry.delete(0, END)
    def CercaAccountComando():
        global ScrollPosizioneUno
        global ScrollPosizioneDue
        ScrollPosizioneUno= myscrollbar.get()[0]
        ScrollPosizioneDue= myscrollbar.get()[1]
        myscrollbar.set(0, 1)
        myscrollbar.config(command=False)
        global Label1
        global Label2
        global Label3        
        try:
            CercaErroreNonTrovato.grid_remove()
        except:
            None
        try:
            CercaErroreNonScritto.grid_remove()
        except:
            None
        try:
            FileCredenziali= open(TrovaDocumenti, "r").readlines()
            c= 3
            while c < len(FileCredenziali):
                menospazio= FileCredenziali[c]
                menospazio= menospazio[0:-1]
                menospaziochiave= FileCredenziali[c + 1]
                menospaziochiave= menospaziochiave[0:-1]
                cl= 0
                global alfabeto
                contacl= 1
                FraseDecifrata= ""
                ListaDecriptazione= []
                MessaggioCifrato= menospazio
                chiavecifratura= menospaziochiave
                chiavecifratura= chiavecifratura.replace("]", "")
                NumeroChiave= alfabeto.index(chiavecifratura[1])
                chiavecifratura= chiavecifratura.replace("[" + chiavecifratura[1] + " ", "")
                cl= 0
                for x in range(11):
                    chiavecifratura= chiavecifratura.replace(alfabeto[NumeroChiave], str(cl))
                    if str(alfabeto[NumeroChiave]) not in chiavecifratura:
                        NumeroChiave+= 1
                        cl+= 1
                cl= 0
                while contacl != len(chiavecifratura):
                    if chiavecifratura[contacl] == " ":
                        ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                        cl= contacl
                    contacl+= 1
                ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                cl= 0
                while cl != len(MessaggioCifrato):
                    cp= ListaDecriptazione.index(cl)
                    FraseDecifrata+= MessaggioCifrato[cp]
                    cl+= 1
                if CercaAccEntry.get() == FraseDecifrata:
                    Label1= FraseDecifrata
                    global ContaRimuovi
                    ContaRimuovi= c
                    c+= 2
                    break
                c+= 7
            contalabel= 0
            FileCredenziali= open(TrovaDocumenti, "r").readlines()
            while contalabel < 2:
                cl= 0
                contacl= 1
                FraseDecifrata= ""
                ListaDecriptazione= []
                MessaggioCifrato= FileCredenziali[c]
                chiavecifratura= FileCredenziali[c + 1]
                chiavecifratura= chiavecifratura.replace("]", "")
                NumeroChiave= alfabeto.index(chiavecifratura[1])
                chiavecifratura= chiavecifratura.replace("[" + chiavecifratura[1] + " ", "")
                cl= 0
                for x in range(11):
                    chiavecifratura= chiavecifratura.replace(alfabeto[NumeroChiave], str(cl))
                    if str(alfabeto[NumeroChiave]) not in chiavecifratura:
                        NumeroChiave+= 1
                        cl+= 1
                cl= 0
                while contacl != len(chiavecifratura):
                    if chiavecifratura[contacl] == " ":
                        ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                        cl= contacl
                    contacl+= 1
                ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                cl= 0
                while cl != len(MessaggioCifrato) - 1:#
                    cp= ListaDecriptazione.index(cl)
                    FraseDecifrata+= MessaggioCifrato[cp]
                    cl+= 1
                c+= 2
                contalabel+= 1
                if contalabel == 1:
                    if FraseDecifrata == "None":
                        Label2= "Mail non inserita."
                    else:
                        Label2= FraseDecifrata
                else:
                    Label3= FraseDecifrata
            SchermataPrincipaleElementi.grid(row=1, column=0, pady=70, sticky="n")   
            SchermataCercaAccount.grid_remove()
            listadisabled= frame.grid_slaves()
            for elemento in listadisabled:
                elemento.config(state=DISABLED)
            for elementocolorecarattere in listadisabled:
                try:
                    elementocolorecarattere.config(disabledforeground="SystemDisabledText")
                except:
                    None
            BottoneGest.config(state=DISABLED)
            window.focus()
            SchermataVisualizzazioneSpecifica.grid()
            VisSpecificaNome.config(state=NORMAL)
            VisSpecificaNome.delete(0, END)
            VisSpecificaNome.insert(0, Label1)
            VisSpecificaNome.config(state=DISABLED)
            VisSpecificaMail.config(state=NORMAL)
            VisSpecificaMail.delete(0, END)
            VisSpecificaMail.insert(0, Label2)
            VisSpecificaMail.config(state=DISABLED)
            VisSpecificaPass.config(state=NORMAL)
            VisSpecificaPass.delete(0, END)
            VisSpecificaPass.insert(0, Label3)
            VisSpecificaPass.config(state=DISABLED)
        except:
            if CercaAccEntry.get() == "":
                CercaErroreNonScritto.grid(row=1, column=0, columnspan=3, pady=5)
            else:
                CercaErroreNonTrovato.grid(row=1, column=0, columnspan=3, pady=5)
    def IndietroVisSpecificaComando():
        global ScrollPosizioneUno
        global ScrollPosizioneDue
        myscrollbar.set(ScrollPosizioneUno, ScrollPosizioneDue)
        myscrollbar.config(command=canvas.yview)
        SchermataPrincipaleElementi.grid_remove()
        global TastoIndietroAvanti1o2
        TastoIndietroAvanti1o2= 0
        SchermataVisualizzazioneSpecifica.grid_remove()
        window.focus()
        VisSpecificaNome.delete(0, END)
        VisSpecificaMail.delete(0, END)
        VisSpecificaPass.delete(0, END)
        BottoneGest.config(state=NORMAL)
        AggiungiBottone.config(state=NORMAL)
        CercaBottone.config(state=NORMAL)
        ImpostazioniBottone.config(state=NORMAL)
        InfoBottone.config(state=NORMAL)
        VisualizzaTutteLeCredenziali()
    def ModificaAccountSpecifico():
        global TastoIndietroAvanti1o2
        TastoIndietroAvanti1o2+= 1
        ScrittaIntroduzioneVisSpecifica.config(text="Modifica credenziali")
        BottoneEliminaAccountSpecifica.grid(row=4, column=0, columnspan=2, pady=10)
        VisSpecificaNome.config(state=NORMAL)
        VisSpecificaNome.focus()
        VisSpecificaNome.select_range(0, END)
        VisSpecificaMail.config(state=NORMAL)
        VisSpecificaPass.config(state=NORMAL)
        if VisSpecificaMail.get() == "Mail non inserita.":
            VisSpecificaMail.delete(0, END)
        global Linea1
        global Linea2
        global Linea3
        Linea1= SpazioVisSpecifica.create_line(140, 71,
                                               361, 71,
                                               width=2,
                                               fill="#E1E1E1")
        Linea2= SpazioVisSpecifica.create_line(140, 109,
                                               361, 109,
                                               width=2,
                                               fill="#E1E1E1")
        Linea3= SpazioVisSpecifica.create_line(140, 147,
                                               361, 147,
                                               width=2,
                                               fill="#E1E1E1")
        BottoneIndietroVisSpec.grid_remove()
        ModificaBottoneIcona.grid_remove()
        BottoneConfermaModAcc.grid(row=0, column=1, pady=0, sticky="NE")
        BottoneAnnullaModAcc.grid(row=0, column=0, pady=0, sticky="NW")
    def AnnullaModificaAccountSpecifico():
        try:
            global TimerVisAccountSpecifico
            TimerVisAccountSpecifico.cancel()
        except:
            None
        global TastoIndietroAvanti1o2
        TastoIndietroAvanti1o2+= 1
        ScrittaIntroduzioneVisSpecifica.config(text="Visualizza credenziali")
        BottoneEliminaAccountSpecifica.grid_remove()
        BottoneEliminaAccountSpecificaConferma.grid_remove()
        BottoneIndietroVisSpec.grid(row=0, column=0, pady=0, sticky="NW")
        ModificaBottoneIcona.grid(row=0, column=1, pady=0, sticky="NE")
        BottoneConfermaModAcc.grid_remove()
        BottoneAnnullaModAcc.grid_remove()
        global Label1
        global Label2
        global Label3
        VisSpecificaNome.delete(0, END)
        VisSpecificaNome.insert(0, Label1)
        VisSpecificaNome.config(state=DISABLED)
        VisSpecificaMail.delete(0, END)
        VisSpecificaMail.insert(0, Label2)
        VisSpecificaMail.config(state=DISABLED)
        VisSpecificaPass.delete(0, END)
        VisSpecificaPass.insert(0, Label3)
        VisSpecificaPass.config(state=DISABLED)
        SpazioVisSpecifica.itemconfig(Linea1, fill="#FDFDFD")
        SpazioVisSpecifica.itemconfig(Linea2, fill="#FDFDFD")
        SpazioVisSpecifica.itemconfig(Linea3, fill="#FDFDFD")
    def ConfermaModificaAccountSpecifico():
        global ContaRimuovi
        SpazioVisSpecifica.itemconfig(Linea1, fill="#FDFDFD")
        SpazioVisSpecifica.itemconfig(Linea2, fill="#FDFDFD")
        SpazioVisSpecifica.itemconfig(Linea3, fill="#FDFDFD")
        try:
            os.remove("CriptazioneCred_Modifica.txt")
        except:
            None
        os.rename(TrovaDocumenti, "CriptazioneCred_Modifica.txt")
        file=open(TrovaDocumenti, "a")
        file1=open("CriptazioneCred_Modifica.txt", "r").readlines() 
        x= 0
        while x < len(file1):
            if x < ContaRimuovi or x > ContaRimuovi+6:
                file.write(file1[x])
            x+= 1
        file.close()

        global errore1
        global errore2
        global errore3
        errore1= "Negativo"
        errore2= "Negativo"
        errore3= "Negativo"
        nomenonvalido= "Nome non valido!"
        nomenoninserito= "Devi inserire un nome!"
        nomeusato= "Nome servizio già in uso!"
        mailnonvalida= "Mail non valida!"
        passnonvalida= "Password non valida!"
        passnoninserita= "Inserisci una password!"
        c= 0
        for x in VisSpecificaNome.get():
            if x == " ":
                c+= 1    
        if len(VisSpecificaNome.get()) == c and c > 0:
            caso1= 1
            errore1= "Positivo"
        if VisSpecificaNome.get() == "":
            caso1= 2
            errore1= "Positivo"
        FileCredenziali= open(TrovaDocumenti, "r").readlines()
        c= 3
        while c < len(FileCredenziali):
            menospazio= FileCredenziali[c]
            menospazio= menospazio[0:-1]
            menospaziochiave= FileCredenziali[c + 1]
            menospaziochiave= menospaziochiave[0:-1]
            global cl
            cl= 0
            global alfabeto
            contacl= 1
            FraseDecifrata= ""
            ListaDecriptazione= []
            MessaggioCifrato= menospazio
            chiavecifratura= menospaziochiave
            chiavecifratura= chiavecifratura.replace("]", "")
            NumeroChiave= alfabeto.index(chiavecifratura[1])
            chiavecifratura= chiavecifratura.replace("[" + chiavecifratura[1] + " ", "")
            cl= 0
            for x in range(11):
                chiavecifratura= chiavecifratura.replace(alfabeto[NumeroChiave], str(cl))
                if str(alfabeto[NumeroChiave]) not in chiavecifratura:
                    NumeroChiave+= 1
                    cl+= 1
            cl= 0
            while contacl != len(chiavecifratura):
                if chiavecifratura[contacl] == " ":
                    ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                    cl= contacl
                contacl+= 1
            ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
            cl= 0
            while cl != len(MessaggioCifrato):
                cp= ListaDecriptazione.index(cl)
                FraseDecifrata+= MessaggioCifrato[cp]
                cl+= 1
            if VisSpecificaNome.get() == FraseDecifrata:
                caso1= 3
                errore1= "Positivo"
            c+= 7
            
        if VisSpecificaMail.get() != "":
            try:
                VisSpecificaMail.get().index("@")
                try:
                    VisSpecificaMail.get().index(".com")
                except:
                    VisSpecificaMail.get().index(".it")
            except:
                errore2= "Positivo"
        c= 0
        for x in VisSpecificaPass.get():
            if x == " ":
                c+= 1     
        if len(VisSpecificaPass.get()) == c and c > 0:
            caso3= 1
            errore3= "Positivo"
        if VisSpecificaPass.get() == "":
            caso3= 2
            errore3= "Positivo"
            
        if errore3 == "Positivo":
            if caso3 == 1:
                testoerrore3= passnonvalida
            if caso3 == 2:
                testoerrore3= passnoninserita    
            SpazioVisSpecifica.itemconfig(Linea3, fill="#F64747")
            VisSpecificaPass.focus()
        if errore2 == "Positivo":
            SpazioVisSpecifica.itemconfig(Linea2, fill="#F64747")
            VisSpecificaMail.focus()
        if errore1 == "Positivo":
            if caso1 == 1:
                testoerrore1= nomenonvalido
            if caso1 == 2:
                testoerrore1= nomenoninserito
            if caso1 == 3:
                testoerrore1= nomeusato
            SpazioVisSpecifica.itemconfig(Linea1, fill="#F64747")
            VisSpecificaNome.focus()
            
        if errore1 == "Positivo" or errore2 == "Positivo" or errore3 == "Positivo":
            os.remove(TrovaDocumenti)
            os.rename("CriptazioneCred_Modifica.txt", TrovaDocumenti)
        else:
            try:
                global TimerVisAccountSpecifico
                TimerVisAccountSpecifico.cancel()
            except:
                None
            os.remove("CriptazioneCred_Modifica.txt")
            ScrittaIntroduzioneVisSpecifica.config(text="Visualizza credenziali")
            FileCredenziali= open(TrovaDocumenti, "a")
            contatoretraduzione= 1
            while contatoretraduzione <= 3:
                cl= 0
                MessaggioCifrato= []
                if contatoretraduzione == 1:
                    NuovoNomeModificato= VisSpecificaNome.get()
                    frase= NuovoNomeModificato
                if contatoretraduzione == 2:
                    if VisSpecificaMail.get() == "":
                        NuovaMailModificato= "Mail non inserita."
                        frase= "None"
                    else:
                        NuovaMailModificato= VisSpecificaMail.get()
                        frase= NuovaMailModificato
                if contatoretraduzione == 3:
                    NuovaPassModificato= VisSpecificaPass.get()
                    frase= NuovaPassModificato
                while len(MessaggioCifrato) != len(frase):
                    numero= randint(0, len(frase)-1)
                    if numero not in MessaggioCifrato:
                        MessaggioCifrato.append(numero)
                chiavecifratura= str(MessaggioCifrato)
                while cl != len(frase):
                    cp= MessaggioCifrato.index(cl)
                    MessaggioCifrato[cp]= frase[cl]
                    cl+= 1
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index(",")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaVirgola*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index(" ")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnBuco*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index("[")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaQuadraA*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index("]")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnaQuadraB*/-+"
                    except:
                        break
                while 0 == 0:
                    try:
                        cp= MessaggioCifrato.index("'")
                        MessaggioCifrato[cp]= "+-/*QuiCiVaUnApostrofo*/-+"
                    except:
                        break
                chiavecifratura= chiavecifratura.replace(",", "")
                MessaggioCifrato= str(MessaggioCifrato)
                MessaggioCifrato= MessaggioCifrato.replace("'", "")
                MessaggioCifrato= MessaggioCifrato.replace(",", "")
                MessaggioCifrato= MessaggioCifrato.replace(" ", "")
                MessaggioCifrato= MessaggioCifrato.replace("[", "")
                MessaggioCifrato= MessaggioCifrato.replace("]", "")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaVirgola*/-+", ",")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnBuco*/-+", " ")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaQuadraA*/-+", "[")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnaQuadraB*/-+", "]")
                MessaggioCifrato= MessaggioCifrato.replace("+-/*QuiCiVaUnApostrofo*/-+", "'")

                chiavecifratura= chiavecifratura.replace("[", "")
                chiavecifratura= chiavecifratura.replace("]", "")
                cl= 0
                NumeroChiaveIniziale= randint(0,20)
                NumeroChiave= NumeroChiaveIniziale
                for x in range(11):
                    chiavecifratura= chiavecifratura.replace(str(cl), alfabeto[NumeroChiave])
                    if str(cl) not in chiavecifratura:
                        NumeroChiave+= 1
                        cl+= 1
                chiavecifratura= "[" + alfabeto[NumeroChiaveIniziale] + " " + chiavecifratura + "]"
                FileCredenziali.write(MessaggioCifrato + "\n" + chiavecifratura + "\n")
                contatoretraduzione+= 1
            FileCredenziali.write("\n")
            FileCredenziali.close()
            global TastoIndietroAvanti1o2
            TastoIndietroAvanti1o2+= 1
            BottoneEliminaAccountSpecifica.grid_remove()
            BottoneEliminaAccountSpecificaConferma.grid_remove()
            BottoneIndietroVisSpec.grid(row=0, column=0, pady=0, sticky="NW")
            ModificaBottoneIcona.grid(row=0, column=1, pady=0, sticky="NE")
            BottoneConfermaModAcc.grid_remove()
            BottoneAnnullaModAcc.grid_remove()
            global Label1
            global Label2
            global Label3
            VisSpecificaNome.delete(0, END)
            Label1= NuovoNomeModificato
            VisSpecificaNome.insert(0, Label1)
            VisSpecificaNome.config(state=DISABLED)
            VisSpecificaMail.delete(0, END)
            Label2= NuovaMailModificato
            VisSpecificaMail.insert(0, Label2)
            VisSpecificaMail.config(state=DISABLED)
            VisSpecificaPass.delete(0, END)
            Label3= NuovaPassModificato
            VisSpecificaPass.insert(0, Label3)
            VisSpecificaPass.config(state=DISABLED)
            SpazioVisSpecifica.itemconfig(Linea1, fill="#FDFDFD")
            SpazioVisSpecifica.itemconfig(Linea2, fill="#FDFDFD")
            SpazioVisSpecifica.itemconfig(Linea3, fill="#FDFDFD")
    def TempoScadutoEliminaAccountSpecifico():
        TempoScadutoOppureIndietro= str(SpazioVisSpecifica.grid_slaves())
        if TempoScadutoOppureIndietro == "[<tkinter.Button object .!frame2.!frame2.!frame7.!canvas.!button6>, <tkinter.Button object .!frame2.!frame2.!frame7.!canvas.!button4>, <tkinter.Button object .!frame2.!frame2.!frame7.!canvas.!button3>, <tkinter.Entry object .!frame2.!frame2.!frame7.!canvas.!entry3>, <tkinter.Label object .!frame2.!frame2.!frame7.!canvas.!label4>, <tkinter.Entry object .!frame2.!frame2.!frame7.!canvas.!entry2>, <tkinter.Label object .!frame2.!frame2.!frame7.!canvas.!label3>, <tkinter.Entry object .!frame2.!frame2.!frame7.!canvas.!entry>, <tkinter.Label object .!frame2.!frame2.!frame7.!canvas.!label2>, <tkinter.Label object .!frame2.!frame2.!frame7.!canvas.!label>]":
            BottoneEliminaAccountSpecificaConferma.grid_remove()
            BottoneEliminaAccountSpecifica.grid(row=4, column=0, columnspan=2, pady=10)
    def EliminaAccountSpecificaComando():
        global TimerVisAccountSpecifico
        TimerVisAccountSpecifico= Timer(3, TempoScadutoEliminaAccountSpecifico)
        TimerVisAccountSpecifico.start()
        BottoneEliminaAccountSpecifica.grid_remove()
        BottoneEliminaAccountSpecificaConferma.grid(row=4, column=0, columnspan=2, pady=10)
    def EliminaAccountSpecificaConfermaComando():
        try:
            global TimerVisAccountSpecifico
            TimerVisAccountSpecifico.cancel()
        except:
            None
        global ScrollPosizioneUno
        global ScrollPosizioneDue
        myscrollbar.set(ScrollPosizioneUno, ScrollPosizioneDue)
        myscrollbar.config(command=canvas.yview)
        global TastoIndietroAvanti1o2
        TastoIndietroAvanti1o2= 0
        SchermataPrincipaleElementi.grid(row=1, column=0, pady=0, sticky="n")
        ScrittaIntroduzioneVisSpecifica.config(text="Visualizza credenziali")
        BottoneEliminaAccountSpecificaConferma.grid_remove()
        SpazioVisSpecifica.itemconfig(Linea2, fill="#FDFDFD")
        SpazioVisSpecifica.itemconfig(Linea3, fill="#FDFDFD")
        SpazioVisSpecifica.itemconfig(Linea1, fill="#FDFDFD")
        BottoneEliminaAccountSpecifica.grid_remove()
        BottoneIndietroVisSpec.grid(row=0, column=0, pady=0, sticky="NW")
        ModificaBottoneIcona.grid(row=0, column=1, pady=0, sticky="NE")
        BottoneConfermaModAcc.grid_remove()
        BottoneAnnullaModAcc.grid_remove() 
        SchermataVisualizzazioneSpecifica.grid_remove()
        global ContaRimuovi
        os.rename(TrovaDocumenti, "CriptazioneCred_Modifica.txt")
        file=open(TrovaDocumenti, "a")
        file1=open("CriptazioneCred_Modifica.txt", "r").readlines() 
        x= 0
        while x < len(file1):
            if x < ContaRimuovi or x > ContaRimuovi+6:
                file.write(file1[x])
            x+= 1
        os.remove("CriptazioneCred_Modifica.txt")
        file.close()
        SchermataPrincipaleElementi.grid_remove()
        BottoneGest.config(state=NORMAL)
        AggiungiBottone.config(state=NORMAL)
        CercaBottone.config(state=NORMAL)
        ImpostazioniBottone.config(state=NORMAL)
        InfoBottone.config(state=NORMAL)
        VisualizzaTutteLeCredenziali()
    ###########################
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=878, height=463, bg="#FDFDFD") 
    def show_lan(BottoneNomeAccount):
        try:
            SchermataCercaAccount.grid_remove()
            SchermataPrincipale.focus()
            AggiungiBottone.config(state=NORMAL)
            CercaBottone.config(state=NORMAL)
            ImpostazioniBottone.config(state=NORMAL)
            InfoBottone.config(state=NORMAL)
        except:
            None
        global ScrollPosizioneUno
        global ScrollPosizioneDue
        ScrollPosizioneUno= myscrollbar.get()[0]
        ScrollPosizioneDue= myscrollbar.get()[1]
        myscrollbar.set(0, 1)
        myscrollbar.config(command=False)
        SchermataPrincipaleElementi.grid(row=1, column=0, pady=70, sticky="n")
        global Label1
        global Label2
        global Label3
        CercaAccEntry.delete(0, END)

        FileCredenziali= open(TrovaDocumenti, "r").readlines()
        c= 3
        while c < len(FileCredenziali):
            menospazio= FileCredenziali[c]
            menospazio= menospazio[0:-1]
            menospaziochiave= FileCredenziali[c + 1]
            menospaziochiave= menospaziochiave[0:-1]
            cl= 0
            global alfabeto
            contacl= 1
            FraseDecifrata= ""
            ListaDecriptazione= []
            MessaggioCifrato= menospazio
            chiavecifratura= menospaziochiave
            chiavecifratura= chiavecifratura.replace("]", "")
            NumeroChiave= alfabeto.index(chiavecifratura[1])
            chiavecifratura= chiavecifratura.replace("[" + chiavecifratura[1] + " ", "")
            cl= 0
            for x in range(11):
                chiavecifratura= chiavecifratura.replace(alfabeto[NumeroChiave], str(cl))
                if str(alfabeto[NumeroChiave]) not in chiavecifratura:
                    NumeroChiave+= 1
                    cl+= 1
            cl= 0
            while contacl != len(chiavecifratura):
                if chiavecifratura[contacl] == " ":
                    ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                    cl= contacl
                contacl+= 1
            ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
            cl= 0
            while cl != len(MessaggioCifrato):
                cp= ListaDecriptazione.index(cl)
                FraseDecifrata+= MessaggioCifrato[cp]
                cl+= 1
            if  FraseDecifrata == BottoneNomeAccount[0:-1]:
                Label1= FraseDecifrata
                global ContaRimuovi
                ContaRimuovi= c
                c+= 2
                break
            c+= 7
        contalabel= 0
        FileCredenziali= open(TrovaDocumenti, "r").readlines()
        while contalabel < 2:
            cl= 0
            contacl= 1
            FraseDecifrata= ""
            ListaDecriptazione= []
            MessaggioCifrato= FileCredenziali[c]
            chiavecifratura= FileCredenziali[c + 1]
            chiavecifratura= chiavecifratura.replace("]", "")
            NumeroChiave= alfabeto.index(chiavecifratura[1])
            chiavecifratura= chiavecifratura.replace("[" + chiavecifratura[1] + " ", "")
            cl= 0
            for x in range(11):
                chiavecifratura= chiavecifratura.replace(alfabeto[NumeroChiave], str(cl))
                if str(alfabeto[NumeroChiave]) not in chiavecifratura:
                    NumeroChiave+= 1
                    cl+= 1
            cl= 0
            while contacl != len(chiavecifratura):
                if chiavecifratura[contacl] == " ":
                    ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
                    cl= contacl
                contacl+= 1
            ListaDecriptazione.append(int(chiavecifratura[cl:contacl]))
            cl= 0
            while cl != len(MessaggioCifrato) - 1:#
                cp= ListaDecriptazione.index(cl)
                FraseDecifrata+= MessaggioCifrato[cp]
                cl+= 1
            c+= 2
            contalabel+= 1
            if contalabel == 1:
                if FraseDecifrata == "None":
                    Label2= "Mail non inserita."
                else:
                    Label2= FraseDecifrata
            else:
                Label3= FraseDecifrata

        listadisabled= frame.grid_slaves()
        for elemento in listadisabled:
           elemento.config(state=DISABLED)
        for elementocolorecarattere in listadisabled:
           try:
                elementocolorecarattere.config(disabledforeground="SystemDisabledText")
           except:
                None
        BottoneGest.config(state=DISABLED)
        AggiungiBottone.config(state=DISABLED)
        CercaBottone.config(state=DISABLED)
        ImpostazioniBottone.config(state=DISABLED)
        InfoBottone.config(state=DISABLED)
        SchermataVisualizzazioneSpecifica.grid()
        VisSpecificaNome.config(state=NORMAL)
        VisSpecificaNome.delete(0, END)
        VisSpecificaNome.insert(0, Label1)
        VisSpecificaNome.focus()
        VisSpecificaNome.select_range(0, END)
        VisSpecificaMail.config(state=NORMAL)
        VisSpecificaMail.delete(0, END)
        VisSpecificaMail.insert(0, Label2)
        VisSpecificaPass.config(state=NORMAL)
        VisSpecificaPass.delete(0, END)
        VisSpecificaPass.insert(0, Label3)
        
        ScrittaIntroduzioneVisSpecifica.config(text="Modifica credenziali")
        BottoneEliminaAccountSpecifica.grid(row=4, column=0, columnspan=2, pady=10)
        if VisSpecificaMail.get() == "Mail non inserita.":
            VisSpecificaMail.delete(0, END)
        BottoneIndietroVisSpec.grid_remove()
        ModificaBottoneIcona.grid_remove()
        BottoneConfermaModAcc.grid(row=0, column=1, pady=0, sticky="NE")
        BottoneAnnullaModAcc.grid(row=0, column=0, pady=0, sticky="NW")
        ModificaAccountSpecifico()
        
    canvas= Canvas(SchermataVisualizzazioneCredenziali, highlightbackground="#FDFDFD")
    frame= Frame(canvas, bd=0, bg="#FDFDFD")
    myscrollbar= Scrollbar(SchermataVisualizzazioneCredenziali,
                           orient="vertical",
                           width=15,
                           command=canvas.yview,
                           bd=0,
                           relief="flat",activebackground="red",bg="red",
                           activerelief="flat")
    canvas.configure(yscrollcommand=myscrollbar.set)
    myscrollbar.pack(side="right", fill= "y")
    canvas.pack(side="bottom")
    canvas.create_window((0, 0), window=frame, anchor="nw")
    frame.bind("<Configure>", myfunction)
    VisualizzaTutteLeCredenziali()
    ###########################

    #Inizio schermata home dichiara
    BottoneGest= Button(SchermataPrincipaleMenù,
                        text="Gestore Password",
                        bg="#F3F3F3",
                        bd=0,
                        disabledforeground="#606060",
                        font="Times 12",
                        activebackground="#F3F3F3",
                        takefocus= False,
                        command=RicaricaAccountVisComando)
    AggiungiBottone= Button(SchermataPrincipaleMenù,
                            text="Aggiungi",
                            bg="#F3F3F3",
                            bd=0,
                            disabledforeground="#606060",
                            activebackground="#F3F3F3",
                            command=AggiungiNuovoAccountMenù)
    CercaBottone= Button(SchermataPrincipaleMenù,
                         text="Cerca",
                         bg="#F3F3F3",
                         disabledforeground="#606060",
                         bd=0,
                         activebackground="#F3F3F3",
                         command=CercaAccount)
    ImpostazioniBottone= Button(SchermataPrincipaleMenù,
                                text="Impostazioni",
                                bg="#F3F3F3",
                                disabledforeground="#606060",
                                bd=0,
                                activebackground="#F3F3F3",
                                command=ImpostazioniSchermataGenerale)
    InfoBottone= Button(SchermataPrincipaleMenù,
                        text="Info",
                        bg="#F3F3F3",
                        disabledforeground="#606060",
                        bd=0,
                        activebackground="#F3F3F3",
                        command=InformazioniSchermataAppari)
    #Fine schermata home dichiara
    #Inizio aggiungi dichiara
    SpazioAggiungiNuovoAccount= Canvas(SchermataAggiungiAccount,
                                       bg="#FDFDFD",
                                       bd=1,
                                       highlightbackground="#F3F3F3",
                                       highlightcolor="#F3F3F3")
    ScrittaIntroduzioneNuovo= Label(SpazioAggiungiNuovoAccount,
                                    text="Nuovo account",
                                    bg="#FDFDFD",
                                    font="helvetica 15",
                                    height=1)
    ScrittaInserisciNome= Label(SpazioAggiungiNuovoAccount,
                                text="Inserisci il nome del servizio:",
                                bg="#FDFDFD",
                                font="helvetica 12")
    InserisciNome=  Entry(SpazioAggiungiNuovoAccount,
                          relief="groove",
                          selectforeground="#F3F3F3",
                          selectbackground="black",
                          disabledforeground="#606060",
                          width=20,
                          bg="#F3F3F3",
                          font="helvetica 15")
    ScrittaInserisciMail= Label(SpazioAggiungiNuovoAccount,
                                text="Inserisci la mail (facoltativo):",
                                bg="#FDFDFD",
                                font="helvetica 12")
    InserisciMail=  Entry(SpazioAggiungiNuovoAccount,
                          relief="groove",
                          selectforeground="#F3F3F3",
                          selectbackground="black",
                          disabledforeground="#606060",
                          width=20,
                          bg="#F3F3F3",
                          font="helvetica 15")
    ScrittaInserisciPass= Label(SpazioAggiungiNuovoAccount,
                                text="Inserisci la password:",
                                bg="#FDFDFD",
                                font="helvetica 12")
    InserisciPass=  Entry(SpazioAggiungiNuovoAccount,
                          relief="groove",
                          selectforeground="#F3F3F3",
                          selectbackground="black",
                          disabledforeground="#606060",
                          width=20,
                          bg="#F3F3F3",
                          font="helvetica 15")
    BottoneConfermaCredenziali= Button(SpazioAggiungiNuovoAccount,
                                       relief="flat",
                                       bg="#F3F3F3",
                                       text="Salva account",
                                       width=20,
                                       bd=0,
                                       height=2,
                                       activebackground="#F3F3F3",
                                       takefocus= False,
                                       command=ConfermaNuovoAccount)
    ScrittaAccountNuovoAggiuntoConferma= Label(SpazioAggiungiNuovoAccount,
                                               text="Account aggiunto!",
                                               bg="#FDFDFD",
                                               fg="green")
    BottoneRiscriviCredenziali= Button(SpazioAggiungiNuovoAccount,
                                       relief="flat",
                                       bg="#F3F3F3",
                                       text="Ho capito!",
                                       width=20,
                                       bd=0,
                                       height=2,
                                       activebackground="#F3F3F3",
                                       takefocus= False,
                                       command=ConfermaRiscriviNuovoAccount)
    BottoneHomeAggiungi= Button(SpazioAggiungiNuovoAccount,
                                relief="flat",
                                bg="#F3F3F3",
                                text="←",
                                bd=0,
                                width=3,
                                height=1,
                                activebackground="#F3F3F3",
                                takefocus= False,
                                command=BottoneHomeAggiungi)
    BottoneAltreCredenziali= Button(SpazioAggiungiNuovoAccount,
                                    relief="flat",
                                    bg="#F3F3F3",
                                    text="Aggiungi altro",
                                    width=20,
                                    bd=0,
                                    height=2,
                                    activebackground="#F3F3F3",
                                    takefocus= False,
                                    command=NuoveCredenziali)
    #Fine aggiungi dichiara
    #Inizio impostazioni dichiara
    SpazioImpostazioniAccount= Canvas(SchermataImpostazioni,
                                      bg="#FDFDFD",
                                      bd=1,
                                      highlightbackground="#F3F3F3",
                                      highlightcolor="#F3F3F3")
    ScrittaImposta= Label(SpazioImpostazioniAccount,
                          text="Impostazioni",
                          bg="#FDFDFD",
                          font="Times 18 bold")
    BottoneEsportaPassword= Button(SpazioImpostazioniAccount,
                                   relief="flat",
                                   text="Esporta credenziali",
                                   bg="#F3F3F3",
                                   bd=0,
                                   width=25,
                                   height=3,
                                   disabledforeground="#606060",
                                   activebackground="#F3F3F3",
                                   command=EsportaComando)
    BottoneImportaPassword= Button(SpazioImpostazioniAccount,
                                   relief="flat",
                                   text="Importa credenziali",
                                   bg="#F3F3F3",
                                   bd=0,
                                   width=25,
                                   height=3,
                                   disabledforeground="#606060",
                                   activebackground="#F3F3F3",
                                   command=ImportaComando)
    BottoneModificaPass= Button(SpazioImpostazioniAccount,
                                relief="flat",
                                text="Cambia password di accesso",
                                bg="#F3F3F3",
                                bd=0,
                                width=25,
                                height=3,
                                disabledforeground="#606060",
                                activebackground="#F3F3F3",
                                command=ModificaPassAccesso)
    BottoneEliminaTutto= Button(SpazioImpostazioniAccount,
                                relief="flat",
                                text="Elimina tutte le credenziali",
                                bg="#F3F3F3",
                                bd=0,
                                width=25,
                                height=3,
                                disabledforeground="#606060",
                                activebackground="#F3F3F3",
                                command=EliminaTutteCredenzialiFile)
    BottoneEliminaTuttoConferma= Button(SpazioImpostazioniAccount,
                                        relief="flat",
                                        text="Premi per confermare",
                                        bg="#F3F3F3",
                                        bd=0,
                                        width=25,
                                        height=3,
                                        disabledforeground="#606060",
                                        activebackground="#E1E1E1",
                                        command=EliminaTutteCredenzialiFileConferma)
    BottoneHomeDaImposta= Button(SpazioImpostazioniAccount,
                                 relief="flat",
                                 bg="#F3F3F3",
                                 bd=0,
                                 text="←",
                                 width=3,
                                 height=1,
                                 activebackground="#F3F3F3",
                                 takefocus= False,
                                 command=HomeDaImposta)
    #Fine impostazioni dichiara
    #Inizio importa dichiara
    SpazioImportaAccount= Canvas(SchermataImporta,
                                 bg="#FDFDFD",
                                 bd=1,
                                 highlightbackground="#F3F3F3",
                                 highlightcolor="#F3F3F3")
    ScrittaImportaIntroduzione= Label(SpazioImportaAccount,
                                      text="Importa credenziali",
                                      bg="#FDFDFD",
                                      font="helvetica 15")
    CercaAccountDaListaImporta=  Entry(SpazioImportaAccount,
                                       relief="groove",
                                       selectforeground="#F3F3F3",
                                       selectbackground="black",
                                       disabledforeground="#606060",
                                       width=20,
                                       bg="#F3F3F3",
                                       font="helvetica 15")
    BottoneImportaCred= Button(SpazioImportaAccount,
                               relief="flat",
                               bd=0,
                               bg="#F3F3F3",
                               text="Importa",
                               width=20,
                               height=2,
                               activebackground="#F3F3F3",
                               takefocus= False,
                               command=ImportaCredenzialiComando)
    BottoneMenuImporta= Button(SpazioImportaAccount,
                               relief="flat",
                               bg="#F3F3F3",
                               text="←",
                               bd=0,
                               width=3,
                               height=1,
                               activebackground="#F3F3F3",
                               takefocus= False,
                               command=MenuImportaComando)
    ScrittaCercaAccountImporta= Label(SpazioImportaAccount,
                                      text="Inserisci il nome del file (CSV):",
                                      bg="#FDFDFD",
                                      font="helvetica 12")
    CredenzialiImportate= Label(SpazioImportaAccount,
                                text="File importato!",
                                bg="#FDFDFD",
                                fg="green")
    CredenzialiErroreImportazioneFileNonValido= Label(SpazioImportaAccount,
                                                      text="File non valido!",
                                                      bg="#FDFDFD",
                                                      fg="red")
    CredenzialiErroreImportazione= Label(SpazioImportaAccount,
                                         text="File non trovato!",
                                         bg="#FDFDFD",
                                         fg="red")
    BottoneImportaNuoveCredenziali= Button(SpazioImportaAccount,
                                           relief="flat",
                                           bd=0,
                                           bg="#F3F3F3",
                                           text="Importa altro",
                                           width=20,
                                           height=2,
                                           activebackground="#F3F3F3",
                                           takefocus= False,
                                           command=ImportaAltreCredenzialiComando)
    #Fine importa dichiara
    #Inizio cambia password di accesso dichiara
    SpazioModificaPassAccesso= Canvas(SchermataCambiaPassAccesso,
                                      bg="#FDFDFD",
                                      bd=1,
                                      highlightbackground="#F3F3F3",
                                      highlightcolor="#F3F3F3")
    ScrittaIntroduzioneLogInMod= Label(SpazioModificaPassAccesso,
                                       text="Modifica password",
                                       bg="#FDFDFD",
                                       font="helvetica 15")
    ScrittaInserisciPassMod= Label(SpazioModificaPassAccesso,
                                   text="Inserisci la password:",
                                   bg="#FDFDFD",
                                   font="helvetica 12")
    InserisciPassword1Mod= Entry(SpazioModificaPassAccesso,
                                 relief="groove",
                                 selectforeground="#F3F3F3",
                                 selectbackground="black",
                                 disabledforeground="#606060",
                                 width=20,
                                 bg="#F3F3F3",
                                 font="helvetica 15")
    ScrittaInserisciPass2Mod= Label(SpazioModificaPassAccesso,
                                    text="Conferma la password:",
                                    bg="#FDFDFD",
                                    font="helvetica 12")
    InserisciPassword2Mod= Entry(SpazioModificaPassAccesso,
                                 relief="groove",
                                 selectforeground="#F3F3F3",
                                 selectbackground="black",
                                 disabledforeground="#606060",
                                 width=20,
                                 bg="#F3F3F3",
                                 font="helvetica 15")
    BottoneConfermaMod= Button(SpazioModificaPassAccesso,
                               relief="flat",
                               text="Modifica",
                               bg="#F3F3F3",
                               bd=0,
                               width=20,
                               height=2,
                               disabledforeground="#606060",
                               activebackground="#F3F3F3",
                               takefocus= False,
                               command=ConfermaModificaPass)
    BottoneMenuMod= Button(SpazioModificaPassAccesso,
                           relief="flat",
                           bg="#F3F3F3",
                           text="←",
                           bd=0,
                           width=3,
                           height=1,
                           activebackground="#F3F3F3",
                           takefocus= False,
                           command=BottoneMenuModifica)
    PassModificataScrittaMod= Label(SpazioModificaPassAccesso,
                                    text="Password modificata!",
                                    bg="#FDFDFD",
                                    fg="green")
    ScrittaErroreErrataMod= Label(SpazioModificaPassAccesso,
                                  text="Password non valida",
                                  bg="#FDFDFD",
                                  fg="red")
    ScrittaErroreDiverseMod= Label(SpazioModificaPassAccesso,
                                   text="Le password non coincidono!",
                                   bg="#FDFDFD",
                                   fg="red")
    ScrittaErroreVuotoMod= Label(SpazioModificaPassAccesso,
                                 text="Devi inserire una password!",
                                 bg="#FDFDFD",
                                 fg="red")
    #Fine cambia password di accesso dichiara
    #Inizio informazioni dichiara
    SpazioInformazioni= Canvas(SchermataInformazioni,
                               bg="#FDFDFD",
                               bd=1,
                               highlightbackground="#F3F3F3",
                               highlightcolor="#F3F3F3")
    SpazioBottoniInfo= Canvas(SpazioInformazioni,
                              width=400,
                              height=29,
                              bg="#F3F3F3",
                              bd=-2)
    BottoniInfoCerchio1= SpazioBottoniInfo.create_oval(141, 6,
                                                       159, 24,
                                                       width=3,
                                                       fill="#F3F3F3",
                                                       outline="#FDFDFD")
    BottoniInfoCerchio2= SpazioBottoniInfo.create_oval(191, 6,
                                                       209, 24,
                                                       width=3,
                                                       fill="#FDFDFD",
                                                       outline="#FDFDFD")
    BottoniInfoCerchio3= SpazioBottoniInfo.create_oval(241, 6,
                                                       259, 24,
                                                       width=3,
                                                       fill="#FDFDFD",
                                                       outline="#FDFDFD")
    BottoneAvanti= Button(SpazioInformazioni,
                          relief="flat",
                          font="helvetica 13 bold",
                          bg="#F3F3F3",
                          text="→",
                          bd=0,
                          width=3,
                          height=1,
                          activebackground="#F3F3F3",
                          command=InfoAvantiComando)
    BottoneIndietro= Button(SpazioInformazioni,
                            relief="flat",
                            font="helvetica 13 bold",
                            bg="#F3F3F3",
                            text="←",
                            bd=0,
                            width=3,
                            height=1,
                            activebackground="#F3F3F3",
                            command=InfoIndietroComando)
    ScrittaTitoloInfoEsporta= Label(SpazioInformazioni,
                                    text="Info esportazione credenziali",
                                    bg="#FDFDFD",
                                    font="Times 18 bold")   
    ScrittaInfoEsporta= Label(SpazioInformazioni,
                              justify=LEFT,   
                              text="Procedura:\n        Dopo esserti recato sull'apposita schermata premi il\n        pulsante \"Esporta credenziali\".\n\nFunzione:\n        Una volta premuto il pulsante, sul desktop verrà creato un\n        file CSV (Password Gestore.csv). Il pulsante verrà quindi\n        disattivato fino a quando non saranno aggiunte nuove\n        credenziali.",
                              bg="#FDFDFD",
                              font="helvetica 12")
    ScrittaTitoloInfoImporta= Label(SpazioInformazioni,
                                    text="Info importazione credenziali",
                                    bg="#FDFDFD",
                                    font="Times 18 bold")        
    ScrittaInfoImporta= Label(SpazioInformazioni,
                              justify=LEFT,   
                              text="Procedura:\n        Dopo esserti recato sull'apposita schermata premi il\n        pulsante \"Importa credenziali\".\n\nFunzione:\n        Una volta premuto il pulsante, ti verrà chiesto il nome del\n        file CVS da cui importare le credenziali (il file deve essere\n        situato sul desktop).\n",
                              bg="#FDFDFD",
                              font="helvetica 12")
                                
    ScrittaTitoloInfoGenerale= Label(SpazioInformazioni,
                                     text="Info generali e suggerimenti",
                                     bg="#FDFDFD",
                                     font="Times 18 bold")   
    ScrittaInfoGenerale= Label(SpazioInformazioni,
                               justify=LEFT,   
                               text="Suggerimenti:\n        Puoi utilizzare alcuni pulsanti con i tasti \"Invio\" ed \"Esc\".\n        Usa\"Canc\" eliminare la selezione da un qualunque widget.",
                               bg="#FDFDFD",
                               font="helvetica 12")
    ScrittaFineEmanueleCiotola= Label(SpazioInformazioni,
                                      text="Software utilizzabile gratuitamente.\nÈ severamente vietato estrarre o modificare il codice sorgente.\n\nVersione: 2.0        Sviluppato da: Emanuele Ciotola\n",
                                      bg="#FDFDFD",
                                      font="helvetica 12")
    #Fine informazioni dichiara
    #Inizio cerca account dichiara
    SpazioCercaAccount= Canvas(SchermataCercaAccount,
                               bg="#FDFDFD",
                               bd=1,
                               highlightbackground="#F3F3F3",
                               highlightcolor="#F3F3F3")
    SpazioCercaPrimaDellaEntry= Label(SpazioCercaAccount, bg="#FDFDFD")
    CercaAccEntry=  Entry(SpazioCercaAccount,
                          relief="flat",
                          selectforeground="#F3F3F3",
                          selectbackground="black",
                          disabledforeground="#606060",
                          width=26,
                          bg="#F3F3F3",
                          font="hlevetica 13")
    CercaBottoneIcona= Canvas(SpazioCercaAccount,
                              width=25,
                              height=25,
                              bg="#FDFDFD",
                              highlightbackground="#FDFDFD")
    CercaBottoneIcona= Button(SpazioCercaAccount,
                              relief="flat",
                              bg="#FDFDFD",
                              bd=0,
                              activebackground="#FDFDFD",
                              takefocus= False,
                              image=ImmagineBottoneCerca,
                              command=CercaAccountComando)
    CercaErroreNonTrovato= Label(SpazioCercaAccount,
                                 text="Nessun account con questo nome!",
                                 bg="#FDFDFD")
    CercaErroreNonScritto= Label(SpazioCercaAccount,
                                 text="Inserisci il nome dell'account che vuoi cercare!",
                                 bg="#FDFDFD")
    #Fine cerca account dichiara
    #Inizio visualizzazione specifica dichiara
    SpazioVisSpecifica= Canvas(SchermataVisualizzazioneSpecifica,
                               bg="#FDFDFD",
                               bd=1,
                               highlightbackground="#F3F3F3",
                               highlightcolor="#F3F3F3")
    BottoneIndietroVisSpec= Button(SpazioVisSpecifica,
                                   relief="flat",
                                   bg="#F3F3F3",
                                   bd=0,
                                   text="←",
                                   width=3,
                                   height=1,
                                   activebackground="#F3F3F3",
                                   takefocus= False,
                                   command=IndietroVisSpecificaComando)
    ModificaBottoneIcona= Button(SpazioVisSpecifica,
                                 relief="flat",
                                 bg="#F3F3F3",
                                 bd=0,
                                 activebackground="#F3F3F3",
                                 takefocus= False,
                                 image=ImmagineBottoneModifica,
                                 command=ModificaAccountSpecifico)
    ScrittaIntroduzioneVisSpecifica= Label(SpazioVisSpecifica,
                                           text="Visualizza credenziali",
                                           bg="#FDFDFD",
                                           font="helvetica 15")
    ScrittaVisSpecificaNome= Label(SpazioVisSpecifica,
                                   text="Nome account:",
                                   bg="#FDFDFD",
                                   font="helvetica 12")
    ScrittaVisSpecificaMail= Label(SpazioVisSpecifica,
                                   text="Indirizzo mail:",
                                   bg="#FDFDFD",
                                   font="helvetica 12")
    ScrittaVisSpecificaPass= Label(SpazioVisSpecifica,
                                   text="Password:",
                                   bg="#FDFDFD",
                                   font="helvetica 12")
    Linea1= SpazioVisSpecifica.create_line(140, 71,
                                               361, 71,
                                               width=2,
                                               fill="#FDFDFD")
    Linea2= SpazioVisSpecifica.create_line(140, 109,
                                           361, 109,
                                           width=2,
                                           fill="#FDFDFD")
    Linea3= SpazioVisSpecifica.create_line(140, 147,
                                           361, 147,
                                           width=2,
                                           fill="#FDFDFD")
    VisSpecificaNome=  Entry(SpazioVisSpecifica,
                             relief="groove",
                             selectforeground="#FDFDFD",
                             selectbackground="black",
                             disabledforeground="black",
                             disabledbackground= "#FDFDFD",
                             width=20,
                             bg="#FDFDFD",
                             bd=0,
                             font="helvetica 14")
    VisSpecificaMail=  Entry(SpazioVisSpecifica,
                             relief="groove",
                             selectforeground="#FDFDFD",
                             selectbackground="black",
                             disabledforeground="black",
                             disabledbackground= "#FDFDFD",
                             width=20,
                             bg="#FDFDFD",
                             bd=0,
                             font="helvetica 14")
    VisSpecificaPass=  Entry(SpazioVisSpecifica,
                             relief="groove",
                             selectforeground="#FDFDFD",
                             selectbackground="black",
                             disabledforeground="black",
                             disabledbackground= "#FDFDFD",
                             width=20,
                             bg="#FDFDFD",
                             bd=0,
                             font="helvetica 14")
    BottoneConfermaModAcc= Button(SpazioVisSpecifica,
                                  relief="flat",
                                  text="✓",
                                  bg="#F3F3F3",
                                  bd=0,
                                  width=3,
                                  height=1,
                                  disabledforeground="#606060",
                                  activebackground="#F3F3F3",
                                  takefocus= False,
                                  command=ConfermaModificaAccountSpecifico)
    BottoneAnnullaModAcc= Button(SpazioVisSpecifica,
                                  relief="flat",
                                  text="\u274C",
                                  bg="#F3F3F3",
                                  bd=0,
                                  width=3,
                                   height=1,
                                  disabledforeground="#606060",
                                  activebackground="#F3F3F3",
                                  takefocus= False,
                                  command=AnnullaModificaAccountSpecifico)
    BottoneEliminaAccountSpecifica= Button(SpazioVisSpecifica,
                                           relief="flat",
                                           text="Elimina account",
                                           bg="#F3F3F3",
                                           bd=0,
                                           width=20,
                                           height=2,
                                           disabledforeground="#606060",
                                           activebackground="#F3F3F3",
                                           takefocus= False,
                                           command=EliminaAccountSpecificaComando)
    BottoneEliminaAccountSpecificaConferma= Button(SpazioVisSpecifica,
                                                   relief="flat",
                                                   text="Premi per confermare",
                                                   bg="#F3F3F3",
                                                   bd=0,
                                                   width=20,
                                                   height=2,
                                                   disabledforeground="#606060",
                                                   activebackground="#F3F3F3",
                                                   takefocus= False,
                                                   command=EliminaAccountSpecificaConfermaComando)
    #Fine visualizzazione specifica dichiara

    #Inizia schermata home posiziona
    BottoneGest.grid(row=0, column=0, padx=270, pady=1, sticky=N)
    AggiungiBottone.grid(row=0, column=1, padx=5, pady=5, sticky=N)
    CercaBottone.grid(row=0, column=3, padx=5, pady=5, sticky=N)
    ImpostazioniBottone.grid(row=0, column=4, padx=5, pady=5, sticky=N)
    InfoBottone.grid(row=0, column=5, padx=5, pady=5, sticky=N)
    #Fine schermata home posiziona
    #Inizio aggiungi posiziona
    SpazioAggiungiNuovoAccount.grid(row=0, pady=0)
    ScrittaIntroduzioneNuovo.grid(padx=5, pady=5)
    BottoneHomeAggiungi.grid(row=0, sticky="NW")
    ScrittaInserisciNome.grid(padx=15)
    InserisciNome.grid(padx=15, pady=5)
    ScrittaInserisciMail.grid(padx=15)
    InserisciMail.grid(padx=15, pady=5)
    ScrittaInserisciPass.grid(padx=15)
    InserisciPass.grid(padx=15, pady=5)
    BottoneConfermaCredenziali.grid(padx=5, pady=10)
    #Fine aggiungi posiziona
    #Inizio Impostazioni posiziona
    SpazioImpostazioniAccount.grid(row=0, pady=0)
    ScrittaImposta.grid(padx=15, pady=5)
    BottoneHomeDaImposta.grid(row=0, column=0, pady=0, padx=0, sticky="NW")
    BottoneEsportaPassword.grid()
    BottoneImportaPassword.grid(padx=15, pady=5)
    BottoneModificaPass.grid()
    BottoneEliminaTutto.grid(padx=15, pady=5)
    file2= open(TrovaDocumenti, "r").readlines()
    if len(file2) < 4:
        BottoneEsportaPassword.config(state=DISABLED)
        BottoneEliminaTutto.config(state=DISABLED)
    else:
        BottoneEsportaPassword.config(state=NORMAL)
        BottoneEliminaTutto.config(state=NORMAL)
    #Fine impostazioni posiziona
    #Inizio importa posiziona
    SpazioImportaAccount.grid(row=0, pady=0)
    BottoneMenuImporta.grid(row=0, column=0, pady=0, padx=0, sticky="NW")
    ScrittaImportaIntroduzione.grid(row=0, column=0, padx=15, pady=3)
    ScrittaCercaAccountImporta.grid(row=1, column=0, padx=15, pady=5)
    CercaAccountDaListaImporta.grid(row=2, column=0, padx=15)
    BottoneImportaCred.grid(row=4, column=0, padx=15, pady=10)
    #Fine importa posiziona
    #Inizio cambia password di accesso posiziona
    SpazioModificaPassAccesso.grid(row=0, pady=0)
    BottoneMenuMod.grid(row=0, column=0, pady=0, padx=0, sticky="NW")
    ScrittaIntroduzioneLogInMod.grid(row=0, column=0, padx=15, pady=3)
    ScrittaInserisciPassMod.grid(row=1, column=0, padx=15, pady=5)
    InserisciPassword1Mod.grid(row=2, column=0, padx=15)
    ScrittaInserisciPass2Mod.grid(row=3, column=0, padx=15, pady=5)
    InserisciPassword2Mod.grid(row=4, column=0, padx=15)
    BottoneConfermaMod.grid(row=6, column=0, pady=10)
    #Inizio cambia password di accesso posiziona
    #Inizio informazioni posiziona
    SpazioInformazioni.grid(row=0, pady=0)
    SpazioBottoniInfo.grid(row=3, sticky="S")
    BottoneAvanti.grid(row=3, column=0, pady=0, padx=0, sticky="SE")
    BottoneIndietro.grid(row=3, column=0, pady=0, padx=0, sticky="SW")
    #Fine informazioni posiziona
    #Inizio cerca account posiziona
    SpazioCercaAccount.grid(row=0, sticky="N")
    SpazioCercaPrimaDellaEntry.grid(row=0, column=0, padx=2, pady=5)
    CercaAccEntry.grid(row=0, column=1, pady=5)
    CercaBottoneIcona.grid(row=0, column=2, padx=2, ipadx=2)
    #Fine cerca account posiziona
    #Inizio visualizzazione specifica posiziona
    SpazioVisSpecifica.grid(row=0, pady=0)
    BottoneIndietroVisSpec.grid(row=0, column=0, pady=0, padx=0, sticky="NW")
    ModificaBottoneIcona.grid(row=0, column=1, pady=0, ipadx=4, ipady=2, sticky="NE")
    ScrittaIntroduzioneVisSpecifica.grid(row=0, columnspan=2, padx=15, pady=5)
    ScrittaVisSpecificaNome.grid(row=1, padx=10, pady=7, sticky="W")
    VisSpecificaNome.grid(row=1, column=1, pady=7, padx=10)
    ScrittaVisSpecificaMail.grid(row=2, padx=10, pady=7, sticky="W")
    VisSpecificaMail.grid(row=2, column=1, pady=7, padx=10)
    ScrittaVisSpecificaPass.grid(row=3, padx=10, pady=7, sticky="W")
    VisSpecificaPass.grid(row=3, column=1, pady=7, padx=10)
    #Fine visualizzazione specifica posiziona

#Inizio registra/entra/errore
    if RoL == "l":
        ScrittaIntroduzioneLogIn= Label(SchermataLogRegErr,
                                        text="Per continuare esegui il Login!",
                                        width=27,
                                        height=1,
                                        bg="#FDFDFD",
                                        font="helvetica 15")
        ScrittaInserisciPass= Label(SchermataLogRegErr,
                                    text="Inserisci la password:",
                                    width=27,
                                    height=1,
                                    bg="#FDFDFD",
                                    font="helvetica 12")
        InserisciPassword=  Entry(SchermataLogRegErr,
                                  relief="groove",
                                  selectforeground="#F3F3F3",
                                  selectbackground="black",
                                  width=20,
                                  bg="#F3F3F3",
                                  font="helvetica 15",
                                  show="*")
        ScrittaErroreErrata= Label(SchermataLogRegErr,
                                   text="La password è errata!",
                                   bg="#FDFDFD",
                                   fg="red")
        ScrittaErroreVuoto= Label(SchermataLogRegErr,
                                  text="Devi inserire una password!",
                                  bg="#FDFDFD",
                                  fg="red")
        BottoneConferma= Button(SchermataLogRegErr,
                                relief="flat",
                                bg="#F3F3F3",
                                text="Accedi",
                                width=20,
                                bd=0,
                                height=2,
                                activebackground="#F3F3F3",
                                takefocus= False,
                                command=ConfermaRegistrazione)

        ScrittaIntroduzioneLogIn.grid(row=0, column=0, columnspan=3, pady=5, padx=5)
        ScrittaInserisciPass.grid(row=1, column=1)
        InserisciPassword.grid(row=2, column=1, pady=5, padx=5)
        InserisciPassword.focus()
        BottoneConferma.grid(row=4, column=1, pady=5)
        SchermataLogRegErr.grid(row=0, column=0)
    else:
        ScrittaIntroduzioneLogIn= Label(SchermataLogRegErr,
                                        text="Per continuare devi registrarti!",
                                        width=27,
                                        height=1,
                                        bg="#FDFDFD",
                                        font="helvetica 15")
        ScrittaInserisciPass= Label(SchermataLogRegErr,
                                    text="Inserisci una password:",
                                    width=27,
                                    height=1,
                                    bg="#FDFDFD",
                                    font="helvetica 12")
        InserisciPassword=  Entry(SchermataLogRegErr,
                                  relief="groove",
                                  selectforeground="#F3F3F3",
                                  selectbackground="black",
                                  width=20,
                                  bg="#F3F3F3",
                                  font="helvetica 15")
        ScrittaInserisciPass2= Label(SchermataLogRegErr,
                                     text="Conferma la password:",
                                     width=27,
                                     height=1,
                                     bg="#FDFDFD",
                                     font="helvetica 12")
        InserisciPassword2=  Entry(SchermataLogRegErr,
                                   relief="groove",
                                   selectforeground="#F3F3F3",
                                   selectbackground="black",
                                   width=20,
                                   bg="#F3F3F3",
                                   font="helvetica 15")
        ScrittaErroreErrata= Label(SchermataLogRegErr,
                                   text="Password non valida",
                                   bg="#FDFDFD",
                                   fg="red")
        ScrittaErroreDiverse= Label(SchermataLogRegErr,
                                    text="Le password non coincidono!",
                                    bg="#FDFDFD",
                                    fg="red")
        ScrittaErroreVuoto= Label(SchermataLogRegErr,
                                  text="Devi inserire una password!",
                                  bg="#FDFDFD",
                                  fg="red")
        BottoneConferma= Button(SchermataLogRegErr,
                                relief="flat",
                                bg="#F3F3F3",
                                text="Registrati",
                                width=20,
                                bd=0,
                                height=2,
                                activebackground="#F3F3F3",
                                takefocus= False,
                                command=ConfermaRegistrazione)
        
        ScrittaIntroduzioneLogIn.grid(row=0, column=0, columnspan=3, pady=5, padx=5)
        ScrittaInserisciPass.grid(row=1, column=1)
        InserisciPassword.grid(row=2, column=1, pady=5, padx=5)
        InserisciPassword.focus()
        ScrittaInserisciPass2.grid(row=3, column=1)
        InserisciPassword2.grid(row=4, column=1, pady=5, padx=5)
        BottoneConferma.grid(row=6, column=1, pady=5)
        SchermataLogRegErr.grid(row=0, column=0)
else:
    window.geometry("313x213")
    ScrittaErroreConnessione= Label(window,
                                       text="Durante il primo avvio\nil progrmma necessita una\nconnessione internet!\nDopo aver connesso il\ndispositivo a internet\nriavvia il programma\nper continuare.",
                                       bg="#FDFDFD",
                                       fg="red",
                                       font="Helvetica 18")
    ScrittaErroreConnessione.grid(row=0, column=0, pady=8, padx=11)
#Fine registra/entra/errore




def _on_mousewheel(event):
    VerificaScrollPresenzaCredenziali= open(TrovaDocumenti, "r").readlines()
    NomeFrameAttualeScroll= str(SchermataPrincipaleElementi.grid_slaves())
    NomeFrameAttualeScroll2= str(window.grid_slaves())
    if len(VerificaScrollPresenzaCredenziali) > 24 and NomeFrameAttualeScroll2 != "[<tkinter.Frame object .!frame>]" and NomeFrameAttualeScroll == "[]" or NomeFrameAttualeScroll == "[<tkinter.Frame object .!frame2.!frame4.!frame2>]":
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
def myfunction(event):
       canvas.configure(scrollregion=canvas.bbox("all"), width=200, height=200, bg="#FDFDFD")    
def RimuoviFocus(event):
    window.focus()
    print(canvas.grid_slaves())
def EseguiAzioneTastoInvio(event):
    global TastoIndietroAvanti1o2
    NomeFrameAttuale= str(SchermataPrincipaleElementi.grid_slaves())
    if NomeFrameAttuale == "[]" and BottoneConfermaNonPremere == "Premi":
        BottoneConferma.invoke()
    elif NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame>]":
        NomeFrameAttuale= str(SpazioAggiungiNuovoAccount.grid_slaves())
        global BottoneAggiungiOppureAggiungiAltroOppureHoCapito
        if BottoneAggiungiOppureAggiungiAltroOppureHoCapito == "Aggiungi":
            BottoneConfermaCredenziali.invoke()
        elif BottoneAggiungiOppureAggiungiAltroOppureHoCapito == "AggiungiAltro":
            BottoneAltreCredenziali.invoke()
        elif BottoneAggiungiOppureAggiungiAltroOppureHoCapito == "HoCapito":
            BottoneRiscriviCredenziali.invoke()
    elif NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame2>]":
        CercaBottoneIcona.invoke()
    elif NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame5>]":
        if TastoIndietroAvanti1o2 % 2 == 0:
            BottoneImportaCred.invoke()
        elif TastoIndietroAvanti1o2 % 2 != 0:
            BottoneImportaNuoveCredenziali.invoke()
    elif NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame6>]":
        global NonCambiarePass
        if NonCambiarePass == "Cambia":
            BottoneConfermaMod.invoke()
    elif NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame7>]":
        if TastoIndietroAvanti1o2 % 2 == 0:
            ModificaBottoneIcona.invoke()
        elif TastoIndietroAvanti1o2 % 2 != 0:
            BottoneConfermaModAcc.invoke()
def TornaIndietroTastoEsc(event):
    NomeFrameAttuale= str(SchermataPrincipaleElementi.grid_slaves())
    if NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame>]":
        BottoneHomeAggiungi.invoke()
    elif NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame2>]":
        BottoneGest.invoke()
    elif NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame3>]":
        BottoneHomeDaImposta.invoke()
    elif NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame4>]":
        BottoneGest.invoke()
    elif NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame5>]":
        BottoneMenuImporta.invoke()
    elif NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame6>]":
        BottoneMenuMod.invoke()
    elif NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame7>]":
        global TastoIndietroAvanti1o2
        if TastoIndietroAvanti1o2 % 2 == 0:
            BottoneIndietroVisSpec.invoke()
        elif TastoIndietroAvanti1o2 % 2 != 0:
            BottoneAnnullaModAcc.invoke()
def IndietroConFreccia(event):
    NomeFrameAttuale= str(SchermataPrincipaleElementi.grid_slaves())
    if NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame4>]":
        global ContatoreInformazioni
        if ContatoreInformazioni != 0:
            BottoneIndietro.invoke()
            window.focus()
def AvantiConFreccia(event):
    NomeFrameAttuale= str(SchermataPrincipaleElementi.grid_slaves())
    if NomeFrameAttuale == "[<tkinter.Frame object .!frame2.!frame4.!frame4>]":
        BottoneAvanti.invoke()
        window.focus()

canvas.bind_all("<MouseWheel>", _on_mousewheel)
window.bind("<Delete>", RimuoviFocus)
window.bind("<Return>", EseguiAzioneTastoInvio)
window.bind("<Escape>", TornaIndietroTastoEsc)
window.bind("<Left>", IndietroConFreccia)
window.bind("<Right>", AvantiConFreccia)

window.mainloop()
