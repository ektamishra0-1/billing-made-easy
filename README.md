# 🧾 Billing Made Easy

> A lightweight web application that automates Daily Sales Report preprocessing for pathology laboratories and diagnostic organizations.

Billing Made Easy was developed to eliminate repetitive manual Excel editing performed during daily billing workflows. Instead of manually cleaning reports before further processing, users simply upload their Daily Sales Report, and the application automatically processes the data and returns a clean, standardized Excel file ready for use.

Originally built for a real pathology laboratory, the application is actively used in a production workflow by real users and continues to evolve based on practical business requirements.

---

# 🌍 Real-World Usage

Unlike many portfolio or academic projects, **Billing Made Easy is built around an actual business workflow.**

The application is currently used within a pathology laboratory to automate the preprocessing of Daily Sales Report Excel files before they are used for billing and reporting.

By replacing repetitive manual Excel editing with a single upload, the application helps reduce:

- Manual work
- Human error
- Processing time
- Repetitive data-cleaning tasks

The project continues to improve based on real user feedback and operational needs.

---

# ✨ Features

- 📤 Upload Daily Sales Report Excel files
- ⚡ Automatic Excel preprocessing
- 👤 Cleans patient names
- 🗑 Removes unnecessary columns
- 📥 Downloads the cleaned Excel file instantly
- 🌐 Simple web interface designed for non-technical users
- 📱 Responsive design
- ☁️ Deployable on Vercel
- 🚀 Easily extendable with additional processing pipelines

---

# ⚙️ Current Processing Pipeline

When an Excel file is uploaded, the application automatically:

1. Reads the Excel file using **Pandas**
2. Skips unnecessary header rows
3. Removes unwanted columns
   - Mobile
   - Email
4. Cleans the **PName** column by
   - Keeping only the patient's name
   - Removing everything after `/`
   - Trimming extra spaces
5. Generates a new cleaned Excel workbook
6. Automatically downloads the processed file

---

# 🏥 Intended Users

Billing Made Easy is designed for organizations that regularly process Excel reports, including:

- Pathology Laboratories
- Diagnostic Centres
- Medical Billing Teams
- Hospital Administration
- Healthcare Organizations
- Small & Medium Businesses with repetitive Excel workflows

No technical knowledge is required to use the application.

---

# 🛠 Tech Stack

## Backend

- FastAPI
- Pandas
- OpenPyXL

## Frontend

- HTML5
- CSS3
- JavaScript

## Deployment

- Vercel

---

# 📂 Project Structure

```
billing-made-easy/
│
├── api/
│   └── index.py          # FastAPI backend
│
├── templates/
│   └── index.html        # Frontend interface
│
├── requirements.txt
├── vercel.json
└── README.md
```

---

# 🚀 Running Locally

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/billing-made-easy.git
```

Navigate to the project

```bash
cd billing-made-easy
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn api.index:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

# 🌐 Live Demo

The application is publicly accessible at:

billing-made-easy-qcv4t3zkc-chaosify.vercel.app

---

# 📊 Workflow

```
          Upload Excel
                │
                ▼
      Read using Pandas
                │
                ▼
        Clean & Process Data
                │
                ▼
     Generate New Excel File
                │
                ▼
      Download Processed File
```

---

# 🎯 Why This Project?

Many pathology laboratories generate Daily Sales Reports that require manual cleaning before they can be used for billing, reporting, or further processing.

While each individual edit is simple, performing the same repetitive tasks every day is time-consuming and increases the chance of human error.

Billing Made Easy automates this repetitive work, allowing staff to process reports in seconds while maintaining consistent formatting and improving operational efficiency.

---

# 🔮 Future Roadmap

This project is intended to grow into a more comprehensive billing workflow platform.

Planned features include:

- Multiple report-processing pipelines
- Drag-and-drop uploads
- Batch processing
- Report validation
- Processing history
- User authentication
- Analytics dashboard
- Invoice generation
- Laboratory workflow automation
- AI-assisted billing insights

---

# 👨‍💻 About

Billing Made Easy is a real-world software project developed to improve operational efficiency within a pathology laboratory.

Rather than being built solely as a learning exercise, the application addresses an actual business need and is actively used by people in a production environment. Development is driven by practical feedback, with a focus on reducing manual effort, improving consistency, and making everyday billing workflows faster and more reliable.

---

## ⭐ If you found this project interesting, consider giving it a star!
