# VIDEOLINKKI ESITTELYVIDEOON: https://youtu.be/FCb2Rh9wwIw

import tkinter as tk
import threading
import random
import winsound
import time

# KOTI-IKÄVÄ JA PAKOSUUNNITELMA (1 PISTETTÄ)

# Luodaan pääikkuna
ikkuna = tk.Tk()                        # Luodaan pääikkuna
ikkuna.title("Pako autiolta saarelta")  # Asetetaan ikkunalle otsikko
ikkuna.geometry("1200x1200+1300+100")   # Asetetaan ikkunan koko ja sijainti näytöllä
ikkuna.configure(bg='blue')             # Asetetaan taustaväri

# Luodaan saari, mantere ja uintimatka
autiosaari = tk.Canvas(ikkuna, width=300, height=1180, bg='#eab676', highlightthickness=0) # Luodaan autiosaari jonka koko on 300x1200 pikseliä ja taustaväri on vaalean ruskea. Highlightthickness=0 poistaa reunuksen
autiosaari.pack(side=tk.LEFT) # Sijoitetaan autiosaari ikkunan vasempaan reunaan
autiosaari_label = tk.Label(autiosaari, text="Autiosaari", bg='#eab676', fg='black', font=("Helvetica", 20, "bold")) # Luodaan tekstikenttä, jossa lukee "Autiosaari". Taustaväri on vaalean ruskea ja tekstin väri on musta. Fonttikoko on 20 ja boldattu
autiosaari_label.place(x=80, y=5) # Sijoitetaan tekstikenttä autiosaaren yläreunaan

meri = tk.Canvas(ikkuna, width=600, height=1200, bg='blue', highlightthickness=0) # Luodaan meri jonka koko on 600x1200 pikseliä ja taustaväri on sininen. Highlightthickness=0 poistaa reunuksen
meri.pack(side=tk.LEFT) # Sijoitetaan meri saaren oikealle puolelle

mantere = tk.Canvas(ikkuna, width=300, height=1200, bg='green', highlightthickness=0) # Luo mantere jonka koko on 300x1200 pikseliä ja taustaväri on vihreä. Highlightthickness=0 poistaa reunuksen
mantere.pack(side=tk.RIGHT) # Sijoitetaan mantere ikkunan oikeaan reunaan
mantere_label = tk.Label(mantere, text="Mantere", bg='green', fg='black', font=("Helvetica", 20, "bold")) # Luodaan tekstikenttä, jossa lukee "Mantere". Taustaväri on vihreä ja tekstin väri on musta. Fonttikoko on 20 ja boldattu
mantere_label.place(x=90, y=10) # Sijoitetaan tekstikenttä mantereen yläreunaan

# Määritellään apinan askelpituus ja askelten määrä uintimatkaa varten
askeleet = 100      # Apina ui 100 askelta
askel_pituus = 6    # Yksi askel on 6 pikseliä, koska meri on 600 pikseliä leveä

# Funktiot, joilla Ernesti ja Kernesti lähettävät apinan uintimatkalle
def e_laheta_apina():
    print("Ernesti lähetti apinan") # Tulostetaan konsoliin viesti apinan lähettämisestä
    apina_e = meri.create_oval(0, 40, 10, 50, fill="brown") # Luodaan apina. Koordinaatit ovat apinan vasemman yläkulman (ensimmäinen lukupari) ja oikean alakulman (toinen lukupari) koordinaatit
    for i in range(askeleet):       # Toistetaan koodia askelmäärän (100) verran
        meri.move(apina_e, askel_pituus, 0) # Siirretään apinaa yksi askel (6 pikseliä) oikealle
        ikkuna.update()     # Päivitetään ikkuna
        ikkuna.after(10)    # Pieni viive apinan liikkeessä

def k_laheta_apina():
    print("Kernesti lähetti apinan")# Tulostetaan konsoliin viesti apinan lähettämisestä
    apina_k = meri.create_oval(0, 1140, 10, 1150, fill="brown") # Luodaan apina. Koordinaatit ovat apinan vasemman yläkulman (ensimmäinen lukupari) ja oikean alakulman (toinen lukupari) koordinaatit
    for i in range(askeleet):       # Toistetaan koodia askelmäärän (100) verran
        meri.move(apina_k, askel_pituus, 0) # Siirretään apinaa yksi askel oikealle
        ikkuna.update()     # Päivitetään ikkuna
        ikkuna.after(10)    # Pieni viive apinan liikkeessä

