SELECT * FROM "01_fund_master" LIMIT 5;

SELECT COUNT(*) FROM "02_nav_history";

SELECT scheme_name, nav
FROM "01_fund_master"
LIMIT 10;

SELECT *
FROM "08_investor_transactions"
LIMIT 5;

SELECT *
FROM "09_portfolio_holdings"
ORDER BY weight_pct DESC
LIMIT 5;