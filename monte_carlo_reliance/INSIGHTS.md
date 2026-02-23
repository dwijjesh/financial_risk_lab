# Monte Carlo Simulation – Reliance Industries

## Objective
To analyze long-horizon downside risk for Reliance Industries using
Monte Carlo simulation and understand why probability of loss can
remain high even over multi-year horizons.

## Why Reliance?
Reliance Industries was chosen due to its long trading history,
high liquidity, and exposure to multiple economic regimes.
Its structural growth makes it a strong test case for evaluating
the limitations of standard Monte Carlo assumptions.

## Method
- Historical log returns
- Mean and volatility estimated from past data
- 20,000 Monte Carlo simulations
- 5-year investment horizon

## Key Observations
- Probability of loss remains elevated even over longer horizons
- Outcome distribution is highly skewed
- Extreme downside paths dominate risk metrics

## Limitations
- Assumes stationary returns
- Ignores regime changes
- Overestimates downside risk for structurally growing firms

## Next Improvements
- Regime-based volatility
- Drawdown-focused metrics
- SIP vs lump sum comparison

## How to Read the Outcome Distribution Plot:
![Final price distribution](final_price_distribution.png)

Each bar in the histogram represents the frequency of final simulated
prices after a 5-year investment horizon.

### How this plot was generated
- Daily log returns were calculated from historical price data
- Mean and volatility were estimated from this return series
- 20,000 random price paths were simulated over a 5-year horizon
- The final price from each simulation was recorded
- These final prices were aggregated into a histogram

### How to interpret the plot
- The x-axis shows possible final price outcomes after 5 years
- The y-axis shows the probability density of those outcomes
- The distribution is right-skewed with a long left tail
- While most outcomes are positive, extreme downside scenarios
  contribute significantly to loss probability

### Why this matters
- This visualization explains why probability-of-loss metrics remain
elevated despite favorable average outcomes. Tail risk dominates
the distribution, which can mislead long-term investors if interpreted
without context.
