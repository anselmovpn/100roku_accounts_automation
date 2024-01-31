import pyautogui as p
import time as t
import pyperclip as py

p.PAUSE = 2
p.press("win")
p.write("chrome")
p.press("enter")
p.hotkey("ctrl","shift","n")

p.write("https://my.roku.com/signup")
p.press("enter")
t.sleep(20)

nomes = ["Bruno", "Carla", "Pedro", "Sofia", "Andre", "Laura", "Lucas", "Maria", "Tiago", "Ines", 
         "Joao", "Rita", "Miguel", "Diana", "Luis", "Paula", "Hugo", "Clara", "Nuno", "Ana", 
         "Marco", "Sara", "Rui", "Catarina", "Alex", "Lidia", "Davi", "Andreia", "Eric", "Jessica", 
         "Tania", "Jose", "Elsa", "Leandro", "Vera", "Filipe", "Bruna", "Igor", "Joaquim", "Tania", 
         "Hugo", "Ines", "Goncalo", "Mariana", "Renato", "Claudia", "Leo", "Marta", "Dylan", "Monica", 
         "Samuel", "Ligia", "Rafael", "Ana", "Paulo", "Rita", "Bruno", "Lara", "Jose", "Beatriz", 
         "Ivan", "Andreia", "Diogo", "Soraia", "Carlos", "Sofia", "Kevin", "Debora", "Andre", "Iara", 
         "Fabio", "Carla", "Rafaela", "Gustavo", "Nadia", "Marco", "Nuria", "Luan", "Leticia", "Hugo", 
         "Vanessa", "Alan", "Paula", "Vitor", "Lara", "Bruno", "Tania", "Henrique", "Alice", "David", 
         "Raquel", "Andre", "Olga", "Ivan", "Celia", "Igor", "Clara", "Duarte"]

sobrenomes = ["Silva", "Santos", "Oliveira", "Pereira", "Costa", "Rodrigues", "Martins", "Ferreira", 
              "Almeida", "Carvalho", "Cardoso", "Nunes", "Goncalves", "Mendes", "Lima", "Sousa", 
              "Castro", "Fernandes", "Ramos", "Pinto", "Alves", "Cunha", "Gomes", "Ribeiro", 
              "Torres", "Baptista", "Barbosa", "Dias", "Martins", "Silva", "Pereira", "Almeida", 
              "Santos", "Carvalho", "Ferreira", "Nunes", "Goncalves", "Lima", "Rodrigues", "Sousa", 
              "Castro", "Fernandes", "Pinto", "Ramos", "Alves", "Cunha", "Gomes", "Ribeiro", "Torres", 
              "Baptista", "Barbosa", "Costa", "Pereira", "Dias", "Oliveira", "Martins", "Silva", 
              "Pereira", "Almeida", "Carvalho", "Ferreira", "Nunes", "Goncalves", "Lima", "Rodrigues", 
              "Sousa", "Castro", "Fernandes", "Pinto", "Ramos", "Alves", "Cunha", "Gomes", "Ribeiro", 
              "Torres", "Baptista", "Barbosa", "Santos", "Costa", "Pereira", "Dias", "Oliveira", 
              "Martins", "Silva", "Pereira", "Almeida", "Carvalho", "Ferreira", "Nunes", "Goncalves", 
              "Lima", "Rodrigues", "Sousa", "Castro", "Fernandes", "Pinto", "Ramos", "Alves", "Cunha", 
              "Gomes", "Ribeiro", "Torres", "Baptista", "Barbosa"]

#estrutura de repetição

numero_repeticoes = 0
while numero_repeticoes < 101:
    i=numero_repeticoes
    p.click(x=582, y=394)
    p.write(f"yyheu.{numero_repeticoes}@inbox.testmail.app")
    
    
    
    p.press("tab")
    #escreva o que há no índice x do vetor nomes e sobrenomes
    
    nome_escrever = nomes[i]
    sobrenome_escrever = sobrenomes[i]
    p.write(nome_escrever)
    p.press("tab")
    p.write(sobrenome_escrever)
    p.press("tab")
    p.write("aaaaaaaa")
    p.press("tab")
    p.click(x=562, y=287)
    p.click(x=564, y=341)
    p.click(x=558, y=415)
    p.click(x=676, y=542)
    t.sleep(10)
    p.click(x=697, y=690)
    t.sleep(10)
    p.click(x=117, y=360)
    p.scroll(-5000)
    p.click(x=801, y=699)
    t.sleep(10)
    p.click(x=1365, y=117)
    p.click(x=1266, y=513)
    t.sleep(10)
    p.click(x=933, y=368)
    t.sleep(10)

    numero_repeticoes += 1
    

#yyheu.x@inbox.testmail.app