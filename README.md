# infra-devops-hw
Teste Técnico - Infraestrutura e DevOps | H&W Publishing

##  Descrição do Projeto

✅ Uma aplicação web simples em **Python Flask** que retorna "Hello World" e a porta de execução.  
✅ **Duas instâncias** rodando localmente em portas **5000** e **5001**.  
✅ O **Nginx** na instância EC2 faz o balanceamento de carga entre as duas instâncias.  
✅ Pipeline de **CI/CD com GitHub Actions** que faz deploy automático na EC2 sempre que houver push na branch `main`.

---

## ⚙️ Estrutura do Projeto

```
infra-devops-hw/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── app/
│   ├── server.py
│   └── requirements.txt
└── README.md
```

- **.github/workflows/deploy.yml:** Workflow do GitHub Actions para deploy automático.  
- **app/server.py:** Aplicação Flask simples.  
- **app/requirements.txt:** Dependências do projeto.  
- **README.md:** Documentação.

---

## 🌐 Como Executar Localmente

1️⃣ Clone o repositório:
```bash
git clone git@github.com:SEU_USUARIO/infra-devops-hw.git
cd infra-devops-hw/app
```

2️⃣ Instale as dependências:
```bash
pip install flask
```

3️⃣ Rode localmente em uma porta (ex.: 5000):
```bash
PORT=5000 python3 server.py
```

Abra no navegador:
```
http://localhost:5000
```

---

## ☁️ Como Funciona o Deploy Automático (CI/CD)

- O workflow (`.github/workflows/deploy.yml`) roda sempre que você fizer push para a branch `main`.
- Ele faz:
  ✅ Conexão SSH com a EC2 usando secrets configurados (`EC2_HOST`, `EC2_SSH_KEY`)  
  ✅ Copia o código do diretório `app/` para a EC2  
  ✅ Instala dependências no EC2  
  ✅ Mata qualquer processo Flask antigo (`5000` e `5001`)  
  ✅ Sobe duas instâncias Flask (`5000` e `5001`)

---

## 🌐 Configuração do Nginx (Balanceamento de Carga)

1️⃣ O Nginx está configurado na EC2 no arquivo:
```bash
/etc/nginx/sites-available/default
```

2️⃣ Configuração de balanceamento de carga:
```
upstream myapp {
    server 127.0.0.1:5000;
    server 127.0.0.1:5001;
}

server {
    listen 80;

    location / {
        proxy_pass http://myapp;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

3️⃣ Teste a configuração e reinicie o Nginx:
```bash
sudo nginx -t
sudo systemctl restart nginx
```

4️⃣ Acesse no navegador:
```
http://<IP_DA_EC2>/
```
✅ O Nginx vai alternar as requisições entre as portas 5000 e 5001 automaticamente.

---

## 🔑 Secrets do GitHub Actions

Para que o workflow funcione, configure os **Secrets** no repositório:
- `EC2_HOST`: IP público da sua EC2 (ex.: `xx.xx.xx.xx`)
- `EC2_SSH_KEY`: Conteúdo da sua chave privada `.pem` (NUNCA a chave pública!)

---

##  Resumo das Tecnologias

- **Python 3** e **Flask** para aplicação web simples.  
- **Nginx** como balanceador de carga.  
- **GitHub Actions** para pipeline de CI/CD.  
- **AWS EC2** como ambiente de deploy.

