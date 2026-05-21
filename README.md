# Repositório do projeto do grupo 8 de Banco de Dados e IA - 1° Período.
## Alunos: Lucas Oliveira, Pedro Pereira, Mateus Tarcísio, Daniel Lucas, Breno Neves, Romeu Alves


### escrito por mim (Lucas)
### Pessoal, leiam:
### NÃO TRABALHE NA BRANCH MAIN OU DEVELOP!!!!!
### Cada um vai ter uma branch (ramificação) para trabalhar na parte do seu código, com o seu respectivo nome:
### após clonar o repositorio, dê o comando:

## git pull

##### para atualizar o seu repositorio local com o remoto do github
##### depois, faça o comando

## git fetch

### para baixar todos os arquivos e branches (ramificações) do github remoto para a sua máquina.
### depois, faça o comando

## git branch -a OU git branch --all

### para mostrar todas as branches (ramificações) existentes. Você deve entrar na ramificação com o seu nome.
### depois, faça o comando

## git checkout nome-da-ramificação

### para entrar na sua ramificação.

### COMO FAZER ALTERAÇÕES E MANDAR PARA O REPOSITÓRIO REMOTO - GITHUB - A PARTIR DO GIT BASH

### Para fazer / mandar um arquivo da sua ramificação de trabalho (a ramificação com o seu nome), aqui estão alguns
### comandos opcionais que você pode fazer.

## mkdir
### esse comando cria uma pasta. Pode ser útil para se organizar e não ficar confuso

## cp nome-do-arquivo local-atual local-novo
### esse comando serve para copiar o arquivo de um lugar para o outro.
### NÃO faça isso para copiar de uma branch para outra.
### Nota: se você já está no local do arquivo que você deseja copiar, basta apenas colocar o nome e o local novo.

## vi nome-do-arquivo
### serve para você editar o arquivo no proprio terminal do git bash.
### Nota: se o arquivo não existe, ele vai criar um arquivo com o nome que você colocou. Porém, ele não será salvo caso você saia sem salvá-lo.
### aqui vão algumas teclas simples sobre o comando - vi -
### Tecla INSERT -> serve para você editar o arquivo
### para salvar o arquivo, você deve clicar na Tecla ESC
### quando você clica na Tecla ESC, você vai estar no modo normal (normal mode)
### no Modo Normal, você pode fazer alguns comandos:

### :x  vai salvar o arquivo
### :x! vai salvar o arquivo de forma forçada
### :q  vai sair do arquivo sem salvar
### :q! vai sair do arquivo sem salvar de forma forçada
### Quando um desses comandos forem realizados, você vai sair automaticamente do modo de edição do arquivo.

### O que fazer depois de editar um arquivo?

### Faça um git status, veja os arquivos que precisam ser "empacotados" para fazer o Commit.
### depois, faça um git add nome-do-arquivo (ou git add . se você estiver seguro com o que estiver fazendo)
### depois, faça um git commit -m "mensagem explicando o que você fez"
### depois, faça um git push. O arquivo será salvo na sua ramificação no github
