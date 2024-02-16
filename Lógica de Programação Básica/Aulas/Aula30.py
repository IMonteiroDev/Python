'''
Constante = 'Variáveis' que são inalteradas
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

'''

velocidade = 61 #Velocidade atual do carro
local_carro = 100 #local em que o carro está na estrada!

RADAR_1 = 60 #Velocidade máxima do radar 1
LOCAL_1 = 100 #Local onde o radar 1 está
RADAR_RANGE = 1 #A distância onde o radar pega

veloc_carr_pass_radar1=velocidade>RADAR_1


if veloc_carr_pass_radar1:
    print('Velocidade do carro passou do radar 1')
    
if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        veloc_carr_pass_radar1:
        print('Carro multado em radar 1!')