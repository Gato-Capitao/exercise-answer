import math
def lanche():
    valores = input().split(" ")
    cod, qnt = valores
    cod, qnt = int(cod), int(qnt)
    if cod == 1:
        preco = 4.00
    elif cod == 2:
        preco = 4.50
    elif cod == 3:
        preco = 5.00
    elif cod == 4:
        preco = 2.00
    elif cod == 5:
        preco = 1.50
    total = preco*qnt
    print("TOTAL: R$ {:.2f}".format(total))
def media3():
    #leia 
    notas = input().split(" ")
    nota1, nota2, nota3, nota4 = notas
    nota1, nota2, nota3, nota4 = float(nota1), float(nota2), float(nota3), float(nota4)

    #calcule
    media = ((nota1*2)+(nota2*3)+(nota3*4)+(nota4*1))/10
    print("Media: {:.1f}".format(media))

    if media >= 7:
        print("Aluno aprovado.")
    elif media < 5:
        print("Aluno reprovado.")
    elif media >= 5 and media <= 6.9:
        print("Aluno em exame.")
        notae = float(input())
        print("Nota do exame: {:.1f}".format(notae))
        mediaf = (media+notae)/2
        if media >= 5:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print("Media final: {:.1f}".format(mediaf))
def cordenadas_de_um_ponto():
    valores = input().split(" ")
    x, y = valores
    x, y = float(x), float(y)
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    if x == 0 or y == 0:
        if x == 0 and y == 0:
            print("Origem")
        elif x != 0:
            print("Eixo X")
        elif y != 0:
            print("Eixo Y")
    elif x < 0:
        q2 += 1
        q3 +=1
        if y < 0:
            q3 += 1
        else:
            q2 +=1
    elif x > 0:
        q1 += 1
        q4 += 1
        if y > 0:
            q1 +=1
        else:
            q4 += 1
    if q1 == 2:
        print("Q1")
    elif q2 == 2:
        print("Q2")
    elif q3 == 2:
        print("Q3")
    elif q4 == 2:
        print("Q4")
        print("Q4")
def sort_simples():
    valores = input().split(" ")
    a, b, c = valores
    a, b, c = int(a), int(b), int(c)
    
    if a > b and a > c:
        if b > c:
            ordem = [c, b, a]
        else:
            ordem = [b, c, a]
    elif b > a and b > c:
        if a > c:
            ordem = [c, a, b]
        else:
            ordem = [a, c, b]
    elif c > a and c > b:
        if a > b:
            ordem = [b, a , c]
        else:
            ordem = [a, b, c]

    for i in ordem:
        print(i)
    print("")
    print('''{}
    {}
    {}'''.format(a,b,c))
def triangulo():
    valores =  input().split(" ")
    a, b, c = valores
    a, b, c = float(a), float(b), float(c)

    if a<b+c and b<c+a and c<b+a:
        perimetro = a+b+c
        print('Perimetro = {:.1f}'.format(perimetro))
    else:
        area = ((a+b)*c)/2
        print("Area = {:.1f}".format(area))
def multiplos():
    multiplos = False
    t = 0
    valores = input().split(" ")
    a, b = valores
    a, b = int(a), int(b)
    
    for i in range(b+a):
        r = a*i
        if i>0:
            t = a/i
        if r == b or t == b:
            multiplos = True
            break
    if multiplos == True:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
def tipos_de_triangulos():
    valores =  input().split()
    a, b, c = valores
    a, b, c = float(a), float(b), float(c)
    ordem = [a,b,c]
    ordem.sort(reverse=True)
    a, b, c = ordem
    
    if a>=b+c:
        print("NAO FORMA TRIANGULO")
    else:
        if a**2 == b**2+c**2:
            print("TRIANGULO RETANGULO")
        elif a**2 > b**2+c**2:
            print("TRIANGULO OBTUSANGULO")
        elif a**2 < b**2+c**2:
            print("TRIANGULO ACUTANGULO")
        if a==b and b==c:
            print("TRIANGULO EQUILATERO")
        elif a==b or b==c or a==c:
            print("TRIANGULO ISOSCELES")
def tempo_de_jogo():
    horas = input().split(" ")
    h1, h2 = int(horas[0]), int(horas[1])
    if h1<h2:
        hora = h2-h1
    else:
        hora = (24+h2)-h1
    
    print("O JOGO DUROU %d HORA(S)"%hora)
def ddd():
    ddd = int(input())
    if ddd>30:
        if ddd%2 == 0:
            if ddd==32:
                local = "Juiz de Fora"
        else:
            if ddd == 61:
                local= "Brasilia"
            elif ddd==71:
                local = "Salvador"
            elif ddd == 31:
                local = "Belo Horizonte"
            else:
                local = "DDD nao cadastrado"
    else:
        if ddd == 27:
            local = "Vitoria"
        elif ddd == 21:
            local = "Rio de Janeiro"
        elif ddd == 19:
            local = "Campinas"
        elif ddd == 11:
            local = "Sao Paulo"
        else:
            local = "DDD nao cadastrado"
    print(local)
def animal():
    p1 = input()
    p2 = input()
    p3 = input()
    
    if p1 == "vertebrado":
        if p2 == "ave":
            if p3 == "carnivoro":
                animal = "aguia"
            else:
                animal = "pomba"
        else:
            if p3 == "onivoro":
                animal = "homem"
            else:
                animal = "vaca"
    else:
        if p2 == "inseto":
            if p3 == "hematofago":
                animal = "pulga"
            else:
                animal = "lagarta"
        else:
            if p3 == "hematofago":
                animal = "sanguessuga"
            else:
                animal = "minhoca"
    print(animal)
def aumento_de_salario():
    salario = float(input())
    
    if salario >=0 and salario <=400:
        porcentagem = 15
    elif salario > 400 and salario <= 800:
        porcentagem = 12
    elif salario > 800 and salario <= 1200:
        porcentagem = 10
    elif salario > 1200 and salario <= 2000:
        porcentagem = 7
    elif salario>2000:
        porcentagem = 4
    
    aumento=(salario*porcentagem)/100
    ns=salario+aumento
    print("""Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %""".format(ns, aumento, porcentagem))
def tempocomminutos():
    #Declarar variaveis
    h1, m1, h2, m2 = input().split (" ")
    h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2) 
    horas, minutos = 0, 0
    
    #Condicionais
    if h1 < h2:
        horas = h2-h1
        if m1 < m2:
            minutos = m2-m1
        elif m1 > m2:
            minutos = (m2+60)-m1
            horas -= 1
        else:
            minutos = 0
    elif h1 > h2:
        horas = (24+h2)-h1
        if m1 < m2:
            minutos = m2-m1
        elif m1 > m2:
            minutos = (60+m2)-m1
            horas -= 1
        else:
            minutos = 0
    else:
        if m1 < m2:
            minutos = m2 - m1
            horas = 0
        elif m1 > m2:
            minutos = (60+m2)-m1
            horas = 23
        else:
            horas = 24
            minutos = 0
    
    #Resultado
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
def contadorDeCedulas():
    valor = float(input())
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.5, 0.01]
    
    for i in notas:
        quantidade = int(valor/i)
        print(f"{quantidade} notas de {i}")
        valor -= quantidade*i
    for i in moedas:
        quantidade = int(valor/i)
        print(f"{quantidade} moedas de {i}")
        valor -= quantidade*i
