==========================
Flisol Tweets
==========================

Sistema que irá capturar os tweets que contenha a hashtag ``#flisoldf`` usando o **Twitter API**.

Instalação
--------------------------

A instalação do sistema, é recomendado usar o ``virtualenv`` para isolar toda e qualquer dependência do
projeto, sem afetar o sistema::

1. Crie um ambiente isolado com virtualenv::

    $ virtualenv --no-site-packages flisoltweets
    $ cd flisoltweets/
    flisoltweets$ source ./bin/activate

2. Faça o checkout do projeto::

    (flisoltweets)$ git clone https://github.com/gilsondev/flisol-tweets src

3. Instale as dependências no ambiente desejado (produção: requirements.txt, desenvolvimento: requirements_dev.txt)::

    (flisoltweets)$ cd src
    (flisoltweets) src$ pip install -r requirements.txt

Licença: GPL
