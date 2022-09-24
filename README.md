# Rossmann Sales Prediction
-  A regression project that uses ML Model to predict how much money Rossmann company will receive in the next 6 weeks.

## **Empresa:**

-  Dirk Rossmann GmbH


## **Sobre a Empresa?**

-  A Rossmann é uma das maiores cadeias de **drogarias** da **Europa**, com cerca de **56.200 funcionários** e mais de **4.000 lojas**.
Em **2019**, a Rossmann teve um faturamento de mais de **€ 10 bilhões** na Alemanha, Polônia, Hungria, República Tcheca, Turquia, Albânia, Kosovo e Espanha.


## **Qual o problema de negócio?**

-  O **CFO** da empresa quer saber qual será a **previsão de venda**s das próximas **6 semanas**, de cada loja da **Rossmann** espalhadas por toda Europa, para saber qual será o **budget** destinado à **reforma** das respectivas **lojas**.


## **Objetivo do desafio?**

-  O **desafio** consiste na construção de um **modelo** de aprendizado de máquina de **regressão** para realizar a **previsão de vendas** de cada **loja**.

-  Ao final, devem ser apresentados os **resultados obtidos** bem com o anexo de uma **coluna** chamada **"previsão"** com os **valores encontrados** pelo **modelo treinado**.


## **Sobre os Dados:**

 * **Store:** ID único de cada Store.
 * **Sales:** A quantidade de vendas naquele dia.
 * **Customers:** A quantidade de clientes naquele dia.
 * **Date:** O dia do dado.
 * **DayOfWeek:** Dia da Semana.
 * **Open:** 0 = Loja Fechada; 1 = Loja Aberta.
 * **StateHoliday:** a = Feriado Público; b = Feriado de Páscoa; c = Natal; 0 = None.
 * **SchoolHoliday:** Indica se a Loja naquela data foi afetada pelo fechamento de escolas públicas.
 * **StoreType:** Diferencia entra os 4 tipos de modelo: a; b; c; d.
 * **Assortment:** Indica o tipo de sortimento tem a loja: a = Básico; b = Extra, c = Extendido.
 * **CompetitionDistance:** Indica a distância, em metros, do concorrente mais próximo.
 * **CompetitionOpenSince[Year/Month]:** Indica o ano e mês, aproximados, que o concorrente mais próximo abriu.
 * **Promo:** Indica se a Loja está tendo promoção naquele dia.
 * **Promo2:** Indica se a Loja tem uma promoção extendida: 1 = Loja não participante; 0 = Loja participante.
 * **Promo2Since[Year/Week]:** Descreve o ano e a semana do calendário que a Loja começou a ter promoção extendida.
 * **PromoInterval:** Descreve os 4 meses em que há promoção extendida.



-  No total a base de **dados** contém **1017209 linhas** com **18 colunas**.
-  Como **variável resposta** temos a coluna **Sales**.

## **Que tipos de perguntas devemos responder?**

**1)** Quais são as **previsões de venda** para cada **loja**?

**2)** Qual o **melhor cenário** dado a previsão?

**3)** Qual o **pior cenário** dado a previsão?
