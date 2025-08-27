# 🔐 Atividade de Criptografia - Auditoria e Segurança de Sistemas

Este projeto demonstra **criptografia simétrica (AES)** e **assimétrica (RSA)** em Python.

## O que é criptografia simétrica (AES)

1. É um algoritmo de chave simétrica, ou seja, a mesma chave é usada para cifrar e decifrar os dados.

2. Muito utilizado por ser rápido e seguro, padrão adotado pelo governo dos EUA e por diversos sistemas no mundo.

3. Ideal para proteger grandes volumes de dados.

## O que é assimétrica (RSA)

1. É um algoritmo de chave assimétrica, ou seja, utiliza um par de chaves:
   - Chave pública → usada para cifrar.
   - Chave privada → usada para decifrar.

2. Muito utilizado para segurança em comunicações (ex.: HTTPS, assinaturas digitais).

3. Embora seja mais seguro para troca de chaves, é mais lento que o AES, por isso costuma ser usado em conjunto com algoritmos simétricos.

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/crypto-atividade.git
   cd crypto-atividade
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

3. Execute o sistema:
   ```bash
   python main.py
   ```

4. Escolha a opção desejada (AES ou RSA) e insira o texto desejado.
