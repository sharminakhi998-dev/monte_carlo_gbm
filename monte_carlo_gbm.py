import numpy as np
import matplotlib.pyplot as plt

def simulate_gbm_paths(s0= 100, mu= 0.05, sigma= 0.3, T= 1.0, n_steps= 252, n_paths= 1000, seed= None):


  if seed is not None:
    np.random.seed(seed)

  dt = T/ n_steps
  times = np.linspace(0, T, n_steps + 1)

  random_shocks = np.random.normal(loc=0.0, scale = np.sqrt(dt), size= (n_paths, n_steps))

  W = np.cumsum(random_shocks, axis= 1)
  W = np.hstack([np.zeros((n_paths, 1)), W])

  paths = s0 * np.exp(sigma * W + (mu - 0.5 * sigma**2) * times)
  return times, paths

def plot_paths(times, paths, n_show = 30):
  plt.figure(figsize =(9,5))

  for i in range(min(n_show, paths.shape[0])):
    plt.plot(times, paths[i], linewidth = 0.8, alpha = 0.6)

  mean_path = paths.mean(axis=0)
  plt.plot(times, mean_path, color = "black", linewidth = 2.5, label = "Avg path(Monte carlo estimate)")

  plt.title("Monte Carlo simulation of geometric Brownian Motion")
  plt.xlabel("Time(years)")
  plt.ylabel("Price")
  plt.legend()
  plt.tight_layout()
  plt.savefig("gbm_simulation.png", dpi = 150)
  plt.show()

def summarize(paths):
  final_prices = paths[:,-1]
  print (f"Number of simulations : {len(final_prices)}")
  print (f"Mean final price : {final_prices.mean():.2f}")
  print(f"Std dev of final price : {final_prices.std():.2f}")
  print(f"5th percentile : {np.percentile(final_prices, 5):.2f}")
  print(f"95th percentile : {np.percentile(final_prices, 95):.2f}")
if __name__ == "__main__":
    times, paths = simulate_gbm_paths(
        s0=100,
        mu=0.05,
        sigma=0.3,
        T=1.0,
        n_steps=252,
        n_paths=1000,
        seed= 42,
    )
    summarize(paths)
    plot_paths(times, paths, n_show=30)

