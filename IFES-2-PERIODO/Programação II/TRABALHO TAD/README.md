  ### TRABALHO
        DUPLA: 30 Pontos (26/06 até 23:00)
        - Construir um TAD Matriz
        - CriaMatriz(A,B)
        - Multiplicação(A,B)
        - Negação(A)
        - Trasposição(A)

### Ifes Campus Serra
- BSI – Bacharelado de Sistemas de Informação
- Estrutura de Dados
- Avaliação 3: Trabalho TAD MAtriz
- Obrigatório: Não utilize comandos em Python diferentes daqueles abordados em aula.
- Total: 30 pontos.
- Modalidade: trabalho em dupla.
- Entrega: 27/06/2023, 23h55, via ava.


#### Implementação do tad matriz: 15 PTS
- Implemente um TAD matriz em um arquivo python chamado tadmatriz.py. O TAD mateiz deve conter a seguinte interface:
- a) cria_mat(qlinhas, qcolunas) > tadmat: cria e retorna uma estrutura de dados (lista, dicionário etc.) que representa uma matriz numérica de qlinhas e qcolunas.
- b) soma_mat(tadA, tadB) > tadmat: cria e retorna uma nova tad matriz com a soma dos tad
matriz A e B passados como parâmetros de entrada. Tando os parâmetros de entrada quanto o
valor retornado na saída devem ser tad matrizes. Caso as matrizes de entrada não possam ser
somadas, retornar o valor None.
- c) multi_mat(tadA, tadB) > tadmat: cria e retorna uma nova tad matriz com a multiplicação
matricial dos tad matriz A e B passados como parâmetros de entrada. Tando os parâmetros de
entrada quanto o valor retornado na saída devem ser tad matrizes. Caso as matrizes de entrada
não possam ser multiplicadas, retornar o valor None.
- d) neg_mat(tadA) > tadmat: multiplica por menos um os valores da tad matriz de entrada.
Retorna a própria matriz de entrada com os valores modificados.
- e) transp_mat(tadA) > tadmat: retorna uma nova tad matriz equivalente à transposta da tad
matriz de entrada, tadA.
- f) carrega_mat(nome-do-arquivo) > tadmat: carrega uma matriz numérica a partir do arquivo de
nome passado como parâmetro de entrada. Retorna uma tad matriz com os valores vindos do
arquivo. O formato do arquivo é o mesmo usado nos arquivos fornecidos pelo Professor.
Os arquivos de matrizes são nomeados com nomes de letras: A.txt, B.txt, etc.
- g) salva_mat(tadA,nome-do-arquivo) > tadmat: salva a tad matriz tadA no arquivo texto de
nome igual ao fornecido no segundo parâmetro. Retorna a prórpria tad matriz salva. O formato do
arquivo é o mesmo usado nos arquivos fornecidos pelo Professor.

##### Aplicação do tad matriz (descrição): 15 PTS
- Um arquivo chamado matops.txt contém, em cada linha, uma série de operações com matrizes.
Construa um programa python chamado trabtadmat.py que importa o módulo tadmatriz.py e lê o
arquivo matops.txt linha a linha. Para cada linha lida, o programa descobre a operação matricial e
as matrizes envolvidas na operação, e realiza a operação solicitada. Exemplo: seja o conteúdo da
linha de matops.txt igual a A x D. A aplicação deve processar a linha e fazer as cargas das
matrizes A e D (dos respectivos arquivos) e efetuar a multiplicação matricial entre as matrizes.

- O resultado da multiplicação deve ser salvo em um arquivo chamado AvezesD.txt. Em caso de
somas de matrizes, o nome do arquivo de saída é análogo (por exemplo AmaisD.txt). Veja
exemplo a seguir.

- Exemplo (nomes e conteúdos de matrizes são apenas exemplos)
Conteúdo matops.txt Nomes dos arquivos gerados com os respectivos
A + B AmaisB.txt
A x B AvezesB.txt
C + TD CmaistranspD.txt
A - B AmenosB.txt
-A x B menosAvezesB.txt
A x TD AvezestranspD.txt
-B x TD menosBvezestranspD.txt
Exemplo do arquivo A.txt Exemplo do arquivo D.txt
1 1 1 2 1 5
1 1 1 4 5 9
1 1 1

- Entrega
Compacte os arquivos trabtadmat.py, tadmatriz.py e todos os arquivos de matrizes .txt em
arquivo chamado avaltadmat.zip.
Compactações em formato rar não serão corrigidas.
Entregue o arquivo compactado na tarefa do ava aberta para a avaliação do trabalho de tad
matriz.