def impostoDeRenda():
    def impostoPorcentagem(valor, porcentagem):
        i = (valor*porcentagem)/100
        return i
    valor = float(input())
    
    imposto = 0.0
    if valor <= 2000:
        print("Isento")
    elif valor <= 3000:
        valor-=2000
        imposto += impostoPorcentagem(valor, 8)
        print("R$ {:.2f}".format(imposto))
    elif valor <= 4500:
        imposto += impostoPorcentagem(1000, 8)
        valor -= 3000
        imposto += impostoPorcentagem(valor, 18)
        
        print("R$ {:.2f}".format(imposto))
    else:
        imposto += impostoPorcentagem(1000, 8)
        imposto += impostoPorcentagem(1500, 18)
        valor -= 4500
        imposto += impostoPorcentagem(valor, 28)
        print("R$ {:.2f}".format(imposto))
def mes():
    mes = {
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"
    }
    numMes = int(input())
    print(mes[numMes])
def paresEntreCinco():
    numeros = []
    for i in range(5):
        n = int(input())
        numeros.append(n)
        
    pares = 0
    for i in numeros:
        if(i%2 ==0):
            pares += 1
    print("{} valores pares".format(pares))
def ParesImparesPositivosNegativos():
    valores = []
    positivos = 0
    impares = 0
    negativos = 0
    pares = 0
    
    for i in range(5):
        valores.append(int(input()))
    for i in valores:
        if i%2 == 0:
            pares += 1
        else:
            impares +=1
        if i > 0:
            positivos += 1
        elif i < 0:
            negativos += 1
    print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(pares, impares, positivos, negativos))
def somaDeImparesConsecutivosI():
    #ler X e Y
    valores = []
    valores.append(int(input()))
    valores.append(int(input()))
    
    valores.sort()
    
    total = 0
    #enquanto X for menor que Y
    while(valores[0] < valores[1]-1):
        #x++
        valores[0] += 1
        #se x for impar soma com o total
        if(valores[0]%2 !=0):
            total += valores[0]
        
    print(total)
def intervalo2():
    valores = []
    dentro = 0
    fora = 0
    #ler qntdd de vzs v4i ler
    qntdd = int(input())
    #ler valores para a lista
    for i in range(qntdd):
        valores.append(int(input()))
    for valor in valores:
        if (valor >= 10 and valor <= 20):
            dentro += 1
        else:
            fora += 1
    print("{} in\n{} out".format(dentro, fora))
def parOuImpar():
    """
    Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. 
    Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), 
    ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), 
    embora a descrição correta seja (EVEN NULL), pois por definição zero é par, 
    seu programa deverá imprimir apenas NULL.
    """
    
    valores = []
    #ler qntd de vlrs que serão lidos
    qntd = int(input())
    
    #lç pr ler vlores
    for i in range(qntd):
        valores.append(int(input()))
    for vl in valores:
        if(vl == 0):
            print("NULL")
        else:
            if(vl%2 == 0):
                texto = "EVEN "
            else:
                texto = "ODD "
            if(vl > 0):
                texto += "POSITIVE"
            else:
                texto += "NEGATIVE"
            print(texto)
def quadradoDePares():
    """
    Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, 
    de 1 até N, inclusive N, se for o caso.
    """
    #ler X
    vl = int(input())
    
    #lç de repetico ate X
    contador = 1
    while(contador < vl):
        #X++
        contador += 1
        
        #se X for par
        if(contador%2 == 0):
            print("{}^2 = {}".format(contador, contador**2))
def resto2():
    """
    Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.
    """
    #ler X
    x = int(input())
    count = 1
    #enqunto count < 9999
    while count < 9999:
        #count++
        count += 1
        
        #se count%x == 2
        if(count%x == 2):
            #mostre count
            print(count)
def tabuada():
    """
    Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
    1 x N = N      2 x N = 2N        ...       10 x N = 10N
    """
    #ler X
    x = int(input())
    #enquanto count < 10
    count = 0
    while(count < 10):
        #count++
        count += 1
        #mostra count*x
        print("{} x {} = {}".format(count, x, x*count))
def mediaPonderada():
    """
    Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. 
    Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. 
    Apresente a média ponderada para cada um destes conjuntos de 3 valores, 
    sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.
    """
    vl = []
    
    #Qntd de testes
    qntd = int(input())
    
    #lç de rptç com maximo testes
    for i in range(qntd):
        #ler e adicionar os 3 valores na list
        u = input().split(" ")
        u = [float(w) for w in u]
        vl.append(u)
    
    #lç de rptç pr cd test
    for teste in vl:
        #formula
        x = round(((teste[0]*2)+(teste[1]*3)+(teste[2]*5))/10, 1)
        #mostrar
        print(x)
def sequenciaIJ2():
    #lista com os vlores de J
    j = [7, 6, 5]
    
    #lç de repetição de 1 ate 9
    count = 1
    while count <= 9:
        for valor in j:
            print("I={} J={}".format(count, valor))
        count += 2
def sequenciaIJ3():
    #definir i e j
    i = 1
    j = 7
    
    #enquanto i for menor que 9
    while i <= 9:
        #mostra j
        print("I={} J={}".format(i, j))
        #mostra j-1
        print("I={} J={}".format(i, j-1))
        #mostra j-2
        print("I={} J={}".format(i, j-2))
        #soma 2 em i e j
        i += 2
        j += 2
def sequenciaIJ4():
    #definir I e J
    i = 0
    j = 1
    
    #enqunto I for menor que 2
    while i <= 2:
        j = 1+i
        if(int(j+i) != math.ceil(j+i)):
            #mostre I e J-2
            print("I={} J={}".format(round(i, 1), round(j, 1)))
            
            #mostre I e J-1
            print("I={} J={}".format(round(i, 1), round(j+1, 1)))
            
            #mostre I e J
            print("I={} J={}".format(round(i, 1),  round(j+2, 1)))
        else:
            #mostre I e J-2
            print("I={} J={}".format(int(round(i, 1)), int(j)))
            
            #mostre I e J-1
            print("I={} J={}".format(int(round(i, 1)), int(j+1)))
            
            #mostre I e J
            print("I={} J={}".format(int(round(i, 1)),  int(j+2)))
        i += 0.2