# Painikkeiden tyylit (Kysyin ChatGPT:ltä apua painikkeiden tyylittelyyn)
painikkeiden_tyyli = {
    "bg": "#4CAF50",    # Taustaväri
    "fg": "white",      # Tekstin väri
    "font": ("Helvetica", 10, "bold"),
    "activebackground": "#45a049", # Painikkeen aktivoitu väri
    "activeforeground": "white",   # Painikkeen aktivoitu tekstin väri
    "padx": 20,  # Lisätään tyhjää tilaa sivuille
    "pady": 10,  # Lisätään tyhjää tilaa ylös ja alas
    "width": 22  # Asetetaan painikkeille vakio leveys
}

# Luodaan ja sijoitetaan painikkeet
apinan_lahetys_e = tk.Button(ikkuna, text="Ernesti lähettää apinan", command=e_laheta_apina, **painikkeiden_tyyli)  # Luodaan painike, jossa lukee "Ernesti lähettää apinan". Kun painiketta painetaan, suoritetaan funktio e_laheta_apina. Painikkeen tyylit haetaan painikkeiden_tyyli-sanakirjasta
apinan_lahetys_k = tk.Button(ikkuna, text="Kernesti lähettää apinan", command=k_laheta_apina, **painikkeiden_tyyli) # Luodaan painike, jossa lukee "Kernesti lähettää apinan". Kun painiketta painetaan, suoritetaan funktio k_laheta_apina. Painikkeen tyylit haetaan painikkeiden_tyyli-sanakirjasta

apinan_lahetys_e.place(x=40, y=50)      # Sijoitetaan Ernestin painike x-koordinaattiin 40 ja y-koordinaattiin 50
apinan_lahetys_k.place(x=40, y=1120)    # Sijoitetaan Kernestin painike x-koordinaattiin 40 ja y-koordinaattiin 1120

# KOTI-IKÄVÄ JA PAKOSUUNNITELMA (1 PISTETTÄ) PÄÄTTYY TÄHÄN

# APINOIDEN OPETTAMINEN (2 PISTETTÄ) ALKAA TÄSTÄ

# Luodaan hataviesti-sanakirja, jossa on apinoille opetettavat sanat
hataviesti_sanakirja = {
    "sana1": "Ernesti","sana2": "ja","sana3": "Kernesti","sana4": "tässä","sana5": "terve!",
    "sana6": "Olemme","sana7": "autiolla","sana8": "saarella,","sana9": "voisiko","sana10": "joku",
    "sana11": "tulla","sana12": "sieltä","sana13": "sivistyneestä","sana14": "maailmasta","sana15": "hakemaan",
    "sana16": "meidät","sana17": "pois!","sana18": "Kiitos!"   
}

opittu_sana = "" # Alustetaan muuttuja opittu_sana sanojen tallentamista varten

# Luodaan funktio, joka valitsee opittavan sanan satunnaisesti
def valitse_opittu_sana():
    return random.choice(list(hataviesti_sanakirja.values())) # Palautetaan satunnainen sana hataviesti_sanakirjasta

# Ääniefektit

# Ääniefektit uintimatkan aikana
def uinti_aani():
    winsound.Beep(150, 100)     # 150Hz, 100ms äänimerkki

# Ääniefekti apinan saapuessa mantereelle
def saapumis_aani():
    winsound.Beep(1000, 800)    # 1000Hz, 500ms perillä-äänimerkki

