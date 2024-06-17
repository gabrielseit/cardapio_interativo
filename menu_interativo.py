import tkinter as tk
from tkinter import Toplevel, Label
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Dados do cardápio
menu_items = [
    {
        "nome": "Salada Caesar",
        "imagem": "https://www.estadao.com.br/resizer/v2/Z725JFWNVFGX7NC7R3TDIRKVOI.jpeg?quality=80&auth=47f419b219bee557c23c67bb3f7f2fc9ab982b47943dcc4186e766e7bdd0b6b3&width=720&height=503&smart=true",
        "ingredientes": "Alface, frango grelhado, parmesão, croutons, molho Caesar",
        "nutricionais": "Calorias: 220, Proteínas: 10g, Carboidratos: 15g, Gorduras: 15g"
    },
    {
        "nome": "Sopa de Tomate",
        "imagem": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTF7VHb0sP4ZrjFuhzCz36dmdk6A-7znrDjuA&s",
        "ingredientes": "Tomates, alho, cebola, manjericão, azeite",
        "nutricionais": "Calorias: 90, Proteínas: 2g, Carboidratos: 14g, Gorduras: 3g"
    },
    {
        "nome": "Espaguete à Bolonhesa",
        "imagem": "https://img.cybercook.com.br/receitas/610/espaguete-com-molho-a-bolonhesa-ou-ragu-bolognese-1.jpeg",
        "ingredientes": "Espaguete, carne moída, molho de tomate, cebola, alho, manjericão",
        "nutricionais": "Calorias: 350, Proteínas: 20g, Carboidratos: 50g, Gorduras: 10g"
    },
    {
        "nome": "Frango Grelhado",
        "imagem": "https://www.kitano.com.br/wp-content/uploads/2019/07/SSP_2405-File%E2%95%A0%C3%BC-de-frango-grelhado-com-pa%E2%95%A0%C3%BCprica-e-manjerica%E2%95%A0%C3%A2o.jpg",
        "ingredientes": "Peito de frango, azeite, alho, limão, ervas",
        "nutricionais": "Calorias: 200, Proteínas: 25g, Carboidratos: 0g, Gorduras: 10g"
    },
    {
        "nome": "Torta de Maçã",
        "imagem": "https://bunny-wp-pullzone-fg0ugzbnxk.b-cdn.net/wp-content/uploads/2020/11/receita-simples-e-caseira-de-torta-de-maca-1300x932.png",
        "ingredientes": "Maçãs, farinha, açúcar, manteiga, canela",
        "nutricionais": "Calorias: 300, Proteínas: 3g, Carboidratos: 50g, Gorduras: 12g"
    }
]

# Função para exibir informações nutricionais e ingredientes
def show_info(item):
    info_window = Toplevel(root)
    info_window.title(item['nome'])
    
    label_nome = Label(info_window, text=item['nome'], font=("Arial", 18, "bold"))
    label_nome.pack(pady=10)
    
    label_ingredientes = Label(info_window, text="Ingredientes: " + item['ingredientes'], wraplength=300, justify="left")
    label_ingredientes.pack(pady=10)
    
    label_nutricionais = Label(info_window, text="Informações Nutricionais: " + item['nutricionais'], wraplength=300, justify="left")
    label_nutricionais.pack(pady=10)

# Inicializa a janela principal
root = tk.Tk()
root.title("Cardápio Interativo")

# Adiciona os itens do cardápio
for item in menu_items:
    frame = tk.Frame(root, bd=2, relief="groove")
    frame.pack(side="left", padx=10, pady=10)

    response = requests.get(item['imagem'])
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize((200, 150), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    label_img = Label(frame, image=img_tk)
    label_img.image = img_tk  # Evita que a imagem seja coletada pelo garbage collector
    label_img.pack(pady=5)

    button = tk.Button(frame, text=item['nome'], command=lambda item=item: show_info(item))
    button.pack(pady=5)

# Inicia o loop principal do Tkinter
root.mainloop()