def somaDeImparesConsecutivosII():
    #ler quantidade de testes
    qnt = int(input())
    
    #lç de repetição em um alcance de testes
    for i in range(qnt):
        #soma = 0
        soma = 0
        #ler valores, e deixar em ordem crescente
        v = input().split(" ")
        v[0] = int(v[0])
        v[1] = int(v[1])
        
        v.sort()
        
        #enquanto v1 menor que v2-1
        while(v[0] < v[1]-1):
            #v1++
            v[0] += 1
            #se v1 for impar
            if(v[0]%2 != 0):
                #adiciona 1 em valor
                soma+=v[0]
        #mostrar soma
        print(soma)
def sequenciaDeNumerosESoma():
    while True:
        soma = 0
        v = input().split(" ")
        
        v.sort()
        
        v[0] = int(v[0])
        v[1] = int(v[1])
        if(v[0] <= 0 or v[1] <= 0):
            break
        
        while v[0] <= v[1]:
            soma += v[0]
            print("{} ".format(v[0]), end="")
            v[0]+=1
        print("Sum={}".format(soma))
def bacteriasSuasLoucas():
    grupos = []
    grupo = ""
    transformacoes = {}
    bacteriasTexto = "A"
    qntA, qntB = 0, 0
    
    v = [int(i) for i in input().split(" ")]
    
    for i in range(v[1]):
        t = input().split(" ")
        transformacoes.update({t[0]:t[1]})
    
    for i in range(v[0]):
        listaAB = True
        for c in bacteriasTexto:
            if c == bacteriasTexto[0]:
                if listaAB == False:
                    listaAB = True
                    grupos.append(grupo)
                    grupo = ""
            else:
                if listaAB == True:
                    listaAB = False
                    grupos.append(grupo)
                    grupo = ""
            grupo += c
        grupos.append(grupo)
        bacteriasTexto = ""
        
        for g in grupos:
            if g in transformacoes:
                bacteriasTexto += transformacoes[g]
            else:
                bacteriasTexto += g
        grupos = []
        grupo = ""
    
    for c in bacteriasTexto:
        if c == "A":
            qntA += 1
        else:
            qntB += 1
    print(qntA, qntB)
def xPorY():
    #leia a quantidade de divisões que deverá ser feita
    qntd = int(input())
    #para cada divisao
    for i in range(qntd):
        #leia X e Y
        v = [int(i) for i in input().split(" ")]
        #tente:
        try:
            #mostra X/Y
            print("{:.1f}".format(v[0]/v[1]))
        #execeto:
        except:
            #divisão impossivel
            print("divisao impossivel")
def validacaoDeNota():
    #enquanto for verdade:
    while True:
        #leia a nota1
        nota1 = float(input())
        #se a nota1 for maior ou igual 0 e menor ou igual 10:
        if nota1 >= 0 and nota1 <=10:
            #quebra
            break
        #se n
        else:
            #nota invalida
            print("nota invalida")
    
    #enquanto for verdade:
    while True:
        #leia a nota2
        nota2 = float(input())
        #se a nota2 for maior ou igual 0 e menor ou igual 10:
        if nota2 >= 0 and nota2 <= 10:
            #quebra
            break
        #se n
        else:
            #nota invalida
            print("nota invalida")
    
    #calcula a media
    media = (nota1+nota2)/2
    #mostra o resultado
    print("media = {:.2f}".format(media))
def restoDaDivisao():
    #lista valores
    valores = []
    #ler valores[0]
    valores.append(int(input()))
    #ler valores[1]
    valores.append(int(input()))
    
    #deixa a  lista em ordem crescente
    valores.sort()
    
    #enquato valor0+1 for menor que valor1
    while valores[0] < valores[1]-1:
        #aumenta 1 em valor0
        valores[0]+=1
        #se o resto da divisão por 5 for igual a 2 ou 3:
        if valores[0] %5 == 2 or valores[0]%5 == 3:
            #mostre o numero
            print(valores[0])
def grenais():
    #inter
    inter = 0
    #gremio
    gremio = 0
    #empates
    empates = 0
    
    #enquanto for verdade:
    while True:
        #leia o jogo
        j = [int(i) for i in input().split(" ")]
        #se v[0] for maior que v[1]:
        if(j[0] > j[1]):
            #adiciona 1 em inter
            inter += 1
        #se v[1] for maior que v[0]:
        elif j[1] > j[0]:
            #adiciona 1 em gremio
            gremio += 1
        #se n
        else:
            #adiciona 1 em empate
            empates +=1
        #mostrar Novo grenal (1-sim 2-nao)
        print("Novo grenal (1-sim 2-nao)")
        
        #ler resposta
        r = int(input())
        #se a resposta for 2:
        if r == 2:
            #quebra
            break
    #mostrar quantos grenais tiveram, soma dos resultados
    print("{} grenais".format(inter+gremio+empates))
    
    #quantos o inter ganhou
    print("Inter:{}".format(inter))
    #quantas o gremio ganhou
    print("Gremio:{}".format(gremio))
    #quantos empates aconteceram
    print("Empates:{}".format(empates))
    
    #se o inter tiver ganho mais que o gremio:
    if inter > gremio:
        #vencedor = inter
        v = "Inter venceu mais"
    #se n:
    elif inter < gremio:
        #vencedor = gremio
        v = "Gremio venceu mais"
    else:
        v = "Nao houve vencedor"
    
    #mostra o vencedor
    print(v)
def linguaDoP():
    #texto descriptografado
    textoD = ""
    
    #ler a frase
    frase = input().split(" ")
    
    #para cada palavra
    for p in frase:
        #removeu booleana falsa
        removeu = False
        #para cada caracter em texto:
        for c in p:
            #se removeu for igual verdade:
            if removeu == True:
                #adiciona caracter em texto descriptografado
                textoD += c
                #removeu = False
                removeu = False
            #se n:
            else:
                #removeu = verdade
                removeu = True
        textoD += " "
    #mostra o texto descriptografado
    print(textoD.strip())
def triangulo():
    #função que verifica se é possivel
    def verificar(a, b, c):
        if(abs((b-c)) < a < (b+c)):
            return True
        elif(abs((a-c)) < b < (a+c)):
            return True
        elif(abs((a-b)) < c < (a+b)):
            return True
        else:
            return False
    #ler os 4 valores
    v = [int(a) for a in input().split(" ")]
    
    #se alguma das soluções for verdadeira:
    if(verificar(v[0], v[1], v[2]) or verificar(v[1], v[2], v[3]) or verificar(v[2], v[3], v[0]) or verificar(v[3], v[0], v[1])):
        #mostra S
        print("S")
    #se n:
    else:
        #mostra N
        print("N")
