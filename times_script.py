data_dir = "/home/tobi/Documents/tirocinio_montini/immagini_montini_srl/tempi+specials.txt"
save_file = "/home/tobi/Documents/tirocinio_montini/immagini_montini_srl/results.txt"

somma = 0
with open(data_dir, 'r') as f:
    times = f.read().splitlines()
    print(times)

    for tempo in times:
        numeri = tempo.split('.')
        somma += int(numeri[0])*60
        somma += int(numeri[1])
        print(somma)

with open(save_file, 'w') as f:
    f.write(str(somma/60))