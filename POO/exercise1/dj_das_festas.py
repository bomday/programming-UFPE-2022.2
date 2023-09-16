class Playlist():
  def __init__(self, nome_playlist, genero_playlist, musicas_playlist):
    self.nome_playlist = nome_playlist
    self.genero_playlist = genero_playlist
    self.musicas_playlist = musicas_playlist
  
  def adicionar(self, musica):
    self.musicas_playlist.append(musica)

  def remover(self):
    self.musicas_playlist.pop()
  
  def reproduzir(self):
    print(f'Play em {self.nome_playlist}')
    for musica in self.musicas_playlist:
      print(f'Tocando {musica}...')
    
    print('Essa festa foi um sucesso!')

  def duracao(self):
    duracao_playlist = len(self.musicas_playlist) * 3
    return duracao_playlist

qtd_playlists = int(input())
playlists = []

while qtd_playlists > 0:
  qtd_playlists -= 1
  nome = input()
  genero = input()
  musicas = input()
  lista_musicas = musicas.split(', ')
  
  nova_playlist = Playlist(nome, genero, lista_musicas)
  playlists.append(nova_playlist)
  
genero_prox_festa = input()
duracao_prox_festa = int(input())
playlist_existe = False
playlist_escolhida = ''

for playlist in playlists:
  if playlist.genero_playlist == genero_prox_festa:
    playlist_existe = True
    playlist_escolhida = playlist

if playlist_existe:
  duracao_atual = playlist_escolhida.duracao()
  
  if duracao_atual < duracao_prox_festa:
    num_musicas_permitido = int(duracao_prox_festa / 3)
    num_musicas_adicionar = num_musicas_permitido - len(playlist_escolhida.musicas_playlist)
    
    if num_musicas_adicionar > 0:
      print(f'Precisaremos adicionar mais {num_musicas_adicionar} músicas a playlist {playlist_escolhida.nome_playlist}')
    
    for musica in range(0, num_musicas_adicionar):
      nova_musica = input()
      playlist_escolhida.adicionar(nova_musica)
    
  elif duracao_atual > duracao_prox_festa:
    num_musicas_permitido = duracao_prox_festa / 3
    num_musicas_remover = len(playlist_escolhida.musicas_playlist) - num_musicas_permitido
    
    if num_musicas_remover >= 1:
      print(f'Precisaremos remover {int(num_musicas_remover)} músicas da playlist {playlist_escolhida.nome_playlist}')
      for musica in range(0, int(num_musicas_remover)):
        playlist_escolhida.remover()
  
  playlist_escolhida.reproduzir()
else:
  print(f'Não tenho nenhuma playlist do gênero {genero_prox_festa}, infelizmente não poderei tocar')