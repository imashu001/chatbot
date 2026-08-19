from llm import generate_response

def main():

    while True:
        # handling input 
        user_input = input("You: ").strip()

        # handling empty inputs
        if user_input == "":
            print("Please type something to start chatting")
            continue

        # handling exit / quit keyword
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye")
            break

        # calling and printing llm output
        print(f"chatbot : {generate_response(input=user_input)}")


if __name__ == "__main__":
    main()