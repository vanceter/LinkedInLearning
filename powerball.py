import random

def generate_powerball_number():
    """
    Generates a random Powerball lottery number.

    A Powerball number consists of five unique white ball numbers from 1 to 69,
    and one red Powerball number from 1 to 26.
    """
    # Generate 5 unique white ball numbers from 1 to 69
    white_balls = random.sample(range(1, 70), 5)
    
    # Sort the white ball numbers for a cleaner display
    white_balls.sort()
    
    # Generate 1 red Powerball number from 1 to 26
    powerball = random.randint(1, 26)
    
    return white_balls, powerball

if __name__ == "__main__":
    white_balls, powerball = generate_powerball_number()
    
    # Format the output for better readability
    print("Your Powerball numbers are:")
    print(f"White balls: {white_balls[0]}, {white_balls[1]}, {white_balls[2]}, {white_balls[3]}, {white_balls[4]}")
    print(f"Powerball: {powerball}")
