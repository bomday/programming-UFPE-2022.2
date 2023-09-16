# DJ das festas

**Limite de tempo do código: 2000ms**

Você e seus amigos amam organizar uma festa e como em toda boa festa não pode faltar um bom som, as escolhas das músicas é um momento crucial.

Graças ao seu bom gosto, você foi o escolhido dentre o seu grupinho para ficar responsável pelas playlists que irão tocar em todas as comemorações e com tamanha responsabilidade, você resolve já de antemão ter todas as playlists organizadas com as músicas que poderão tocar nas festas, só esperando o momento certo para dar o play.

Sempre que houver uma festa chegando, seus amigos te enviarão uma mensagem com o gênero das músicas que deverão tocar e quanto tempo essa festa vai durar.

Para garantir que você irá cumprir bem seu papel de DJ, tem alguns pontos que você precisa prestar atenção:

<ol>
    <li>Cada música da sua playlist tem duração de 3 minutos</li>
    <li>A duração total da playlist deve ser o mais próximo possível da duração da festa</li>
    <li>Para descobrir se você precisa adicionar ou remover canções e a quantidade em questão, será preciso calcular quantas músicas inteiras cabem no intervalo de tempo entre a duração da festa e da playlist</li>
    <li>As músicas serão removidas, caso necessário, sempre a partir do final da playlist</li>
    <li>Lembre-se que a lista é de Orientação à Objeto, logo, você deverá criar uma classe Playlist que terá os atributos nome e músicas e os métodos adicionar, remover, reproduzir e duracao.</li>
</ol>

**OBS:** o método duracao deverá retornar o tempo total da playlist e não deve ser um atributo, visto que, sem maiores cuidados, não retrataria a duração real da playlist, mas sim a sua duração no momento em que foi inicializada.

## Input:

Primeiro você receberá um inteiro com a quantidade de playlists que você irá criar

```
qtd_playlists
```

Em seguida, você receberá o nome, gênero e as músicas de cada playlist

```
nome
genero
musica1, musica2, ..., musicaN
```

**OBS:** as musicas virão separadas por uma vírgula e um espaço em branco

Depois de preparar todas as playlists, você receberá uma string contendo o gênero de música que tocará na próxima festa e um inteiro referente à duração da festa.

```
genero
duracao
```

**OBS:** você sempre receberá todos os inputs acima.

Caso você precise adicionar novas músicas à playlist da festa, você as receberá, cada uma em uma linha, de acordo com a quantidade calculada:

```
musica_adicional
```

## Output:

A primeira coisa a ser feita é checar se você tem alguma playlist do gênero solicitado, caso não, você deverá imprimir a seguinte mensagem e encerrar o programa:

```
"Não tenho nenhuma playlist do gênero {genero}, infelizmente não poderei tocar"
```

Caso você tenha alguma playlist do gênero:

1. Se a duração da festa for maior que a duração da playlist e você precise adicionar novas músicas, a saída será:

```
"Precisaremos adicionar mais {n} músicas a playlist {nome_playlist}"
```

2. Se a duração da festa for menor que a duração da playlist e você precise remover alguma música, a saída será:

```
"Precisaremos remover {n} músicas da playlist {nome_playlist}"
```

Em seguida, você deverá chamar seu método reproduzir, que primeiro irá printar:

```
"Play em {nome_playlist}"
```

E a cada música, exibirá:

```
"Tocando {musica}..."
```

Ao final, quando a playlist terminar de reproduzir você deverá imprimir:

```
"Essa festa foi um sucesso!"
```

## Exemplos:

### Caso 1:

Input:
```
2
para dançar
pop
Levitating, Can't Stop The Feeling, Worth It, Happy
hits latinos
latino
Chantaje, Calma, Me Enamoré, Loca, Si te Volviera a Encontrar
latino
15
```

Output:
```
Play em hits latinos
Tocando Chantaje...
Tocando Calma...
Tocando Me Enamoré...
Tocando Loca...
Tocando Si te Volviera a Encontrar...
Essa festa foi um sucesso!
```

### Caso 2:

Input:
```
2
rocks antigos
rock
The Lady In Red, Heaven, Have You Ever Seen The Rain, All Out of Love
paixão bandida
sertanejo
A Culpa É Nossa, Todo Mundo Vai Sofrer, Evidências
rock
21
Every Breath You Take
Endless Love
Time After Time
```

Output:
```
Precisaremos adicionar mais 3 músicas a playlist rocks antigos
Play em rocks antigos
Tocando The Lady In Red...
Tocando Heaven...
Tocando Have You Ever Seen The Rain...
Tocando All Out of Love...
Tocando Every Breath You Take...
Tocando Endless Love...
Tocando Time After Time...
Essa festa foi um sucesso!
```