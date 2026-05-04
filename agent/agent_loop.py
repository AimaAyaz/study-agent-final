# agent_loop.py
# This file will run the full agent pipeline.

from answer_function import generate_answer

def main():
    query = input("Ask something: ")
    print(generate_answer(query, None))

if __name__ == "__main__":
    main()
