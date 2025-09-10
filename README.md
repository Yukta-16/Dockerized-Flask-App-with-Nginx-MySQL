# 🚀 Dockerized Flask App with Nginx & MySQL

This project demonstrates a **multi-container Docker application** using:

* **Flask** (Python web framework)
* **MySQL** (Relational Database)
* **Nginx** (Reverse Proxy)
* **Docker & Docker Compose** (Container orchestration)

It showcases how DevOps engineers can containerize applications, manage multi-service networking, and configure reverse proxies for scalable deployments.

---

## 📌 Features

* 🐳 **Containerized Flask App** with custom Dockerfile
* 🗄️ **MySQL Database** with persistent storage (volumes)
* 🔄 **Nginx Reverse Proxy** to route traffic to Flask
* ⚡ **Docker Compose** for multi-container orchestration
* 🌐 API endpoint to fetch users from database

---

## 📂 Project Structure

```
docker-flask-app/
│── app/
│   ├── app.py               # Flask Application
│   ├── requirements.txt     # Python Dependencies
│── nginx/
│   ├── default.conf         # Nginx Configuration
│── docker-compose.yml       # Multi-container setup
│── Dockerfile               # Flask App Dockerfile
│── README.md                # Documentation
```

---

## 🛠️ Tech Stack

* **Python 3.9 + Flask**
* **MySQL 8.0**
* **Nginx (Alpine)**
* **Docker & Docker Compose**

---

## ⚙️ Setup & Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Yukta-16/Dockerized-Flask-App-with-Nginx-MySQL.git
cd docker-flask-app
```

### 2️⃣ Build & Start Containers

```bash
docker-compose up --build -d
```

### 3️⃣ Verify Containers

```bash
docker ps
```

You should see `flask_app`, `mysql_db`, and `nginx_proxy` running.

---

## 🌐 Access the App

* **Homepage:** [http://localhost:8080](http://localhost:8080)
  → Returns a welcome message

* **Users Endpoint:** [http://localhost:8080/users](http://localhost:8080/users)
  → Fetches users stored in MySQL

---

## 🗄️ Database Setup

1. Enter MySQL container:

   ```bash
   docker exec -it mysql_db mysql -u root -p
   ```

   (Password is `root`)

2. Create table & insert sample data:

   ```sql
   USE flaskdb;

   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(50)
   );

   INSERT INTO users (name) VALUES ('Yukta'), ('DevOps'), ('Engineer');
   ```

3. Refresh `/users` endpoint to see data.

---

## 📊 Architecture

```
          ┌───────────┐
          │   Nginx   │  (Reverse Proxy :80 → Flask:5000)
          └─────┬─────┘
                │
         ┌──────▼──────┐
         │   Flask     │  (Web App :5000)
         └──────┬──────┘
                │
         ┌──────▼──────┐
         │   MySQL     │  (Database with Volumes)
         └─────────────┘
```

---

## 📸 Screenshots (Add after running)

1. Homepage response
2. `/users` API response
3. Docker containers running

---

## 💡 DevOps Concepts Highlighted

* **Dockerfile** → Containerization of Python app
* **docker-compose.yml** → Multi-service orchestration
* **Networking** → Flask ↔ MySQL ↔ Nginx communication
* **Environment Variables** → Secure DB configs
* **Volumes** → Persistent MySQL data
* **Reverse Proxy** → Nginx load balancing request routing

---

## 🚀 Future Improvements

* Add CI/CD pipeline with **GitHub Actions**
* Integrate monitoring with **Prometheus & Grafana**
* Deploy on **Kubernetes (K8s)** for scalability
* Use **Secrets Management** instead of plain env vars

---

## 👩‍💻 Author

**Yukta Thakur**

* 🌐 [LinkedIn](https://linkedin.com/in/your-profile)
* 💻 DevOps Enthusiast | Cloud Learner | Problem Solver

---

## ⭐ Contribute

If you like this project, give it a ⭐ and fork it! Contributions are welcome.

