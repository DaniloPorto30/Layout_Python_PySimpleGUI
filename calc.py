from PySimpleGUI import PySimpleGUI as sg

# Layout

sg.theme('LightBlue2')
layout = [
  [sg.Text('Usuario:', text_color="#191970", font=("arial",20)), sg.Input(key='usuario', font=("arial",17) )],
  [sg.Text('Senha:  ', text_color="#191970", font=("arial",20)), sg.Input(key='senha',font=("arial",17), password_char='*')],
  [sg.Checkbox('Salvar o login?',font="arial")],
  [sg.Button('Entrar',font=("arial",16, 'bold'))]
]

# Janela
janela = sg.Window('Tela de Login', layout, size=(560, 180)).read()
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'danilo' and valores['senha']== '123456':
            print('Bem-vindo ao Layout Python!')
        if valores['usuario'] != 'danilo' or valores['senha']!= '123456' or valores['usuario'] == '' or valores['senha']== '':
            print('Falha ao logar!')
      




