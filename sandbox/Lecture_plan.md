---
title: "Tytuł strony"
description: "Opis strony"
author: "Autor"
date: 2025-01-15
---


# Całkowanie - Podstawowe Pojęcia

## 1. Całka Nieoznaczona

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

Całka nieoznaczona to funkcja pierwotna, czyli funkcja, której pochodna daje zadaną funkcję. Ogólna postać to:

$$
\int f(x) \, dx = F(x) + C
$$

Gdzie:
- $f(x)$ to funkcja podcałkowa,
- $F(x)$ to funkcja pierwotna,
- $C$ to stała całkowania.

**Przykład**:  
Jeśli $f(x) = 2x$, to $F(x) = x^2 + C$.

---

## 2. Całka Oznaczona
Całka oznaczona reprezentuje pole pod wykresem funkcji $f(x)$ w przedziale $[a, b]$. Oblicza się ją według wzoru:

$$
\int_a^b f(x) \, dx = F(b) - F(a)
$$

Gdzie $F(x)$ to funkcja pierwotna.

**Przykład**:  
Pole pod wykresem funkcji $f(x) = x^2$ w przedziale $[0, 2]$:  
$$
\int_0^2 x^2 \, dx = \left[ \frac{x^3}{3} \right]_0^2 = \frac{2^3}{3} - \frac{0^3}{3} = \frac{8}{3}.
$$

---

## 3. Wzory Podstawowe
Kilka przydatnych wzorów:

1. $\int x^n \, dx = \frac{x^{n+1}}{n+1} + C$, dla $n \neq -1$,
2. $\int e^x \, dx = e^x + C$,
3. $\int \frac{1}{x} \, dx = \ln|x| + C$,
4. $\int \sin(x) \, dx = -\cos(x) + C$,
5. $\int \cos(x) \, dx = \sin(x) + C$.

---

## 4. Metody Całkowania
1. **Przez podstawianie**  
   Zamieniasz zmienną na prostszą.  
   **Przykład**:  
   $$
   \int (2x + 1)^3 \, dx
   $$

2. **Przez części**  
   Dla iloczynu dwóch funkcji:  
   $$
   \int u \, dv = uv - \int v \, du
   $$

---

Jeśli masz dodatkowe pytania lub chcesz coś rozszerzyć, daj znać! 😊    