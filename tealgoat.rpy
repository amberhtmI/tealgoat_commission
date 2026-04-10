init python:
    class Cards:
        def __init__(self,image,img,value,category):
            self.image = image
            self.img = img
            self.value = value
            self.category = category

define config.layers = ['master','opponent_card_layer','player_card_layer','transient','screens','overlay']

default clubs_ace = Cards("images/tealgoat/cards/ace_of_clubs.png","ace_of_clubs",1,"high")
default clubs_two = Cards("images/tealgoat/cards/2_of_clubs.png","2_of_clubs",2,"low")
default clubs_three = Cards("images/tealgoat/cards/3_of_clubs.png","3_of_clubs",3,"low")
default clubs_four = Cards("images/tealgoat/cards/4_of_clubs.png","4_of_clubs",4,"low")
default clubs_five = Cards("images/tealgoat/cards/5_of_clubs.png","5_of_clubs",5,"low")
default clubs_six = Cards("images/tealgoat/cards/6_of_clubs.png","6_of_clubs",6,"low")
default clubs_seven = Cards("images/tealgoat/cards/7_of_clubs.png","7_of_clubs",7,"low")
default clubs_eight = Cards("images/tealgoat/cards/8_of_clubs.png","8_of_clubs",8,"high")
default clubs_nine = Cards("images/tealgoat/cards/9_of_clubs.png","9_of_clubs",9,"high")
default clubs_ten = Cards("images/tealgoat/cards/10_of_clubs.png","10_of_clubs",10,"high")
default clubs_jack = Cards("images/tealgoat/cards/jack_of_clubs.png","jack_of_clubs",11,"high")
default clubs_queen = Cards("images/tealgoat/cards/queen_of_clubs.png","queen_of_clubs",12,"high")
default clubs_king = Cards("images/tealgoat/cards/king_of_clubs.png","king_of_clubs",13,"high")
default diamonds_ace = Cards("images/tealgoat/cards/ace_of_diamonds.png","ace_of_diamonds",1,"high")
default diamonds_two = Cards("images/tealgoat/cards/2_of_diamonds.png","2_of_diamonds",2,"low")
default diamonds_three = Cards("images/tealgoat/cards/3_of_diamonds.png","3_of_diamonds",3,"low")
default diamonds_four = Cards("images/tealgoat/cards/4_of_diamonds.png","4_of_diamonds",4,"low")
default diamonds_five = Cards("images/tealgoat/cards/5_of_diamonds.png","5_of_diamonds",5,"low")
default diamonds_six = Cards("images/tealgoat/cards/6_of_diamonds.png","6_of_diamonds",6,"low")
default diamonds_seven = Cards("images/tealgoat/cards/7_of_diamonds.png","7_of_diamonds",7,"low")
default diamonds_eight = Cards("images/tealgoat/cards/8_of_diamonds.png","8_of_diamonds",8,"high")
default diamonds_nine = Cards("images/tealgoat/cards/9_of_diamonds.png","9_of_diamonds",9,"high")
default diamonds_ten = Cards("images/tealgoat/cards/10_of_diamonds.png","10_of_diamonds",10,"high")
default diamonds_jack = Cards("images/tealgoat/cards/jack_of_diamonds.png","jack_of_diamonds",11,"high")
default diamonds_queen = Cards("images/tealgoat/cards/queen_of_diamonds.png","queen_of_diamonds",12,"high")
default diamonds_king = Cards("images/tealgoat/cards/king_of_diamonds.png","king_of_diamonds",13,"high")
default hearts_ace = Cards("images/tealgoat/cards/ace_of_hearts.png","ace_of_hearts",1,"high")
default hearts_two = Cards("images/tealgoat/cards/2_of_hearts.png","2_of_hearts",2,"low")
default hearts_three = Cards("images/tealgoat/cards/3_of_hearts.png","3_of_hearts",3,"low")
default hearts_four = Cards("images/tealgoat/cards/4_of_hearts.png","4_of_hearts",4,"low")
default hearts_five = Cards("images/tealgoat/cards/5_of_hearts.png","5_of_hearts",5,"low")
default hearts_six = Cards("images/tealgoat/cards/6_of_hearts.png","6_of_hearts",6,"low")
default hearts_seven = Cards("images/tealgoat/cards/7_of_hearts.png","7_of_hearts",7,"low")
default hearts_eight = Cards("images/tealgoat/cards/8_of_hearts.png","8_of_hearts",8,"high")
default hearts_nine = Cards("images/tealgoat/cards/9_of_hearts.png","9_of_hearts",9,"high")
default hearts_ten = Cards("images/tealgoat/cards/10_of_hearts.png","10_of_hearts",10,"high")
default hearts_jack = Cards("images/tealgoat/cards/jack_of_hearts.png","jack_of_hearts",11,"high")
default hearts_queen = Cards("images/tealgoat/cards/queen_of_hearts.png","queen_of_hearts",12,"high")
default hearts_king = Cards("images/tealgoat/cards/king_of_hearts.png","king_of_hearts",13,"high")
default spades_ace = Cards("images/tealgoat/cards/ace_of_spades.png","ace_of_spades",1,"high")
default spades_two = Cards("images/tealgoat/cards/2_of_spades.png","2_of_spades",2,"low")
default spades_three = Cards("images/tealgoat/cards/3_of_spades.png","3_of_spades",3,"low")
default spades_four = Cards("images/tealgoat/cards/4_of_spades.png","4_of_spades",4,"low")
default spades_five = Cards("images/tealgoat/cards/5_of_spades.png","5_of_spades",5,"low")
default spades_six = Cards("images/tealgoat/cards/6_of_spades.png","6_of_spades",6,"low")
default spades_seven = Cards("images/tealgoat/cards/7_of_spades.png","7_of_spades",7,"low")
default spades_eight = Cards("images/tealgoat/cards/8_of_spades.png","8_of_spades",8,"high")
default spades_nine = Cards("images/tealgoat/cards/9_of_spades.png","9_of_spades",9,"high")
default spades_ten = Cards("images/tealgoat/cards/10_of_spades.png","10_of_spades",10,"high")
default spades_jack = Cards("images/tealgoat/cards/jack_of_spades.png","jack_of_spades",11,"high")
default spades_queen = Cards("images/tealgoat/cards/queen_of_spades.png","queen_of_spades",12,"high")
default spades_king = Cards("images/tealgoat/cards/king_of_spades.png","king_of_spades",13,"high")