def apinan_liikuttaminen(apina, henkilo, callback=None): # Luodaan funktio apinan_liikuttaminen, joka ottaa parametreina apinan, henkilön ja callback-funktion.
    def liikuta_apinaa():
        global opittu_sana # Otetaan käyttöön globaali muuttuja opittu_sana sanojen tallentamista varten
        opittu_sana = valitse_opittu_sana() # Kutsutaan funktiota valitse_opittu_sana ja tallennetaan palautettu sana muuttujaan opittu_sana
        print(f"{henkilo} apinalle opettama sana: {opittu_sana}") # Tulostetaan konsoliin viesti opetetusta sanasta

        for i in range(askeleet):               # Toistetaan koodia askelmäärän (100) verran 
            meri.move(apina, askel_pituus, 0)   # Siirretään apinaa yksi askel oikealle
            uinti_aani()                        # Kutsutaan uinti_aani-funktiota
            ikkuna.after(50, callback)          # Pieni viive ennen seuraavaa askelta
            ikkuna.update()                     # Päivitetään ikkuna
        saapumis_aani()                         # Kutsutaan saapumis_aani-funktiota, kun apina on saapunut mantereelle
        print(f"{henkilo} lähettämä apina saapui mantereelle ja sanoi: {opittu_sana}") # Tulostetaan konsoliin viesti apinan saapumisesta ja siitä, mitä apina sanoi
    threading.Thread(target=liikuta_apinaa).start() # Käynnistetään jokainen liikuta_apinaa funktio omissa säikeissään

def e_laheta_puhuva_apina(): # Luodaan funktio e_laheta_puhuva_apina
    apina_e = meri.create_oval(0, 40, 10, 50, fill="brown") # Luodaan apina Ernestin lähettämänä
    apinan_liikuttaminen(apina_e, "Ernestin", lambda: None) # Kutsutaan funktiota apinan_liikuttaminen, joka ottaa parametreina apinan, henkilön ja callback-funktion

def k_laheta_puhuva_apina(): # Luodaan funktio k_laheta_puhuva_apina
    apina_k = meri.create_oval(0, 1140, 10, 1150, fill="brown") # Luodaan apina Kernestin lähettämänä
    apinan_liikuttaminen(apina_k, "Kernestin", lambda: None)    # Kutsutaan funktiota apinan_liikuttaminen, joka ottaa parametreina apinan, henkilön ja callback-funktion
    
# Luodaan ja sijoitetaan painikkeet
apinan_lahetys_e = tk.Button(ikkuna, text="Ernesti lähettää puhuvan apinan", command=e_laheta_puhuva_apina, **painikkeiden_tyyli)   # Luodaan painike, jossa lukee "Ernesti lähettää puhuvan apinan". Kun painiketta painetaan, suoritetaan funktio e_laheta_puhuva_apina. Painikkeen tyylit haetaan painikkeiden_tyyli-sanakirjasta
apinan_lahetys_k = tk.Button(ikkuna, text="Kernesti lähettää puhuvan apinan", command=k_laheta_puhuva_apina, **painikkeiden_tyyli)  # Luodaan painike, jossa lukee "Kernesti lähettää puhuvan apinan". Kun painiketta painetaan, suoritetaan funktio k_laheta_puhuva_apina. Painikkeen tyylit haetaan painikkeiden_tyyli-sanakirjasta

apinan_lahetys_e.place(x=40, y=100)     # Sijoitetaan Ernestin painike x-koordinaattiin 40 ja y-koordinaattiin 100
apinan_lahetys_k.place(x=40, y=1070)    # Sijoitetaan Kernestin painike x-koordinaattiin 40 ja y-koordinaattiin 1070

# APINOIDEN OPETTAMINEN (2 PISTETTÄ) PÄÄTTYY TÄHÄN

# APINARYHMÄN UINTIMATKA (3 PISTETTÄ) ALKAA TÄSTÄ

# Ääniefektit

# Ääniefektit uintimatkan aikana
def uinti_aani2():
    winsound.Beep(150, 100)     # 150Hz, 100ms äänimerkki

# Ääniefekti hain syödessä apinan
def hain_syonti_aani():
    winsound.Beep(500, 200)     # 500Hz, 200ms hain syönti-äänimerkki

# Ääniefekti apinan saapuessa mantereelle
def saapumis_aani2():
    winsound.Beep(1000, 800)    # 1000Hz, 800ms perillä-äänimerkki

