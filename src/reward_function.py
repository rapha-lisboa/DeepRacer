def reward_function(params):
    
    # Parâmetros utilizados
    track_length = params['track_length']
    steps = params['steps']
    progress = params['progress']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    is_offtrack = params['is_offtrack']
    
    # Define o numero máximo de steps baseado no comprimento da pista e imaginando um chute de 15 steps por segundo. Forçando o agente a estar por volta de 1 m/s sempre
    MAX_STEPS = round(track_length, 0) * 15
    
    # Calcula 2 marcas para a pista, sendo uma faixa central que representa 10% da largura da pista e o resto
    marker_1 = 0.1 * track_width
    marker_2 = 0.49978 * track_width
    
    # Caso o agente permaneça na faixa central a recompensa recebida é de 1, porém quanto mais ele se aproxima das bordas, menos recompensa ele recebe.
    # a recompensa a medida que a distancia aumenta é representada pela função quadrática de concavidade para baixo representada dentro do elif
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = -5 * distance_from_center**2 + 0.5 * distance_from_center + 1
    else:
        reward = 1e-3

    # A cada step, o progresso atual é comparado com o esperado, dessa forma o agente é recompensado caso esteja se saindo melhor que o esperado
    if progress > (steps/MAX_STEPS) * 100:
        reward += 10
    elif progress == (steps/MAX_STEPS) * 100:
        reward += 5
    else:
        reward *= 0.7

    # Penalização do agente, caso ele saia da pista por completo
    if is_offtrack:
        reward = -5
    
    return float(reward)