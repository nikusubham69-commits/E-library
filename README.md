# Nexus | Modern E-Library Management System

Nexus is a professional-grade, modular web application designed to manage digital publications. Built with a focus on **Data Analytics** and **Scalable Architecture**, it bridges the gap between traditional library management and modern full-stack development.

## 🚀 Key Features
- **Modular Architecture**: Built using Flask Blueprints for clean separation of concerns.
- **Glassmorphism UI**: A high-end, dark-themed interface focused on modern UX/UI principles.
- **Wishlist System**: Personalized "Read Later" functionality for users.
- **Review & Rating**: Integrated star-rating system to collect user sentiment data.
- **Role-Based Access**: Specialized views for Admins (Curation Deck) and regular Users.
- **Cloud Integrated**: Configured for MongoDB Atlas and ready for deployment on Render.

## 🛠️ Tech Stack
- **Frontend**: HTML5, CSS3 (Modern Flexbox/Grid), JavaScript (ES6)
- **Backend**: Python / Flask
- **Database**: MongoDB (NoSQL)
- **Production**: Gunicorn, WSGI

## 📂 Project Structure
```text
E-library/
├── models/          # Data Access Layer (MongoDB logic)
├── routes/          # Controller Layer (Blueprints)
├── static/          # Assets (CSS, JS, Uploads)
├── templates/       # Jinja2 HTML Templates
├── app.py           # Application Entry Point
└── requirements.txt # Dependency Manifest
