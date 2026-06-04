# Common Stack ADT Algorithms

## Descrption
> This document contains common examples and code solutions that use the Stack ADT. If you're unfamiliar with the Stack ADT, please read [the Stack ADT Notes](../../data_structures/stack.md) first.

> Some examples also use terminology such as infix and postfix expressions; if these concepts are unfamiliar, refer to [the Expression Notation Notes](../../miscellaneous/expression_notations.md) before continuing.

## Balanced Brackets/Braces
1. Initialise an empty stack.
2. For every character:
   - If it is an open bracket/brace, then push it onto the stack.
   - If it is a closed bracket/brace, then:
     - If the stack is empty, return `ERROR - not balanced`.
     - Pop an element from the stack.
     - If the popped bracket/brace does not match the current character, return `ERROR - not balanced`.
   - If it is a non-bracket character, skip it.
3. If the stack is **not empty**, return `ERROR - not balanced`.
4. Otherwise, return `BALANCED`.

---

### Python Code

```py
def is_balanced(expression):
    stack = Stack()

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        # If opening bracket, push to stack
        if char in "([{":
            stack.push(char)

        # If closing bracket
        elif char in ")]}":
            if stack.is_empty():
                return "ERROR - not balanced"

            top = stack.pop()
            if top != pairs[char]:
                return "ERROR - not balanced"

        # Ignore non-bracket characters
        else:
            continue

    # If anything left in stack, it's not balanced
    if not stack.is_empty():
        return "ERROR - not balanced"

    return "BALANCED"
```

---

### Example Run Through

```py
print(is_balanced("[{()]"))
```

---

| Iteration | Char | Stack State     | Explanation                                 |
| --------- | ---- | --------------- | ------------------------------------------- |
| 1         | [    | [`[`]           | Push opening bracket                        |
| 2         | {    | [`[`, `{`]      | Push opening bracket                        |
| 3         | (    | [`[`, `{`, `(`] | Push opening bracket                        |
| 4         | )    | [`[`, `{`]      | Pop `(` → matches `)`                       |
| 5         | ]    | ERROR           | Pop `{` → does not match `]` → not balanced |

### Output:
```
ERROR - not balanced
```

---

## Postfix Expression Evaluation
1. Initialise an empty stack.
2. For every token in the expression:
   - If the token is an operand (number), push it onto the stack.
   - If the token is an operator:
     - Pop the top two operands from the stack.
     - Perform the arithmetic operation using the operands (the first popped value is the right operand, and the second popped value is the left operand).
     - Push the result back onto the stack.
3. After all tokens are processed:
   - If the stack contains exactly one value, return it as the final answer.
   - Otherwise, return `ERROR`.

---

### Python Code

```py
def evaluate_postfix(expression):
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        # Check if token is a number (supports integers and decimals)
        try:
            value = float(token)
            stack.push(value)
        except ValueError:
            # Token is an operator
            if stack.size() < 2:
                return "ERROR"

            right = stack.pop()  # first popped = right operand
            left = stack.pop()   # second popped = left operand

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                if right == 0:
                    return "ERROR"
                result = left / right
            else:
                return "ERROR"

            stack.push(result)

    return stack.pop() if stack.size() == 1 else "ERROR"
```

---

### Example Run Through

```py
print(evaluate_postfix("2 1 - 3 *")) 
```

---

| Iteration | Token | Stack State | Explanation                         |
| --------- | ----- | ----------- | ----------------------------------- |
| 1         | 2     | [2]         | Push operand                        |
| 2         | 1     | [2, 1]      | Push operand                        |
| 3         | -     | [1]         | Pop 1 (right), Pop 2 (left) → 2 - 1 = 1, then push the result back onto the stack | 
| 4         | 3     | [1, 3]      | Push operand                        |
| 5         | *     | [3]         | Pop 3 (right), Pop 1 (left) → 1 * 3 = 3, then push the result back onto the stack |

### Output:
```
3
```

---

## Infix to Postfix Conversion
1. Initialise an empty stack and an empty output string.
2. For every token in the expression:
   - If the token is an operand (number):
     - Append it to the output string.
   - If the token is an open parenthesis `(`:
     - Push it onto the stack.
   - If the token is an operator:
     - If the stack is empty:
       - Push the operator onto the stack.
     - If the stack is not empty:
       - Pop the operators of **greater or equal precedence** from the stack and append them to the output string.
       - Stop when we encounter either a "(", an operator of lower precedence, or when the stack is empty.
       - Push the operator onto the stack.
   - If the token is a closing parenthesis `)`:
     - Pop operators from the stack and append them to the output string until the matching `(` is found.
     - Pop and discard the `(`.
3. After all tokens are processed:
   - Pop all remaining operators from the stack and append them to the output string.
4. Return the output string.

---

### Python Code

```py
s
```

---

## Notes
> N/A.