# Fast API Assignment - Restaurant Management System 

A RESTful backend service for user management, restaurant operations, and order processing built with **FastAPI**, **Tortoise ORM**, and **Aerich**[span_1](start_span)[span_1](end_span).

---

## Features

### 1. User Management & Soft Deletion
* **CRUD operations**: Endpoints to register, retrieve, update, and delete users[span_2](start_span)[span_2](end_span).
* **Balance enforcement**: Ensures user wallet balances cannot fall below zero via Pydantic and database constraints[span_3](start_span)[span_3](end_span).
* **Soft delete**: Implements non-destructive user removal (`is_deleted` flag) to protect historical order records[span_4](start_span)[span_4](end_span).
* **Role separation**: Supports Normal Users, Restaurant Owners, and Administrators[span_5](start_span)[span_5](end_span).

### 2. Authentication & Session Control
* **JWT token authentication**: Login endpoint issuing signed JSON Web Tokens (`access_token`)[span_6](start_span)[span_6](end_span).
* **Database session tracking**: Tokens are registered in the database upon login[span_7](start_span)[span_7](end_span).
* **Complete logout**: The logout endpoint removes the active token from the database, instantly invalidating sessions[span_8](start_span)[span_8](end_span).
* **Protected routes**: Route-level dependency checks verifying token validity and user roles[span_9](start_span)[span_9](end_span).

### 3. Restaurant & Menu Management
* **Admin-only creation**: Only system administrators can create restaurants and assign owners[span_10](start_span)[span_10](end_span).
* **Multi-owner support**: Associates restaurants with owners through explicit ownership permissions[span_11](start_span)[span_11](end_span).
* **Menu CRUD**: Restaurant owners can add dishes, update prices and inventory quantities, and remove items[span_12](start_span)[span_12](end_span).
* **Owner profile enrichment**: User retrieval endpoints return affiliated restaurants if the account is an owner[span_13](start_span)[span_13](end_span).
* **Search & filters**: Menu querying filtered by category, price range, and rating[span_14](start_span)[span_14](end_span).

### 4. Ordering & Analytics
* **Order placement**: Normal users can create multi-item orders strictly within a single restaurant[span_15](start_span)[span_15](end_span).
* **Validation**: Validates that order total does not exceed user balance and item counts do not exceed available stock[span_16](start_span)[span_16](end_span).
* **Recency sorting**: Browse restaurants ordered by most recent transaction activity[span_17](start_span)[span_17](end_span).
* **Owner analytics**:
  * Item order frequencies (how many times each dish was ordered)[span_18](start_span)[span_18](end_span).
  * Top customer rankings by total order count[span_19](start_span)[span_19](end_span).
  * Detailed order histories[span_20](start_span)[span_20](end_span).

---

## Tech Stack & Prerequisites

* **Python 3.10+**
* **FastAPI** (Web framework)[span_21](start_span)[span_21](end_span)
* **Tortoise ORM** (Async ORM)[span_22](start_span)[span_22](end_span)
* **Aerich** (Database migrations)[span_23](start_span)[span_23](end_span)
* **PostgreSQL** or **SQLite** (Database)
* **Pytest & HTTPX** (Testing suite)[span_24](start_span)[span_24](end_span)

---

## Installation & Setup

### Clone the Repository
```bash
# Clone the repository
git clone https://github.com/jtg-induction/FastAPI-assignment1-TrijalLuhariwala-UID00832

# Create python virtual environment
python3 -m venv venv

#Activate virtual environment
source venv/bin/activate

#Install requirements
pip install -r requirement.txt
```

### Build and run the app

```bash
# Run the application in development mode
uvicorn app.main:app --reload
```

### To apply Aerich future migrations

```bash
# Run the application in development mode
aerich migrate
aerich upgrade
```
