# Secure Voting System

## Table of Contents

- [Secure Voting System](#secure-voting-system)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
    - [User Authentication](#user-authentication)
    - [Role-Based Access Control](#role-based-access-control)
    - [Voting Mechanism](#voting-mechanism)
    - [Election Management](#election-management)
    - [Vote Encryption](#vote-encryption)
    - [Results Calculation](#results-calculation)
  - [Tech Stack](#tech-stack)
  - [Installation and Setup](#installation-and-setup)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
      - [1. Clone the Repository](#1-clone-the-repository)
      - [2. Navigate to the Project Directory](#2-navigate-to-the-project-directory)
      - [3. Create a Virtual Environment](#3-create-a-virtual-environment)
      - [4. Install Dependencies](#4-install-dependencies)
      - [5. Initialize the Database](#5-initialize-the-database)
      - [6. Run the Application](#6-run-the-application)
      - [7. Access the Application](#7-access-the-application)
  - [API Documentation](#api-documentation)
  - [Directory Structure](#directory-structure)
  - [Application Architecture](#application-architecture)
  - [Challenges and Learning Opportunities](#challenges-and-learning-opportunities)

## Introduction

The **Secure Voting System** is a web application that allows users to participate in elections or polls securely and efficiently. The system ensures that each user can vote only once per election and that all votes are securely recorded and stored.

## Features

### User Authentication

- **Registration and Login**: Users can register and log in using JSON Web Tokens (JWT) for authentication.
- **Secure Passwords**: Passwords are hashed to enhance security.

### Role-Based Access Control

- **User Roles**: Different roles such as **Admin** and **Voter** with specific permissions.
- **Admin Capabilities**: Admins can create and manage elections, view results, and manage users.

### Voting Mechanism

- **Active Elections**: Users can view active elections and cast their votes.
- **Secure Voting**: Votes are securely stored in the MySQL database.
- **Prevent Double Voting**: The system ensures that each user can vote only once per election.

### Election Management

![alt text](https://github.com/a6m1n0/Alx_Portfolio_Project/blob/main/Screenshot%20from%202024-09-27%2011-18-57.png?raw=true)

https://github.com

- **CRUD Operations**: Admins can create, update, or delete elections.
- **Timed Elections**: Elections have a start and end time, after which voting is disabled.

### Vote Encryption

- **Encrypted Votes**: Votes are encrypted to ensure they are secure and tamper-proof.
- **Secure Communication**: Uses JWT for secure communication between the client and server.

### Results Calculation

- **Automatic Tallying**: After an election ends, the system calculates and displays results.
- **Access Control**: Results can be displayed publicly or restricted to certain roles.

## Tech Stack

- **Backend Framework**: Python Flask for server-side logic.
- **Database**: MySQL for storing user data, election details, and votes.
- **Authentication**: JWT Extended for handling secure user authentication and authorization.

## Installation and Setup

### Prerequisites

- Python 3.x
- MySQL
- Virtual Environment Tool (optional but recommended)

### Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/a6m1n0/Alx_Portfolio_Project.git
```

#### 2. Navigate to the Project Directory

```bash
cd Alx_Portfolio_Project
```

#### 3. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### 4. Install Dependencies

```bash
pip3 install -r requirements.txt
```

#### 5. Initialize the Database

Run the migrations to set up the database schema.

```bash
flask db init
flask db migrate
flask db upgrade
```

#### 6. Run the Application

```bash
flask run
```

#### 7. Access the Application

Navigate to `http://localhost:5000` in your web browser or use a tool like Postman to interact with the API endpoints.

## API Documentation

For detailed information on the API endpoints, request and response formats, refer to the [API Documentation](https://documenter.getpostman.com/view/38335007/2sAXqpA4eG).

This documentation provides comprehensive details on how to interact with the Secure Voting System's RESTful API, including:

- **Authentication Endpoints**: Registering new users, logging in, and token refresh.
- **Election Management**: Creating, updating, and deleting elections (Admin only).
- **Candidate Management**: Managing candidates for each election.
- **Voting Endpoints**: Casting votes and retrieving voting status.
- **Results Retrieval**: Accessing election results after voting has concluded.
- **Audit Logs**: Monitoring system activities for security and transparency.

## Directory Structure

```plaintext
Alx_Portfolio_Project/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── election.py
│   │   ├── candidate.py
│   │   ├── vote.py
│   │   └── audit_log.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── election.py
│   │   ├── candidate.py
│   │   └── vote.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── election_service.py
│   │   ├── candidate_service.py
│   │   └── vote_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── security.py
│   │   └── encryption.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   ├── election_schema.py
│   │   ├── candidate_schema.py
│   │   └── vote_schema.py
│   ├── extensions.py
│   ├── blueprints.py
│   └── app.py
├── migrations/
│   ├── versions/
│   └── alembic.ini
├── requirements.txt
└── run.py
```

## Application Architecture

```plaintext
+-------------------------------------------+
|                Flask App                  |
|                                           |
| +------------+     +------------------+   |
| | Blueprints |     |     Services     |   |
| +------+-----+     +---------+--------+   |
|        |                    |             |
|        |                    |             |
|        v                    v             |
|  +-----------+     +-------------------+  |
|  |    API    |     |     Repository    |  |
|  +-----+-----+     +---------+---------+  |
|        |                    |             |
|        v                    v             |
|  +------------+      +------------+       |
|  |  Schemas   |      |    Models  |       |
|  +------------+      +------+-----+       |
|                              |            |
|                              v            |
|                         +----------+      |
|                         | Database |      |
|                         +----------+      |
+-------------------------------------------+
```

- **Blueprints**: Modularize the application routes.
- **Services**: Contain business logic, interacting with the database through the repository pattern.
- **Repository**: Manages database interactions, keeping the data access logic separate.
- **Models**: Represent the database tables and structure.
- **Schemas**: Manage data validation and serialization.

## Challenges and Learning Opportunities

- **Secure Authentication and Authorization**: Implementing JWT-based authentication and role-based access control.
- **Data Security**: Handling sensitive data securely by encrypting votes and hashing passwords.
- **Data Integrity**: Ensuring data is not tampered with and preventing unauthorized access.
- **RESTful API Development**: Learning to create a RESTful API using Flask.
- **Audit Logging**: Implementing comprehensive logging for transparency and security.
- **Database Management**: Working with MySQL databases and managing data effectively.
