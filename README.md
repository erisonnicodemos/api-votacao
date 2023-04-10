# Sistema de votação
O objetivo deste projeto é desenvolver uma API em Python, implementando um CRUD simples para receber inscrições do BBB 24. Para isso, utilizamos o framework web FastAPI, que é conhecido por sua alta performance e facilidade de uso, além de oferecer recursos úteis para a construção de APIs, como a validação automática de dados de entrada, a documentação automática da API.

## Estrutura do projeto
O projeto utiliza uma arquitetura MVC (Model-View-Controller), que separa a lógica de negócios da aplicação (Model), da interface do usuário (View) e da interação entre os dois (Controller). Essa arquitetura ajuda a manter o código organizado e fácil de entender, permitindo a escalabilidade e manutenção do código. A estrutura de diretórios do projeto é a seguinte:

```
├── controllers
│   ├── candidate_controller.py
│   ├── paredao_controller.py
│   └── vote_controller.py
├── main.py
├── model
│   ├── candidate_model.py
│   ├── paredao_model.py
│   └── vote_model.py

```
## Banco de Dados
O projeto utiliza o SQLite como banco de dados, que é uma boa opção para pequenos bancos de dados. No entanto, para bancos de dados maiores ou de alta demanda, outros bancos de dados mais escaláveis, como o PostgreSQL ou MySQL, podem ser mais apropriados. Além disso, outras considerações de performance, como a otimização de consultas e o uso de cache, podem ser importantes para garantir a melhor performance possível.

## Melhorias de Escalabilidade
Para lidar com múltiplos votos simultâneos, uma melhoria que poderia ser implementada seria a utilização de um sistema de filas para gerenciar o processamento dos votos. Isso permitiria enfileirar os votos em uma fila e processá-los em segundo plano de forma assíncrona, reduzindo a carga do sistema e melhorando a performance. O uso de filas pode ser implementado com bibliotecas como Celery ou RabbitMQ.

Outra melhoria seria o uso do Kubernetes para gerenciar a infraestrutura da aplicação, permitindo a escalabilidade horizontal e a tolerância a falhas. Com o Kubernetes, é possível aumentar dinamicamente o número de réplicas de contêineres da aplicação para atender a demanda crescente de votação.

# Front-end
Caso seja necessário desenvolver um frontend para consumo da API o Next.js seria uma boa opção para o frontend, devido à sua facilidade de uso e escalabilidade, bem como sua capacidade de oferecer uma experiência de usuário rápida e responsiva. O Next.js também fornece recursos úteis, como a pré-renderização, roteamento dinâmico e geração de páginas estáticas, permitindo que as páginas sejam carregadas rapidamente.
