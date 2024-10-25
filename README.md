# README - Script de Web Scraping para Extração de Jogos

## Descrição
Este projeto contém um script de automação que utiliza Selenium para extrair informações sobre jogos do site "Fitgirl Repacks". O objetivo é facilitar a busca por novos lançamentos, economizando tempo em comparação com a navegação manual pelas páginas do site.

## Funcionalidades
- Navegação automática por várias páginas do site.
- Extração dos títulos dos jogos listados nas páginas.
- Remoção de acentos e caracteres especiais dos títulos para facilitar a leitura.
- Registro dos jogos encontrados em um arquivo de log.
- Mensuração do tempo necessário para processar cada página.

## Requisitos
- Python 3.x
- Bibliotecas:
  - Selenium
  - WebDriver Manager
  - Unidecode

## Instalação
Para instalar as dependências necessárias, você pode usar o gerenciador de pacotes `pip`. Execute os seguintes comandos em seu terminal:

```bash
pip install selenium webdriver-manager unidecode
```
## Configuração
ChromeDriver: O script utiliza o ChromeDriver para controlar o navegador Chrome. O WebDriver Manager cuida automaticamente da instalação do ChromeDriver, portanto, você não precisa configurá-lo manualmente.

Executando o Script: Certifique-se de ter o Google Chrome instalado em seu sistema. Após isso, você pode executar o script diretamente, que abrirá o navegador em modo "headless" (sem interface gráfica) e começará a coletar os títulos dos jogos.

## Uso
Abra o arquivo scraping_fitgirl.py em um editor de texto ou IDE de sua escolha.
Altere a variável numero_de_paginas para definir quantas páginas você deseja navegar. O valor padrão é 10.
Execute o script:
```bash
python scraping_fitgirl.py
```
Após a execução, o log com os jogos encontrados será registrado em um arquivo chamado log.txt.

## Exemplo de Log
Após a execução do script, o arquivo log.txt conterá informações sobre a execução, como os títulos dos jogos encontrados e o tempo total de processamento. Um exemplo de entrada no log pode ser:
```ruby
Processou https://fitgirl-repacks.site/page/1/ em 3.12 segundos.
Processou https://fitgirl-repacks.site/page/2/ em 2.95 segundos.
Jogos encontrados:
1. Mexico, 1921. A Deep Slumber.
2. Game Title 2.
3. Game Title 3.
...
```

## Erros Comuns
TimeoutException: Ocorre se a página não carregar dentro do tempo esperado. Isso pode ser ajustado na linha que define o tempo de espera no script.
Problemas com Caracteres: Os títulos podem conter caracteres especiais, mas o script utiliza a biblioteca unidecode para remover acentos e garantir que os títulos sejam legíveis.