default current_bet = 1
default previous_bet = 1
default round_winner = ''

default player_deck = [
    clubs_ace,clubs_two,clubs_three,clubs_four,clubs_five,clubs_six,clubs_seven,clubs_eight,clubs_nine,clubs_ten,clubs_jack,clubs_queen,clubs_king,
    diamonds_ace,diamonds_two,diamonds_three,diamonds_four,diamonds_five,diamonds_six,diamonds_seven,diamonds_eight,diamonds_nine,diamonds_ten,diamonds_jack,diamonds_queen,diamonds_king,
    hearts_ace,hearts_two,hearts_three,hearts_four,hearts_five,hearts_six,hearts_seven,hearts_eight,hearts_nine,hearts_ten,hearts_jack,hearts_queen,hearts_king,
    spades_ace,spades_two,spades_three,spades_four,spades_five,spades_six,spades_seven,spades_eight,spades_nine,spades_ten,spades_jack,spades_queen,spades_king
]
default player_hand = []
default player_picked = None
default player_arrows = []
default player_chips = 10

default player_status = None

default opponent_deck = [
    clubs_ace,clubs_two,clubs_three,clubs_four,clubs_five,clubs_six,clubs_seven,clubs_eight,clubs_nine,clubs_ten,clubs_jack,clubs_queen,clubs_king,
    diamonds_ace,diamonds_two,diamonds_three,diamonds_four,diamonds_five,diamonds_six,diamonds_seven,diamonds_eight,diamonds_nine,diamonds_ten,diamonds_jack,diamonds_queen,diamonds_king,
    hearts_ace,hearts_two,hearts_three,hearts_four,hearts_five,hearts_six,hearts_seven,hearts_eight,hearts_nine,hearts_ten,hearts_jack,hearts_queen,hearts_king,
    spades_ace,spades_two,spades_three,spades_four,spades_five,spades_six,spades_seven,spades_eight,spades_nine,spades_ten,spades_jack,spades_queen,spades_king
]
default opponent_hand = []
default opponent_picked = None
default opponent_arrows = []
default opponent_chips = 10

