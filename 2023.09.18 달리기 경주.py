players =["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
result= ["mumu", "kai", "mine", "soe", "poe"]

def solution(players, callings):

    idx_player = {i:player for i,player in enumerate(players)}
    player_idx = {player:i for i,player in enumerate(players)}

    print(idx_player)
    print(player_idx)
    # for i in range(len(callings)):
    #     print('i====>',i)
    for i in callings:
        cur_idx = player_idx[i]
        pre_idx = cur_idx -1
        pre_player = idx_player[pre_idx]
        cur_player = i

        player_idx[cur_player] = pre_idx
        player_idx[pre_player] = cur_idx

        idx_player[pre_idx] = cur_player
        idx_player[cur_idx] = pre_player
    return list(idx_player.values())

solution(players, callings)





print(800 // 600)
