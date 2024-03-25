Esse repositório refere-se à função de recompensa do AWS DeepRacer, um módulo da AWS para treinamento de agentes de aprendizado por reforço, onde podemos alterar funções de recompensa, hiperparametros, ações e utilizar diversos ambientes, representados por diversas pistas que podem ser utilizadas para treino e testes.

---

# Função de Recompensa

Desenvolvida pela linguagem python, a função de recompensa que se encontra [aqui](./src/reward_function.py) se baseia em 3 estratégias que juntas foram escolhidas para o treinamento do modelo, são elas: 'Progresso ao longo do tempo', 'Distância do centro', 'Saiu da pista'. Para implementá-las, foram utilizado os seguintes parâmetros.

## Progresso ao longo do tempo
- **Track Length**: Representa o comprimento total da pista. É utilizada para a definição do número máximo de steps, dessa forma podemos definir uma velocidade esperada, dado que estamos "apressando" que o agente termine a volta.
<br>
<br>
- **Steps**: Representa o número de steps dados até o momento atual. Um step pode ser representado pela tomada de 1 ação, dado que para o modelo, podemos indicar como domínio um conjunto de parâmetros que representam o estado que ele se encontra e a imagem é a ação que será tomada. É utilizado para ver se o progresso do agente está além do esperado, em que o progresso esperado é dado pela razão dos steps atuais e o número máximo que pode ser dado, multiplicado por 100.
<br>
<br>
- **Progress**: Representa a porcentagem do trajeto realizada naquele momento. Assim como foi explicado no tópico referente ao parâmetro "Steps", é utilizado para a comparação do progresso atual com o esperado, recompensando caso ele esteja se saindo melhor que o esperado e punindo caso ele esteja se saindo pior.
<br>
<br>
## Distância do centro
- **Track Width**: Representa a largura da pista. É utilizado para calcular faixas que demarcam porcentagens da pista em relação ao centro, com isso o agente é recompensado cada vez mais que se aproxima do centro.
<br>
<br>
- **Distance from Center**: Representa a distância do centro. É utilizado para localizar em que faixa definida pela largura da pista o agente se encontra e dessa forma dar a devida recompensa que o agente merece.
<br>
<br>
## Saiu da pista
- **Is Offtrack**: Representa um valor booleano que diz se o carro inteiro se econtra fora da pista ou não. É utilizado para penalizar sempre que o agente foge da pista.