def apinan_liikuttaminen2(apina, henkilo, callback=None):
    global opittu_sana
    opittu_sana = valitse_opittu_sana()
    print(f"Apinalle opetettu sana: {opittu_sana}")

    for i in range(askeleet):
        # Asetetaan 1% mahdollisuus joutua hain syömäksi jokaisella askeleella
        if random.random() < 0.01:              # Jos satunnainen luku on pienempi kuin 0.01, apina joutuu hain syömäksi
            hain_syonti_aani()                  # Kutsutaan hain_syonti_aani-funktiota
            print(f"{henkilo}n apina syötiin!") # Tulostetaan konsoliin viesti apinan syömisestä
            meri.delete(apina)                  # Poistetaan syöty apina merestä
            return                              # Apina syötiin, pysäytetään matka
        
        meri.move(apina, askel_pituus, 0)       # Siirretään apinaa yksi askel oikealle
        uinti_aani2()                           # Kutsutaan uinti_aani2-funktiota
        ikkuna.after(50, callback)              # Pieni viive ennen seuraavaa askelta
        ikkuna.update()                         # Päivitetään ikkuna
    saapumis_aani2()                            # Kutsutaan saapumis_aani2-funktiota, kun apina on saapunut mantereelle
    print(f"{henkilo}n lähettämä apina saapui mantereelle") # Tulostetaan konsoliin viesti apinan saapumisesta

# Luodaan funktio apinoiden lähettämiseksi uintimatkalle
def e_laheta_puhuva_apina2(): 
    apina_e = meri.create_oval(0, 40, 10, 50, fill="brown") # Luodaan apina Ernestin lähettämänä
    apinan_liikuttaminen2(apina_e, "Ernesti", lambda: None) # Kutsutaan funktiota apinan_liikuttaminen2, joka ottaa parametreina apinan, henkilön ja callback-funktion

# Luodaan funktio apinoiden lähettämiseksi uintimatkalle
def k_laheta_puhuva_apina2(): 
    apina_k = meri.create_oval(0, 1140, 10, 1150, fill="brown")
    apinan_liikuttaminen2(apina_k, "Kernesti", lambda: None)

# luodaan Ernestille funktio 10 apinan lähettämiseksi uintimatkalle
def e_laheta_10_apinaa():
    for _ in range(10):     # Toistetaan koodia 10 kertaa
        ikkuna.after(150)   # Pieni viive ennen seuraavaa apinan lähettämistä
        ikkuna.update()     # Päivitetään ikkuna
        threading.Thread(target=e_laheta_puhuva_apina2).start() # Käynnistetään jokainen e_laheta_puhuva_apina2-funktio omissa säikeissään

# luodaan Kernestille funktio 10 apinan lähettämiseksi uintimatkalle
def k_laheta_10_apinaa():
    for _ in range(10):     # Toistetaan koodia 10 kertaa
        ikkuna.after(150)   # Pieni viive ennen seuraavaa apinan lähettämistä
        ikkuna.update()     # Päivitetään ikkuna
        threading.Thread(target=k_laheta_puhuva_apina2).start() # Käynnistetään jokainen k_laheta_puhuva_apina2-funktio omissa säikeissään

apinan_lahetys_10_e = tk.Button(ikkuna, text="Ernesti lähettää 10 apinaa", command=e_laheta_10_apinaa, **painikkeiden_tyyli)    # Luodaan painike, jossa lukee "Ernesti lähettää 10 apinaa". Kun painiketta painetaan, suoritetaan funktio e_laheta_10_apinaa. Painikkeen tyylit haetaan painikkeiden_tyyli-sanakirjasta
apinan_lahetys_10_k = tk.Button(ikkuna, text="Kernesti lähettää 10 apinaa", command=k_laheta_10_apinaa, **painikkeiden_tyyli)   # Luodaan painike, jossa lukee "Kernesti lähettää 10 apinaa". Kun painiketta painetaan, suoritetaan funktio k_laheta_10_apinaa. Painikkeen tyylit haetaan painikkeiden_tyyli-sanakirjasta

apinan_lahetys_10_e.place(x=40, y=150)  # Sijoitetaan Ernestin painike x-koordinaattiin 40 ja y-koordinaattiin 150
apinan_lahetys_10_k.place(x=40, y=1020) # Sijoitetaan Kernestin painike x-koordinaattiin 40 ja y-koordinaattiin 1020

# APINARYHMÄN UINTIMATKA (3 PISTETTÄ) PÄÄTTYY TÄHÄN

# KUMPI EHTII ENSIN? (4 PISTETTÄ) ALKAA TÄSTÄ

