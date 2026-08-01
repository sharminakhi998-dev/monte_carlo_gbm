# Monte Carlo Stock Price Simulator 📈

This code simulates possible future stock price paths using Geometric Brownian Motion (the same math behind Black-Scholes).

Basically: instead of guessing one future price, this code simulates thousands of "what if" scenarios and look at the spread.

## How it works

The stock price follows a Geometric Brownian Motion:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

Its exact solution is:

$$
S_t = S_0 \exp\left[\left(\mu-\frac{1}{2}\sigma^2\right)t+\sigma W_t\right]
$$

where:

- $S_0$ is the initial stock price
- $\mu$ is the expected return or drift
- $\sigma$ is the volatility
- $W_t$ is a Brownian motion

Brownian motion is generated using normally distributed increments:

```math
\Delta W_i \sim \mathcal{N}(0,\Delta t).
```

The simulated stock price is updated using

```math
S_{t_{i+1}}
=
S_{t_i}
\exp\left[
\left(\mu-\frac{1}{2}\sigma^2\right)\Delta t
+\sigma\Delta W_i
\right].
```

Repeating this process over all time steps generates one possible stock-price path. Running the simulation many times produces a range of possible outcomes rather than a single estimate.

