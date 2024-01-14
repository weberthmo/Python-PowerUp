#pip install flet
import flet as ft

def main(pagina):
    texto = ft.Text("HashZap")
    nome_usuario = ft.TextField(label="Escreva seu nome")
    
    def entrar_chat(evento):
        popup.open = False
        pagina.remove(btn_iniciar)
        pagina.update()
        print(nome_usuario.value)
    
    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("HashZap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )
    
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    btn_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    
    pagina.add(texto)
    pagina.add(btn_iniciar)
    
ft.app(main)