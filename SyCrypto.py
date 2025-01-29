import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

def gerar_chave():
    """
    Gera uma nova chave de criptografia e a exibe na caixa de texto da chave.
    """
    chave = Fernet.generate_key()
    chave_text.delete("1.0", tk.END)  # Limpa qualquer texto existente
    chave_text.insert(tk.END, chave.decode())  # Insere a chave decodificada

def criptografar():
    """
    Criptografa o texto de entrada usando a chave fornecida.
    """
    try:
        chave = chave_text.get("1.0", tk.END).strip().encode()  # Obtém a chave e a codifica
        f = Fernet(chave)
        texto_claro = entrada_text.get("1.0", tk.END).strip().encode()
        texto_cifrado = f.encrypt(texto_claro)
        saida_text.delete("1.0", tk.END)
        saida_text.insert(tk.END, texto_cifrado.decode())
    except Exception as e:
        messagebox.showerror("Erro", f"Erro durante a criptografia: {e}")


def descriptografar():
    """
    Descriptografa o texto cifrado usando a chave fornecida.
    """
    try:
        chave = chave_text.get("1.0", tk.END).strip().encode()
        f = Fernet(chave)
        texto_cifrado = entrada_text.get("1.0", tk.END).strip().encode()
        texto_claro = f.decrypt(texto_cifrado)
        saida_text.delete("1.0", tk.END)
        saida_text.insert(tk.END, texto_claro.decode())

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while decrypting: {e}")



# Crie a janela principal
janela = tk.Tk()
janela.title("SyCripto by Sy.bl")

# Rótulos e caixas de texto
chave_label = tk.Label(janela, text="Crypto Key:")
chave_label.grid(row=0, column=0, padx=5, pady=5)
chave_text = tk.Text(janela, height=1, width=50)
chave_text.grid(row=0, column=1, padx=5, pady=5)

gerar_chave_button = tk.Button(janela, text="Generate a Key", command=gerar_chave)
gerar_chave_button.grid(row=0, column=2, padx=5, pady=5)

entrada_label = tk.Label(janela, text="Input:")
entrada_label.grid(row=1, column=0, padx=5, pady=5)
entrada_text = tk.Text(janela, height=5, width=50)
entrada_text.grid(row=1, column=1, padx=5, pady=5)


criptografar_button = tk.Button(janela, text="Encrypt", command=criptografar)
criptografar_button.grid(row=2, column=0, padx=5, pady=5)

descriptografar_button = tk.Button(janela, text="Decrypt", command=descriptografar)
descriptografar_button.grid(row=2, column=1, padx=5, pady=5)


saida_label = tk.Label(janela, text="Output:")
saida_label.grid(row=3, column=0, padx=5, pady=5)
saida_text = tk.Text(janela, height=5, width=50)
saida_text.grid(row=3, column=1, padx=5, pady=5)


janela.mainloop()


