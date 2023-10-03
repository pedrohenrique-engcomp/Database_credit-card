**Dataset Link:** [https://www.kaggle.com/mlg-ulb/creditcardfraud](https://www.kaggle.com/mlg-ulb/creditcardfraud)

1. Primeiro, crie um ambiente virtual no terminal  Visual Studio através do seguinte comando:


```virtualenv venv```



**OBSERVAÇÃO:** "venv" é o nome do ambiente virtual. Você pode dar o nome que preferir.

2. Em seguida, ative o ambiente virtual:

No Windows:

```venv\Scripts\activate```


Em sistemas baseados em Unix (Linux, macOS):

```source venv/bin/activate```



3. Instale os requisitos do arquivo `requirements.txt` com o seguinte comando:

```pip install -r requirements.txt```



4. (OPCIONAL) Crie um superusuário executando o seguinte comando na raiz do diretório:

```python manage.py createsuperuser```



5. Inicie o servidor digitando o seguinte comando:

```python manage.py runserver```



**OBSERVAÇÃO:** Se você estiver adicionando algum modelo em `models.py` ou fazendo alguma alteração, não se esqueça de criar as migrações e aplicá-las ao banco de dados:


```python manage.py makemigrations```

```python manage.py migrate```

6. Install 'pandas' using pip:

```pip install pandas```


Dessa forma, você estará pronto para começar a trabalhar no seu projeto Django! Lembre-se de adaptar os comandos conforme necessário ao seu ambiente de desenvolvimento.



