# Monte Carlo Stock Price Simulator 📈

Simulates possible future stock price paths using Geometric Brownian Motion (the same math behind Black-Scholes).

Basically: instead of guessing one future price, we simulate thousands of "what if" scenarios and look at the spread.

## How it works

- Uses the formula `S_t = S0 * exp(sigma * W_t + mu*t - 0.5*sigma^2*t)`
- `W_t` = Brownian motion, built from random normal steps
- Run it many times → get a range of possible outcomes, not just one number

## Usage

```bash
pip install numpy matplotlib
python monte_carlo_gbm.py
```

Adjust the parameters at the bottom of the script to try different scenarios:

```python
simulate_gbm_paths(
    s0=100,      # starting price
    mu=0.05,     # expected return (drift)
    sigma=0.3,   # volatility
    T=1.0,       # time horizon in years
    n_paths=1000 # number of simulations
)
```

## Output

- Console: mean/std/5th-95th percentile of final prices
- A plot of simulated paths + the average path
- Saves the plot as `gbm_simulation.png`

## Why

Made this while studying continuous-time finance (Black-Scholes / GBM). Good way to actually *see* what "volatility" and "drift" do instead of just staring at the formula.
