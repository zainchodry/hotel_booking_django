
# 🏨 Hotel Booking System (Django)

A complete hotel booking web application built using **Django**, featuring authentication, hotel listings, room details, room booking, payments, and user dashboard.

---

## 🚀 Features

### 🔐 User Authentication
- User Registration  
- Login / Logout  
- Profile Page  
- Access control using Django Auth  

---

### 🏨 Hotels & Rooms
- List of all hotels  
- Each hotel shows all related rooms  
- Room details page with image, price, availability  
- Booking option only when the room is available  

---

### 🛏️ Room Booking
- Users can book rooms  
- Booking form  
- Automatically marks room as unavailable  
- Prevents booking if already booked  

---

### 💳 Payment System
- Payment page  
- Payment success page  
- Mock payment handling  
- Uses Booking ID  

---

### 📊 Dashboard
- Shows user-related details  
- Accessible after login  

---

## 📁 Project Structure

```
hotel_booking_django/
│
├── accounts/
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── dashboard/
│   ├── views.py
│   └── urls.py
│
├── hotel/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── payments/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
└── templates/
    ├── base.html
    ├── hotel_list.html
    ├── room_detail.html
    ├── book_room.html
    ├── room_unavailable.html
    ├── login.html
    ├── register.html
    └── dashboard.html
```

---

## 🔧 Setup & Installation

### 1️⃣ Clone the project
```
git clone https://github.com/zainchodry/hotel_booking_django.git
cd hotel_booking_django
```

### 2️⃣ Create Virtual Environment
```
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scriptsctivate      # Windows
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Server
```
python manage.py runserver
```

Now open:  
➡ **http://127.0.0.1:8000/**  

---

## 🧪 Testing

Use admin panel:

```
python manage.py createsuperuser
```

Login at:  
➡ http://127.0.0.1:8000/admin/

---

## 📌 Important URLs

| Feature | URL |
|--------|-----|
| Dashboard | `/` |
| Hotels List | `/hotel/` |
| Room Detail | `/hotel/room/<id>/` |
| Book Room | `/hotel/room/<id>/book/` |
| Payment Page | `/payments/pay/<booking_id>/` |
| Login | `/accounts/login/` |
| Register | `/register` |

---

## 📸 Screens Included
- Hotel List  
- Room Details  
- Booking Form  
- Room Unavailable  
- Login / Register  
- Dashboard  
- Base Navbar Template  

---

## 🧑‍💻 Technologies Used
- Django  
- Python  
- Bootstrap 5  
- SQLite3  
- HTML / CSS  

---

## 📄 License
This project is open source and free to use.

---

## 🌟 Author
**Developed by:** *enigmatix*  