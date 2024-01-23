import requests
from deep_translator import GoogleTranslator
import customtkinter

main = customtkinter.CTk()
main.geometry("300x160")
main.title("Consultor do tempo")
main.iconbitmap("nuvem.ico")
titulo = customtkinter.CTkLabel(main,text="Consultor do tempo",font=("Arial",25))
titulo.pack(padx = 10,pady=10)
entrada = customtkinter.CTkEntry(main,placeholder_text="CEP:",width=200,font=("Arial",15))
entrada.pack(padx = 10,pady = 10)
def janeladeerro():
    janela = customtkinter.CTk()
    janela.geometry("300x100")
    janela.title("Consultor do tempo")
    janela.iconbitmap("nuvem.ico")
    lbl = customtkinter.CTkLabel(janela,text="ERRO AO CONSULTAR CEP \n CONFIRA O CEP DIGITADO",font=("Arial",20),text_color="red")
    lbl.pack(padx=10,pady=10)
    janela.mainloop()
def principal():
    try:
        zip_code = entrada.get()
        link = 'https://viacep.com.br/ws/{}/json/'.format(zip_code)
        req = requests.get(link,timeout=3)
        endereco = req.json()
        cidade = endereco['localidade']
        logradouro = endereco['logradouro']
        bairro = endereco['bairro']
        link = 'https://viacep.com.br/ws/{}/json/'.format(zip_code)
        req = requests.get(link,timeout=3)
        endereco = req.json()
        cidade = endereco['localidade']
        logradouro = endereco['logradouro']
        bairro = endereco['bairro']

        api_key = '278701c7e42258b92df4e23adb0cefc8'
        link_api2 = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}"
        requisicao = requests.get(link_api2)
        requisicao_dic = requisicao.json()
        desc = requisicao_dic
        descricao_tempo = desc['weather'][0]['main']
        translated = GoogleTranslator(source='en', target='pt').translate(text=descricao_tempo)
        temperatura_atual = desc['main']['temp']
        temperatura_atual_celcius = temperatura_atual - 273.15
        temperatura_minima = desc['main']['temp_min']
        temperatura_minima_celcius = temperatura_minima - 273.15
        temperatura_maxima = desc['main']['temp_max']
        temperatura_maxima_celcius = temperatura_maxima - 273.15
        informacoes = customtkinter.CTk()
        informacoes.geometry("430x360")
        informacoes.title("Consultor do tempo")
        informacoes.iconbitmap("nuvem.ico")
        label1 = customtkinter.CTkLabel(informacoes,text="Situação atual do tempo: {}".format(translated),font=("Arial",25),text_color="#BFDCFE")
        label1.pack(padx = 10, pady =10)
        label2 = customtkinter.CTkLabel(informacoes,text="Temperatura atual: {:.1f}°C".format(temperatura_atual_celcius),font=("Arial",15),text_color="#048ADE")
        label2.pack(padx = 10, pady =10)
        label3 = customtkinter.CTkLabel(informacoes,text="temperatura mínima: {:.1f}°C".format(temperatura_minima_celcius),font=("Arial",15),text_color="#048ADE")
        label3.pack(padx = 10, pady =10)
        label4 = customtkinter.CTkLabel(informacoes,text="temperatura máxima: {:.1f}°C".format(temperatura_maxima_celcius),font=("Arial",15),text_color="#048ADE")
        label4.pack(padx = 10, pady =10)
        label5 = customtkinter.CTkLabel(informacoes,text="============================================",font=("Arial",15),text_color="#E1011C")
        label5.pack(padx = 10, pady =10)
        label6 = customtkinter.CTkLabel(informacoes,text="Cidade: {}\n Rua: {}\n Bairro: {}".format(cidade,logradouro,bairro),font=("Arial",15),text_color="#E04F66")
        label6.pack(padx=10,pady=10)
        informacoes.mainloop()
    except:
        janeladeerro()

botao = customtkinter.CTkButton(main,text="Consultar",command=principal)
botao.pack()
main.mainloop()