def semente1():
    #preenchidas lista
    preenchidas = []
    #dias
    dias = 0
    
    #ler tamanho da lista e numero de gotas
    t = int(input().split(" ")[0])
    #criar lista em um alcance de tamanho
    fita = list(range(t))
    
    #ler posicoes das gotas
    p = [int(i)-1 for i in input().split(" ")]
    
    #adiciona valor 1 nas posicoes
    for a in p:
        fita[a] = "a"
    
    #enquanto tiver 0 em fita:
    while  fita.count("a") != len(fita):
        
        #preencher as colunas ao do reagente
        #para cada posicao:
        for i in p:
            #tenta:
            try:
                if(fita[i+1] != "a"):
                    #adicionar 1 na proxima posicao
                    fita[i+1] = "a"
                    #adicionar a proxima posicao na lista de preenchidas
                    preenchidas.append(i+1)
            #exceto:
            except:
                #nada
                pass
            #tenta:
            try:
                if(fita[i-1] != "a" and not i-1 < 0):
                    #adicionar 1 na posicao anterior
                    fita[i-1] = "a"
                    #adiciona posicao anterior na lista de preenchidas
                    preenchidas.append(i-1)
            #exceto:
            except:
                #nada
                pass
        
        #posicao será igual a lista de preenchidas
        p = list(preenchidas)
        #reseta a lista preenchidas
        preenchidas = []
        
        #aumenta 1 em dias
        dias += 1
    #mostra 1
    print(dias)
def tipoDeCombustivel():
    #qntAlcool
    qntAlcool = 0
    #qntGasolina
    qntGasolina = 0
    #qntDiesel
    qntDiesel = 0
    
    #enquanto for verdade:
    while True:
        #ler valor
        v = int(input())
        
        #se valor for 1:
        if(v == 1):
            #alcool
            qntAlcool += 1
        #se n se valor for 2:
        elif(v==2):
            #gasolina
            qntGasolina+=1
        #se n se valor for 3:
        elif(v==3):
            #diesel
            qntDiesel+=1
        #se n se valor for 4:
        elif(v==4):
            #quebra
            break
    """Mostra
    MUITO OBRIGADO
    
    Alcool:
    Gasolina:
    Diesel:
    """
    print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(qntAlcool, qntGasolina, qntDiesel))
def multiplosDe13():
    #soma dos numeros
    soma = 0
    #lista com os valores
    v = []
    #ler valor 1
    v.append(int(input()))
    #ler valor 2
    v.append(int(input()))
    
    #deixar em ordem
    v.sort()
    
    #enquanto x for menor ou igual y:
    while v[0] <= v[1]:
        #se x o resto da divisao de 13 for diferente de 0:
        if(v[0]%13 != 0):
            #adiciona x em soma
            soma += v[0]
        #adiciona 1 em x
        v[0] += 1
    #mostra soma
    print(soma)
def pum():
    #ler quantidade de linhas
    l = int(input())
    #contador
    count = 0
    #para cada linha:
    for i in range(l):
        #mostre contador+1, contador+2, contador+3
        print("{} {} {} PUM".format(count+1, count+2, count+3))
        #contador +3
        count += 4
def quadradoEAoCubo():
    #ler as linhas
    l = int(input())
    #para cada linha:
    for i in range(l):
        #mostre a linha, ela ao quadradado e ao cubo
        print("{} {} {}".format(i+1, (i+1)**2, (i+1)**3))
def fibonacciFacil():
    #texto
    texto = ""
    #ler sequencia
    s = int(input())
    #lista com 0 e 1
    lista = [0, 1]
    
    #contador = 2
    count = 2
    #enquanto contador for menor que alcance da lista:
    while count < s:
        #soma = (contador-2)+(contador-1) de lista
        soma = lista[count-2]+lista[count-1]
        #adiciona lista em lista dos num
        lista.append(soma)
        #adiciona 1 em contador
        count += 1
    #para cada valor em lista:
    for v in lista:
        #adiciona v em texto
        texto += str(v)+" "
        
    #tira as bordas
    texto = texto.strip()
    #mostra
    print(texto)
def idades():
    #quantidade de idades lidas
    lidas = 0
    #soma das idades
    soma = 0
    #enquanto for verdade:
    while True:
        #ler idade
        idade = int(input())
        #se idade for menor que 0:
        if idade < 0:
            #quebra
            break
        #adiciona idade em soma das idades
        soma += idade
        #adiciona 1 em idades lidas
        lidas += 1
    #media é igual a soma das idades dividida pela quantidade de idades lidas
    try:
        media = soma/lidas
    except:
        media = 0
    #mostrar media
    print("{:.2f}".format(media))
def fliper():
    #ler valores
    v = [int(i) for i in input().split(" ")]
    
    #se valor1 for igual 0:
    if v[0] == 0:
        #return C
        return "C"
    #se n
    else:
        #se valor2 for igual 1
        if v[1] == 1:
            #return A
            return "A"
        #se n
        else:
            #return B
            return "B"
def sequenciaS():
    #soma
    soma = 0
    #contador que é igual 1
    count = 1
    #enquanto contador for menor que ou igual 100
    while count <= 100:
        #adiciona em soma 1/contador
        soma += 1/count
        #adiciona 1 em contador
        count += 1
    #mostra o resultado
    print("{:.2f}".format(soma))
def sequenciaS2():
    #soma
    soma = 1
    #divisor
    divisor = 2
    
    #contador = 3
    count = 3
    #enquanto contador for menor ou igual 39:
    while count <=39:
        #soma vai ser igual a contador dividido pelo divisor
        soma+= count/divisor
        #dobra o divisor
        divisor = divisor*2
        #adiciona 2 em contador
        count += 2
    #mostra soma
    print("{:.2f}".format(soma))
def ultrapassandoZ():
    #qntdU
    qntdU = 1
    #ler x
    x = int(input())
    
    #ler z
    z = int(input())
    #enquanto x for maior ou igual z:
    while x >= z:
        #leia z
        z = int(input())
    
    #xinicial
    xi = x+1
    #enquanto z for maior ou igual x:
    while z >= x:
        #adiciona ele mesmo com 1
        x += xi
        #adiciona 1 em qntdU
        qntdU += 1
        
        #adiciona 1 em xi
        xi += 1
    
    #mostra qntU
    print(qntdU)
def somandoInteirosConsectivos():
    r = 0
    #ler valores
    v = [int(a) for a in input().split(" ")]
    
    #declarar A
    a = v[0]
    
    #contador = 1
    count = 1
    #enquanto contador for menor que o tamanho da lista menos 1
    while count < len(v):
        #se v[contador] for maior que 0:
        if v[count] > 0:
            #n é igual a v contador
            n = v[count]
        #adiciona 1 em contador
        count += 1
    
    #contador = 1
    count = 0
    #enquanto contador for menor que N-1
    while count < n:
        #soma A+contador em A
        r += a+count
        
        #adicionar 1 em contador
        count += 1
    #mostra A
    print(r)
def competicaoDeJogos():
    #qntd de alunos
    qntdA = 0
    #ler quantidade de universidades que irão participar
    qntdU = int(input())
    #ler quantidade de alunos que cada universidade pode mandar
    y = input().split(" ")
    v = []
    for p in y:
        try:
            v.append(int(p))
        except:
            pass
    #para cada quantidade de alunos que as universidades podem mandar
    for i in v:
        #divide a quantidade por 3
        alunos = i/3
        
        #arredonda para inteiro
        alunos = int(alunos)
        
        #adiciona em qntd de alunos o produto por 3
        qntdA += alunos*3
    
    #mostra a quantidade
    print(qntdA)