default opponent_checked = False

default battle_one_won = None
default battle_two_won = None
default battle_three_won = None

default horse_friendship = 1

label cardgame_reset():
    $ current_bet = 1
    $ previous_bet = 1
    $ round_winner = ''

    $ player_status = None
    $ opponent_checked = False
    
    $ player_hand = []
    $ player_picked = None
    $ player_arrows = []
    $ player_chips = 10
    $ player_deck = [
        clubs_ace,clubs_two,clubs_three,clubs_four,clubs_five,clubs_six,clubs_seven,clubs_eight,clubs_nine,clubs_ten,clubs_jack,clubs_queen,clubs_king,
        diamonds_ace,diamonds_two,diamonds_three,diamonds_four,diamonds_five,diamonds_six,diamonds_seven,diamonds_eight,diamonds_nine,diamonds_ten,diamonds_jack,diamonds_queen,diamonds_king,
        hearts_ace,hearts_two,hearts_three,hearts_four,hearts_five,hearts_six,hearts_seven,hearts_eight,hearts_nine,hearts_ten,hearts_jack,hearts_queen,hearts_king,
        spades_ace,spades_two,spades_three,spades_four,spades_five,spades_six,spades_seven,spades_eight,spades_nine,spades_ten,spades_jack,spades_queen,spades_king
    ]
    $ opponent_hand = []
    $ opponent_picked = None
    $ opponent_chips = 10
    $ opponent_arrows = []
    $ opponent_deck = [
        clubs_ace,clubs_two,clubs_three,clubs_four,clubs_five,clubs_six,clubs_seven,clubs_eight,clubs_nine,clubs_ten,clubs_jack,clubs_queen,clubs_king,
        diamonds_ace,diamonds_two,diamonds_three,diamonds_four,diamonds_five,diamonds_six,diamonds_seven,diamonds_eight,diamonds_nine,diamonds_ten,diamonds_jack,diamonds_queen,diamonds_king,
        hearts_ace,hearts_two,hearts_three,hearts_four,hearts_five,hearts_six,hearts_seven,hearts_eight,hearts_nine,hearts_ten,hearts_jack,hearts_queen,hearts_king,
        spades_ace,spades_two,spades_three,spades_four,spades_five,spades_six,spades_seven,spades_eight,spades_nine,spades_ten,spades_jack,spades_queen,spades_king
    ]

transform cardgame_position:
    align(0.0, 0.0)

transform card_size_adjust:
    zoom 0.75
    matrixcolor None

transform card_hovered:
    zoom 0.8
    matrixcolor TintMatrix('#e0c650')

transform card_flip_back:
    xzoom -1.0
    linear 0.5 xzoom 0.0

transform card_flip_front:
    xzoom 0.0
    linear 0.5 xzoom 1.0

transform opponent_card_pos:
    pos(500,265)

transform player_card_pos:
    pos(1045,265)

