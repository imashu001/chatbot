def main():

    while True:
        user_input = input("You: ").strip()

        if user_input == "":
            print("Please type something to start chatting")
            continue

        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye")
            break

        print(f"You said: {user_input}")


if __name__ == "__main__":
    main()