def trocandoDeMesa():
    #dicionario com lugares modificados
    lugares = {}
    
    def trocarOsLugares(v1, v2):

        #se v1 n estiver em lugares modificados
        if v1 not in lugares:
                #adiciona com o seu id de origem
                lugares.update({v1:v1})
            #se v2 n estiver em lugares modificados
        if v2 not in lugares:
            #adiciona no dicionario em seu id de origem
            lugares.update({v2:v2})
        #variavel vaga que vai ser igual v1
        vaga = lugares[v1]
        #o id de v1 será o id de v2
        lugares[v1] = lugares[v2]
        #o id de v2 será a variavel vaga
        lugares[v2] = vaga
    
    def procurarFuncionario(id):
        #qntdRedirecionado = 0
        qntdRedirecionado = 0
        #mesa 
        mesa = 0
        
        #se id n estiver em acentos trocados:
        if(id not in lugares):
            #retorna qntdRedirecionado
            return qntdRedirecionado
        #se n
        else:
            mesa = id
            #enquanto o id da mesa n for o id que ele está procurando:
            while lugares[mesa] != id:
                #mesa vai ser igual a mesa com o numero do id do cara que estava nql mesa
                mesa = lugares[mesa]
                #qntdRedirecionado = 1
                qntdRedirecionado += 1
            #retorna qntdRedirecionado
            return qntdRedirecionado

    
    
    #ler quantidade de funcionarios e de mesas.
    qntdMF = int(input())
    #ler a quantidade de eventos que precisarão ser processados
    qntdE = int(input())
    
    #para cada evento
    for e in range(qntdE):
        #ler valores
        v = [int(i) for i in input().split(" ")]
        #se for igual v0 for igual 1:
        if v[0] == 1:
            #trocar os lugares
            trocarOsLugares(v[1], v[2])
        #se n:
        else:
            #procurar funcionario
            #mostra quantas vezes ele se redirecionou
            print(procurarFuncionario(v[1]))
def divisores1():
    #ler numero
    num = int(input())
    #para um em um alcance de numero+1:
    for i in range(1, num+1):
        #o numero dividido para um
        r = num/i
        #se ele arredondado for igual a ele sem estar arredondado:
        if(int(r) == r):
            #imprima
            print(i)
def resgateEmQuedaLivre():
    """
    ler quantidade de testes
    
    para cada teste:
        ler a quatidade de pessoas que pularam e adicionar suas cordenadas em uma lista
        
    para cada cordenada:
        procurar a outra cordenada mais proxima, que seja diferente da que já está armazenada nele.
        adiciona em um dicionario
    
    para cada um paraquedistas:
        calcular a diferença entre seu ponto mais próximo
        somar em teia
    
    mostrar resultado
    """
    """"
    paraquedista = {
        pP = [lista de pessoas presas a ele],
        p = "em quem ele está preso",
        x:cordenada x,
        y:cordendada y
    }
    """
    bancoDeDados = {}
    cordenadas = []
    def calcularDistancia(xa, ya, xb, yb):
        #formula raiz quadrada de (xb-xa)²+(yb-ya)²
        resultado = math.sqrt((xb-xa)**2+(yb-ya)**2)
        
        #retornar resultado
        return resultado

    def procurarCordenadaMaisProxima():
        teia = 0
        #para cada um em cordenadas enumerada
        for n, v in enumerate(cordenadas):
            difM = 0
            primeira = True
            ligacao = False
            p = 0
            for i, c in enumerate(cordenadas):
                if(n != i and i not in bancoDeDados[n]["pP"] and bancoDeDados[i]["p"] == None):
                    diferenca = calcularDistancia(v[0], v[1], c[0], c[1])
                    if(diferenca < difM or primeira):
                        primeira = False
                        ligacao = True
                        difM = diferenca
                        p = i
            
            if ligacao:
                teia += difM
                bancoDeDados[n]["p"] = p
                bancoDeDados[p]["pP"].append(n)
                ligacao = False
            
        return teia
    
    #ler qntd de testes
    t = int(input())
    
    #para cada teste:
    for i in range(t):
        #ler quantidade de paraquedistas
        qntdP = int(input())
        
        #para cada paraquedista:
        for i in range(qntdP):
            #ler sua cordenada e adicionar na lista cordenadas
            c = [int(i) for i in input().split(" ")]
            bancoDeDados.update({i:{"pP":[], "p":None, "x":c[0], "y":c[1]}})
            cordenadas.append(c)
        
        #procurar cordendada mais próxima para cada paraquedista
        teia = procurarCordenadaMaisProxima()
        teia = round(teia)/100
        print(teia)
        #mostrar teia
        teia = 0
        bancoDeDados = {}
        cordenadas = []
def somaDeImparesConsecutivos3():
    """
    ler a quantidade de processos que devem ser feitos
    
    para cada processo:
        ler a quatidade de impares que devem ser lidas
        
        enquanto a quantidade de impares for menor que a quantidade lida:
            se o num for impar:
                soma e adiciona 1 em quantidade de impares
            aumenta 1 em num

        mostra a quantidade de impares
        
        reseta tudo
        
    """
    #ler qntd de processos
    qntP = int(input())
    
    #para cada processo
    for i in range(qntP):
        #ler valores
        v = [int(i) for i in input().split(" ")]
        
        #soma
        s = 0
        #numero = valor inicial
        num = v[0]
        #impares = 0
        impares = 0
        #enquanto contador for menor que a quantidade de impares que deve ser lidas:
        while impares < v[1]:
            #se o numero for impar:
            if num%2 != 0:
                #adiciona 1 em impares
                impares += 1
                #adiciona num em soma
                s += num
            #adiciona 1 em contador
            num += 1
        #mostra o resultado
        print(s)
def somaDeParesConsecutivos():
    """
    enquanto for verdade:
        ler x
        caso x seja 0:
            quebra
        caso não:
            enquanto a quantidade de pares encontrados for menor que 5:
                se o num for par adiciona 1 em pares e adiciona num em soma
                
                adiciona 1 em x
            
    """
    
    #enquanto for verdade:
    while True:
        #ler x
        x = int(input())
        #se x for igual 0:
        if x == 0:
            #quebre
            break
        #se n:
        else:
            #soma = 0
            soma = 0
            #qntd de pares
            qntdP = 0
            #enquanto a quantidade de pares for menor que 5:
            while qntdP < 5:
                #se x for par:
                if(x%2 == 0):
                    #adiciona 1 em pares
                    qntdP += 1
                    #adiciona x em soma
                    soma += x
                #adiciona 1 em x
                x += 1
            print(soma)
