# Projeto: Servidor de Banco de Dados na AWS

## Descrição
Este projeto tem como objetivo hospedar um banco de dados PostgreSQL na nuvem AWS, utilizando instâncias EC2 para provisionamento do servidor. Ferramentas adicionais como PuTTY, DBeaver e Python são empregadas para acesso e gerenciamento do banco de dados.

## Ferramentas Utilizadas
- **AWS EC2:** Instâncias na nuvem para hospedar o banco de dados.
- **PuTTY:** Cliente SSH para acesso remoto seguro ao servidor.
- **DBeaver:** Ferramenta GUI para administração e interação com o banco PostgreSQL.
- **Python:** Scripts para enviar os dados de um arquivo csv local para o banco.

## Como Configurar
1. **Provisionar Instância EC2:**
   - Acesse o AWS Management Console.

   ![alt text](image.png)


   - Pesquiser por EC2.

   ![alt text](image-1.png)


   - Após isso clique em instâncias.

   ![alt text](image-2.png)


   - Crie uma nova instância EC2 clicando em executar.

   ![alt text](image-3.png)


   - De um nome a sua instância

   ![alt text](image-4.png)

   - Você deve escolher um sistema operacional para a instância no caso irei escolher o ubunto porque é mais facil de configurar é gratuito após isso deve se  disso deve se escolher um tipo de instância no caso irei escolher a t2.micro que é gratuita

   ![alt text](image-5.png)


   ![alt text](image-6.png)


   - Após isso você deve criar uma par de chaves de login você deve dar um nome para elas , além disso devem ser criadas no tipo ppk pois iremos utilizar o putty para nos ajudar com este projeto, ao criar um par de chaves elas serão baixadas no seu computador guarde elas pois serão usadas mais tarde

   ![alt text](image-7.png)

   ![alt text](image-8.png)


   - Um detalhe importante que preciso comentar são sobre os grupos de segurança onde por este projeto ser para fins de aprendizado iremos setar para permitir o tráfego SSH de qualquer ip 

   ![alt text](image-9.png)


   - Agora clique em executar a instância

   ![alt text](image-11.png)




2. **Conectar-se à Instância via PuTTY:**
   - Agora iremos conectar ao Putty, primeiramente em instâncias precisamos pegar algumas informações, clicando no ID da instância onde você consegue ter acesso as informações:

   ![alt text](image-13.png)


   - Clique em conectar, e vá ate a parte de cliente SSH.

   ![alt text](image-15.png)

   ![alt text](image-16.png)


   - Agora para podermos configurar o putty iremos pegar algumas informações como o servidor de dns público , o usuario que é ubunto e a chave de acesso que foi baixada no seu computador durante este processo também será necessária.

   ![alt text](image-20.png)


   ![alt text](image-18.png)


   ![alt text](image-19.png)



   
   - Após este processo iremos iniciar a conexão que ira abrir um prompt como este .

   ![alt text](image-21.png)

   - Após rodar estes codigos no prompt iremos criar um tunnel de SSH e nosso banco não ficar exposto na internet 

   - Você ira adicionar está etapa a conexão que ja tinha feito antes com o tunnel criado iremos para o dbeaver

   ![alt text](image-23.png)

   - com o dbeaver aberto iremos adicionar o banco de dados aos acessos dele 

   ![alt text](image-24.png)

   - Após a conexão ele vai estar assim : 

   ![alt text](image-25.png)

   - nesta parte iremos criar um script sql para criamos as tabelas 

   ![alt text](image-26.png)

   ![alt text](img.png)

   - agora iremos rodar nosso script para inserir os dados do nosso arquivo csv no banco de dados 

   ![alt text](img-1.png)

   - por fim iremos fazer uma verificação para ver se os dados foram realmente inseridos : 

   ![alt text](img-2.png)

