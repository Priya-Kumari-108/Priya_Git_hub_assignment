# GitHub & Git Hands-On Project: Flask To-Do App

This repository contains a **Flask-based To-Do web application**, created as part of a hands-on assignment to practice Git and GitHub workflows. It demonstrates working with **branches**, **SSH**, **merge conflicts**, **Git reset**, **rebase**, and **feature integration**, along with connecting to a **MongoDB** backend.

Project Overview

The application includes:

- A `/api` route serving data from a JSON file
- A frontend To-Do form
- A backend `/submittodoitem` POST route that stores data in MongoDB
- Git operations like branching, merging, rebasing, and resolving conflicts

---

Branch Structure

| Branch        | Purpose                                                  |
|---------------|----------------------------------------------------------|
| `main`        | Final, stable version of the project                     |
| `Priya-Kumari-108` | Initial branch for uploading complete Flask project |
| `Priya-Kumari-108_new` | JSON data update branch                        |
| `master_1`    | Frontend development (To-Do form)                        |
| `master_2`    | Backend route `/submittodoitem` with MongoDB            |


Completed Workflow

1.  Repository & SSH Setup
- Created GitHub repository
- Cloned using **SSH**
- Generated and configured SSH keys
- Created branch `Priya-Kumari-108` and uploaded the entire Flask app
- Merged to `main`

 2.  JSON API Update
- Created `Priya-Kumari-108_new` branch
- Updated JSON file used in `/api` route
- Merged changes into `main`, resolving merge conflicts by **accepting changes from the new branch**

3. To-Do Feature Development

  Frontend (Branch: `master_1`)
- Created a To-Do page with a form for:
  - Item Name
  - Item Description

 Backend (Branch: `master_2`)
- Created a Flask POST route `/submittodoitem` to:
  - Accept `itemName` and `itemDescription`
  - Store them in **MongoDB**

- Merged both branches into `main`

 Form Enhancement: master_1
- Enhanced the To-Do form with these fields:
  1. ✅ **Item ID** (Commit 1)
  2. ✅ **Item UUID** (Commit 2)
  3. ✅ **Item Hash** (Commit 3)


Git History Cleanup

 Git Reset & Recommit
- Performed soft reset to rollback to commit containing **only Item ID**:
  ```bash
  git reset --soft <commit_hash>
  git commit -m "Recommit only Item ID"
