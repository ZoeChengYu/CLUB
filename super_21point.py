import random

# 1. 定義花色加權與牌面基準值
SUITS_BONUS = {'Spades': 0.30, 'Hearts': 0.10, 'Diamonds': -0.10, 'Clubs': -0.30}
RANKS_BASE = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10.25, 'Q': 10.5, 'K': 10.75, 'A': 11 
}

def create_deck():
    deck = []
    for suit, suit_val in SUITS_BONUS.items():
        for rank, rank_val in RANKS_BASE.items():
            deck.append({
                'rank': rank, 'suit': suit, 
                'suit_val': suit_val, 'total_val': rank_val + suit_val
            })
    random.shuffle(deck)
    return deck

def evaluate_hand(hand):
    """
    計算手牌的總點數，並同時回傳該副牌的「最大單張」與「最小單張」。
    包含 A 的動態降級邏輯 (爆牌時 11 -> 1)。
    """
    total_points = 0.0
    aces = []
    non_aces = []
    
    for card in hand:
        if card['rank'] == 'A':
            aces.append(card['suit_val'])
        else:
            non_aces.append(card['total_val'])
            total_points += card['total_val']
            
    # 小花色的 A 優先處理 (先排序)
    aces.sort()
    
    # 先假設所有 A 都是 11 點
    for suit_val in aces:
        total_points += (11.0 + suit_val)
        
    final_single_values = list(non_aces)
    
    # 如果爆牌，從花色最小的 A 開始降級為 1 點
    for suit_val in aces:
        if total_points > 21.0:
            total_points -= 10.0
            final_single_values.append(1.0 + suit_val)
        else:
            final_single_values.append(11.0 + suit_val)
            
    max_single = max(final_single_values)
    min_single = min(final_single_values)
    
    return total_points, max_single, min_single

def demo_single_round_with_new_bust_rule():
    print("=== 遊戲開始：大家各自默默補牌 ===")
    deck = create_deck()
    num_players = 8
    hands = [[] for _ in range(num_players)]

    # 初始發牌
    for _ in range(2):
        for i in range(num_players):
            hands[i].append(deck.pop())

    # 補牌階段
    for i in range(num_players):
        # 假設玩家策略：補到 15~18 點才停手
        threshold = random.uniform(15.0, 18.0) 
        while True:
            pts, _, _ = evaluate_hand(hands[i])
            if pts < threshold:
                hands[i].append(deck.pop())
            else:
                break
        print(f"玩家 {i+1} 補牌結束 (不公開狀態)")

    print("\n=== 一輪結束：統一攤牌結算！ ===")
    
    valid_players = []  # 存放未爆牌玩家 (索引, 總點數, 最大單張)
    busted_players = [] # 存放已爆牌玩家 (索引, 總點數, 最小單張)

    for i in range(num_players):
        pts, max_s, min_s = evaluate_hand(hands[i])
        cards_str = ", ".join([f"{c['suit'][:1]}{c['rank']}" for c in hands[i]])
        
        if pts <= 21.0:
            print(f"玩家 {i+1} 存活: [{cards_str}] -> 總計 {pts:.2f} 點 (單張最大 {max_s:.2f})")
            valid_players.append({'id': i, 'pts': pts, 'tiebreaker': max_s})
        else:
            print(f"玩家 {i+1} 爆牌: [{cards_str}] -> 總計 {pts:.2f} 點 (單張最小 {min_s:.2f}) 💥")
            busted_players.append({'id': i, 'pts': pts, 'tiebreaker': min_s})

    print("\n=== 最終結果 ===")
    winner = None
    
    if valid_players:
        # 路線 1：有人存活。比總點數最大 -> 平手比單張最大
        # 排序邏輯：點數降序 (大到小)，若點數相同則單張降序 (大到小)
        valid_players.sort(key=lambda x: (x['pts'], x['tiebreaker']), reverse=True)
        winner = valid_players[0]
        print(f"🏆 正常獲勝！贏家是 玩家 {winner['id']+1}")
        print(f"📊 獲勝數據 - 總點數: {winner['pts']:.2f}, 關鍵最大牌: {winner['tiebreaker']:.2f}")
        
    else:
        # 路線 2：全場爆牌。比總點數最小 -> 平手比單張最小
        # 排序邏輯：點數升序 (小到大)，若點數相同則單張升序 (小到大)
        busted_players.sort(key=lambda x: (x['pts'], x['tiebreaker']))
        winner = busted_players[0]
        print(f"💀 全場大亂鬥 (皆爆牌)！贏家是「爆最少」的 玩家 {winner['id']+1}！")
        print(f"📊 獲勝數據 - 總點數: {winner['pts']:.2f}, 關鍵最小牌: {winner['tiebreaker']:.2f}")

    print("💰 贏家拿走桌上全部 8 份賭金！")

# 執行測試
demo_single_round_with_new_bust_rule()