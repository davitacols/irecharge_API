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
    ```

2. **Change to the project directory:**

    ```bash
    cd irecharge-api
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the MySQL database:**

    - Create a database named `irecharge`.
    - Update the `DATABASE_URL` in `main.py` with your MySQL credentials.

### Run the Application

Start the FastAPI application using [Uvicorn](https://www.uvicorn.org/):

```bash
uvicorn main:app --reload