label cardgame_battle1(gamenumber):
    scene minigame_background
    if gamenumber == 1:
        show horse g1 neutral
        show kid g1 neutral
    elif gamenumber == 2:
        if horse_friendship > 5:
            show horse g2 hf neutral
        elif horse_friendship < 1:
            show horse g2 lf neutral
        else:
            if battle_one_won == True:
                show horse g2 wong1 neutral
            else:
                show horse g2 lostg1 neutral
        if battle_one_won == True:
            show kid g2 wong1 neutral
        else:
            show kid g2 lostg1 neutral
    else:
        if horse_friendship > 5:
            show horse g3 hf neutral
        elif horse_friendship < 1:
            show horse g3 lf neutral
        else:
            if battle_one_won == True and battle_two_won == True:
                show horse g3 wong1 wong2 neutral
            elif battle_one_won == True and battle_two_won == False:
                show horse g3 wong1 lostg2 neutral
            elif battle_one_won == False and battle_two_won == True:
                show horse g3 lostg2 wong2 neutral
            else:
                show horse g3 lostg2 lostg2 neutral
        if battle_one_won == True and battle_two_won == True:
            show kid g3 wong1 wong2 neutral
        elif battle_one_won == True and battle_two_won == False:
            show kid g3 wong1 lostg2 neutral
        elif battle_one_won == False and battle_two_won == True:
            show kid g3 lostg2 wong2 neutral
        else:
            show kid g3 lostg2 lostg2 neutral
    show minigame_table

    $ player_hand.append(player_deck[renpy.random.randint(0,len(player_deck)-1)])
    $ player_deck.remove(player_hand[0])
    $ player_hand.append(player_deck[renpy.random.randint(0,len(player_deck)-1)])
    $ player_deck.remove(player_hand[1])
    $ opponent_hand.append(opponent_deck[renpy.random.randint(0,len(opponent_deck)-1)])
    $ opponent_deck.remove(opponent_hand[0])
    $ opponent_hand.append(opponent_deck[renpy.random.randint(0,len(opponent_deck)-1)])
    $ opponent_deck.remove(opponent_hand[1])
    while player_chips < 20 and opponent_chips < 20:
        if len(player_deck) == 0:
            $ player_deck = [
                clubs_ace,clubs_two,clubs_three,clubs_four,clubs_five,clubs_six,clubs_seven,clubs_eight,clubs_nine,clubs_ten,clubs_jack,clubs_queen,clubs_king,
                diamonds_ace,diamonds_two,diamonds_three,diamonds_four,diamonds_five,diamonds_six,diamonds_seven,diamonds_eight,diamonds_nine,diamonds_ten,diamonds_jack,diamonds_queen,diamonds_king,
                hearts_ace,hearts_two,hearts_three,hearts_four,hearts_five,hearts_six,hearts_seven,hearts_eight,hearts_nine,hearts_ten,hearts_jack,hearts_queen,hearts_king,
                spades_ace,spades_two,spades_three,spades_four,spades_five,spades_six,spades_seven,spades_eight,spades_nine,spades_ten,spades_jack,spades_queen,spades_king
            ]
        if len(opponent_deck) == 0:
            $ opponent_deck = [
                clubs_ace,clubs_two,clubs_three,clubs_four,clubs_five,clubs_six,clubs_seven,clubs_eight,clubs_nine,clubs_ten,clubs_jack,clubs_queen,clubs_king,
                diamonds_ace,diamonds_two,diamonds_three,diamonds_four,diamonds_five,diamonds_six,diamonds_seven,diamonds_eight,diamonds_nine,diamonds_ten,diamonds_jack,diamonds_queen,diamonds_king,
                hearts_ace,hearts_two,hearts_three,hearts_four,hearts_five,hearts_six,hearts_seven,hearts_eight,hearts_nine,hearts_ten,hearts_jack,hearts_queen,hearts_king,
                spades_ace,spades_two,spades_three,spades_four,spades_five,spades_six,spades_seven,spades_eight,spades_nine,spades_ten,spades_jack,spades_queen,spades_king
            ]
        while len(player_hand) < 2 and len(player_deck)-1 >= 1:
            $ player_hand.append(player_deck[renpy.random.randint(0,len(player_deck)-1)])
            $ player_deck.remove(player_hand[1])
        while len(opponent_hand) < 2 and len(opponent_deck)-1 >= 1:
            $ opponent_hand.append(opponent_deck[renpy.random.randint(0,len(opponent_deck)-1)])
            $ opponent_deck.remove(opponent_hand[1])
        
        $ opponent_arrows = []
        $ player_arrows = []
        $ player_arrows.append(player_hand[0].category)
        $ player_arrows.append(player_hand[1].category)
        $ opponent_arrows.append(opponent_hand[0].category)
        $ opponent_arrows.append(opponent_hand[1].category)

        $ player_status = None
        $ opponent_checked = False


        # CHANGE EXPRESSION BASED ON NUMBER OF CHIPS
        if player_chips >= 13:
            show kid high_chips
        if opponent_chips >= 13:
            show horse low_chips
        if player_chips <= 7:
            show kid low_chips
        if opponent_chips <= 7:
            show horse high_chips


        show screen cardgame_overlay

        show screen cardgame_notify("Opponent is picking their card...")
        pause 1.5

        # OPPONENT PICKING THEIR CARD
        if player_hand[0].category == "high" and player_hand[1].category == "high":
            if opponent_hand[0].category == "high" and opponent_hand[1].category == "high":
                if opponent_hand[0].value >= opponent_hand[1].value:
                    $ opponent_picked = opponent_hand[0]
                    $ opponent_hand.remove(opponent_hand[0])
                else:
                    $ opponent_picked = opponent_hand[1]
                    $ opponent_hand.remove(opponent_hand[1])
            elif opponent_hand[0].category == "low" and opponent_hand[1].category == "low":
                if opponent_hand[0].value <= opponent_hand[1].value:
                    $ opponent_picked = opponent_hand[0]
                    $ opponent_hand.remove(opponent_hand[0])
                else:
                    $ opponent_picked = opponent_hand[1]
                    $ opponent_hand.remove(opponent_hand[1])
            else:
                if opponent_hand[0].value >= opponent_hand[1].value:
                    $ opponent_picked = opponent_hand[0]
                    $ opponent_hand.remove(opponent_hand[0])
                else:
                    $ opponent_picked = opponent_hand[1]
                    $ opponent_hand.remove(opponent_hand[1])
        elif player_hand[0].category == "low" and player_hand[1].category == "low":
            if opponent_hand[0].category == "high" and opponent_hand[1].category == "high":
                if opponent_hand[0].value <= opponent_hand[1].value:
                    $ opponent_picked = opponent_hand[0]
                    $ opponent_hand.remove(opponent_hand[0])
                else:
                    $ opponent_picked = opponent_hand[1]
                    $ opponent_hand.remove(opponent_hand[1])
            elif opponent_hand[0].category == "low" and opponent_hand[1].category == "low":
                if opponent_hand[0].value >= opponent_hand[1].value:
                    $ opponent_picked = opponent_hand[0]
                    $ opponent_hand.remove(opponent_hand[0])
                else:
                    $ opponent_picked = opponent_hand[1]
                    $ opponent_hand.remove(opponent_hand[1])
            else:
                if opponent_hand[0].value >= opponent_hand[1].value:
                    $ opponent_picked = opponent_hand[0]
                    $ opponent_hand.remove(opponent_hand[0])
                else:
                    $ opponent_picked = opponent_hand[1]
                    $ opponent_hand.remove(opponent_hand[1])
        else: 
            if opponent_hand[0].category == "high" and opponent_hand[1].category == "high":
                if opponent_hand[0].value >= opponent_hand[1].value:
                    $ opponent_picked = opponent_hand[0]
                    $ opponent_hand.remove(opponent_hand[0])
                else:
                    $ opponent_picked = opponent_hand[1]
                    $ opponent_hand.remove(opponent_hand[1])
            elif opponent_hand[0].category == "low" and opponent_hand[1].category == "low":
                if opponent_hand[0].value <= opponent_hand[1].value:
                    $ opponent_picked = opponent_hand[0]
                    $ opponent_hand.remove(opponent_hand[0])
                else:
                    $ opponent_picked = opponent_hand[1]
                    $ opponent_hand.remove(opponent_hand[1])
            else:
                if opponent_hand[0].value >= opponent_hand[1].value:
                    $ opponent_picked = opponent_hand[0]
                    $ opponent_hand.remove(opponent_hand[0])
                else:
                    $ opponent_picked = opponent_hand[1]
                    $ opponent_hand.remove(opponent_hand[1])
        show screen cardgame_notify("Opponent has picked their card!")
        pause 1.5
        show screen cardgame_notify("Player is picking their card...")
        pause 1.5
        # PLAYER PICKING THEIR CARD SCREEN
        call screen cardgame_pick_card()
        show screen cardgame_notify("Player has picked their card!")
        pause 1.5
        # CHECK / RAISE / FOLD SCREEN
        # LOOP UNTIL BOTH PLAYER AND HORSE CHECK OR PLAYER FOLDS
        while player_status == None or opponent_checked != True:
            $ player_status = None
            $ opponent_checked = False

            call screen cardgame_action_choice()
 

            if _return == "poker_fold":
                show screen cardgame_notify("Player folds!")
                pause 1.5
                $ player_status = "fold"
                $ opponent_checked = True
            else:
                if _return == "poker_check":
                    show screen cardgame_notify("Player checks!")
                    pause 1.5
                    $ player_status = "check"
                elif _return == "poker_raise":
                    call screen cardgame_raise()
                    if _return == "poker_deal":
                        show screen cardgame_notify("Player raised the bet to [current_bet]!")
                        pause 1.5
                    elif _return == "poker_back":
                        show screen cardgame_notify("Player checks!")
                        pause 1.5
                        $ player_status = "check"
                $ previous_bet = current_bet
                
        
            # OPPONENT ACTION CHOICE
            if player_status == "fold":
                pass
            else:
                if opponent_picked.value == 1:
                    # HORSE KEEPS BETTING
                    if opponent_chips - current_bet > 2 and player_chips - current_bet >= 1:
                        $ current_bet += 1
                        show screen cardgame_notify("Opponent raised the bet to [current_bet]!")
                        pause 1.5
                    else:
                        show screen cardgame_notify("Opponent checks!")
                        pause 1.5
                        $ opponent_checked = True
                elif opponent_picked.value == 12 or opponent_picked.value == 13:
                    if player_arrows == ["low","low"]:
                        # HORSE KEEPS BETTING
                        if opponent_chips - current_bet > 2 and player_chips - current_bet >= 1:
                            $ current_bet += 1
                            show screen cardgame_notify("Opponent raised the bet to [current_bet]!")
                            pause 1.5
                        else:
                            show screen cardgame_notify("Opponent checks!")
                            pause 1.5
                            $ opponent_checked = True
                    elif player_arrows == ["low","high"] or player_arrows == ["high","low"]:
                        # HORSE ATTEMPTS TO RAISE, WORKS 80% OF THE TIME
                        if renpy.random.randint(1,5) != 1:
                            if opponent_chips - current_bet >= 1 and player_chips - current_bet >= 1:
                                $ current_bet += 1
                                show screen cardgame_notify("Opponent raised the bet to [current_bet]!")
                                pause 1.5
                        else:
                            show screen cardgame_notify("Opponent checks!")
                            pause 1.5
                            $ opponent_checked = True
                    elif player_arrows == ["high","high"]:
                        # HORSE ATTEMPTS TO RAISE, WORKS 50% OF THE TIME
                        if renpy.random.randint(1,2) == 1:
                            if opponent_chips - current_bet >= 1 and player_chips - current_bet >= 1:
                                $ current_bet += 1
                                show screen cardgame_notify("Opponent raised the bet to [current_bet]!")
                                pause 1.5
                        else:
                            show screen cardgame_notify("Opponent checks!")
                            pause 1.5
                            $ opponent_checked = True
                elif opponent_picked.value == 11 or opponent_picked.value == 10:
                    if player_arrows == ["low","low"]:
                        # HORSE RAISES
                        if opponent_chips - current_bet >= 1 and player_chips - current_bet >= 1:
                            $ current_bet += 1
                            show screen cardgame_notify("Opponent raised the bet to [current_bet]!")
                            pause 1.5
                        else:
                            show screen cardgame_notify("Opponent checks!")
                            pause 1.5
                            $ opponent_checked = True
                    elif player_arrows == ["low","high"] or player_arrows == ["high","low"]:
                        # HORSE ATTEMPTS TO RAISE, WORKS 65% OF THE TIME
                        if renpy.random.randint(1,20) >= 13:
                            if opponent_chips - current_bet >= 1 and player_chips - current_bet >= 1:
                                $ current_bet += 1
                                show screen cardgame_notify("Opponent raised the bet to [current_bet]!")
                                pause 1.5
                        else:
                            show screen cardgame_notify("Opponent checks!")
                            pause 1.5
                            $ opponent_checked = True
                    elif player_arrows == ["high","high"]:
                        # HORSE ATTEMPTS TO RAISE, WORKS 20% OF THE TIME
                        if renpy.random.randint(1,5) == 2:
                            if opponent_chips - current_bet >= 1 and player_chips - current_bet >= 1:
                                $ current_bet += 1
                                show screen cardgame_notify("Opponent raised the bet to [current_bet]!")
                                pause 1.5
                        else:
                            show screen cardgame_notify("Opponent checks!")
                            pause 1.5
                            $ opponent_checked = True
                elif opponent_picked.value == 9 or opponent_picked.value == 8:
                    if player_arrows == ["low","low"]:
                        # HORSE RAISES
                        if opponent_chips - current_bet >= 1 and player_chips - current_bet >= 1:
                            $ current_bet += 1
                            show screen cardgame_notify("Opponent raised the bet to [current_bet]!")
                            pause 1.5
                        else:
                            show screen cardgame_notify("Opponent checks!")
                            pause 1.5
                            $ opponent_checked = True
                    elif player_arrows == ["low","high"] or player_arrows == ["high","low"]:
                        # HORSE CHECKS
                        show screen cardgame_notify("Opponent checks!")
                        pause 1.5
                        $ opponent_checked = True
                    elif player_arrows == ["high","high"]:
                        # HORSE CHECKS
                        show screen cardgame_notify("Opponent checks!")
                        pause 1.5
                        $ opponent_checked = True
                elif opponent_picked.value == 7:
                    if player_arrows == ["low","low"]:
                        # HORSE RAISES
                        if opponent_chips - current_bet >= 1 and player_chips - current_bet >= 1:
                            $ current_bet += 1
                            show screen cardgame_notify("Opponent raised the bet to [current_bet]!")
                            pause 1.5
                        else:
                            show screen cardgame_notify("Opponent checks!")
                            pause 1.5
                            $ opponent_checked = True
                    elif player_arrows == ["low","high"] or player_arrows == ["high","low"]:
                        # HORSE CHECKS
                        show screen cardgame_notify("Opponent checks!")
                        pause 1.5
                        $ opponent_checked = True
                    elif player_arrows == ["high","high"]:
                        # HORSE CHECKS
                        show screen cardgame_notify("Opponent checks!")
                        pause 1.5
                        $ opponent_checked = True
                else:
                    if player_arrows == ["low","low"]:
                        # HORSE CHECKS
                        show screen cardgame_notify("Opponent checks!")
                        pause 1.5
                        $ opponent_checked = True
                    elif player_arrows == ["low","high"] or player_arrows == ["high","low"]:
                        # HORSE CHECKS
                        show screen cardgame_notify("Opponent checks!")
                        pause 1.5
                        $ opponent_checked = True
                    elif player_arrows == ["high","high"]:
                        # HORSE CHECKS
                        show screen cardgame_notify("Opponent checks!")
                        pause 1.5
                        $ opponent_checked = True
                $ previous_bet = current_bet
        # RESULTS

        if player_status == "fold":
            $ round_winner = 'Opponent'
            $ current_bet = previous_bet
        else:
            if opponent_picked.value == 1 and player_picked.value == 2:
                $ round_winner = 'Player'
            elif opponent_picked.value == 2 and player_picked.value == 1:
                $ round_winner = 'Opponent'
            elif opponent_picked.value == player_picked.value:
                $ round_winner = "Tie"
            elif opponent_picked.value == 1 and player_picked.value != 2:
                $ round_winner = 'Opponent'
            elif opponent_picked.value != 2 and player_picked.value == 1:
                $ round_winner = 'Player'
            else:
                if opponent_picked.value > player_picked.value:
                    $ round_winner = 'Opponent'
                elif opponent_picked.value < player_picked.value:
                    $ round_winner = 'Player'

        $ renpy.show("card_back",[card_size_adjust,opponent_card_pos],layer="opponent_card_layer")
        $ renpy.show("card_back",[card_size_adjust,player_card_pos],layer="player_card_layer")
        pause 0.5
        $ renpy.show("card_back",[card_flip_back,card_size_adjust,opponent_card_pos],layer="opponent_card_layer")
        pause 0.5
        $ renpy.show(opponent_picked.img,[card_flip_front,card_size_adjust,opponent_card_pos],layer="opponent_card_layer")
        pause 0.5
        $ renpy.show("card_back",[card_flip_back,card_size_adjust,player_card_pos],layer="player_card_layer")
        pause 0.5
        $ renpy.show(player_picked.img,[card_flip_front,card_size_adjust,player_card_pos],layer="player_card_layer")
        pause 0.5

        if round_winner != 'Tie':
            if round_winner == "Opponent":
                $ player_chips -= current_bet
                $ opponent_chips += current_bet
            else:
                $ opponent_chips -= current_bet
                $ player_chips += current_bet
            show screen cardgame_notify("[round_winner] has won the round!")
            pause 1.5
        else:
            show screen cardgame_notify("There was a tie!")
            pause 1.5

        if round_winner == 'Player':
            show kid player_wins_round
            show horse player_wins_round
            pause 1.5
            show kid neutral
            show horse neutral
        elif round_winner == 'Opponent':
            show kid player_loses_round
            show horse player_loses_round
            pause 1.5
            show kid neutral
            show horse neutral

        $ current_bet = 1
        $ renpy.hide(opponent_picked.img, layer="opponent_card_layer")
        $ renpy.hide(player_picked.img, layer="player_card_layer")
        pause 1.0
    show screen cardgame_notify("[round_winner] has won the game!")
    pause 1.5
    hide screen cardgame_overlay
    if player_chips >= 20:
        if gamenumber == 1:
            $ battle_one_won = True
        elif gamenumber == 2:
            $ battle_two_won = True
        elif gamenumber == 3:
            $ battle_three_won = True
    elif opponent_chips >= 20:
        if gamenumber == 1:
            $ battle_one_won = False
        elif gamenumber == 2:
            $ battle_two_won = False
        elif gamenumber == 3:
            $ battle_three_won = False
    return


