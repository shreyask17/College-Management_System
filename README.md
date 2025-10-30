# 🎓 College Management System

*A web-based college management portal built with Django & Bootstrap.*

---

## 📌 Project Overview  
The **College Management System** is a Django-based web application designed to streamline and manage various college operations efficiently.  
It provides role-based dashboards for **students**, **teachers**, and **administrators**, enabling smooth interaction and data management through an intuitive interface.

---

## ⚙️ Features  
* 🏠 **Home Page** – Clean and modern landing page with navigation  
* 👩‍🎓 **Student Dashboard** – View personal details and assigned courses  
* 👨‍🏫 **Teacher Dashboard** – Manage and view allocated courses  
* 🛠️ **Admin Panel** – Add, update, and manage students, teachers, and courses  
* 💾 **MySQL Integration** – All data is stored securely using MySQL database  
* 🎨 **Bootstrap Styling** – Responsive and modern UI using Bootstrap 5  

---

## 🧠 Tech Stack  

| Category | Technology |
|-----------|-------------|
| Backend | Django (Python) |
| Frontend | HTML, CSS, Bootstrap |
| Database | MySQL |
| Version Control | Git & GitHub |

---

## 🚀 Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/College-Management_System.git
cd College-Management_System
```
2️⃣ Create Virtual Environment
```bash
python -m venv v_env
v_env\Scripts\activate   # On Windows
source v_env/bin/activate  # On macOS/Linux
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Configure Database
```bash
# In settings.py, update your MySQL credentials

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'college_management',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
5️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
6️⃣ Run the Server
```bash
python manage.py runserver
```
7️⃣ Access Project
```bash
🏠 Home Page → http://127.0.0.1:8000/
🎓 Student Dashboard → http://127.0.0.1:8000/student/1/
👨‍🏫 Teacher Dashboard → http://127.0.0.1:8000/teacher/1/
⚙️ Admin Panel → http://127.0.0.1:8000/admin/
```
8️⃣ Create Admin User
```bash
python manage.py createsuperuser
# After creation, login using those credentials at:
# http://127.0.0.1:8000/admin/
```
🗂️ Project Structure
bash
```bash
College-Management_System/
│
├── college_app/               # Main Django app (models, views, urls)
├── templates/                 # HTML templates (base, home, dashboards)
├── static/                    # CSS, JS, images (if added)
├── manage.py                  # Django management script
├── requirements.txt           # All dependencies
└── README.md                  # Project documentation
```
💡 Note:
Make sure your MySQL Workbench (or MySQL Server) is running in the background before starting the Django app.