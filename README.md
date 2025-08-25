# 🩸 Blood Bank Management System

## 📖 Introduction
This project is a **Blood Bank Management System** designed to facilitate blood donation and request processes. It allows users to donate blood, make blood requests, and track their donation and request history. The system offers features for both donors and patients, with an admin panel to manage and approve donation requests.

---

## 🎯 Goals
- Enable **donors** to register, donate blood, and view their donation history.
- Allow **patients** to make blood requests specifying blood group and required units.
- Provide an **admin panel** to manage donors, requests, and donation history.
- Ensure **efficient tracking** of blood group types, units donated, and request statuses.

---

## 📂 Dataset Information
The system tracks and manages the following types of data:
- **Donor Information**: Name, Age, Blood Group, Disease History, Contact Information.
- **Donation History**: Donor ID, Unit of Blood, Donation Date, Approval Status.
- **Request History**: Patient ID, Blood Group Request, Required Units, Request Status.

---

## 🛠️ Tech Stack
- **Python/Django** – Backend framework to manage database and logic.
- **HTML/CSS (TailwindCSS)** – Frontend design and layout.
- **PostgreSQL (Supabase)** – Cloud-hosted database used to manage donor, recipient, and blood inventory records.
- **Whitenoise** – Serves static files (CSS, JS, images) efficiently in production without needing an external CDN or storage service.
- **Tailwind CSS + Custom CSS** – Used for responsive design and additional manual styling.

---

## 📊 Features
- **User Authentication**: Secure login and profile management for Donors, Patients, and Admin.
- **Blood Donation**: Donors can sign up and donate blood, with approval status.
- **Blood Request**: Patients can request blood based on their needs, blood type, and location.
- **Donation History**: Donors can view their donation records and track their activity.
- **Admin Panel**: Admins can manage users, donations, and requests, ensuring smooth operations.
- **Contact Page**: Users can reach out with queries, feedback, or support requests directly through the system.

---

## 🚀 Running the Project
1. **Fork the repository**  
   Click the **Fork** button at the top-right of this repository to create your own copy.  

2. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Blood-Bank-MS.git
   cd Blood-Bank-MS
   ```

3. **Install dependencies**
   Ensure Python is installed and then run the following command to install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Migrate database**
   Run the following to set up the database:
   ```bash
   python manage.py migrate
   ```

5. **Run the server**
   Start the Django development server with:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   Open your browser and navigate to:
   ```plaintext
   http://127.0.0.1:8000/
   ```

---

## 🔮 Possible Future Improvements
- Integrate **SMS/Email notifications** for updates on donation requests.
- Implement **real-time data tracking** for blood request statuses.
- Improve the **admin dashboard** for more detailed statistics and insights.
- Use **machine learning** to predict urgent donation requests based on trends.

---

## 📜 License
Released under the **[MIT License](LICENSE)** – free to use and modify with credit to the author.

---

## 👤 Author
**Shuba S**  
📧 Email: shuba9902@gmail.com  
💼 [LinkedIn](https://www.linkedin.com/in/shuba-s01/) | 🐙 [GitHub](https://github.com/Shuba0S/)
