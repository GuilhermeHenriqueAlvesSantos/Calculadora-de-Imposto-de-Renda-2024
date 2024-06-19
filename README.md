## Projeto de Cálculo de Imposto de Renda


### Descrição do Projeto

Este projeto foi desenvolvido como parte de um trabalho em grupo para a disciplina de [Nome da Disciplina] do curso [Nome do Curso]. O objetivo é calcular o imposto de renda a ser pago por contribuintes com base em faixas de rendimento e suas respectivas alíquotas.

### Funcionalidades Implementadas

1. **Leitura de Aliquotas**: O programa lê as faixas de renda e alíquotas a partir do arquivo `aliquotas2024.txt`.
2. **Processamento de Contribuintes**: Os nomes e salários dos contribuintes são lidos do arquivo `contribuintes2024.txt` e processados para determinar o imposto devido.
3. **Cálculo do Imposto**: Com base nas faixas de renda e alíquotas definidas, o programa calcula o imposto de renda de cada contribuinte e salva os resultados no arquivo `result.txt`.

### Instruções de Uso

1. **Pré-requisitos**:
   - Python 3.x instalado no seu sistema.
   - Certifique-se de ter os arquivos `aliquotas2024.txt` e `contribuintes2024.txt` disponíveis no diretório de execução do programa.

2. **Execução**:
   - Abra um terminal e navegue até o diretório onde estão os arquivos do projeto.
   - Execute o script Python `calculo_imposto.py` utilizando o comando:
     ```bash
     python calculo_imposto.py
     ```
   - O programa processará os arquivos de entrada e salvará os resultados no arquivo `result.txt`.

### Exemplo de Saída

Se tudo ocorrer corretamente, o arquivo `result.txt` conterá resultados como:

```
Eduardo Freitas está isento de imposto
Guilherme Santos Deve pagar R$1234.56
Marcus Divino Deve pagar R$789.12
```

### Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request com melhorias ou correções.

### Autores

- Eduardo Freitas
- Guilherme Santos
- Marcus Divino

### Tecnologias Utilizadas

- Arquivos de texto: Utilizados para armazenar as faixas de renda, salários dos contribuintes e resultados.
  
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
