# Secure Online Voting System

## Table of Contents

- [Secure Online Voting System](#secure-online-voting-system)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
    - [User Authentication](#user-authentication)
    - [Role-Based Access Control](#role-based-access-control)
    - [Voting Mechanism](#voting-mechanism)
    - [Election Management](#election-management)
    - [Vote Encryption](#vote-encryption)
    - [Results Calculation](#results-calculation)
    - [Audit Log](#audit-log)
  - [Tech Stack](#tech-stack)
  - [Installation and Setup](#installation-and-setup)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Navigate to the Project Directory](#navigate-to-the-project-directory)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Configure Environment Variables](#configure-environment-variables)
  - [Initialize the Database](#initialize-the-database)
  - [Run the Application](#run-the-application)
  - [Access the Application](#access-the-application)
  - [Directory Structure](#directory-structure)
  - [Application Architecture](#application-architecture)
  - [Challenges and Learning Opportunities](#challenges-and-learning-opportunities)

## Introduction

The **Secure Online Voting System** is a web application that allows users to participate in elections or polls securely and efficiently. The system ensures that each user can vote only once per election and that all votes are securely recorded and stored.

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

- **CRUD Operations**: Admins can create, update, or delete elections.
- **Timed Elections**: Elections have a start and end time, after which voting is disabled.

### Vote Encryption

- **Encrypted Votes**: Votes are encrypted to ensure they are secure and tamper-proof.
- **Secure Communication**: Uses JWT for secure communication between the client and server.

### Results Calculation

- **Automatic Tallying**: After an election ends, the system calculates and displays results.
- **Access Control**: Results can be displayed publicly or restricted to certain roles.

### Audit Log

- **Activity Logging**: Maintains an audit log of all activities such as user logins, votes cast, and election management for transparency and security.

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

1. **Clone the Repository**

```bash
   git clone https://github.com/yourusername/secure_online_voting_system.git

```

---

## Navigate to the Project Directory

```bash
cd secure_online_voting_system
```

## Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Rename `.env.example` to `.env` and update the configuration settings such as database credentials and secret keys.

## Initialize the Database

Run the migrations to set up the database schema.

```bash
flask db init
flask db migrate
flask db upgrade
```

## Run the Application

```bash
flask run
```

## Access the Application

Navigate to `http://localhost:5000` in your web browser or use a tool like Postman to interact with the API endpoints.

## Directory Structure

```plaintext
secure_online_voting_system/
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
│   ├── routes/
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
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_election.py
│   ├── test_candidate.py
│   └── test_vote.py
├── .env
├── .gitignore
├── requirements.txt
└── run.py
```

## Application Architecture

```plaintext
+--------------------------------------------+
|                   Flask App                |
|                                            |
| +------------+     +------------------+    |
| | Blueprints |     |     Services     |    |
| +------+-----+     +---------+--------+    |
|        |                    |             |
|        |                    |             |
|        v                    v             |
|  +-----------+     +-------------------+  |
|  |  Routes   |     |     Repository    |  |
|  +-----+-----+     +---------+---------+  |
|        |                    |             |
|        v                    v             |
|  +------------+      +------------+       |
|  |  Schemas   |      |    Models  |       |
|  +------------+      +------+-----+       |
|                              |            |
|                              v            |
|                         +---------+       |
|                         |  Database |     |
|                         +---------+       |
+--------------------------------------------+
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
