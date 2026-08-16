# ETF Strategy Performance Prediction

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

- This project investigates whether an ETF momentum strategy is likely to continue outperforming the S&P 500 over the next 12 months. Historical strategy returns and relevant market indicators will be used to evaluate expected future performance and downside risk. The problem is important because historical profitability alone does not guarantee that a trading strategy will remain effective under changing market conditions.

- The primary stakeholder is a portfolio manager who must decide whether to continue, reduce, or terminate capital allocation to the strategy. The project is primarily predictive. A useful output would include expected 12-month excess return relative to the S&P 500, associated risk measures such as volatility and maximum drawdown, and a concise forecast report that supports the portfolio allocation decision.

## Stakeholder & User

- Decision owner: Portfolio Manager
- User of analysis: Portfolio Manager / Quantitative Analyst
- Decision: Continue, reduce, or stop allocation
- Horizon: Next 12 months

## Useful Answer & Decision

- Type: Predictive
- Benchmark: S&P 500
- Metrics:
  - Expected excess return
  - Volatility
  - Maximum drawdown
- Deliverable: Forecast and risk report

## Assumptions & Constraints

- Historical market relationships remain reasonably informative.
- Sufficient ETF liquidity is available.
- Transaction costs affect realized performance.
- Historical market and strategy data are available.
- Strategy capacity may limit scalability.

## Known Unknowns / Risks

- Future market regimes may differ from historical regimes.
- Macroeconomic shocks may affect strategy performance.
- Historical patterns may not persist.
- Transaction costs and market impact may reduce realized returns.

## Lifecycle Mapping

- Define whether the strategy remains viable
  → Problem Framing & Scoping
  → Defined decision problem

- Collect historical market and strategy data
  → Data Collection
  → Analysis-ready dataset

- Estimate future strategy performance
  → Modeling
  → 12-month performance forecast

- Support portfolio allocation
  → Reporting
  → Forecast and risk report

## Repo Plan

- `data/`: raw and processed data
- `src/`: reusable Python functions
- `notebooks/`: exploratory analysis and modeling
- `docs/`: stakeholder-facing documents