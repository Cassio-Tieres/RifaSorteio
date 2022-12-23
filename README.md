# Tecnologias

* Python 3.11.1
* PyInstaller

# Libs

* Random (as rd) --> Para randomizar os itens da lista
* Time (as t) --> Aplica um temporizador na duração de execução do programa.

# Como funciona esse código?

1. Primeiro a importação das libs necessárias para que esse código funcione <br>
![imports](https://user-images.githubusercontent.com/68880880/209251550-7e32bac5-693c-4f2c-8d45-9440208f9399.png)

2. Cria uma lista contendo todas as informações (no caso, os números da rifa) dentro de uma variável chamada  lista_de_numeros_rifa <br>
![lista rifa code](https://user-images.githubusercontent.com/68880880/209251805-90b8a523-c270-4f99-81f4-673ae2ed25dc.png) <br>
(Veja que os valores escritos foram do tipo String, isso acontece pois a biblioteca Random não consegue randomizar valores int ou float).

3. Criamos as funcionalidades do sistema, ou seja, criamos uma def (uma definição/função), chamada de iniciaprograma()). <br>
Basicamente, todos os códigos necessários estão nessa def.

* Utilizamos o método print para imprimir as informações para o usuário
* Depois um loop for que percorre todos os itens da lista_de_numeros_rifa e imprime cada item na tela, um abaixo do outro
* Criamos uma variável que irá armazenar um dado digitado pelo usuário utilizando a função input
* Utilizamos um if/ELSE para validar se a resposta do usuário é S ou N e caso seja S utilizei um loop while para imprimir um tipo de loading...ao final do 
while a vem, enfim, o resultado da rifa. Caso o dado inserido pelo usuário seja um N (ou outro valor), o programa irá dar um reload e irá começar novamente.

![def inicia](https://user-images.githubusercontent.com/68880880/209252924-6d0ac5e2-18cb-4a17-b5a3-d4e0be6f64ce.png)


4. Por fim, chamamos a função iniciaprograma() para que o programa seja carregado e chamaos também a lib Time (como t) utilizando o método sleep(), onde definimos que 
a tela do programa irá ser fechada após 5s aberta. <br>
![chama funcoes](https://user-images.githubusercontent.com/68880880/209252984-b20a019d-bbd8-4b67-a9c5-5bab35f382ac.png)