#Luodaaan sanakirjat Pohterin ja Eteterin vastaanottamille sanoille
pohterin_vastaanottamat_sanat = {}
eteterin_vastaanottamat_sanat = {}
pelastettu = False # Alustetaan muuttuja pelastettu kilpailun tilan seuraamista varten

# Ääniefektit

# Ääniefektit uintimatkan aikana
def uinti_aani3():
    winsound.Beep(150, 10)     # 150Hz, 100ms äänimerkki

# Ääniefekti apinan saapuessa mantereelle
def saapumis_aani3():
    winsound.Beep(1000, 80)    # 1000Hz, 800ms perillä-äänimerkki

# Luodaaan funktio apinoiden lähettämiseksi kilpailuun
def apinan_liikuttaminen_kilpailu(apina, henkilo, vastaanotetut_sanat): # Luodaan funktio, joka ottaa parametreina apinan, henkilön ja vastaanotetut_sanat-sanakirjan
    opittu_sana = random.choice(list(hataviesti_sanakirja.values()))    # Valitaan opittu sana satunnaisesti hataviesti_sanakirjasta

    for i in range(askeleet):  # Toistetaan koodia askelmäärän (100) verran
        # n. 1% mahdollisuus joutua hain syömäksi jokaisella askeleella
        if random.random() < 0.008: # Jos satunnainen luku on pienempi kuin 0.008, apina joutuu hain syömäksi
            hain_syonti_aani()      # Kutsutaan hain_syonti_aani-funktiota
            print(f"{henkilo}n apina syötiin!") # Tulostetaan konsoliin viesti apinan syömisestä
            meri.delete(apina)  # Poistetaan syöty apina merestä
            return              # Apina syötiin, pysäytetään matka
        if pelastettu:          # Jos kilpailu on jo päättynyt, pysäytetään matka
            meri.delete(apina)  # Poistetaan apina merestä
            return              # Pysäytetään matka
        meri.move(apina, askel_pituus, 0)   # Siirretään apinaa yksi askel oikealle
        uinti_aani3()                        # Kutsutaan uinti_aani-funktiota
        ikkuna.update()                     # Päivitetään ikkuna
        time.sleep(0.001)                    # Pieni viive ennen seuraavaa askelta

    saapumis_aani3()
     # Tallennetaan sana riippuen siitä, kuka lähetti apinan
    if henkilo == "Ernesti":
        pohterin_vastaanottamat_sanat[f"Apina {len(pohterin_vastaanottamat_sanat)+1}"] = opittu_sana # Tallennetaan opittu sana Pohterin vastaanottamien sanojen sanakirjaan
    elif henkilo == "Kernesti":
        eteterin_vastaanottamat_sanat[f"Apina {len(eteterin_vastaanottamat_sanat)+1}"] = opittu_sana

    uniikit_sanat_pohteri = set(pohterin_vastaanottamat_sanat.values())
    uniikit_sanat_eteteri = set(eteterin_vastaanottamat_sanat.values())
    print(f"{henkilo}n apina saapui mantereelle ja sanoi: {opittu_sana}")
    print(f"Pohterin vastaanottamat sanat: {pohterin_vastaanottamat_sanat} ja uniikkien sanojen määrä: {len(uniikit_sanat_pohteri)}" )
    print(f"Eteterin vastaanottamat sanat: {eteterin_vastaanottamat_sanat} ja uniikkien sanojen määrä: {len(uniikit_sanat_eteteri)}" )
    # Tarkistetaan onko Pohteri tai Eteteri saavuttanut yli 10 uniikkia sanaa
    if len(set(pohterin_vastaanottamat_sanat.values())) > 10:
        print("Pohterin vastaanottamien sanojen joukossa on yli 10 uniikkia sanaa.")
        laheta_pelastus_laiva("Ernesti")
    elif len(set(eteterin_vastaanottamat_sanat.values())) > 10:
        print("Eteterin vastaanottamien sanojen joukossa on yli 10 uniikkia sanaa.")
        laheta_pelastus_laiva("Kernesti")
            
def e_laheta_puhuva_apina_kilpailu():
    apina_e = meri.create_oval(0, 40, 10, 50, fill="brown")
    apinan_liikuttaminen_kilpailu(apina_e, "Ernesti", pohterin_vastaanottamat_sanat)

