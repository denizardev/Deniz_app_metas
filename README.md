# MetaDiaria - Denizard

## Descrição

O **MetaDiaria  é um aplicativo desenvolvido em Python com Tkinter para gerenciamento de tarefas diárias. O objetivo do aplicativo é permitir que os usuários adicionem, visualizem e organizem suas tarefas, além de acompanhar o tempo gasto em cada uma delas. O aplicativo também suporta funcionalidades de visualização de tarefas por data, armazenamento de dados em um arquivo Excel e uma interface personalizável com diferentes cores de fundo.

## Funcionalidades Implementadas

1. **Interface Gráfica:**
   - Desenvolvido com Tkinter para criar uma interface gráfica amigável.
   - Utiliza o `tkcalendar` para exibir um calendário e selecionar datas.

2. **Entrada de Tarefas:**
   - Permite adicionar tarefas com uma descrição e o tempo estimado em minutos.
   - Adiciona as tarefas a um dicionário, que é atualizado e exibido na lista de tarefas.

3. **Visualização de Tarefas:**
   - Mostra as tarefas do dia selecionado no calendário.
   - Exibe uma mensagem quando não há tarefas para o dia selecionado.

4. **Conversão de Tempo:**
   - Converte minutos em horas e minutos restantes.

5. **Personalização de Interface:**
   - Permite trocar a cor de fundo da interface para diversas opções.

6. **Persistência de Dados:**
   - Salva e carrega as tarefas de um arquivo Excel (`tarefas.xlsx`) utilizando as bibliotecas `pandas` e `openpyxl`.

7. **Internacionalização:**
   - Exibe o dia da semana em inglês e francês para a data selecionada.

## Funcionalidades Futuras

1. **Lista de Objetivos:**
   - Adicionar uma aba separada para listar e gerenciar objetivos, além de mostrar progresso.

2. **Calendário e Tarefas:**
   - Implementar um calendário mais avançado para mostrar o progresso das tarefas diárias, semanais, mensais e anuais.

3. **Funcionalidade Pomodoro:**
   - Adicionar uma funcionalidade Pomodoro para ajudar na gestão do tempo de trabalho e pausas.

4. **Armazenamento de Metas:**
   - Armazenar metas em uma tabela para gerar gráficos de progresso.

5. **Opções Avançadas de Cores:**
   - Implementar uma paleta de cores mais avançada e permitir a seleção de cores personalizadas.

6. **Melhorias na Interface:**
   - Ajustar o tamanho dos componentes da interface para uma melhor experiência em diferentes tamanhos de tela.
   - Melhorar a visualização e edição das tarefas.

## Instalação

Para executar o projeto, você precisará instalar as bibliotecas necessárias:

```bash
pip install pandas openpyxl tkcalendar
