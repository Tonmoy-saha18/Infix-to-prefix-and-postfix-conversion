class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False


def priority(symbol):
    if symbol == '^':
        return 3
    elif symbol == '*' or symbol == '/':
        return 2
    elif symbol == '+' or symbol == '-':
        return 1
    else:
        return 0


def postfix(string):
    postfix_expression = ''
    stack = Stack()
    for a in string:
        if a.isalpha() or a.isdigit():
            postfix_expression += a
        else:
            prev = stack.peek()
            if prev is None or a == '(':
                stack.push(a)
            else:
                checker = True
                while checker:
                    prev = stack.peek()
                    if a != ')':
                        priority_check_present = priority(a)
                        priority_check_past = priority(prev)
                        if priority_check_present > priority_check_past:
                            stack.push(a)
                            checker = False
                        elif priority_check_past > priority_check_present:
                            value = stack.pop()
                            postfix_expression += value
                        else:
                            if a == '^':
                                stack.push('^')
                                checker = False
                            else:
                                value = stack.pop()
                                postfix_expression += value
                    else:
                        if prev == '(':
                            value = stack.pop()
                            checker = False
                        else:
                            value = stack.pop()
                            postfix_expression += value

    while not stack.isempty():
        value = stack.pop()
        postfix_expression += value

    return postfix_expression


def prefix(string):
    string = string[::-1]
    prefix_expression = ''
    stack = Stack()
    for a in string:
        if a.isalpha() or a.isdigit():
            prefix_expression += a
        else:
            prev = stack.peek()
            if prev is None or a == ')':
                stack.push(a)
            else:
                checker = True
                while checker:
                    prev = stack.peek()
                    if a != '(':
                        priority_check_present = priority(a)
                        priority_check_past = priority(prev)
                        if priority_check_present >= priority_check_past:
                            if a == '^' and priority_check_past == priority_check_present:
                                value = stack.pop()
                                prefix_expression += value
                            else:
                                stack.push(a)
                                checker = False
                        else:
                            value = stack.pop()
                            prefix_expression += value
                    else:
                        if prev == ')':
                            value = stack.pop()
                            checker = False
                        else:
                            value = stack.pop()
                            prefix_expression += value

    while not stack.isempty():
        value = stack.pop()
        prefix_expression += value

    return prefix_expression[::-1]


if __name__ == '__main__':
    print("Type 'console', 'file' or 'exit' for the choice")
    while True:
        choice = input("Enter your choice:")
        if choice == 'console' or choice == 'Console':
            infix = input("Enter the infix expression:")
            conversion_choice = input("If you want to covert the expression to postfix then type 'postfix' else type 'prefix':")
            if conversion_choice == 'postfix' or conversion_choice == 'Postfix':
                answer = postfix(infix)
                print("Postfix expression:", answer)
            elif conversion_choice == 'prefix' or 'Prefix':
                answer = prefix(infix)
                print("Prefix expression:", answer)
            else:
                print("Enter a valid conversion name")
        elif choice == 'file' or choice == 'File':
            path = input("Enter the path of the infix expression file:")
            with open(path, 'r+') as file:
                infix = file.readline()
                conversion_choice = input("If you want to covert the expression to postfix then type 'postfix' else type 'prefix':")
                if conversion_choice == 'postfix' or conversion_choice == 'Postfix':
                    answer = postfix(infix)
                    file.write("\n")
                    file.write(answer)
                elif conversion_choice == 'prefix' or 'Prefix':
                    answer = prefix(infix)
                    file.write('\n')
                    file.write(answer)
                else:
                    print("Enter a valid conversion name")
        elif choice == 'exit' or choice == 'Exit':
            break
        else:
            print("You have entered a invalid choice please enter a valid choice or type exit to terminate from the program")