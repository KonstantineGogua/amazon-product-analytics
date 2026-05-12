# Amazon Product Analytics Dashboard

## Project Overview

This project analyzes Amazon product data using Python, SQL, and Power BI to uncover insights related to product ratings, pricing, discounts, and customer engagement.

The goal was to build a complete analytics workflow from raw CSV data to an interactive business intelligence dashboard.

---

## Dashboard Preview

### Main Dashboard View

![Main Dashboard View](screenshots/header.png)

---

### Dashboard Lower Section

![Dashboard Lower Section](screenshots/lower.png)

---

## SQL Analysis Example

![SQL Analysis Example](screenshots/sql_analysis_example.png)

---

## Tools Used

- Python (Pandas)
- MySQL
- Power BI
- CSV Data Processing

---

## Project Workflow

1. Cleaned and transformed raw Amazon product data using Python
2. Performed SQL analysis queries to explore business insights
3. Built an interactive Power BI dashboard
4. Analyzed relationships between pricing, ratings, discounts, and customer engagement

---

## Dashboard Features

### KPI Cards

- Average Rating
- Average Discount %
- Total Products
- Total Reviews

### Interactive Features

- Category slicer for dynamic filtering

### Visualizations

- Average Rating by Category
- Top Reviewed Products
- Price vs Product Rating Scatter Plot

---

## Key Insights

- Most products maintain ratings between 3.8 and 4.5 regardless of price
- Electronics categories dominate customer engagement and review activity
- Higher discounts do not necessarily result in higher product ratings
- Product popularity is concentrated among a relatively small number of products

---

## SQL Analysis

SQL queries included:

- Highest rated categories
- Most reviewed products
- Discount analysis
- Premium product analysis

---

## Project Structure

```text
amazon-product-analytics/
├── data/
├── scripts/
├── sql/
├── dashboard/
├── screenshots/
│   ├── header.png
│   ├── lower.png
│   └── sql_analysis_example.png
└── README.md