def bemVindosEBemVindasAoInverno():
    """
    ler temperaturas
    
    
    Se a temperatura desceu do 1º para o 2º dia, 
    mas subiu ou permaneceu constante do 2º para o 3º, 
    as pessoas ficam felizes (primeira figura).
    
    Se a temperatura subiu do 1º para o 2º dia, 
    mas desceu ou permaneceu constante do 2º para o 3º, 
    as pessoas ficam tristes (segunda figura).
    
    Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, 
    mas subiu do 2º para o 3º menos do que subira do 1º para o 2º, 
    as pessoas ficam tristes (terceira figura).
    
    Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, 
    mas subiu do 2º para o 3º no mínimo o tanto que subira do 1º para o 2º, 
    as pessoas ficam felizes (quarta figura).
    
    Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, 
    mas desceu do 2º para o 3º menos do que descera do 1º para o 2º, 
    as pessoas ficam felizes (quinta figura).
    
    Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, 
    mas desceu do 2º para o 3º no mínimo o tanto que descera do 1º para o 2º, 
    as pessoas ficam tristes (sexta figura).
    
    Se a temperatura permaneceu constante do 1º para o 2º dia, 
    as pessoas ficam felizes se subiu do 2º para o 3º dia ou tristes caso contrário (respectivamente, 
    sétima e oitava figuras).
    """
    #ler temperaturas
    t = [int(i) for i in input().split(" ")]
    
    if(t[0] > t[1]):
        if(t[1] < t[2]):
            print(":)")
        else:
            if(t[1]-t[2] < t[0]-t[1]):
                print(":)")
            else:
                print(":(")
    elif(t[0] < t[1]):
        if(t[1] > t[2]):
            print(":(")
        else:
            if(t[1]-t[2] > t[0]-t[1]):
                print(":(")
            else:
                print(":)")
    else:
        if t[1] < t[2]:
            print(":)")
        else:
            print(":(")
def nossosDiasNuncaVoltarao():
    """
    ler quantos caracteres devem ser mostrados
    
    mostrar texto
    """
    texto = "LIFE IS NOT A PROBLEM TO BE SOLVED"
    #ler qntd de caracters
    x = int(input())
    
    #mostrar
    print(texto[0:x])
def oFilme():
    """
    ler valor antigo e valor novo
    
    obter a diferença do novo pelo antigo
    
    calcular a porcentagem entre eles(x =(diferenca*100)/antigo)
    
    mostrar resultado com 2 casas decimais
    """
    
    #ler valores antigo e novo
    v = [float(i) for i in input().split(" ")]
    
    #calcular a diferenca entre eles
    d = v[1]-v[0]
    
    #calcular porcentagem
    p = (d*100)/v[0]
    
    #mostrar resultado
    print("{:.2f}%".format(p))
def letras():
    """
    ler caracter

    ler texto 

    para cada um em texto:
        se tiver caracter no texto:
            adiciona 1 em contem
        
    calcular a porcentagem = (contem*100)/qntdDePlavras no array texto
    """
    contem = 0
    #ler caracter
    c = input()
    #ler texto
    t = input().split(" ")
    #para cada um em texto
    for i in t:
        #se tiver caracter no texto:
        if(c in i):
            #adiciona 1 em contem
            contem += 1
    
    #calcular porcentagem = (contem*100)/qntdDePlavras no array texto
    p = (contem*100)/len(t)
    
    #mostrar porcentagem com 1 casa após a decimal
    print("{:.1f}".format(p))
def positivosEMedia():
    valores = []
    for i in range(6):
        valores.append(float(input()))
    positivos = 0
    somaDosValores = 0
    media = 0.0
    for i in valores:
        if i >= 0:
            positivos += 1
            somaDosValores += i
            media = somaDosValores/positivos
        
    print("{} valores positivos\n{:.1f}".format(positivos, media))
def tempoDeUmEvento():
    dia1 = int(input().split(" ")[1])
    tempo = input().split(" ")
    hora1 = int(tempo[0])
    minuto1 = int(tempo[2])
    segundo1 = int(tempo[4])

    
    dia2 = int(input().split(" ")[1])
    tempo = input().split(" ")
    hora2 = int(tempo[0])
    minuto2 = int(tempo[2])
    segundo2 = int(tempo[4])

    tempo1 = (dia1*24*60*60)+(hora1*60*60)+(minuto1*60)+segundo1
    tempo2 = (dia2*24*60*60)+(hora2*60*60)+(minuto2*60)+segundo2

    resultado = tempo2 - tempo1

    dias = int(resultado/(24*60*60))
    resultado -= dias*24*60*60

    horas = int(resultado/(60*60))
    resultado -= horas*60*60

    minutos = int(resultado/60)
    resultado -= minutos*60

    segundos = resultado

    
    print("{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)".format(dias, horas, minutos, segundos))
def maiorEPosicao():
    #lista com valores
    lista1 = []
    
    #lç de repeticao até 100
    for i in range(100):
        #adicionar valor na lista
        lista1.append(int(input()))
        
    #cria uma lista com os mesmos valores da lista passada, mas em ordem decrescente
    lista2 = [a for a in lista1]
    lista2.sort(reverse=True)

    #para cada valor na lista valores
    for count, valor in enumerate(lista1):
        #se o primeiro valor da lista2 for igual valor
        if(lista2[0] == valor):
            #imprime o valor
            print(valor)
            #imprime o contador
            print(count+1)
            break
def experiencias():
    #dicionario com as experiencias
    experiencias = {
        "coelho":0,
        "rato":0,
        "sapo":0
    }
    #ler qntd de experiencia
    qnt = int(input())

    #lç de repeticao até a qntd de experiencias
    for i in range(qnt):
        #Lê o valor com split
        valor = input().split(" ")

        #se valor[1] for C } 
        if(valor[1] == "C"):
            experiencias["coelho"] += int(valor[0])
        #senao se valor[1] for R } soma o valor[0] com a experiencia no dicionario
        elif(valor[1] == "R"):
            experiencias["rato"] += int(valor[0])
        #senao} 
        else:
            experiencias["sapo"] += int(valor[0])
    #Calcula o total de experiencia
    texperiencias = experiencias["coelho"]+experiencias["rato"]+experiencias["sapo"]

    #calcula a porcentagem de cada um( (tcobaias*100)/testes)
    pCoelho = (experiencias["coelho"]*100)/texperiencias
    pRato = (experiencias["rato"]*100)/texperiencias
    pSapo = (experiencias['sapo']*100)/texperiencias

    #Mostrar valores
    print("Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}\nPercentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %".format(texperiencias, experiencias["coelho"], experiencias["rato"], experiencias["sapo"], pCoelho, pRato, pSapo))
def sequenciaIJ():
    i = 1
    j = 60
    while j >= 0:
        print("I={} J={}".format(i, j))
        i += 3
        j -= 5
