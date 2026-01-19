[readme_whats_app_bot_scheduler.md](https://github.com/user-attachments/files/24719823/readme_whats_app_bot_scheduler.md)
# 🤖 WhatsApp Bot Scheduler (Selenium + Python)

Este projeto é um **bot de envio automático de mensagens pelo WhatsApp Web**, utilizando **Python, Selenium e systemd**, com agendamento diário configurável.

Ele foi desenvolvido para rodar em **VPS / servidor Linux**, funcionando em background mesmo após fechar o terminal.

---

## 🚀 Funcionalidades

- ✅ Envio automático de mensagens pelo WhatsApp Web
- ⏰ Agendamento diário por horário (hora e minuto)
- 🔁 Execução contínua em background via `systemd`
- 🧠 Uso de perfil persistente do Chrome (mantém login)
- 📸 Captura de screenshots para debug

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Selenium
- Google Chrome
- ChromeDriver (via `webdriver-manager`)
- systemd (Linux)

---

## 📂 Estrutura do Projeto

```
whatsapp-bot/
├── chrome/
│   └── profile/          # Perfil persistente do Chrome (WhatsApp logado)
├── src/
│   ├── main.py           # Entry point do sistema
│   ├── scheduler.py      # Agendador (schedule)
│   ├── whatsapp.py       # Lógica de envio da mensagem
│   └── config.py         # Configurações gerais
├── venv/
├── debug_erro.png
├── debug_erro_final.png
└── mensagem_enviada.png
```

---

## ⚙️ Configuração

### 1️⃣ Variáveis de Ambiente

Configure as variáveis no sistema ou no serviço `systemd`:

```bash
export WHATSAPP_NUMBER=5586999999999
export CHROME_PROFILE_PATH=/opt/whatsapp-bot/chrome/profile
```

---

### 2️⃣ Arquivo `config.py`

```python
WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")
MESSAGE = "Testando um negócio"

SEND_HOUR = 12
SEND_MINUTE = 17
```

> ⚠️ O horário é baseado no **timezone da VPS**.

---

## 🧪 Primeiro Uso (Login no WhatsApp Web)

1. Execute o bot manualmente uma vez:

```bash
python src/main.py
```

2. O Chrome abrirá
3. Faça login no WhatsApp Web via QR Code
4. Feche o navegador

O login ficará salvo no perfil configurado.

---

## ▶️ Executando Manualmente

```bash
source venv/bin/activate
python src/main.py
```

---

## ⚙️ Executando em Background (systemd)

### Exemplo de serviço: `/etc/systemd/system/whatsapp-bot.service`

```ini
[Unit]
Description=WhatsApp Bot
After=network.target

[Service]
User=root
WorkingDirectory=/opt/whatsapp-bot
ExecStart=/opt/whatsapp-bot/venv/bin/python src/main.py
Restart=always
Environment=WHATSAPP_NUMBER=5586999999999
Environment=CHROME_PROFILE_PATH=/opt/whatsapp-bot/chrome/profile

[Install]
WantedBy=multi-user.target
```

Ativar o serviço:

```bash
systemctl daemon-reload
systemctl enable whatsapp-bot
systemctl start whatsapp-bot
```

Ver logs:

```bash
journalctl -u whatsapp-bot -f
```

---

## 📸 Debug e Logs

- `mensagem_enviada.png` → screenshot após tentativa de envio
- `debug_erro.png` / `debug_erro_final.png` → erro ao localizar elementos

Esses arquivos ajudam a entender se:

- A conversa abriu
- O campo de texto estava disponível
- A mensagem foi digitada

---

## ⚠️ Observações Importantes

- O WhatsApp Web **não é oficialmente suportado para automação**
- XPath pode mudar a qualquer momento
- O envio pode falhar se:
  - WhatsApp não estiver logado
  - Layout mudar
  - Internet instável

Este projeto é indicado para **uso pessoal, estudos ou MVP**.

---

## 📌 Próximas Melhorias (Ideias)

- ⏳ Espera inteligente com `WebDriverWait`
- 🔁 Retry automático em caso de falha
- 🧪 Teste de presença do input antes de enviar
- 📲 Integração com WhatsApp Cloud API

---

## 📄 Licença

Projeto de uso livre para fins educacionais e pessoais.

---

💬 Qualquer melhoria, ajuste ou dúvida — fique à vontade para contribuir!
