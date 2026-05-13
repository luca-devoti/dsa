# Common Stack ADT Algorithms

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
s
```

---

## Postfix Expression Evaluation
1. Initialise an empty stack.
2. For every token in the expression:
   - If the token is an operand (number), push it onto the stack.
   - If the token is an operator:
     - Pop the top two operands from the stack.
     - Perform the arithmetic operation using the operands.
     - Push the result back onto the stack.
3. After all tokens are processed:
   - If the stack contains exactly one value, return it as the final answer.
   - Otherwise, return `ERROR`.

---

### Python Code

```py
s
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