def desafioA():
    #valores, A, B e C
    valores = [int(i) for i in input().split(" ")]

    #se a e b forem igual 0:
    if(valores[0] == 0 and valores[1] == 0):
        #formula do 0
        resultado = (valores[2])
        if(resultado < 0):
            return "N"
        resultado = math.sqrt(resultado)
    #se n:
    else:
        #formula normal
        resultado = (valores[2])/(valores[0]+valores[1])
        if(resultado < 0):
            return "N"
        resultado = math.sqrt(resultado)
    #mostrar resultado
    if(int(resultado) != resultado):
        #não é exato
        return "N"
    #se não:
    else:
        #é exato
        return("Y")
def desafioC():
    #ler palavra
    palavra = input()
    #listinha
    listinha = []
    # listaInicial
    listaInicial = []
    # listaFinal
    listaFinal = []
    
    # final = verdadeiro
    final = True
    # para cada letra em palavra
    for i in palavra:
    #   se final:
        if final:
            #adiciona letra na lista final
            listaFinal.append(i)
            final = False
        #se n:
        else:
            #adiciona na inicial
            listaInicial.append(i)
            final = True
    listaFinal.reverse()
    #Para cada valor em lista inicial
    for i in listaInicial:
        #mostra valor com final = ""
        print(i, end="")
    #para cada valor em listinha:
    for i in listaFinal:
        #mostra valor com final = ""
        print(i, end="")
    print("")
def desafioI():
    #quantidade de degraus
    qntd = int(input())

    #ler valores
    v = [int(i) for i in input().split(" ")]
    h = v[0]*10**-2
    c = v[1]*10**-2
    #hipotenusa
    #hipotenusa = ((c**2)+(l**2))**(1/2)
    hipotenusa = ((c**2)+(h**2))**0.5
    
    #area = h*hipotenusa
    area = ((v[2]*10**-2)*(hipotenusa))

    #total = quantidade * area
    total = area*qntd
    total = round(total, 4)

    #mostrar
    print("{:.4f}".format(total))
def desafioF():
    #ler numero
    num1 = float(input())
    lista = []
    solution = False
    #em um alcance de 99999999:
    
    for i in range(999999998):
        num = str(i+1)
        num2 = float(num[1:(len(num))]+num[0])
        #se o texto modificado multiplicado pelo num1 for igual a texto modificado:
        
        if num2 == int(num)*num1:
            #mostra o numero
            print(num)
            solution = True
    if solution == False:
        print("No solution")
def desafioJ():
    #quantidade de mensagens recebidas
    qntd = int(input())
    if(qntd == 0 or qntd < 0):
        return
    #dicionario com as conversas
    conversas = {}

    #tempos
    tempos = []

    #para cada um em um alcance de quantidade
    for i in range(qntd):
        #ler valores
        valores = input().split(" ")
        valores[1] = int(valores[1])
        valores[2] = int(valores[2])
        tempo = valores[1]-valores[2]

        #adicionar valores nas conversas
        conversas.update({tempo:valores[0]})
        #adicionar tempo na lista de tempos
        tempos.append(tempo)

    #deixa a lista de tempos em ordem decrescente
    tempos.sort()

    #mostra o nome do planeta de acordo com o maior tempo
    print(conversas[tempos[0]])
def fechadura():
    """
    ler a quantidade de pinos e onde eles precisam estar

    ler a posicao que cada pino esta

    para cada um no tamanho de lista-1:
        calcular a diferença do tamnho que precisa estar e o tamanho que esta
        adicionar diferenca no item
        adicionar diferenca no proximo item
        adicionar o valor absoluto em movimentos
    
    mostrar movimento
    """
    #mov
    mov = 0

    #ler a quantidade de pinos e a posição em que eles precisam estar
    v = [int(q) for q in input().split(" ")]

    #ler a lista de pinos e suas posicoes
    pinos = [int(p) for p in input().split(" ")]

    #para cada um em um alcance do tamanho da lista pinos
    for i in range(len(pinos)-1):
        #calcula a diferença
        dif = v[1]-pinos[i]
        #adiciona a diferenca no pino
        pinos[i] += dif
        #adiciona a diferenca no próximo pino
        pinos[i+1] += dif
        #adiciona o valor absoluto em mov
        mov += abs(dif)
    #mostrar mov
    print(mov)
def crescimentoPopulacional():
    """
    ler a quantidade de testes

    para cada teste:
        ler valores
        anos = 1
        enquanto a populacao da cidade A for menor e anos for menor igual 100:
            adiciona o aumenta na cidade A
            adiciona o aumento em B
            aumenta os anos
        
        se a for maior que b:
            mostra anos
        se n:
            se passou mais de 1 seculo
    """
    #ler a quantidade de testes
    t = int(input())

    #para cada teste:
    for i in range(t):
        #ler valores
        v = [float(a) for a in input().split(" ")]

        #anos
        anos = 0
        #enquanto anos for menor 100 e A for menor igual B:
        while anos < 100 and v[0] <= v[1]:
            #adiciona 1 em anos
            anos += 1
            #aumenta a populacao de A
            v[0] += int((v[0]*v[2])/100)
            #aumenta a populacao de B
            v[1] += int((v[1]*v[3])/100)
        #se A for maior que B:
        if(v[0]>v[1]):
            #mostra os anos
            print(anos, "anos.")
            print(v)
        #se n
        else:
            #Mais de 1 seculo.
            print("Mais de 1 seculo.")
def fila():
    """
    ler a quantidade inicial de pessoas na fila

    ler a fila inicial

    ler a quantidade de pessoas que sairam da fila

    ler as pessoas que sairam da fila

    remover as pessoas da lista fila inicial

    mostrar a fila final
    """
    texto = ""
    #ler qntd na fila inicial
    qntdFI = int(input())

    #ler filaI
    fila = [int(p) for p in input().split(" ")]

    #ler qntd de pessoas que sairam da fila
    qntdS = int(input())

    #ler lista de pessoas que sairam da fila
    s = [int(b) for b in input().split(" ")]

    #para cada pessoa na lista que saiu da fila
    for v in s:
        #remove da lista
        fila.remove(v)
    
    #para cada valor na fila:
    for p in fila:
        texto += str(p)+" "
    print(texto.strip())
def loteria():
    """
    ler aposta de flavinho

    ler numeros que foram sorteados

    para cada um na aposta de flavinho:
        se a aposta estiver nos numeros sorteados:
            adiciona em acertou mais um
    
    mostrar resultado de acordo com a quantidade de acertos:
    """
    #acertos
    acertos = 0
    #ler aposta
    apostas = [int(a) for a in input().split(" ")]

    #ler numeros que foram sorteados
    sorteados = [int(b) for b in input().split(" ")]

    #para cada aposta de flavinho:
    for a in apostas:
        #se a aposta estiver em numeros sorteados
        if(a in sorteados):
            #aumenta 1 em acertos
            acertos+= 1
    #se a qntd de acertos for igual 6:
    if acertos == 6:
        #sena
        print("sena")
    #se n se a quantidade de acertos for igual 5:
    elif(acertos == 5):
        #quina
        print("quina")
    #se n se a quantidade de acertos for igual 4:
    elif(acertos == 4):
        #quarta
        print("quadra")
    #se n se a quantidade de acertos for igual 3:
    elif(acertos==3):
        #terno
        print("terno")
    #se n:
    else:
        #azar
        print("azar")
