# Fast API Assignment - Restaurant Management System 

A RESTful backend service for user management, restaurant operations, and order processing built with **FastAPI**, **Tortoise ORM**, and **Aerich**

---

# Features

### 1. User Management & Soft Deletion
* **CRUD operations**: Endpoints to register, retrieve, update, and delete users.
* **Balance enforcement**: Ensures user wallet balances cannot fall below zero via Pydantic and database constraints.
* **Soft delete**: Implements non-destructive user removal (`is_deleted` flag) to protect historical order records.
* **Role separation**: Supports Normal Users, Restaurant Owners, and Administrators.

### 2. Authentication & Session Control
* **JWT token authentication**: Login endpoint issuing signed JSON Web Tokens (`access_token`).
* **Database session tracking**: Tokens are registered in the database upon login.
* **Complete logout**: The logout endpoint removes the active token from the database, instantly invalidating sessions.
* **Protected routes**: Route-level dependency checks verifying token validity and user roles.

### 3. Restaurant & Menu Management
* **Admin-only creation**: Only system administrators can create restaurants and assign owners.
* **Multi-owner support**: Associates restaurants with owners through explicit ownership permissions.
* **Menu CRUD**: Restaurant owners can add dishes, update prices and inventory quantities, and remove items.
* **Owner profile enrichment**: User retrieval endpoints return affiliated restaurants if the account is an owner.
* **Search & filters**: Menu querying filtered by category, price range, and rating.

### 4. Ordering & Analytics
* **Order placement**: Normal users can create multi-item orders strictly within a single restaurant.
* **Validation**: Validates that order total does not exceed user balance and item counts do not exceed available stock.
* **Recency sorting**: Browse restaurants ordered by most recent transaction activity.
* **Owner analytics**:
  * Item order frequencies (how many times each dish was ordered).
  * Top customer rankings by total order count.
  * Detailed order histories.
 
---

## Tech Stack & Prerequisites

* **Python 3.10+**
* **FastAPI** (Web framework)
* **Tortoise ORM** (Async ORM)
* **Aerich** (Database migrations)
* **PostgreSQL** or **SQLite** (Database)
* **Pytest & HTTPX** (Testing suite)

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
