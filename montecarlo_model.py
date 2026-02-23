import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import t

# ================================
# USER INPUT
# ================================

ticker = "RELIANCE.NS"

start_date = "2010-01-01"
T = 5                 # years to simulate
steps = 252            # trading days
simulations = 20000

# ================================
# DOWNLOAD DATA
# ================================
data = yf.download(ticker, start=start_date, progress=False)
close_prices = data["Close"]

# ================================
# RETURNS (REALISTIC SETUP)
# ================================
# Log returns
returns = np.log(close_prices / close_prices.shift(1)).dropna()

# Winsorize daily returns (control outliers)
returns = returns.clip(lower=-0.12, upper=0.12)

# ================================
# VOLATILITY (RISK FIRST)
# ================================
sigma = returns.std().values[0] * np.sqrt(252)
sigma = min(sigma, 0.6)   # volatility cap

# ================================
# DRIFT (MEAN-REVERTING & SHRUNK)
# ================================
raw_mu = returns.mean().values[0] * 252
mu = 0.2 * raw_mu         # shrink optimism

theta = mu                # long-run mean
kappa = 1.2               # mean reversion speed

# ================================
# INITIAL PRICE
# ================================
S0 = close_prices.iloc[-1].values[0]
dt = T / steps

# ================================
# MONTE CARLO SIMULATION
# ================================
price_paths = np.zeros((steps, simulations))
price_paths[0] = S0

log_price = np.log(S0) * np.ones(simulations)

for step in range(1, steps):

    # Fat-tailed shocks
    Z = t.rvs(df=4, size=simulations)

    # Mean-reverting drift
    drift = kappa * (theta - mu) * dt

    # Log-return evolution
    log_price = (
        log_price
        + drift
        - 0.5 * sigma**2 * dt
        + sigma * np.sqrt(dt) * Z
    )

    price_paths[step] = np.exp(log_price)

# ================================
# FINAL DISTRIBUTION
# ================================
final_prices = price_paths[-1]

median_price = np.median(final_prices)
mean_price = np.mean(final_prices)

prob_loss = np.mean(final_prices < S0) * 100
worst_5 = np.percentile(final_prices, 5)
best_95 = np.percentile(final_prices, 95)

expected_return_percent = ((mean_price / S0) - 1) * 100

# ================================
# OUTPUT
# ================================
print("\n================ REAL-WORLD MONTE CARLO RESULTS ================")
print(f"Stock               : {ticker}")
print(f"Current Price       : ₹{S0:.2f}")
print(f"Median Future Price : ₹{median_price:.2f}")
print(f"Mean Future Price   : ₹{mean_price:.2f}")
print(f"Expected Return     : {expected_return_percent:.2f}%")
print(f"Probability of Loss : {prob_loss:.2f}%")
print(f"Worst Case (5%)     : ₹{worst_5:.2f}")
print(f"Best Case (95%)     : ₹{best_95:.2f}")
print("===============================================================\n")

# ================================
# PLOT
# ================================
plt.figure(figsize=(10, 5))
plt.plot(price_paths[:, :50])
plt.title(f"Real-World Monte Carlo Simulation – {ticker}")
plt.xlabel("Days")
plt.ylabel("Price")
plt.tight_layout()
plt.show()