def vaiTerCopa():
    '''
    enquanto for verdade:
        Tenta ler as reclamaçoes em inteiro:
            se as tiver 1 reclamação ou mais:
                vai ter duas copas
            se n:
                vai ter copa
        
        caso não:
            quebre
    '''
    #enquanto for verdade
    while True:
        #tente
        try:
            #ler a qntd de reclamações
            r = int(input())
            #se a qntd de reclamações for maior que -
            if r > 0:
                #mostre vai ter duas
                print("vai ter duas!")
            #se n
            else:
                #mostre vai ter copa
                print("vai ter copa!")
        #exceto:
        except:
            #quebre
            break
def aCorridaDeLesmas():
    """
    enquanto for verdade:
        leia a quantidade de lesmas
        
        ler a velocidade maxima de todas as lesmas
        
        deixar a a lista da velocidade de lesmas em ordem decrescente
        
        se o primeiro valor for menor que 10:
            nivel 1
        se n se o primeiro valor for menor que 20:
            nivel 2
        se n:
            nivel 3
    """
    #enquanto for verdade:
    while True:
        try:
            #leia a quantidade maxima de lesmas
            qntd = int(input())
            
            #ler a lista de velocidades
            vlcds = [int(v) for v in input().split(" ")]
            
            #deixar em ordem decrescente
            vlcds.sort(reverse=True)
            
            #se o valor 0 da lista for menor que 10:
            if vlcds[0] < 10:
                #nivel 1
                print(1)
            #se n se o valor 0 é menor que 20:
            elif(vlcds[0] < 20):
                #nivel 2
                print(2)
            #se n:
            else:
                #nivel 3
                print(3)
        except:
            break
def corvoContador():
    """
    enquanto o corvo ainta não tiver gritado 3 vezes:
        ler o texto
        se for uma piscada:
            adiciona valor da piscada em soma
        se n:
            aumenta mais um em gritos
            mostra o valor soma
            reseta o valor soma
    """
    #soma
    soma = 0
    #gritos
    gritos = 0
    
    #valores das piscadas
    piscadas = {
        "---":0,
        "--*":1,
        "-*-":2,
        "-**":3,
        "*--":4,
        "*-*":5,
        "**-":6,
        "***":7
    }

    #enquanto o corvo tiver gritado menos de 3 vezes:
    while gritos < 3:
        #ler a string
        texto = input()
        #se a string estiver em piscada:
        if(texto in  piscadas):
            #adiciona valor da piscada em soma
            soma += piscadas[texto]
        #se n:
        else:
            #adiciona mais 1 em gritos
            gritos += 1
            #mostra o valor da soma
            print(soma)
            #reseta o valor soma
            soma = 0
def bazinga():
    """
    leia a quantidade de casos
    
    para cada um em casos:
        leia o jogo
        se o jogo 2 estiver na lista de quem vence de jogo 1:
            caso num o Raj tapaceou!
        se n se o jogo 2 estiver na lista de quem perde de jogo 1:
            caso num Bazinga!
        se n:
            caso numm De novo!
    """
    #personagens
    personagens = {
        "pedra":{"perde":["papel", "Spock"], "vence":["tesoura", "lagarto"]},
        "papel":{"perde":["tesoura", "lagarto"], "vence":["pedra", "Spock"]},
        "tesoura":{"perde":["Spock", "pedra"], "vence":["papel", "lagarto"]},
        "lagarto":{"perde":["tesoura", "pedra"], "vence":["papel", "Spock"]},
        "Spock":{"perde":["lagarto", "papel"], "vence":["tesoura", "pedra"]}
    }
    #leia a quantidade de casos
    casos = int(input())
    #para cada um em casos:
    for c in range(casos):
        #leia o jogo
        jg = input().split(" ")
        #se jogo[1] estiver na lista de personagens[jogo[0]] que ele perde:
        if(jg[1] in personagens[jg[0]]["perde"]):
            #caso num Raj trapaceou!
            print("Caso #{}: Raj trapaceou!".format(c+1))
        #se n se o jogo[1] estiver na lista de personagens que jogo[0] ganha:
        elif(jg[1] in personagens[jg[0]]["vence"]):
            #caso num Bazinga!
            print("Caso #{}: Bazinga!".format(c+1))
        #se n:
        else:
            #caso num De novo!
            print("Caso #{}: De novo!".format(c+1))
def pecaPeridida():
    """
    ler quantidade de peças
    
    ler a lista de peças que o carinha possui
    
    contador = 1
    enquanto contador for menor que a ou igual quantidade de peças:
        se contador não estiver na lista:
            mostra contador
            para o programa
        adiciona 1 em contador
    """
    
    #ler a quantidade de peças
    qntdP = int(input())
    #ler a lista de peças que o carinha possui
    p = [int(a) for a in input().split(" ")]
    
    #contador = 1
    contador = 1
    
    #enquanto contador for menor ou igual a quantidade de peças
    while contador <= qntdP:
        #se o contador não estiver em lista:
        if(contador not in p):
            #mostra o contador
            print(contador)
            #para o programa
            break
        #adiciona 1 em contador
        contador += 1
def semente():
    """
    ler o tamanho da fita e a quantidade de fitas iniciais
    
    ler as posicoes iniciais
    
    calcular a distancia de cada cada ponto inicial até onde ele consegue ir
    adicionando esses valores em uma lista
    se 1 ponto inicial estiver ligado a outro, a diferença é dividida por 2
    
    mostrar a maior diferença
    """
    #lista das diferenças
    diferencas = []
    #ler o tamanho da fita e a quantidade de fitas iniciais
    v = [int(i) for i in input().split(" ")]
    
    #ler as posicoes iniciais
    posicoes = [int(a) for a in input().split(" ")]
    
    #para cada posição:
    for n, p in enumerate(posicoes):
        #se for a primeira posição:
        if(n == 0):
            #calcula a diferença da posicao até 1
            dif = p-1
            #adiciona a diferença em diferenças
            diferencas.append(dif)
            
        #se tiver mais algum item na lista:
        try:
            #calcula a diferença entre ele, divide por 2 e arredonda para cima
            dif = math.ceil(((posicoes[n+1]-1)-p)/2)
            #adiciona essa diferença em diferenças
            diferencas.append(dif)
        #se não:
        except:
            #calcula a diferença entre o final da lista e ele
            dif = v[0]-p
            #adiciona em diferenças
            diferencas.append(dif)
    
    #ordenada a lista diferenças em ordem decrescente
    diferencas.sort(reverse=True)
    #mostra o primeiro valor
    print(diferencas[0])


while True:
    resgateEmQuedaLivre()