def k_laheta_puhuva_apina_kilpailu():
    apina_k = meri.create_oval(0, 1140, 10, 1150, fill="brown")
    apinan_liikuttaminen_kilpailu(apina_k, "Kernesti", eteterin_vastaanottamat_sanat)

def aloita_kilpailu():
    satamavahti_pohteri = mantere.create_oval(0, 40, 10, 50, fill="black")
    pohteri = tk.Label(ikkuna, text="Pohteri", bg="green", fg="white", font=("Helvetica", 10, "bold"))
    pohteri.place(x=900, y=10)
    satamavahti_eteteri = mantere.create_oval(0, 1140, 10, 1150, fill="white")
    eteteri = tk.Label(ikkuna, text="Eteteri", bg="green", fg="white", font=("Helvetica", 10, "bold"))
    eteteri.place(x=900, y=1160)
    laheta_apinat_kilpailuun()

def laheta_apinat_kilpailuun():
    global pelastettu   # Otetaan käyttöön globaali muuttuja pelastettu kilpailun tilan seuraamista varten
    if not pelastettu:  # Tarkistetaan, ettei kilpailu ole jo päättynyt
        threading.Thread(target=e_laheta_puhuva_apina_kilpailu).start() # Käynnistetään Ernestin apinan lähettäminen kilpailuun omassa säikeessään
        threading.Thread(target=k_laheta_puhuva_apina_kilpailu).start() # Käynnistetään Kernestin apinan lähettäminen kilpailuun omassa säikeessään
    
        # Jos kumpikaan ei ole vielä voittanut, kutsutaan funktiota uudelleen kilpailun jatkamiseksi
        ikkuna.after(2000, laheta_apinat_kilpailuun)

# Luodaan funktio pelastuslaivan lähettämiseksi
def laheta_pelastus_laiva(voittaja):
    global pelastettu  # Otetaan käyttöön globaali muuttuja pelastettu kilpailun tilan seuraamista varten
    if not pelastettu: # Tarkistetaan, ettei kilpailu ole jo päättynyt
        pelastettu = True # Asetetaan pelastettu-muuttuja arvoksi True, jotta kilpailu päättyy
        if voittaja == "Ernesti": # Jos Ernesti voitti kilpailun
            print("Pohteri tulkitsi Ernestin hätäviestin ja lähetti pelastuslaivan") # Tulostetaan konsoliin viesti pelastuslaivan lähettämisestä
            laiva = meri.create_rectangle(550, 40, 600, 50, fill="black") # Luodaan pelastuslaiva
        else: # Jos Kernesti voitti kilpailun
            print("Eteteri tulkitsi Kernestin hätäviestin ja lähetti pelastuslaivan") # Tulostetaan konsoliin viesti pelastuslaivan lähettämisestä
            laiva = meri.create_rectangle(550, 1140, 600, 1150, fill="white") # Luodaan pelastuslaiva
        for i in range(askeleet):   # Lähetetään pelastuslaiva saarelle
            askel_pituus = 5.5      # Asetetaan askel_pituus arvoksi 5.5
            meri.move(laiva, -askel_pituus, 0) # Siirretään pelastuslaivaa askel vasemmalle
            ikkuna.update()         # Päivitetään ikkuna
            ikkuna.after(100)       # Pieni viive ennen seuraavaa askelta
        print(f"Jee! {voittaja} iloitsee, kun hänen hätäviestinsä pääsi ensimmäisenä perille") # Tulostetaan konsoliin viesti voittajan ilosta
        time.sleep(2)               # Pieni viive ennen pelastuslaivan lähettämistä takaisin mantereelle
        for i in range(askeleet):   # Lähetetään pelastuslaiva takaisin mantereelle
            askel_pituus = 5.5      # Asetetaan askel_pituus arvoksi 5.5
            meri.move(laiva, askel_pituus, 0) # Siirretään pelastuslaivaa askel oikealle
            ikkuna.update()         # Päivitetään ikkuna
            ikkuna.after(100)       # Pieni viive ennen seuraavaa askelta
        print("Pelastuslaiva on saapunut mantereelle noudettuaan Ernestin ja Kernestin!")   # Tulostetaan konsoliin viesti pelastuslaivan saapumisesta mantereelle
        laske_juhla_ateria(pohterin_vastaanottamat_sanat, eteterin_vastaanottamat_sanat)    # Kutsutaan funktiota laske_juhla_ateria, joka ottaa parametreina Pohterin ja Eteterin vastaanottamat sanat

