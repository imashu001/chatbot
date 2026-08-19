from llm import generate_response

import datetime

def main():
    try:

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
            # print(f"chatbot : {generate_response(input=user_input)}")

            # streaming response 
            print("Chatbot: ", end="", flush=True)

            for chunk in generate_response(user_input):
                print(chunk["message"]["content"], end="", flush=True)
                if chunk["done"] == True and chunk["done_reason"] == 'stop':
                    print()
                    print(f"Total Duration[ {chunk['total_duration'] / 1_000_000_000} seconds]  ** Token input = {chunk['prompt_eval_count']} ** Token Output = {chunk["eval_count"]}")

            print()
    except KeyboardInterrupt:
        print("User Interrupted stopping he chatbot :: GOODBYE")

    except Exception as e:
        print(f"Unknown exception detected {e}")


if __name__ == "__main__":
    main()