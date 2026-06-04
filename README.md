# 🏥 Hospital Appointment Booking System

A robust and scalable web application built using Python and the Django framework. This system digitalizes clinical appointment scheduling, displays medical departments, showcases available doctors in real-time, handles media file uploads, and manages dynamic booking workflows seamlessly.

## ✨ Core Features & Application Workflow

The application consists of multiple interconnected pages driven by Django's dynamic MVT (Model-View-Template) architecture, modular routing, and media configurations:

- **🏠 Home & About Pages (`/`, `/about/`):** Informative landing pages introducing the hospital's mission and medical infrastructure.
- **📅 Dynamic Appointment Booking (`/booking`):** A clean booking interface powered by Django Forms (`BookingForm`). It securely validates patient details (Name, Phone, Email) and records schedules dynamically.
- **🎟️ Instant Confirmation Screen:** Upon successful form submission, the system routes the user to a dedicated confirmation page (`confirmation.html`) to display successful token or slot details.
- **👨‍⚕️ Real-time Doctor Directory (`/doctors/`):** Fetches and displays comprehensive profiles of all medical specialists directly from the database, showcasing names, specialties, and dynamic profile images.
- **🗂️ Categorized Medical Departments (`/department`):** Segregates and lists operational hospital departments along with their detailed structural descriptions.
- **📞 Contact Portal (`/condact`):** A dedicated page allowing users to access emergency details and contact information.
- **🛡️ Secure Admin Dashboard (`/admin/`):** Utilizes Django's built-in administration portal to safely add, modify, or remove doctor profiles, slots, and clinical departments.

## 🗄️ Database & Project Architecture

The application is structured cleanly with modular routing and native relational database handling:
1. **Modular Routing (`include`):** The project-level URL configuration delegates traffic smoothly to the application-level routes (`home.urls`) for better codebase scaling.
2. **Media Static Routing:** Dynamically handles file-system routing using `settings.MEDIA_URL` to securely store and render doctor profile pictures uploaded from the admin panel.
3. **Data Models:**
   - `Department`: Stores information about the clinical wings (Name, Description).
   - `Doctor`: Links medical staff profiles to specific departments via a `ForeignKey` and binds them to Django's built-in `User` authentication.
   - `Booking`: Logs patient registration inputs, maps them against a relational `Doctor` model instance, and locks chosen dates along with pre-configured time slots.

## 🛠️ Tech Stack Used

- **Backend Framework:** Python 3.x, Django Web Framework
- **Form Handling:** Django ModelForms
- **Database:** SQLite3 (Default relational Django DB)
- **Frontend Technologies:** HTML5, CSS3, JavaScript (Bootstrap Framework)

## 🚀 How to Run the Project Locally

Follow these sequential steps to set up and run this project on your system:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/hospital-booking-system.git](https://github.com/your-username/hospital-booking-system.git)