# funktio kilpailun nollaamiseksi
def nollaa_kilpailu():
    global pelastettu
    pelastettu = False
    pohterin_vastaanottamat_sanat.clear()
    eteterin_vastaanottamat_sanat.clear()
    
    print("Kilpailu nollattu!")

# Luodaan ja sijoitetaan kilpailupainike
apinan_lahetys_satamavahdille = tk.Button(ikkuna, text="Kilpailu", command=aloita_kilpailu, **painikkeiden_tyyli)   # Luodaan painike, jossa lukee "Kilpailu". Kun painiketta painetaan, suoritetaan funktio aloita_kilpailu. Painikkeen tyylit haetaan painikkeiden_tyyli-sanakirjasta
apinan_lahetys_satamavahdille.place(x=40, y=600) # Sijoitetaan kilpailupainike x-koordinaattiin 40 ja y-koordinaattiin 600

# Luodaan kilpailun nollauspainike
nollaa_kilpailu_painike = tk.Button(ikkuna, text="Nollaa kilpailu", command=nollaa_kilpailu, **painikkeiden_tyyli)  # Luodaan painike, jossa lukee "Nollaa kilpailu". Kun painiketta painetaan, suoritetaan funktio nollaa_kilpailu. Painikkeen tyylit haetaan painikkeiden_tyyli-sanakirjasta
nollaa_kilpailu_painike.place(x=40, y=650) # Sijoitetaan nollaa_kilpailu_painike x-koordinaattiin 40 ja y-koordinaattiin 650

# KUMPI EHTII ENSIN? (4 PISTETTÄ) PÄÄTTYY TÄHÄN

# LOPUKSI ON AIHETTA JUHLAAN (5 PISTETTÄ) ALKAA TÄSTÄ

# Luodaan funktio juhla-aterioiden määrän laskemiseksi, joka ottaa parametreina Pohterin ja Eteterin vastaanottamat sanat
def laske_juhla_ateria(pohterin_vastaanottamat_sanat, eteterin_vastaanottamat_sanat): 
    # Lasketaan kuinka monta sanaa on vastaanotettu
    apinoiden_maara_ernesti = len(pohterin_vastaanottamat_sanat)
    apinoiden_maara_kernesti = len(eteterin_vastaanottamat_sanat)

    # Lasketaan juhla-aterioiden määrä (4 ateriaa per 1 apina)
    juhla_aterioita_ernesti = apinoiden_maara_ernesti * 4
    juhla_aterioita_kernesti = apinoiden_maara_kernesti * 4

    # Lasketaan kuinka paljon mustapippuria kuluu
    mustapippuri_ernesti = apinoiden_maara_ernesti * 2
    mustapippuri_kernesti = apinoiden_maara_kernesti * 2

    # Lasketaan mustapippurin yhteismäärä
    mustapippuri_yhteensa = mustapippuri_ernesti + mustapippuri_kernesti

    # Tulostetaan laskelmat
    print("Juhla-ateria laskelmat:")
    print(f"Ernestin lähettämiä ja uintimatkasta selvinneitä apinoita: {apinoiden_maara_ernesti} kpl")
    print(f"Kernestin lähettämiä ja uintimatkasta selvinneitä apinoita: {apinoiden_maara_kernesti} kpl")
    print(f"Ernestin juhla-aterioita: {juhla_aterioita_ernesti}")
    print(f"Kernestin juhla-aterioita: {juhla_aterioita_kernesti}")
    if juhla_aterioita_ernesti > juhla_aterioita_kernesti:
        print("Ernestillä oli isommat juhlat!")
    elif juhla_aterioita_ernesti < juhla_aterioita_kernesti:
        print("Kernestillä oli isommat juhlat!")
    else:
        print("Ernesti ja Kernesti pitivät yhtä isot juhlat!")
    print(f"Mustapippuria kuluu yhteensä: {mustapippuri_yhteensa} tl")

# Käynnistä ohjelma
ikkuna.mainloop()