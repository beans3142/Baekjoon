import sys
input = sys.stdin.readline

def evaluate_expression(expression):
    def parse_set(s):
        return set(s[1:-1])
    
    def to_sorted_string(s):
        return "{" + "".join(sorted(s)) + "}"

    def precedence(op):
        if op == '*':
            return 3
        if op == '+':
            return 2
        if op == '-':
            return 1
        return 0

    def apply_op(op, a, b):
        if op == '+':
            return a | b
        if op == '*':
            return a & b
        if op == '-':
            return a - b
        return set()

    def evaluate(tokens):
        values = []
        ops = []
        i = 0
        
        while i < len(tokens):
            if tokens[i] == ' ':
                i += 1
                continue
            if tokens[i] == '{':
                j = i
                while tokens[j] != '}':
                    j += 1
                values.append(parse_set(tokens[i:j+1]))
                i = j + 1
            elif tokens[i] == '(':
                ops.append(tokens[i])
                i += 1
            elif tokens[i] == ')':
                while len(ops) != 0 and ops[-1] != '(':
                    op = ops.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    values.append(apply_op(op, val1, val2))
                ops.pop()
                i += 1
            elif tokens[i] in "+-*":
                while (len(ops) != 0 and precedence(ops[-1]) >= precedence(tokens[i])):
                    op = ops.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    values.append(apply_op(op, val1, val2))
                ops.append(tokens[i])
                i += 1
        
        while len(ops) != 0:
            op = ops.pop()
            val2 = values.pop()
            val1 = values.pop()
            values.append(apply_op(op, val1, val2))
        
        return values[-1]
    
    return to_sorted_string(evaluate(expression))

def main():
    while True:
        try:
            print(evaluate_expression(input().rstrip()))
        except:
            break

if __name__ == "__main__":
    main()
