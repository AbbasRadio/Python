from pygame import mixer

mixer.init()
#song.mp3 is the name of the song here {you can use it as per your need}
mixer.music.load("song.mp3")
mixer.music.set_volume(20)
mixer.music.play()
while True:
    print("Press 'P' to Pause, 'R' to Resume")
    print("Press 'E' to Exit")
    choice=input(" ")
    
    if choice == 'P':
        mixer.music.pause()
        
    elif choice == 'R':
        mixer.music.unpause()
        
    elif choice == 'E':
        mixer.music.stop()
        break