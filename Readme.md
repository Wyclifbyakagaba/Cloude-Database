# FUMU Sports Cloud Athlete Manager

## Project Overview

The **FUMU Sports Cloud Athlete Manager** is a Python application that manages athlete information using **Google Firebase Cloud Firestore**.

The application demonstrates how a cloud database can be used to store, retrieve, search, update, and delete athlete records.

1. Module

**Cloud Databases**

2. Project

**FUMU Sports Cloud Athlete Manager**

3.Technologies

* Python
* Google Firebase
* Cloud Firestore
* Firebase Admin SDK
* Git and GitHub
* Zoom video recorder 
* YOutube video social media uploader

4. Features

The application provides the following CRUD operations:

1. **Add Athlete** – Creates a new athlete record in Firestore.
2. **View Athletes** – Displays all athletes stored in the database.
3. **Search Athletes** – Searches athlete records by name, sport, club, or email.
4. **Update Athlete** – Changes information belonging to an existing athlete.
5. **Delete Athlete** – Removes an athlete from the database.

5. Database

The application uses **Google Cloud Firestore**.

The main Firestore collection is:

```text
athletes
```

Each athlete document can contain:

```text
name
age
gender
sport
club
phone
email
```

6. Project Structure

```text
FUMU-Cloud-Athlete-Manager/
│
├── README.md
├── main.py
├── firestore_service.py
├── requirements.txt
├── .gitignore
└── serviceAccountKey.json
```

> `serviceAccountKey.json` contains private Firebase credentials. It must never be uploaded to GitHub.

7. Requirements

Install Python 3.10 or newer.

Install the required Firebase package:

```bash
pip install -r requirements.txt
```

8. Firebase Setup

### 1. Create a Firebase project

Go to the Firebase Console and create a project.

### 2. Enable Cloud Firestore

Open the Firebase project and create a Cloud Firestore database,

### 3. Create a service account

Open:

```text
Project Settings
→ Service Accounts
→ Generate new private key
```

Download the JSON credentials.

Rename the downloaded file:

```text
serviceAccountKey.json
```

Place it in the same folder as `main.py`.

9. Protect the credentials

The credentials are excluded using `.gitignore`.

Never commit this file:

```text
serviceAccountKey.json
```

10. Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

11.Running the Application

Start the program with:

```bash
python main.py
```

The application displays a menu similar to:

```text
========================================
 FUMU SPORTS CLOUD ATHLETE MANAGER
========================================

1. Add Athlete
2. View Athletes
3. Search Athletes
4. Update Athlete
5. Delete Athlete
0. Exit
```

12.CRUD Operations

### Create

The Add Athlete option creates a new document in the `athletes` Firestore collection.

### Read

The View Athletes option retrieves athlete documents from Firestore.

### Search

The Search option allows the user to find athletes using information such as:

* Name
* Sport
* Club
* Email

### Update

The Update option changes selected information for an existing athlete.

### Delete

The Delete option permanently removes an athlete document from Firestore.

## Example Athlete

```text
Name: John Doe
Age: 21
Gender: Male
Sport: Football
Club: FUMU FC
Phone: 0700000000
Email: john@example.com
```

## Testing Checklist

Before submitting the project, test:

* [ ] Firebase connection works.
* [ ] Athlete can be added.
* [ ] Athletes can be viewed.
* [ ] Athletes can be searched.
* [ ] Athlete information can be updated.
* [ ] Athlete can be deleted.
* [ ] Invalid input does not crash the application.
* [ ] Firebase credentials are not committed to GitHub.


14.Video link:
:https://youtube.com/shorts/mIlbmr_PBvk?si=boDZ0ahRSkepPNQG
zoom :2026-09-15 19.23.51 Mr sooda Wyclif's Zoom Meeting
<audio controls src="audio1913869618.m4a" title="Title"></audio> <video controls src="video1913869618.mp4" title="Title"></video>

15.Security

The Firebase service account key is private.

The following file must remain local:

```text
serviceAccountKey.json
```

It is included in `.gitignore` so Git does not upload it.

20.Learning Outcome

This project demonstrates practical use of a cloud database by connecting a Python application to Firebase Cloud Firestore and implementing Create, Read, Update, and Delete operations.

## Author

**Byakagaba Wycliff**

FUMU Sports Cloud Athlete Manager
