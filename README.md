# AprenderMesmoEngine

Motor de produção de vídeos educativos em Manim para o canal **Aprender Mesmo**.

## Requisitos

- Windows
- Git
- VS Code
- Python 3.13
- FFmpeg

> Não usar Python 3.14 neste projeto enquanto as dependências do Manim não tiverem suporte estável no Windows.

## Primeira instalação num computador

### 1. Clonar o repositório

```powershell
git clone https://github.com/project021126-crypto/AprenderMesmoEngine.git
cd AprenderMesmoEngine

2. Criar o ambiente virtual
py -3.13 -m venv .venv

3. Ativar o ambiente virtual
.venv\Scripts\Activate.ps1

4. Instalar todas as dependências
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Trabalhar nos dias seguintes

Abrir a pasta no VS Code e executar:

python -m pip install -r requirements.txt


Renderizar um episódio
python -m engine.render universo ep001_eclipse Episodio001Eclipse -q l




Estrutura principal

engine/                  Motor reutilizável
episodios/               Código de cada episódio
assets/                  Imagens, personagens, sons e fontes
docs/                    Regras e documentação técnica
scripts/                 Automatizações
requirements.txt         Dependências Python


Organização dos episódios

episodios/
├── universo/
│   ├── ep001_eclipse.py
│   ├── ep002_lua.py
│   └── ep003_marte.py
├── matematica/
├── fisica/
└── quimica/


