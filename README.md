# 🤖 Automação de Cadastro de Produtos com Playwright

Projeto desenvolvido a partir da Atividade 1 da Jornada Python, com foco em automação de tarefas repetitivas na web.

A versão inicial da atividade utilizava PyAutoGUI para simular cliques e digitação. Nesta versão, o projeto foi otimizado com auxílio de Inteligência Artificial, substituindo a automação por coordenadas fixas por uma abordagem mais robusta, eficiente e profissional utilizando Playwright.

---

## 🚀 Objetivo

Automatizar o cadastro de produtos em um sistema web, realizando:

- Acesso ao sistema
- Login automático
- Leitura de produtos via arquivo CSV
- Preenchimento automático dos campos
- Cadastro em massa dos produtos

---

## 🧠 Otimização com Inteligência Artificial

Após a conclusão da atividade original, o projeto passou por um processo de refatoração com apoio de IA para melhorar sua estrutura, eficiência e robustez.

A IA foi utilizada como ferramenta de apoio técnico para revisar a arquitetura, reduzir repetições, melhorar a organização do código e aplicar boas práticas de desenvolvimento Python.

Entre as melhorias realizadas estão:

- Substituição do PyAutoGUI por Playwright
- Eliminação de coordenadas fixas
- Redução de repetição de código
- Separação de responsabilidades
- Uso de variáveis de ambiente
- Validação da base CSV
- Tratamento de erros
- Estrutura modular do projeto

---

## 🛠️ Tecnologias utilizadas

- Python
- Playwright
- Pandas
- Python-dotenv

---

## 📂 Estrutura do projeto

```bash
├── main.py
├── config.py
├── automacao.py
├── login.py
├── utils.py
├── requirements.txt
├── produtos.csv
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Funcionalidades

- Login automatizado no sistema
- Leitura de dados a partir de arquivo CSV
- Cadastro automático de produtos
- Tratamento de campos vazios
- Tratamento de erros durante a execução
- Organização modular do código
- Separação entre configuração, login, automação e execução principal

---

## 🔐 Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
EMAIL=pythonimpressionador@gmail.com
SENHA=sua senha
```

> O arquivo `.env` não deve ser enviado ao GitHub.

---

## 📦 Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Acesse a pasta do projeto:

```bash
cd automacao-cadastro-produtos
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Instale os navegadores necessários para o Playwright:

```bash
playwright install
```

---

## ▶️ Como executar

Execute o projeto com:

```bash
python main.py
```

---

## 📌 Diferença entre a versão original e a versão otimizada

| Versão original | Versão otimizada |
|---|---|
| PyAutoGUI | Playwright |
| Coordenadas fixas | Seletores HTML |
| Código sequencial | Código modular |
| Maior dependência da tela | Maior estabilidade |
| Menor escalabilidade | Melhor manutenção |
| Dados sensíveis no código | Uso de `.env` |

---

## 📚 Aprendizados

Este projeto contribuiu para o desenvolvimento de conhecimentos em:

- Automação web
- Refatoração de código
- Playwright
- Manipulação de dados com Pandas
- Variáveis de ambiente
- Organização modular
- Tratamento de exceções
- Boas práticas em Python
- Uso estratégico de IA no desenvolvimento

---

## 🔮 Próximas melhorias

- Implementar logs de execução
- Gerar relatório de produtos cadastrados
- Criar interface gráfica
- Adicionar testes automatizados
- Integrar com banco de dados
- Dockerizar o projeto

---

## 👨🏽‍💻 Autor

Diego Montagnane

[LinkedIn](https://www.linkedin.com/in/diegomontagnane/)