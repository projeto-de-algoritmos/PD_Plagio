# Plagio


**Número da Lista**: 26<br>
**Conteúdo da Disciplina**: Final<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0011267  |  Giovanna Borges Bottino        |
| 18/0119818  |  Felipe Boccardi Silva Agustini |

## Sobre 
O projeto Plagio é um programa para detectar plagio. O software consiste em um sistema que utiliza do algoritimo de alinhamento de sequencia para trazer a porcentagem de similaridade entre dois textos.

## Screenshots

![imagem 1](/public/1.png)

![imagem 2](/public/2.png)

![imagem 3](/public/3.png)

## Video 

https://user-images.githubusercontent.com/23579166/216804214-bc337bd1-b675-4a6e-83d3-9da00951b2f4.mp4

## Instalação 
*Linguagem*: Python<br>
*Framework*: flask<br>

### Crie um ambiente em python 3
```
python3 -m venv env
```

### Ative o ambiente
```
source env/bin/activate
```
ou se estiver usando windows

```
.\env\Scripts\activate
```
### Instale as dependencias
```
pip install -r requirements.txt
```

## Uso 

### Após a instalação entre na pasta

```
cd src/
```

### Rode executando o comando
```
flask run
```

## Testes 

Para rodar os testes basta executar o comando a baixo.
```
python -m unittest tests/unit/test_texto.py
```
