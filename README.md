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
   - Pesquiser por EC2.


   - ![alt text](img\image_5.png)

   -Após isso clique em instâncias.

   ![alt text](img\image6.png)


   - Crie uma nova instância EC2 clicando em executar.


   ![alt text](img\image_7.png)


   - Os principais detalhes são selecionar uma maquina Ubunto , um tipo de instancia , e a criação de uma chave privada do tipo .ppk
   
   ![alt text](img\image.png)
   ![alt text](img\image_2.png)
   ![alt text](img\image_3.png)
   - Ao criar a chave, o download dela e feito automaticamente 
   - Um detalhe importante é permitir o tráfego SSH de qualquer origem, considerando que este projeto é voltado para fins de estudo 
   ![alt text](img\image_4.png)
   - Agora clique em executar a instância
2. **Conectar-se à Instância via PuTTY:**
   - Converta a chave PEM para PPK usando o PuTTYgen.
   - Configure PuTTY para conectar à instância EC2 utilizando o arquivo PPK.
   - Acesse a instância via SSH.

3. **Instalar PostgreSQL no Servidor:**
   - Atualize os pacotes do sistema:
     ```bash
     sudo apt update && sudo apt upgrade
     ```
   - Instale o PostgreSQL:
     ```bash
     sudo apt install postgresql postgresql-contrib
     ```

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
