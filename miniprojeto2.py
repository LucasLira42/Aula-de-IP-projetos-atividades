("\033[30;47mTexto Preto no Fundo Branco\033[m")
("\033[31;47mTexto Vermelho no Fundo Branco\033[m")
("\033[32;40mTexto Verde no Fundo Preto\033[m")
("\033[33;44mTexto Amarelo no Fundo Azul\033[m")
("\033[34;43mTexto Azul no Fundo Amarelo\033[m")
("\033[35;46mTexto Magenta no Fundo Ciano\033[m")
("\033[36;45mTexto Ciano no Fundo Magenta\033[m")
("\033[37;41mTexto Branco no Fundo Vermelho\033[m")


G="\033[32m"
Y="\033[33m"
r="\033[0m"
A="\033[34m"

print(f"Oi, Pode me chamar de {A}Din{r}!\nSou um assistente financeiro\ne vou te ajudar com as contas e os objetivos.\n")

print("[DADOS PESSOAIS]\n")

print(f"Primeiro preciso de algumas informações\nMe diz teu {Y}nome{r}:", end="")
name = input("")
print(f"O {Y}dia{r} em que tu nasceu:",end="")
day=input()
print(f"Agora o {Y}mês{r}:",end="")
month=input()
print(f"E o {Y}ano{r}:",end="");year=input()
print("\n")

print("- - -\n")

print(f"Muito bem, então conferindo seus dados, estou registrando aqui.\n{G}{name}{r} nascimento em {G}{day}/{month}/{year}{r}\n")

print("[DADOS FINANCEIROS]\n")

print(f"Agora me infoma por favor alguns dados financeiros\nSe você somar o dinheiro que tem guardado, me diz o toal desse {Y}patrimônio{r}: R$",end="");totalp=float(input())
print(f"Me diz teu {Y}salário{r}: R$",end=""); slrio= float(input())
print("Sobre os seus gastos, me informa em partes por favor.")
print(f"Quanto custa teu {Y}aluguel{r},(incluindo condomínio e outras taxas): R$",end=""); aluguel=float(input())
print(f"Mais ou menos qunato você gasta fazendo {Y}feira{r} todo mês?: R$",end=""); feira=float(input())
print(f"E com {Y}comida{r} fora de casa, em média da quanto? R$",end=""); comida=float(input())
print(f"Na mobilidade, quanto que gasta com {Y}transporte{r} (ônibus,uber,gasolina,etc)? : R$",end=""); transporte=float(input())
print(f"Pra terminar, quanto você gasta com {Y}outros{r} (lazer,roupas,etc)? : R$",end=""); outros=float(input())
print("\n")
gastost= (aluguel + feira + comida + transporte + outros)

print("- - -")
print("\n")

print(f"Obrigado {G}{name}{r}, resumindo as informações financeiras até agora:\nOs seus gastos discriminados são:")
print(f"{G}Aluguel{r}: R$ {aluguel}")
print(f"{G}Feira{r}: R$ {feira}")
print(f"{G}Comida{r}: R$ {comida}")
print(f"{G}Transporte{r}: R$ {transporte}")
print(f"{G}Outros{r}: R$ {outros}")
print(f"{G}Gastos totais{r}: R$ {gastost}")
print("\n")
Result= slrio-gastost

print("- - -")
print("\n")

print(f"Pra termina, calculando o seu saldo mensal, com base em todos os gastos\ne no teu salário, o valor resultante é de {G}R$ {Result} {r}")
print(f"Desse valor,considerando que qualquer investimento é válido,\no quanto você conseguiria {Y}investir{r} todo mês? : R$",end=""); invest=input()
print(f"Ok, anotado, o valor do investimento mensal é {G}R$ {invest}{r}")
print("Acredito que coletei todas as informações")













