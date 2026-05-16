# Counting Primitive Operations

## Description
> Counting primitive operations is a method of theoretical algorithm analysis used to estimate an algorithm's running time in a way that is independent of hardware or programming language. Instead of measuring seconds, we count the number of steps performed.

---

## Key Idea
- If a function contains **nested loops**, it is usually easiest to:
1. Start with the **innermost loop**.
2. Count the operations inside that loop
3. Multiply by the number of iterations
4. Add **1 extra operation** for the final failed loop condition
5. Work outward toward the outer loops

---

## Example Run Through

```py
def rate(n):
    total = 0
    i = 0
    while i < n:
        j = 1
        while j < 8:
            total += j
            j *= 2
        i += 1
    return total
```

---

## Step 1 - Count Operations of the Inner Loop

```py
# j = 1
while j < 8:
    total += j
    j *= 2
```

1. Loop block contains 3 operations: `while j < 8`, `total += j`, `j *= 2`
2. `j` values: `1 → 2 → 4 → 8`, therefore block executes 3 times
3. Final failed condition at `j = 8` adds 1 extra operation

Inner loop operations:

```text
(3 × 3 + 1) = 10
```

---

## Step 2 - Outer Loop

```py
# i = 0
while i < n:
    j = 1
    # inner loop = 10 operations
    i += 1
```

1. Outer block contains 13 operations: `while loop condition`, `j = 1`, `inner loop (10)`, `i += 1`
2. `i` starts at `0` and increments by `1`, therefore loop executes `n` times
3. Final failed condition at `i = n` adds 1 extra operation

Outer loop operations:

```text
(10 + 3)n + 1 = 13n + 1
```

---

## Step 3 - Top-Level Operations

```py
total = 0
i = 0
# (13)n + 1
return total
```

1. Top-level contains 3 more operations: `total = 0`, `i = 0`, `return total`

Final operations:

```text
(13n + 1) + 3 = 13n + 4
```

---

# Final Answer

- Expanded: `((3 × 3 + 1) + 3)n + 4`
- Simplified: `13n + 4`

---

## Notes
> Personally, when solving these, I keep everything in expanded form and simplify at the end.