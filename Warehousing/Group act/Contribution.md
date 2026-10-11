# My Contribution

## Number 3

### 1. Architecture Overview

- **Architecture Type:** Star Schema (with two fact tables to properly handle both line-item sales and payment transactions).
- **Primary Grain:**
  - `fact_order_sales`: One row per **Order Line Item** (`order_details`).
  - `fact_payments`: One row per **Payment Transaction** (`payments`).

---

### 2. Fact Tables

#### A. `fact_order_sales`

Captures the core product sales metrics linked to customers, menu items, categories, and time.

| Column Name | Data Type | Description / Role |
|---|---|---|
| `order_sales_key` | INT (PK) | Surrogate key for the fact table |
| `order_id` | INT | Natural key from `orders` |
| `customer_key` | INT (FK) | Links to `dim_customer` |
| `menu_item_key` | INT (FK) | Links to `dim_menu_item` |
| `category_key` | INT (FK) | Links to `dim_category` |
| `date_key` | INT (FK) | Links to `dim_date` (`YYYYMMDD`) |
| `quantity` | INT | **Measure:** Quantity ordered |
| `unit_price` | DECIMAL(10,2) | **Measure:** Price per unit at the time of sale |
| `line_total` | DECIMAL(10,2) | **Measure:** Calculated as `quantity * unit_price` |

#### B. `fact_payments`

Captures financial transaction flows introduced by the new `payments` table.

| Column Name | Data Type | Description / Role |
|---|---|---|
| `payment_fact_key` | INT (PK) | Surrogate key for payment facts |
| `payment_id` | INT | Natural key from `payments` |
| `order_id` | INT | Natural key from `orders` |
| `customer_key` | INT (FK) | Links to `dim_customer` |
| `date_key` | INT (FK) | Links to `dim_date` |
| `payment_method_key` | INT (FK) | Links to `dim_payment_method` |
| `amount` | DECIMAL(10,2) | **Measure:** Payment amount processed |
| `payment_status` | VARCHAR(30) | Status (e.g., Completed, Failed) |

---

### 3. Dimension Tables & SCD Strategies

#### A. `dim_customer` (Customer Dimension)

- **SCD Strategy:** **SCD Type 2** (Tracks historical changes to customer phone numbers and delivery addresses).

| Column Name | Data Type | Description |
|---|---|---|
| `customer_key` | INT (PK) | Surrogate key |
| `customer_id` | INT | Natural key from `customers` |
| `customer_name` | VARCHAR(100) | Customer name |
| `phone` | VARCHAR(20) | Phone number |
| `address` | VARCHAR(255) | Delivery address |
| `effective_date` | DATE | Version start date |
| `expiry_date` | DATE | Version end date |
| `is_current` | BOOLEAN | Flag (`TRUE` for the active record) |

#### B. `dim_menu_item` (Menu Item Dimension)

- **SCD Strategy:** **SCD Type 2** (Essential for capturing price changes over time so historical sales reports remain accurate).

| Column Name | Data Type | Description |
|---|---|---|
| `menu_item_key` | INT (PK) | Surrogate key |
| `menu_item_id` | INT | Natural key from `menu_items` |
| `item_name` | VARCHAR(100) | Item name |
| `price` | DECIMAL(10,2) | Price for the item version |
| `availability` | TINYINT(1) | Availability flag |
| `effective_date` | DATE | Version start date |
| `expiry_date` | DATE | Version end date |
| `is_current` | BOOLEAN | Flag indicating the active version |

#### C. `dim_category` (Category Dimension)

- **SCD Strategy:** **SCD Type 1** (Overwrites updates since categories rarely have historical tracking requirements).

| Column Name | Data Type | Description |
|---|---|---|
| `category_key` | INT (PK) | Surrogate key |
| `category_id` | INT | Natural key from `categories` |
| `category_name` | VARCHAR(50) | Category name |

#### D. `dim_payment_method` (Payment Method Dimension)

- **SCD Strategy:** **SCD Type 1** (Stores attributes for payment types such as Cash, Credit Card, and Digital Wallet).

| Column Name | Data Type | Description |
|---|---|---|
| `payment_method_key` | INT (PK) | Surrogate key |
| `payment_method` | VARCHAR(30) | Method description (e.g., Credit Card) |

#### E. `dim_date` (Date Dimension)

- **SCD Strategy:** Static / pre-calculated calendar table.

| Column Name | Data Type | Description |
|---|---|---|
| `date_key` | INT (PK) | Integer format `YYYYMMDD` |
| `full_date` | DATE | Standard calendar date |
| `month_name` | VARCHAR(15) | Month name |
| `quarter` | INT | Quarter (1–4) |
| `year` | INT | Four-digit year |
