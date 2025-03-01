# 📧 Auto Responder de E-mails com Python

![Badge](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)


Este projeto automatiza a leitura e resposta de e-mails recebidos por uma conta específica. Ele identifica palavras-chave no e-mail, busca a resposta correspondente em um banco de dados SQLite e envia uma resposta automática.

## 🚀 Funcionalidades

- ✅ Ler e-mails não lidos de uma conta específica
- ✅ Identificar palavras-chave no corpo do e-mail
- ✅ Buscar respostas no banco de dados SQLite
- ✅ Enviar respostas automáticas com `smtplib`
- ✅ Marcar os e-mails como lidos após responder

## 🛠 Tecnologias Utilizadas

- `Python` 🐍 (linguagem principal)
- `imaplib` 📩 (leitura de e-mails)
- `smtplib` 📤 (envio de e-mails)
- `sqlite3` 🗄️ (banco de dados para respostas padrão)
- `email` ✉️ (manipulação do conteúdo dos e-mails)

## 🔧 Instalação e Configuração

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual e ative:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure suas credenciais de e-mail no arquivo `auto_responder.py`:

   ```python
   EMAIL_USER = "seu-email@gmail.com"
   EMAIL_PASS = "sua-senha-de-aplicativo"
   ```

   ⚠️ **Use uma senha de aplicativo!** Se estiver usando Gmail, ative a autenticação em dois fatores e gere uma senha de aplicativo em [Google Account Security](https://myaccount.google.com/security).

## 📜 Passo a Passo

1. Criar o banco de dados SQLite:

   ```bash
   python criar_bd.py
   ```

   Isso criará o arquivo `respostas.db` contendo respostas automáticas predefinidas.

2. Executar o script de respostas automáticas:

   ```bash
   python auto_responder.py
   ```

   O script acessará sua caixa de entrada, verificará e-mails não lidos, buscará respostas e enviará automaticamente.

## 🔥 Exemplo de Uso

📩 **E-mail recebido:**

```text
Assunto: Garantia do produto  
Corpo: Olá, gostaria de saber sobre a garantia dos produtos.  
```

💡 **Resposta automática enviada:**

```text
Assunto: Re: Garantia do produto  
Corpo: Todos os produtos possuem garantia de 1 ano contra defeitos de fabricação.  
```

## 🚀 Possíveis Melhorias Futuras

- 🔹 Melhorar a análise semântica para entender perguntas mais complexas
- 🔹 Criar uma interface gráfica para facilitar a configuração
- 🔹 Integrar com APIs de CRM para análise de clientes

## 🤝 Contribuição

Sinta-se à vontade para contribuir! Para isso:
1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b minha-feature`).
3. Faça commit das suas alterações (`git commit -m 'Adicionando minha feature'`).
4. Envie para o repositório remoto (`git push origin minha-feature`).
5. Abra um Pull Request.

## 📜 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

_Made with ❤️ by [Alex](https://github.com/alexwithrock)_
