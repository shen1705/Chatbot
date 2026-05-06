from sources.engine import ChatEngine
import sys

def main():
    print("--- Starting  ---")
    try:
        
        bot = ChatEngine()
        print("READY! Please type your question")
    except Exception as e:
        print(f"ERROR! {e}")
        sys.exit(1)

    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["exit"]:
            print("Shut down")
            break
            
        if not user_input.strip():
            continue
        #response 
        response = bot.get_response(user_input)
        print(f"\nAI: {response}")

if __name__ == "__main__":
    main()