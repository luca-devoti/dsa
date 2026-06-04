# Expression Notations

## Description
> Expression notations describe how mathematical expressions are written and structured so they can be interpreted correctly by humans or computers.

---

## Infix Notation

- Infix expressions are mathematical expressions where the operator is placed between its operands. This is the most common notation used by humans.  
- For example, the expression **2 + 3** is an infix expression.  

- Infix expressions follow operator precedence rules, which determine the order in which operations are evaluated.  
- A common way to remember these rules is **BEDMAS** (Brackets, Exponents, Division/Multiplication, Addition/Subtraction).  

### Pros:
- More natural and easier for humans to read and understand.  

### Cons:
- Can be difficult for computers to parse and evaluate efficiently, since they must account for operator precedence and bracket rules.  

---

## Postfix Notation

- Postfix expressions, also known as Reverse Polish Notation (RPN), are a mathematical notation where the operator comes after its operands. This differs from infix notation, where the operator is placed between operands.  
- For example, the expression **2 3 +** is a postfix expression equivalent to the infix expression **2 + 3**.  

- Postfix expressions do not require parentheses or operator precedence rules because the order of operations is determined by the position of the operators and operands.  
- They are typically evaluated from left to right using a stack-based approach.

### Pros:
- Eliminates the need for brackets (parentheses).  
- Easier and more efficient for computers to evaluate since there is no need to handle operator precedence or parentheses.  

### Cons:
- Harder for humans to read and interpret compared to infix notation.  
- Requires understanding of stack-based evaluation to compute results.  