screen cardgame_pick_card():
    default btn_hovered = None

    imagebutton:
        pos(500,265)
        idle player_hand[0].image 
        hovered SetScreenVariable('btn_hovered',0)
        unhovered SetScreenVariable('btn_hovered',None)
        if btn_hovered == 0:
            at card_hovered
        else:
            at card_size_adjust
        action [SetVariable('player_picked',player_hand[0]), RemoveFromSet(set=player_hand,value=player_hand[0]),Return()]
    imagebutton:
        pos(1045,265)
        idle player_hand[1].image 
        hovered SetScreenVariable('btn_hovered',1)
        unhovered SetScreenVariable('btn_hovered',None)
        if btn_hovered == 1:
            at card_hovered
        else:
            at card_size_adjust
        action [SetVariable('player_picked',player_hand[1]), RemoveFromSet(set=player_hand,value=player_hand[1]),Return()]

screen cardgame_action_choice():
    add "images/tealgoat/cards/card_back.png" pos(500,265) at card_size_adjust
    add "images/tealgoat/cards/card_back.png" pos(1045,265) at card_size_adjust
    hbox:
        xalign 0.5
        ypos 910
        spacing 20
        imagebutton auto "images/tealgoat/minigame_check_%s.png" action Return("poker_check")
        imagebutton auto "images/tealgoat/minigame_raise_%s.png" action Return("poker_raise")
        imagebutton auto "images/tealgoat/minigame_fold_%s.png" action Return("poker_fold")

