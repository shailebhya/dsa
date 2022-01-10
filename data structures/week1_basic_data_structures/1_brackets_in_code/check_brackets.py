# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        # print(opening_brackets_stack)

        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i+1))

        if next in ")]}":
            if not opening_brackets_stack:
              # return "False"
              return i+1              


            top =  opening_brackets_stack.pop()
            if not are_matching(top.char,next):
              return i+1
                # return text.index(opening_brackets_stack[-1])+1
    if opening_brackets_stack:
      top = opening_brackets_stack.pop()
      return top.position

            # Process closing bracket, write your code here
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
