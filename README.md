# coding-project-template

# 🚗 Car Dealership Application

This project is part of the **IBM Full Stack Software Developer Capstone**.  
It represents a fictional national car dealership website where customers can browse branches by state, read reviews, and post their own reviews after signing up.

---

## 🧩 Project Overview

### Steps accomplished
- Forked and cloned the provided GitHub repository containing the project template.  
- Set up the predefined **Django** backend application.  
- Created static pages to fulfill initial user stories.  
- Ran the application locally in the IBM Cloud IDE environment.  
- Implemented user management using the **Django authentication system** and created a **React** frontend.  
- Developed backend services:  
  - Created a **Node.js server** using **MongoDB** to manage dealers and reviews.  
  - Dockerized the backend for portability.  
- Deployed a **Sentiment Analyzer microservice** (using IBM Watson AI) on **IBM Code Engine** to analyze customer review sentiment.  
- Added **Django models and views** for `CarMake` and `CarModel`.  
- Integrated the dealership and reviews microservices through **Django proxy views**.  
- Built **dynamic pages** using Django templates:  
  - Page displaying all dealers  
  - Page displaying reviews for a specific dealer  
  - Page allowing authenticated users to add reviews  
- Implemented **CI/CD** for automated linting and testing.  
- Deployed the entire application on **Kubernetes**.  

---

## 🧱 Solution Architecture

The solution uses multiple technologies and microservices working together:

### 1. Django Application ("Dealerships Website")
- Serves as the main user interface.
- Provides proxy microservices for the end user:

| Endpoint | Description |
|-----------|--------------|
| `/get_cars/` | Retrieve the list of cars |
| `/get_dealers/` | Retrieve all dealers |
| `/get_dealers/:state` | Retrieve dealers filtered by state |
| `/dealer/:id` | Retrieve dealer details by ID |
| `/review/dealer/:id` | Retrieve reviews for a specific dealer |
| `/add_review/` | Submit a new review |

**Database:** SQLite (stores `CarMake` and `CarModel` data)

---

### 2. Dealerships and Reviews Service (Node.js + MongoDB)
This microservice runs in a **Docker container** and manages dealerships and customer reviews.

| Endpoint | Description |
|-----------|--------------|
| `/fetchDealers` | Fetch all dealers |
| `/fetchDealer/:id` | Fetch a dealer by ID |
| `/fetchReviews` | Fetch all reviews |
| `/fetchReview/dealer/:id` | Fetch reviews for a dealer by ID |
| `/insertReview` | Insert a new review |

The Django app communicates with this service through HTTP requests (via proxy functions).

---

### 3. Sentiment Analyzer Service (IBM Code Engine)
A microservice leveraging **IBM Watson Natural Language Understanding** to analyze the sentiment of reviews.

| Endpoint | Description |
|-----------|--------------|
| `/analyze/:text` | Returns the sentiment (`positive`, `negative`, or `neutral`) for the given text |

---

### 4. System Integration

1. **User** interacts with the Django-based frontend via the web browser.  
2. Django proxies API calls to:
   - The **Node.js Mongo service** for dealer and review data.  
   - The **Watson Sentiment Analyzer** for sentiment classification.  
3. Django renders dynamic pages combining data from all sources.  

---

## ⚙️ Tech Stack Summary

| Layer | Technology |
|-------|-------------|
| Frontend | React.js, HTML, CSS |
| Backend | Django (Python) |
| Microservices | Node.js + Express |
| Database | MongoDB & SQLite |
| Deployment | Docker, Kubernetes, IBM Code Engine |
| AI Integration | IBM Watson NLU |
| CI/CD | GitHub Actions / IBM Cloud toolchain |

---

## 🧠 Key Features

- User authentication (login/register/logout)
- Dealer listings with filtering by state
- Dealer detail pages with reviews
- Authenticated users can post new reviews
- Sentiment analysis integrated with reviews
- Full microservice-based architecture

---