screen cardgame_raise():
    vbox:
        ypos 200
        xalign 0.5
        spacing 20
        text "Current bet: [current_bet]" color('#ffffff') size 50
    hbox:
        ypos 465
        xalign 0.5
        spacing 20
        imagebutton auto "images/tealgoat/chip_one_%s.png" action If(player_chips - current_bet >= 1 and opponent_chips - current_bet >= 1, true = SetVariable('current_bet', current_bet+1))
    imagebutton auto "images/tealgoat/minigame_clear_%s.png" action SetVariable('current_bet', previous_bet) ypos 800 xalign 0.5
    hbox:
        ypos 910
        spacing 20
        xalign 0.5
        imagebutton auto "images/tealgoat/minigame_deal_%s.png" action Return("poker_deal")
        imagebutton auto "images/tealgoat/minigame_check_%s.png" action [SetVariable('current_bet', previous_bet),Return('poker_back')]

screen cardgame_notify(message):
    zorder 100
    frame:
        align(0.5,0.1)
        xysize(600,200)
        background Solid("#000")
        text message align(0.5,0.5)
        timer 1.5 action Hide("cardgame_notify")

screen cardgame_overlay():
    vbox:
        pos(355,10)
        spacing 10
        for i in opponent_arrows:
            add "images/tealgoat/arrow_[i].png"
    vbox:
        pos(1485,10)
        spacing 10
        for i in player_arrows:
            add "images/tealgoat/arrow_[i].png"
    text "[opponent_chips]/20" size 60 pos(120,700)
    text "[player_chips]/20" size 60 pos(1600,700)