# Chapter 3.1: Propositional Logic 


## Logical Equivalence

Two (molecular) statements $P$ and $Q$ are **logically equivalent**
provided $P$ is true precisely when $Q$ is true. That is, $P$ and $Q$ have the
same truth value under any assignment of truth values to their atomic parts
(i.e. They have the same truth table).


## De Morgan's Laws
$$
\lnot(P \land Q) \text{ is logically equivalent to }
\lnot P \lor \lnot Q \text{.}\\
\lnot(P \lor Q) \text{ is logically equivalent to }
\lnot P \land \lnot Q \text{.}
$$


## Implications are Disjunctions
$$
P \rightarrow Q \text{ is logically equivalent to } \lnot P \lor Q \text{.}
$$


## Negation of an Implication
$$
\lnot (P \rightarrow Q) \text{ is logically equivalent to }
P \lor \lnot Q \text{.}
$$


## Predicate Logic

[Predicate Logic](https://en.wikipedia.org/wiki/First-order_logic) is a
formal language that uses
[quantified variables](https://en.wikipedia.org/wiki/Quantifier_(logic))
and [predicates](https://www.merriam-webster.com/dictionary/predicate) to
construct statements.

For example:
```
P(x): x is prime.
O(x): x is odd.
```
$$
\forall x((P(x) \land x > 2) \rightarrow O(x)) \text{.}
$$


## Converse and Contrapositive

The **converse** of an implication $P \rightarrow Q$ is the implication
$Q \rightarrow P$. The converse is *not* logically equivalent to the original
implication, its truth is independent of the truth of the original statement.

The **contrapositve** of an implication $P \rightarrow Q$ is the implication
$\lnot Q \rightarrow \lnot P$. An implication and its contrapositive are
logically equivalent.
