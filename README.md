# Web Scraping Mercado Livre - Case Samsung


## 📖 Descrição do Projeto

Este projeto implementa um pipeline de ETL (Extração, Transformação e Carregamento) para dados de notebooks disponíveis no Mercado Livre. Utiliza o framework Scrapy para coleta de dados, pandas para manipulação e transformação, e Streamlit para visualização interativa. O objetivo é construir uma base de dados estruturada para análise de mercado.

---

## 🛠️ Estrutura do Repositório

```plaintext
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   ├── data.jsonl          # Dados brutos extraídos
│   ├── mercadolivre.db     # Banco de dados SQLite com dados processados
├── src/
│   ├── dashboard/
│   │   └── app.py          # Interface interativa com Streamlit
│   ├── extraction/
│   │   ├── scrapy.cfg      # Configuração do Scrapy
│   │   └── coleta/
│   │       ├── spiders/
│   │       │   └── notebook.py  # Spider para scraping de notebooks
│   │       ├── items.py    # Definição de modelos de dados do Scrapy
│   │       ├── settings.py # Configurações do Scrapy
│   ├── transformLoad/
│       └── main.py         # Script para transformação e carregamento
```

---

## 🚀 Funcionalidades Principais

1. **Extração de Dados**:
   - O spider [`NotebookSpider`](src/extraction/coleta/spiders/notebook.py) coleta informações como marca, modelo, preço, avaliações e vendedor diretamente do Mercado Livre.

2. **Transformação de Dados**:
   - O script [`main.py`](src/transformLoad/main.py) realiza:
     - Tratamento de valores ausentes.
     - Conversão de tipos para colunas numéricas.
     - Filtragem de produtos com base em critérios específicos.

3. **Carregamento de Dados**:
   - Os dados processados são armazenados em um banco de dados SQLite ([`mercadolivre.db`](data/mercadolivre.db)).

4. **Visualização Interativa**:
   - O dashboard Streamlit ([`app.py`](src/dashboard/app.py)) apresenta os dados com KPIs e gráficos dinâmicos.

---

## 🛠️ Tecnologias e Ferramentas

- **Python**: Linguagem principal para desenvolvimento.
- **Scrapy**: Framework para web scraping.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **SQLite**: Banco de dados relacional leve.
- **Streamlit**: Ferramenta para criação de dashboards interativos.

---

## 📦 Guia de Instalação

1. **Clone o repositório**:
   ```bash
   
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o spider para coleta de dados**:
   ```bash
   scrapy crawl notebook
   ```

4. **Realize a transformação e carregamento dos dados**:
   ```bash
   python src/transformLoad/main.py
   ```

5. **Inicie o dashboard interativo**:
   ```bash
   streamlit run src/dashboard/app.py
   ```

---

## 📊 Visualização e Análise

O dashboard interativo apresenta:

- **Indicadores-Chave (KPIs)**:
  - Total de itens coletados.
  - Preço médio dos notebooks.
  - Avaliação média dos produtos.
  - Marca que se destacou

- **Gráficos e Tabelas**:
  - Distribuição de preços.
  - Avaliações por marca.

---

## 📝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Realize os commits das alterações:
   ```bash
   git commit -m "Implementação da minha feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request para revisão.

---

## 🛡️ Licenciamento

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

## 🙌 Agradecimentos

Este projeto foi desenvolvido como parte da iniciativa **Jornada de Dados**. Para mais informações, acesse [Jornada de Dados](https://suajornadadedados.com.br/).
