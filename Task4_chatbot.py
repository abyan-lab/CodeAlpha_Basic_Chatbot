def run_bot():
    print("Bot: Hey there! I'm a simple rule-based bot.")
    print("(type 'bye' to stop)")

    while True:
        text = input("Me: ").lower()

        if "hello" in text or "hi" in text:
            print("Bot: Hi! How's your day going?")
        
        elif "how are you" in text:
            print("Bot: I'm good, just running some code. You?")
            
        elif "bye" in text:
            print("Bot: Goodbye! Catch you later.")
            break
            
        elif "thank" in text:
            print("Bot: No problem at all!")
            
        else:
            print("Bot: I didn't quite get that, but that's cool.")

if __name__ == "__main__":
    run_bot()