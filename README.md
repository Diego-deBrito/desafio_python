# 📝 Desafio Técnico – RPA 

##  Objetivo

Criar uma automação que processe uma planilha de novos clientes, valide os dados e realize:

1. Cadastro automático em um sistema web (formulário de exemplo).
2. Validação de CPF e e-mail.
3. Envio de e-mail de boas-vindas.
4. Registro dos clientes em um banco de dados ou planilha de histórico.

O candidato pode usar **Python, Make ou n8n** – a escolha é livre.

---

## 📂 Entrada

O processo receberá diariamente uma planilha Excel com as seguintes colunas:

* Nome
* CPF
* E-mail
* Telefone
* Data de Nascimento

Exemplo:

| Nome           | CPF         | E-mail                                    | Telefone    | Data de Nascimento |
| -------------- | ----------- | ----------------------------------------- | ----------- | ------------------ |
| João Silva     | 12345678901 | [joao@email.com](mailto:joao@email.com)   | 11999999999 | 1990-01-01         |
| Maria Oliveira | 98765432100 | [maria@email.com](mailto:maria@email.com) | 21988887777 | 1985-05-12         |

---

## 🚀 Tarefas

1. **Leitura da planilha**

   * Ler todos os registros do arquivo.

2. **Validação**

   * Validar se o CPF está no formato correto (11 dígitos numéricos).
   * Validar se o e-mail segue formato válido.
   * Registrar em um **log de erros** os cadastros inválidos.

3. **Cadastro automático (RPA)**

   * Preencher os campos do formulário de cadastro em um sistema web (pode ser simulado com qualquer página de exemplo, como um formulário de teste).

4. **Notificação por e-mail**

   * Enviar mensagem de boas-vindas para cada cliente válido.

5. **Registro no histórico**

   * Salvar os dados processados em um banco (MySQL/Postgres/SQLite) ou em uma planilha Google Sheets.

---

## ⭐ Pontos Extras (Opcional)

* Agendamento automático (ex: rodar todos os dias às 9h).
* Dashboard simples com indicadores:

  * Cadastros realizados com sucesso.
  * Cadastros que falharam.
* Uso de boas práticas de código (em Python) ou fluxos bem documentados (em Make/n8n).

---

## 📦 Entregáveis

O candidato deve entregar:

* Código-fonte ou fluxo exportado (Make/n8n).
* Instruções de execução (README).
* Print/tela do processo funcionando.
* Arquivo de log de erros (se houver).

---

## 🕐 Tempo Estimado

**4 a 6 horas** (pode ser entregue em até 2 dias).

---

## 🏆 Critérios de Avaliação

1. **Funcionalidade (40%)** – Se o fluxo atende aos requisitos obrigatórios.
2. **Qualidade técnica (30%)** – Organização do código/fluxo, tratamento de erros e boas práticas.
3. **Clareza (20%)** – Documentação e facilidade de entender/executar a solução.
4. **Extras (10%)** – Dashboard, agendamento e melhorias além do pedido.

📁 Arquivos Disponíveis

Na raiz deste repositório você encontrará:

form.html → página com o formulário de cadastro que simula o sistema web.
Abra no navegador (duplo clique) para usar como ambiente de testes.

dados.csv → arquivo de entrada com dados inconsistentes.
Este é o arquivo que sua automação deve processar, limpar/validar e tentar cadastrar no formulário.
