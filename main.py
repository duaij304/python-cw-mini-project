def padel_court_cost(court_type):
    if court_type == "indoor":
        return 30
    elif court_type == "outdoor":
        return 20
    else:
        return 0  


def rackets_cost(racket_brand):
    if racket_brand == "Bullpadel":
        return 100
    elif racket_brand == "Nox":
        return 140
    elif racket_brand == "Siux":
        return 200
    else:
        return 0  

def padel_balls_cost(ball_boxes):
    if ball_boxes == 1:
        return 2
    elif ball_boxes == 2:
        return 3.5
    elif ball_boxes == 3:
        return 5
    else:
        return 0  

def padel_game_cost():
    court_type = input("court type (indoor أو outdoor): ")
    racket_brand = input(" chose the ball  (Bullpadel أو Nox أو Siux): ")
    ball_boxes = input("put the boxes number (1 or 2 or 3): ")
    
    courtCost = padel_court_cost(court_type)
    racket = rackets_cost(racket_brand)
    ball_price = padel_balls_cost(ball_boxes)
    print(f"the total is {courtCost+racket+ball_price}")

padel_game_cost()