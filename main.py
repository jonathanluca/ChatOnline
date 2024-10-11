# Tela incial
    # Titulo: Hashzap
    # Botão: Iniciar chat
        # Quando clicar no Botão: abrir um popup/Modal/alerta
            # Titulo: Bem vindo ao Haszap
            # Caixa de texto: Escreva seu nome no chat
            # Botão: Entrar no chat
                # Quando clicar no botão
                # Sumir com o Botão iniciar chat
                    # Carregar chat
                    # Carregar o campo de enviar mensagem: Digite sua mensagem
                    # Botão enviar
                        # Quando clicar no botão enviar
                        # Enviar mensagem
                        # Limpar a caixa de mensagem

# 3 passo para criar um app no flat
# 1° importar o flet
# 2° Criar uma função principal
# 3° Executar essa função

import flet as ft

def main(pagina):
    #titulo
    titulo = ft.Text("Chat virtual")
    
    pagina.add(titulo)
    
    def enviar_mensagem_tunel(mensagem):
        
        texto_tunel = ft.Text(mensagem)
        
        chat.controls.append(texto_tunel)
        
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_msg_chat(evento):
        
        nome_usuario = caixa_nome.value
        
        texto_campo_mensagem = campo_enviar_mensagem.value
        
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        
        #enviar no tunel
        pagina.pubsub.send_all(mensagem)
        
        # Limpar a caixa de enviar msg
        campo_enviar_mensagem.value = ""
        
        pagina.update()
    
    campo_enviar_mensagem = ft.TextField(label = "Digite aqui sua mensagem", on_submit = enviar_msg_chat)
    
    botao_enviar = ft.ElevatedButton("Enviar", on_click = enviar_msg_chat)
    
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])
    
    # para fazer minhas msg aparecer um embaixo da outra
    chat = ft.Column()
    
    def entrar_no_chat(evento):
        
        # fechar o popup
        popup.open = False
            
        # sumir com o titulo
        pagina.remove(titulo)
        
        # sumir com o botão iniciar chat
        pagina.remove(botao)
        
        # carregar chat
        pagina.add(chat)
        
        # carregar o campo de enviar mensagem
        #pagina.add(campo_enviar_mensagem)
        
        # carregar o botão enviar
        pagina.add(linha_enviar)
        
        # adicionar no chat fulano entrou no chat
        nome_usuario = caixa_nome.value
        
        mensagem = f"{nome_usuario} entrou no chat"
        
        pagina.pubsub.send_all(mensagem) 
        
        pagina.update()
    
    # criar popup
    titulo_popup = ft.Text("Bem vindo no meu primeiro site")
    
    caixa_nome = ft.TextField(label = "Digite seu nome", on_submit = entrar_no_chat)
    
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click = entrar_no_chat)
    
    # criando o popup na tela
    popup = ft.AlertDialog(title = titulo_popup, content = caixa_nome, actions = [botao_popup] )
    
    #botão inicial
    def abrir_popup(evento):
        
        pagina.dialog = popup
        
        popup.open = True
        
        pagina.update()        
    
    botao = ft.ElevatedButton("Iniciar chat", on_click = abrir_popup)
    
    pagina.add(botao)
   
#Usar para abrir na wen
#ft.app(main, view=ft.WEB_BROWSER)
ft.app(target = main, view = ft.AppView.WEB_BROWSER)
#ft.app(main)
                
                                