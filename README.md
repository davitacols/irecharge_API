# iRecharge API Documentation

## Overview

The iRecharge API is designed to manage articles related to different providers, currencies, and prices. It provides CRUD operations (Create, Read, Update, Delete) for articles stored in a MySQL database.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Run the Application](#run-the-application)
- [API Endpoints](#api-endpoints)
  - [List Articles](#list-articles)
  - [Get Article by ID](#get-article-by-id)
  - [Create Article](#create-article)
  - [Update Article](#update-article)
  - [Delete Article](#delete-article)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) (>=3.7)
- [pip](https://pip.pypa.io/en/stable/)
- [MySQL](https://www.mysql.com/) (>=5.7)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/davitacols/irecharge_api.git
    postman https://www.postman.com/material-pilot-19389684/workspace/irecharge/collection/32869036-a5585faa-3d1a-45e9-ad61-e1fac2ef8886?action=share&creator=32869036
    ```

2. **Change to the project directory:**

    ```bash
    cd irecharge-api
    ```


3. **Set up the MySQL database:**

    - Create a database named `irecharge`.
    - Update the `DATABASE_URL` in `main.py` with your MySQL credentials.



## List Articles
**Endpoint:** `GET /articles/`

**Description:** Retrieve a list of all articles.

**Response:**
```json
[
    {
        "article_no": 101,
        "currency": "US Dollar",
        "provider_no": "0001",
        "provider": "Flutterwave",
        "price": 1000
    },
    // ... other articles
]




# API Endpoints

## Get Article by ID
- **Endpoint:** `GET /articles/{article_no}`

- **Description:** Retrieve details of a specific article by its article_no.

- **Response:**


    ```json
    {
        "article_no": 101,
        "currency": "US Dollar",
        "provider_no": "0001",
        "provider": "Flutterwave",
        "price": 1000
    }
    ```

## Create Article

- **Endpoint:** `POST /articles/`

- **Description:** Create a new article.

- **Request:**

    ```json
    {
        "article_no": 104,
        "currency": "EU Euro",
        "provider_no": "0009",
        "provider": "Stripe",
        "price": 1500
    }
    ```
- **Response:**

    ```json
    {
        "article_no": 104,
        "currency": "EU Euro",
        "provider_no": "0009",
        "provider": "Stripe",
        "price": 1500
    }
    ```

## Update Article
- **Endpoint:** `PUT /articles/{article_no}`
- **Description:** Update details of a specific article by its article_no.
- **Request:**
    ```json
    {
        "article_no": 104,
        "currency": "EU Euro",
        "provider_no": "0009",
        "provider": "Stripe",
        "price": 2000
    }
    ```
- **Response:**
    ```json
    {
        "article_no": 104,
        "currency": "EU Euro",
        "provider_no": "0009",
        "provider": "Stripe",
        "price": 2000
    }
    ```

## Delete Article
- **Endpoint:** `DELETE /articles/{article_no}`
- **Description:** Delete a specific article by its article_no.
- **Response:**
    ```json
    {
        "article_no": 104,
        "currency": "EU Euro",
        "provider_no": "0009",
        "provider": "Stripe",
        "price": 2000
    }
    ```

## Testing
To run tests, use pytest:
```bash
pytest tests/



# Contributing
Contributions are welcome! Please check the [Contribution Guidelines](CONTRIBUTING.md) for more details.

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
