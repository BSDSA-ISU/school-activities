# my contrib

## Number 3

### 1. Architecture Overview

* **Architecture Type:** Star Schema (with two fact tables to properly handle both line-item sales and payment transactions).
* **Primary Grain:**
* `fact_order_sales`: One row per **Order Line Item** (`order_details`).
* `fact_payments`: One row per **Payment Transaction** (`payments`).



---

### 2. Fact Tables

#### A. `fact_order_sales`

Captures the core product sales metrics linked to customers, menu items, categories, and time.

| Column Name | Data Type | Description / Role |
| --- | --- | --- |
| `order_sales_key` | INT (PK) | Surrogate key for the fact table |
| `order_id` | INT | Natural key from `orders`<br> |
| `customer_key` | INT (FK) | Links to `dim_customer` |
| `menu_item_key` | INT (FK) | Links to `dim_menu_item` |
| `category_key` | INT (FK) | Links to `dim_category` |
| `date_key` | INT (FK) | Links to `dim_date` (`YYYYMMDD`) |
| `quantity` | INT | **Measure:** Quantity ordered

 |
| `unit_price` | DECIMAL(10,2) | **Measure:** Price per unit at time of sale

 |
| `line_total` | DECIMAL(10,2) | **Measure:** Calculated as `quantity * unit_price` |

#### B. `fact_payments`

Captures financial transaction flows introduced by the new `payments` table.

| Column Name | Data Type | Description / Role |
| --- | --- | --- |
| `payment_fact_key` | INT (PK) | Surrogate key for payment facts |
| `payment_id` | INT | Natural key from `payments`<br> |
| `order_id` | INT | Natural key from `orders`<br> |
| `customer_key` | INT (FK) | Links to `dim_customer` |
| `date_key` | INT (FK) | Links to `dim_date` |
| `payment_method_key` | INT (FK) | Links to `dim_payment_method` |
| `amount` | DECIMAL(10,2) | **Measure:** Payment amount processed

 |
| `payment_status` | VARCHAR(30) | Status (e.g., Completed, Failed)

 |

---

### 3. Dimension Tables & SCD Strategies

#### A. `dim_customer` (Customer Dimension)

* **SCD Strategy:** **SCD Type 2** (Tracks historical changes to customer phone numbers and delivery addresses).

| Column Name | Data Type | Description |
| --- | --- | --- |
| `customer_key` | INT (PK) | Surrogate Key |
| `customer_id` | INT | Natural Key from `customers`<br> |
| `customer_name` | VARCHAR(100) | Customer Name

 |
| `phone` | VARCHAR(20) | Phone Number

 |
| `address` | VARCHAR(255) | Delivery Address

 |
| `effective_date` | DATE | Version start date |
| `expiry_date` | DATE | Version end date |
| `is_current` | BOOLEAN | Flag (`TRUE` for active record) |

#### B. `dim_menu_item` (Menu Item Dimension)

* **SCD Strategy:** **SCD Type 2** (Essential for capturing price changes over time so historical sales reports remain accurate).

| Column Name | Data Type | Description |
| --- | --- | --- |
| `menu_item_key` | INT (PK) | Surrogate Key |
| `menu_item_id` | INT | Natural Key from `menu_items`<br> |
| `item_name` | VARCHAR(100) | Item Name

 |
| `price` | DECIMAL(10,2) | Price version of the item

 |
| `availability` | TINYINT(1) | Availability flag

 |
| `effective_date` | DATE | Version start date |
| `expiry_date` | DATE | Version end date |
| `is_current` | BOOLEAN | Flag indicating active version |

#### C. `dim_category` (Category Dimension)

* **SCD Strategy:** **SCD Type 1** (Overwrites updates since categories rarely have historical tracking requirements).

| Column Name | Data Type | Description |
| --- | --- | --- |
| `category_key` | INT (PK) | Surrogate Key |
| `category_id` | INT | Natural Key from `categories`<br> |
| `category_name` | VARCHAR(50) | Category Name

 |

#### D. `dim_payment_method` (Payment Method Dimension)

* **SCD Strategy:** **SCD Type 1** (Attributes for payment types like Cash, Credit Card, Digital Wallet).

| Column Name | Data Type | Description |
| --- | --- | --- |
| `payment_method_key` | INT (PK) | Surrogate Key |
| `payment_method` | VARCHAR(30) | Method description (e.g., Credit Card)

 |

#### E. `dim_date` (Date Dimension)

* **SCD Strategy:** Static / Pre-calculated calendar table.

| Column Name | Data Type | Description |
| --- | --- | --- |
| `date_key` | INT (PK) | Integer format `YYYYMMDD` |
| `full_date` | DATE | Standard calendar date |
| `month_name` | VARCHAR(15) | Month name |
| `quarter` | INT | Quarter (1-4) |
| `year` | INT | Four-digit year |
