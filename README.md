<!-- PROJECT LOGO AND TITLE -->
<p align="center">
  <a href="https://github.com/Janse-1/clinical-emr">
    <img src="images/logo.png" alt="Logo" width="100" height="100">
  </a>

  <h2 align="center">Clinical Electronic Medical Record System</h2>
  <p align="center">
    A secure Electronic Medical Record (EMR) system for managing patient clinical files and generating structured medical summaries.
    <br />
    <a href="https://github.com/Janse-1/clinical-emr"><strong>Check the Documentation »</strong></a>
    <br />
    <a href="#">View a Live Demo</a>
    •
    <a href="https://github.com/Janse-1/clinical-emr/issues">Report a Bug</a>
    •
    <a href="https://github.com/Janse-1/clinical-emr/issues">Request a Feature</a>
  </p>
</p>

---

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About This Project</a></li>
    <li><a href="#start">Getting Started</a></li>
    <li><a href="#use">Usage Guidelines</a></li>
    <li><a href="#roadmap-section">Project Roadmap</a></li>
    <li><a href="#license-section">License Information</a></li>
    <li><a href="#thanks">Acknowledgments</a></li>
  </ol>
</details>

---

## <a name="about"></a>About This Project

![Project Screenshot][product-screenshot]

This project is a lightweight Electronic Medical Record (EMR) system designed for private medical practice use. The system replaces manual handwritten patient records with a secure digital solution.


### Problem

- Manual handwritten clinical records.
- Difficulty searching and organizing patient files.
- Time-consuming summary creation.
- Lack of digital backup for sensitive medical data.

### Solution

This system provides:

- Secure login authentication for doctors.
- Patient management module.
- Clinical record management.
- Automatic medical summary generation.
- Structured PDF export for legal documentation.
- Data separation per doctor (multi-user ready).

The system is designed for local deployment and internal use only.

[🔝 Back to Top](#readme-top-anchor)

---

## <a name="start"></a>Getting Started

To get the project up and running on your local system, follow these steps:

### Prerequisites

- .NET SDK (latest version)
- SQL Server
- Visual Studio 2022 (recommended)

### Installation

Clone the repository:

```bash
git clone https://github.com/Janse-1/clinical-emr.git
```

Navigate to the project folder:

```bash
cd clinical-emr
```

Restore dependencies:

```bash
dotnet restore
```

Apply database migrations:

```bash
dotnet ef database update
```

Run the application:

```bash
dotnet run
```

The application will run locally on:

```
https://localhost:5001
```

---

## <a name="use"></a>Usage Guidelines

1. Log in using authorized doctor credentials.
2. Create and manage patients.
3. Add clinical records for each patient.
4. Automatically generate structured medical summaries.
5. Export medical records as PDF documents for printing.

Each doctor can only access their own patients and records.

---

## <a name="roadmap-section"></a>Project Roadmap

### Version 1.0 (MVP)

- Authentication system
- Patient management
- Clinical record management
- PDF export
- Local deployment

### Future Improvements

- Multi-clinic support
- Cloud deployment
- Automated backup system
- Advanced reporting and analytics
- AI-assisted medical summary generation

---


## <a name="license-section"></a>License Information

This project is proprietary software developed for a private medical practice.

Unauthorized distribution is not permitted without explicit permission.

---


## <a name="thanks"></a>Acknowledgments

- .NET Community
- Microsoft ASP.NET Documentation
- Open-source contributors and documentation resources

---