# Section 3.2: Chapter Summary Exercises


## Exercise 1

Complete a truth table for the statement $\lnot P \rightarrow (Q \land R)$.
> ```
> +-------+-------+-------+-------------------+
> |   p   |   q   |   r   |  ~p => (q and r)  |
> |-------+-------+-------+-------------------|
> | True  | True  | True  |       True        |
> | True  | True  | False |       True        |
> | True  | False | True  |       True        |
> | True  | False | False |       True        |
> | False | True  | True  |       True        |
> | False | True  | False |       False       |
> | False | False | True  |       False       |
> | False | False | False |       False       |
> +-------+-------+-------+-------------------+
> ```


## Exercise 2

Suppose you know that the statement "if Peter is not tall, then Quincy is fat,
and Robert is skinny" is false. What, if anything, can you conclude about Peter
and Robert if you know that Quincy is indeed fat? Explain.

> The for an implication to be false, the conclusion must be false and the
> hypothesis must be true.  The conclusion is a conjunction, and we know that
> one of the conjuncts is true, so the other must be false (i.e. Robert is not
> skinny). We also know that the hypothesis must be true, so Peter is not
> tall.


## Exercise 3

Are the statements $P \rightarrow (Q \lor R)$ and
$(P \rightarrow Q) \lor (P \rightarrow R)$ logically equivalent?

> Looking at the following truth table:
> ```
> +-------+-------+-------+-----------------+------------------------+
> |   p   |   q   |   r   |  p => (q or r)  |  (p => q) or (p => r)  |
> |-------+-------+-------+-----------------+------------------------|
> | True  | True  | True  |      True       |          True          |
> | True  | True  | False |      True       |          True          |
> | True  | False | True  |      True       |          True          |
> | True  | False | False |      False      |         False          |
> | False | True  | True  |      True       |          True          |
> | False | True  | False |      True       |          True          |
> | False | False | True  |      True       |          True          |
> | False | False | False |      True       |          True          |
> +-------+-------+-------+-----------------+------------------------+
> ```
> we can see that they are logically equivalent. Alternatively, we can reason
> that a disjunction (like the second of these two statements) is false if and
> only if both disjuncts are false. Each of the disjuncts are implications,
> which are false only if they hypothesis is true and the conclusion is false.
> That means only when $Q$ is false, $R$ is false, and $P$ is true will both
> of these statements be false.


## Exercise 4

Is the following a valid deduction rule? Explain.
$$
\begin{array}{c}
P \rightarrow Q \\
P \rightarrow R \\
\hline
\therefore P \rightarrow (Q \land R).
\end{array}
$$
