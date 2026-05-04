from answer_function import generate_answer

def main():
    print("Study Agent is ready!")
    
    while True:
        query = input("\nAsk something (or type 'exit'): ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        print("\nThinking...\n")
        answer = generate_answer(query)
        print("ANSWER:\n")
        print(answer)
        print("\n" + "-"*50)

if __name__ == "__main__":
    main()
