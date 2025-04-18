ball = "neighborhood ball"  # Global

def house():
    ball = "house ball"  # Enclosing
    
    def bedroom():
        ball = "bedroom ball"  # Local
        print(ball)  # Prints: bedroom ball
    
    bedroom()
    print(ball)  # Prints: house ball

house()
print(ball)  # Prints: neighborhood ball