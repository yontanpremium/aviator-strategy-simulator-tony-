import random
import time

def run_aviator_sim():
    balance = 1000  # Your starting virtual money
    bet = 100       # How much you bet each round
    target = 1.50   # When you plan to "Auto Cash Out"
    
    print(f"🚀 Simulation Started! Starting Balance: {balance} KES")
    print(f"Strategy: Cash out at {target}x every time.\n")

    for round_num in range(1, 11):  # Runs 10 rounds
        print(f"--- Round {round_num} ---")
        
        # This is the math the real game uses (Random Number Generator)
        crash_point = round(random.uniform(1.0, 5.0), 2) 
        # Note: In real life, there's a house edge, but we'll keep it simple
        
        print(f"Plane is flying... ✈️")
        time.sleep(1) # Makes it feel like the real game
        
        if crash_point >= target:
            profit = bet * (target - 1)
            balance += profit
            print(f"✅ WON! Plane crashed at {crash_point}x. You cashed out at {target}x.")
        else:
            balance -= bet
            print(f"💥 LOST! Plane crashed at {crash_point}x before you could cash out.")
            
        print(f"Current Balance: {balance:.2f} KES\n")
        
        if balance <= 0:
            print("❌ BUST! You ran out of money.")
            break

    print("--- Simulation Finished ---")
    print(f"Final Balance: {balance:.2f} KES")

if __name__ == "__main__":
    run_aviator_sim()
  
