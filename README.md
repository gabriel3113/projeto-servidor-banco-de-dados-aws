# Projeto: Servidor de Banco de Dados na AWS

## Descrição
Este projeto tem como objetivo hospedar um banco de dados PostgreSQL na nuvem AWS, utilizando instâncias EC2 para provisionamento do servidor. Ferramentas adicionais como PuTTY e DBeaver são empregadas para acesso e gerenciamento do banco de dados.

## Ferramentas Utilizadas
- **AWS EC2:** Instâncias na nuvem para hospedar o banco de dados.
- **PuTTY:** Cliente SSH para acesso remoto seguro ao servidor.
- **DBeaver:** Ferramenta GUI para administração e interação com o banco PostgreSQL.

## Como Configurar
1. **Provisionar Instância EC2:**
   - Acesse o AWS Management Console.

   ![alt text](img\image.png)


   - Pesquiser por EC2.

   ![alt text](img\image-1.png)


   - Após isso clique em instâncias.

   ![alt text](img\image-2.png)


   - Crie uma nova instância EC2 clicando em executar.

   ![alt text](img\image-3.png)


   - De um nome a sua instância

   ![alt text](img\image-4.png)

   - Você deve escolher um sistema operacional para a instância no caso irei escolher o ubunto porque e além disso escolher um tipo de instância no caso irei escolher a t2.micro que é gratuita

   ![alt text](img\image-5.png)


   ![alt text](img\image-6.png)


   - Após isso você deve criar uma par de chaves de login você deve dar um nome para elas , além disso devem ser criadas no tipo ppk pois iremos utilizar o putty para nos ajudar com este projeto, ao criar um par de chaves elas serão baixadas no seu computador guarde elas pois serão usadas mais tarde neste projeto

   ![alt text](img\image-7.png)

   ![alt text](img\image-8.png)


   - Um detalhe importante que preciso comentar são sobre os grupos de segurança onde por este projeto ser para fins de aprendizado iremos setar para permitir o tráfego SSH em qualquer lugar 

   ![alt text](img\image-9.png)


   - Agora clique em executar a instância

   ![alt text](img\image-11.png)




2. **Conectar-se à Instância via PuTTY:**
   - Agora iremos conectar ao Putty, primeiramente em instâncias precisamos pegar algumas informações, clicando no ID da instância você consegue ver as informações:

   ![alt text](img\image-13.png)


   - Clique em conectar, e vá ate a parte de cliente SSH.

   ![alt text](img\image-15.png)

   ![alt text](img\image-16.png)


   - Agora para podermos configurar o putty iremos pegar algumas informações o servidor de dns público , o usuario que é ubunto e a chave de acesso que foi baixada no seu computador durante este processo também será necessária.

   ![alt text](img\image-20.png)


   ![alt text](img\image-18.png)


   ![alt text](img\image-19.png)



   
   - Após este processo iremos iniciar a conexão que ira abrir um prompt como este .

   ![alt text](img\image-21.png)

   - Após rodar estes codigos no prompt iremos criar um tunnel de SSH e nosso banco não ficar exposto na internet 

   - Você ira adicionar está etapa a conexão que ja tinha feito antes com o tunnel criado iremos para o dbeaver

   ![alt text](img\image-23.png)

   - com o dbeaver aberto iremos adicionar o banco de dados aos acessos dele 

   ![alt text](img\image-24.png)

   - Após a conexão ele vai estar assim : 

   ![alt text](img\image-25.png)

   - nesta parte iremos criar um script sql para criamos as tabelas 

   ![alt text](img\image-26.png)

   ![alt text](img.png)

   - agora iremos rodar nosso script para inserir os dados do nosso arquivo csv no banco de dados 

   ![alt text](img\img-1.png)

   - por fim iremos fazer uma verificação para ver se os dados foram realmente inseridos : 

   ![alt text](img\img-2.png)













3. **Instalar PostgreSQL no Servidor:**
   
   - Agora iremos rodar os scripts que coloquei na primeira pasta

4. **Configurar o PostgreSQL:**
   - Inicie o serviço PostgreSQL:
     ```bash
     sudo systemctl start postgresql
     ```
   - Configure o PostgreSQL para aceitar conexões remotas, se necessário.

5. **Conectar ao Banco de Dados via DBeaver:**
   - Instale e configure o DBeaver.
   - Adicione uma nova conexão PostgreSQL usando o endereço público da instância EC2 e as credenciais configuradas.

## Considerações
- Certifique-se de proteger o servidor configurando corretamente as regras de firewall e utilizando autenticação segura.
- Use snapshots da instância para backup do banco de dados.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
