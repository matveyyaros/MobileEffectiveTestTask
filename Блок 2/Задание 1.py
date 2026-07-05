def is_isomorphic(s,t):
    if len(s)!=len(t):
        return False
    map_s = {}
    map_t = {}
    for ch_s, ch_t in zip(s, t):
        if ch_s in map_s:
            if map_s[ch_s] != ch_t:
                return False
        else:
            map_s[ch_s] = ch_t

        if ch_t in map_t:
            if map_t[ch_t] != ch_s:
                return False
        else:
            map_t[ch_t] = ch_s

    return True
    
s='paper'
t='title'
print(is_isomorphic(s,t))
'''
По памяти занимает: O(n) в наихудшем случае
По времени занимает: O(n) в наихудшем случае
Ограничения:
требует дополнительную память для хранения словарей
Достоинства:
простая реализация
'''