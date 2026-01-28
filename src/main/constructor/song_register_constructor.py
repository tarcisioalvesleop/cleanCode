from src.view.song_register_view import SongRegisterView

# SongRegisterView -> Pascal Case (Classes)
# song_register_view -> Snake Case (Funções, métodos, variáveis)

def song_register_process():
    song_register_view = SongRegisterView()
    # instancia do controller

    new_song_informations = song_register_view.registry_song_initial()
    # enviar new_song_informations para controller