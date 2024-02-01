import tkinter as tk
from tkinter import ttk
#from DataBaseConnection import *
######################################
root = tk.Tk()
root.geometry('700x690')
root.title('BDDPROJECT')  # A changer !

# Empecher la redimension de la fenêtre
root.resizable(width=False, height=False)

##########################################################################
# 1. Notre menu :
menu = tk.Frame(root) 
menu.pack()
menu.pack_propagate(False)  # so I can change the width and height below
menu.configure(width=700, height=60)

#switch menu :

def switch(line ,page):
    for child in menu.winfo_children():    #check the children of menu li huma buttons and :
        if isinstance(child,tk.Label):
            child['bg']='SystemButtonFace'

        #verify if it s label then hide
     # Create a new main_fm container
    
    line['bg']='#363062'     #etheir it ll shwo
    for fm in main_fm.winfo_children():
        fm.destroy() #destroy any current page before switching
        root.update()
    page()


    


    
#home
def home_page():
    home_page=tk.Frame(main_fm)
    home_lb=tk.Label(home_page,text=' ACCEUIL ',font=('Impact',15,'bold'), bg='#363062' ,fg='#f5f5f5' ,bd=3)
    home_lb.pack(fill=tk.BOTH , pady=30)
    home_page.pack(fill=tk.BOTH, expand=True) 
    title=tk.Label(home_page ,text="Entrer le titre :",**font_label )
    title.place(x=10 , y=120)
    title_input=tk.Entry(home_page,font=("Bold",13))
    title_input.place(x=120, y=120)
    ###############################
    author=tk.Label(home_page ,text="Entrer l'auteur :",**font_label )
    author.place(x=10 , y=160)
    author_input=tk.Entry(home_page,font=("Bold",13))
    author_input.place(x=130, y=160)
    ####################
    year=tk.Label(home_page ,text="Entrer l'année de publication :",**font_label )
    year.place(x=10 , y=200)
    year_user_input=tk.Entry(home_page,font=("Bold",13))
    year_user_input.place(x=235, y=200)
    #############################
    genre=tk.Label(home_page ,text="Entrer le genre :",**font_label )
    genre.place(x=10 , y=240)
    genre_user_input=tk.Entry(home_page,font=("Bold",13))
    genre_user_input.place(x=135, y=240)  
    ajouter_button=tk.Button(home_page, text='Ajouter', font=("Bold",13) ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d" ,width='10')
    ajouter_button.place(x=10 , y=300 ) 
    afficher_button=tk.Button(home_page, text='Afficher', font=("Bold",13) ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d" ,width='10')
    afficher_button.place(x=120 , y=300 ) 


    
#hachage 
def hachage_page():
    hachage_page=tk.Frame(main_fm)
    heading_lb=tk.Label(hachage_page,text='Algorithme: Hachage' ,font=('Impact',15,'bold'), bg='#363062' ,fg='#f5f5f5' ,bd=3)
    heading_lb.pack( fill=tk.BOTH , pady=30)

    ####
    select_label= tk.Label(hachage_page,text="Choisissez le type de l'algorithme souhaité:  ",**font_label)
    select_label.place(x=40,y=80)
    # Options à afficher dans la combobox
    options = ["Essai lineaire", "Double hachage", "Chaînage séparé", "Chaînage interne"]

    # Variable pour stocker la valeur sélectionnée
    selected_option = tk.StringVar()

    # Créer la combobox
    combo = ttk.Combobox(hachage_page, values=options, textvariable=selected_option , state='readonly'   )
    
    combo.set("Essai lineaire")  # Texte initial
    combo.place( x=40 , y=110)
    def on_select(event ):
        selected_value = combo.get()
        if selected_value == "Essai lineaire":
            combo.set("Essai lineaire")  # Effacer le texte initial lors de la sélection
    # Associer une fonction de rappel à la sélection d'un élément
    combo.bind("<<ComboboxSelected>>", on_select)

    hachage_page.pack(fill=tk.BOTH, expand=True)  
    title=tk.Label(hachage_page ,text="Entrer le titre :",**font_label )
    title.place(x=10 , y=150)
    title_input=tk.Entry(hachage_page,font=("Bold",13))
    title_input.place(x=120, y=150)
    ###############################
    author=tk.Label(hachage_page ,text="Entrer l'auteur :",**font_label )
    author.place(x=10 , y=190)
    author_input=tk.Entry(hachage_page,font=("Bold",13))
    author_input.place(x=130, y=190)
    ####################
    year=tk.Label(hachage_page ,text="Entrer l'année de publication :",**font_label )
    year.place(x=10 , y=230)
    year_user_input=tk.Entry(hachage_page,font=("Bold",13))
    year_user_input.place(x=235, y=230)
    #############################
    genre=tk.Label(hachage_page ,text="Entrer le genre :",**font_label )
    genre.place(x=10 , y=270)
    genre_user_input=tk.Entry(hachage_page,font=("Bold",13))
    genre_user_input.place(x=135, y=270)
    
    ajouter_button=tk.Button(hachage_page, text='Ajouter', font=("Bold",13) ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d" ,width='10')
    ajouter_button.place(x=10 , y=310 ) 
    ###################recherchercher:
    search_frame=tk.Frame(hachage_page)
    search_frame.place(x=100 , y=350)
    search_frame.pack_propagate(False)
    search_frame.configure(width=190 ,height=50 )
    ##
    search_label=tk.Label(search_frame,text='Rechecher par ID :', **font_label)
    search_label.pack(anchor=tk.W)
    search_input=tk.Entry(search_frame, font=("Bold",13))
    search_input.pack(anchor=tk.W)
    rechercher_button=tk.Button(hachage_page, font=("bold",13) ,text='Rechercher' ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d")
    rechercher_button.place(x=290,y=370 )
    delete_button=tk.Button(hachage_page, font=("Bold",13) ,text='Supprimer',bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d")
    delete_button.place(x=395,y=370 )
    modify_button=tk.Button(hachage_page, font=("bold",13) ,text='Modifier' ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d")
    modify_button.place(x=490,y=370 )
    ###ou la base de donnes va s afficher :
    record_frame=tk.Frame(hachage_page)
    record_frame.place(x=25 ,y=410)
    record_frame.pack_propagate(False)
    record_frame.configure(width=650 ,height=220)
    ####
    record_table=ttk.Treeview(record_frame, columns=("h(x)", "Item"), show="headings")
    # Define column headings
    record_table.heading("h(x)", text="h(x)")
    record_table.heading("Item", text="L'ELEMENT")
    # Specify column widths
    record_table.column("h(x)", width=30 )
    record_table.column("Item", width=310)
    record_table.pack(fill=tk.X ) 

#arbres 
def arbre_page():
    arbre_page=tk.Frame(main_fm)
    arbre_lb=tk.Label(arbre_page,text='Algorithme : Les arbres',font=('Impact',15,'bold'),bg='#363062' ,fg='#f5f5f5' ,bd=3 )
    arbre_lb.pack(fill=tk.BOTH , pady=30)
    arbre_page.pack(fill=tk.BOTH, expand=True)  
    #########
    select_label= tk.Label(arbre_page,text="Choisissez le type de l'algorithme souhaité:  ",**font_label)
    select_label.place(x=40 ,y=80)
    options = ["arbre", "arbre"]
    selected_option = tk.StringVar()
    combo = ttk.Combobox(arbre_page, values=options, textvariable=selected_option , state='readonly'   )
    
    combo.set("arbre")  
    combo.place(x=40 , y=110)
    def on_select(event ):
        selected_value = combo.get()
        if selected_value == "Indexe Creux":
            combo.set("Indexe Creux")  
    combo.bind("<<ComboboxSelected>>", on_select) 
    ############
    title=tk.Label(arbre_page ,text="Entrer le titre :",**font_label )
    title.place(x=10 , y=150)
    title_input=tk.Entry(arbre_page,font=("Bold",13))
    title_input.place(x=120, y=150)
    ###############################
    author=tk.Label(arbre_page ,text="Entrer l'auteur :",**font_label )
    author.place(x=10 , y=190)
    author_input=tk.Entry(arbre_page,font=("Bold",13))
    author_input.place(x=130, y=190)
    ####################
    year=tk.Label(arbre_page ,text="Entrer l'année de publication :",**font_label )
    year.place(x=10 , y=230)
    year_user_input=tk.Entry(arbre_page,font=("Bold",13))
    year_user_input.place(x=235, y=230)
    #############################
    genre=tk.Label(arbre_page ,text="Entrer le genre :",**font_label )
    genre.place(x=10 , y=270)
    genre_user_input=tk.Entry(arbre_page,font=("Bold",13))
    genre_user_input.place(x=135, y=270)

    ajouter_button=tk.Button(arbre_page, text='Ajouter', font=("Bold",13) ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d" ,width='10')
    ajouter_button.place(x=10 , y=310 ) 
    ###################recherchercher:
    search_frame=tk.Frame(arbre_page)
    search_frame.place(x=100 , y=350)
    search_frame.pack_propagate(False)
    search_frame.configure(width=190 ,height=50 )
    ##
    search_label=tk.Label(search_frame,text='Rechecher par ID :', **font_label)
    search_label.pack(anchor=tk.W)
    search_input=tk.Entry(search_frame, font=("Bold",13))
    search_input.pack(anchor=tk.W)
    search_button=tk.Button(arbre_page, font=("bold",13) ,text='Rechercher' ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d")
    search_button.place(x=290,y=370 )
    delete_button=tk.Button(arbre_page, font=("Bold",13) ,text='Supprimer',bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d")
    delete_button.place(x=395,y=370 )
    modify_button=tk.Button(arbre_page, font=("bold",13) ,text='Modifier' ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d")
    modify_button.place(x=490,y=370 )
    afficher_button=tk.Button(arbre_page, font=("bold",13) ,text='Afficher' ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d")
    afficher_button.place(x=565,y=370 )
 #indexage            
def indexage_page():
    indexage_page=tk.Frame(main_fm)
    indexage_lb=tk.Label(indexage_page,text='Algorithme : Indexage',font=('Impact',15,'bold'),bg='#363062' ,fg='#f5f5f5' ,bd=3)
    indexage_lb.pack( fill=tk.BOTH , pady=30)
    indexage_page.pack(fill=tk.BOTH, expand=True)
    #########
    select_label= tk.Label(indexage_page,text="Choisissez le type de l'algorithme souhaité:  ",**font_label)
    select_label.place(x=40 ,y=80)
    options = ["Indexe Creux", "Indexe Dense"]
    selected_option = tk.StringVar()
    combo = ttk.Combobox(indexage_page, values=options, textvariable=selected_option , state='readonly'   )
    
    combo.set("Indexe Creux")  
    combo.place(x=40 , y=110)
    def on_select(event ):
        selected_value = combo.get()
        if selected_value == "Indexe Creux":
            combo.set("Indexe Creux")  
    combo.bind("<<ComboboxSelected>>", on_select) 
    #les boutons :
    title=tk.Label(indexage_page ,text="Entrer le titre :",**font_label )
    title.place(x=10 , y=150)
    title_input=tk.Entry(indexage_page,font=("Bold",13))
    title_input.place(x=120, y=150)
    ###############################
    author=tk.Label(indexage_page ,text="Entrer l'auteur :",**font_label )
    author.place(x=10 , y=190)
    author_input=tk.Entry(indexage_page,font=("Bold",13))
    author_input.place(x=130, y=190)
    ####################
    year=tk.Label(indexage_page ,text="Entrer l'année de publication :",**font_label )
    year.place(x=10 , y=230)
    year_user_input=tk.Entry(indexage_page,font=("Bold",13))
    year_user_input.place(x=235, y=230)
    #############################
    genre=tk.Label(indexage_page ,text="Entrer le genre :",**font_label )
    genre.place(x=10 , y=270)
    genre_user_input=tk.Entry(indexage_page,font=("Bold",13))
    genre_user_input.place(x=135, y=270)

    ajouter_button=tk.Button(indexage_page, text='Ajouter', font=("Bold",13) ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d" ,width='10')
    ajouter_button.place(x=10 , y=310 ) 
    ###################recherchercher:
    search_frame=tk.Frame(indexage_page)
    search_frame.place(x=100 , y=350)
    search_frame.pack_propagate(False)
    search_frame.configure(width=190 ,height=50 )
    ##
    search_label=tk.Label(search_frame,text='Rechecher par ID :', **font_label)
    search_label.pack(anchor=tk.W)
    search_input=tk.Entry(search_frame, font=("Bold",13))
    search_input.pack(anchor=tk.W)
    search_button=tk.Button(indexage_page, font=("bold",13) ,text='Rechercher' ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d")
    search_button.place(x=290,y=370 )
    delete_button=tk.Button(indexage_page, font=("Bold",13) ,text='Supprimer',bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d")
    delete_button.place(x=395,y=370 )
    modify_button=tk.Button(indexage_page, font=("bold",13) ,text='Modifier' ,bg='#363062' ,fg="#f5f5f5" ,activebackground="#4d4c7d")
    modify_button.place(x=490,y=370 )
    ###ou la base de donnes va s afficher :
    record_frame=tk.Frame(indexage_page)
    record_frame.place(x=25 ,y=410)
    record_frame.pack_propagate(False)
    record_frame.configure(width=650 ,height=220)
    ####
    record_table=ttk.Treeview(record_frame, columns=("h(x)", "Item"), show="headings")
    # Define column headings
    record_table.heading("h(x)", text="h(x)")
    record_table.heading("Item", text="L'ELEMENT")
    # Specify column widths
    record_table.column("h(x)", width=30 )
    record_table.column("Item", width=310)
    record_table.pack(fill=tk.X ) 
 
   
    
    #########################

                 





# Nos éléments de Menu :#########################################################################
btn_style = {'font': ('Impact', 15), 'bd': 0, 'fg': '#363062', 'activeforeground': '#4d4c7d'}
line_style = {'bg': '#363062'}
font_label={ 'font':("Goudy old style",13 ,'bold')}
######################
home_btn = tk.Button(menu, text='Acceuil', **btn_style , command=lambda: switch(line=home_line ,page=home_page))
home_btn.place(x=0, y=15, width=175)
home_line = tk.Label(menu, **line_style)
home_line.place(x=22, y=50, width=130, height=2)


indexage_btn = tk.Button(menu, text='Indexage', **btn_style, command=lambda: switch(line=indexage_line ,page=indexage_page))
indexage_btn.place(x=175, y=15, width=175)
indexage_line = tk.Label(menu)
indexage_line.place(x=197, y=50, width=130, height=2)

hachage_btn = tk.Button(menu, text='Hachage', **btn_style , command=lambda: switch(line=hachage_line ,page=hachage_page))
hachage_btn.place(x=350, y=15, width=175)
hachage_line = tk.Label(menu)
hachage_line.place(x=372, y=50, width=130, height=2)

Arbres_btn = tk.Button(menu, text='Arbres', **btn_style , command=lambda: switch(line=Arbres_line ,page=arbre_page))
Arbres_btn.place(x=525, y=15, width=175)
Arbres_line = tk.Label(menu)
Arbres_line.place(x=547, y=50, width=130, height=2)
######################################################################################################


main_fm = tk.Frame(root)
main_fm.pack(fill=tk.BOTH, expand=True)
home_page()
root.mainloop()
