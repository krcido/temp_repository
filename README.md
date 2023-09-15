# Descrição do Projeto
Este projeto consiste em uma API gerenciadora de estoques. Nela tem-se a possibilidade de realizar operações CRUD com os registros de itens no banco de dados, além de viabilizar alocações, desalocações, registros de viaturas, geração de logs e controle de requisições. Para tanto utilizou-se as bibliotecas de Python **django** e **django rest framework** baseadas no padrão de projeto **Model View Template (MVT)**.  

# Model View Template
Este padrão de projeto contém camadas e fluxos de controle semelhantes ao padrão MVC(Model View Controller), nele a camada da *view* recebe a requisição do usuário, se comunica com o banco de dados através da camada *model*  e se comunica com os *templates* para fornecer uma renderização da resposta para o usuário. Assim, podemos concluir as seguintes equivalências com o padrão MVC:

*view* = **controller**
*model* = **model**
*template* = **view**


# Funcionamento do projeto
A pasta **samu** consiste na aplicação (API) e a pasta **core** nas configurações do projeto. O arquivo *urls.py* contido na pasta **core**  roteia as requisições do usuário e as direciona para os arquivos *urls* inseridos na API (ex: samu -> urls -> vehicleUrls.py). Nestes arquivos cada *url* invoca alguma das classes *view*, que estão contidas na pasta **view** da aplicação (ex: samu -> views -> equipments -> addEquipmentView.py ). Estas classes fazem a interação com as classes *model* e com as classes *serializers* para permitir operações com o *banco de dados* e a serialização das respostas das requisições.



# A fazer
- Revisão da organização
- Conectar com o banco de dados postgree
- Implementação
- Documentação
- Testes
