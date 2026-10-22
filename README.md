
<div align="center">

# 🔗 TinyURL — Low-Level Design (LLD)

<p align="center">
  <strong>A fast, modular, and lightweight URL shortener built with Python and deployed on Vercel.</strong>
</p>

<!-- Repository Badges -->
<p align="center">
  <a href="https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1/stargazers">
    <img src="https://img.shields.io/github/stars/Spandan2106/TinyURL-SPD-LLD-0.1?style=for-the-badge&color=gold" alt="Stars Badge"/>
  </a>
  <a href="https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1/network/members">
    <img src="https://img.shields.io/github/forks/Spandan2106/TinyURL-SPD-LLD-0.1?style=for-the-badge&color=blue" alt="Forks Badge"/>
  </a>
  <a href="https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1/issues">
    <img src="https://img.shields.io/github/issues/Spandan2106/TinyURL-SPD-LLD-0.1?style=for-the-badge&color=red" alt="Issues Badge"/>
  </a>
  <a href="https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Spandan2106/TinyURL-SPD-LLD-0.1?style=for-the-badge&color=green" alt="License Badge"/>
  </a>
</p>

<!-- Tech Stack Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel"/>
</p>

<!-- Animated Typing Header -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2800&pause=1000&color=22C55E&center=true&vCenter=true&width=600&lines=Shorten+long+URLs+instantly;Clean+and+modular+architecture;Fast+HTTP+redirection+engine" alt="Typing Animation"/>
</p>

<p align="center">
  <a href="https://tinyurl-spd.vercel.app">
    <img src="https://img.shields.io/badge/🚀_Visit_Live_Demo-0070F3?style=for-the-badge&logo=vercel&logoColor=white" alt="Live Demo"/>
  </a>
</p>

</div>

---

## 📖 What Is TinyURL LLD?

**TinyURL LLD** is a URL-shortening application built with Python and deployed on Vercel. It demonstrates the core concepts of Low-Level Design (LLD), modular architecture, URL mapping, and HTTP redirection.

The application converts long URLs into compact, shareable links and redirects users to their original destinations when the shortened links are opened.

### 🔄 How It Works

```text
Long URL
   |
   v
[ URL Validation ]
   |
   v
[ Short Code Generator ]
   |
   v
[ URL Mapping / Storage ]
   |
   v
Short URL (e.g., tiny.url/abc123)


Short URL Request
   |
   v
[ Short Code Lookup ]
   |
   v
[ Redirection Service ]
   |
   v
HTTP Redirect to Original URL
```

---

## 💡 Why This Project?

- **🏗️ Clean Architecture:** Separates application routing, URL-processing logic, and frontend presentation.
- **🔗 Readable Links:** Converts long URLs into short, shareable links.
- **⚡ Fast Redirection:** Resolves short codes and redirects users to their destinations.
- **☁️ Serverless Deployment:** Hosted on Vercel using a Python serverless backend.
- **🧠 LLD Practice:** Demonstrates URL mapping, component separation, and service design.
- **🧪 Extensible Design:** Provides a foundation for adding persistent storage, analytics, expiration, and custom aliases.

---

## 🎯 How to Use

### 1. Try the Live Application

1. Open the [TinyURL Live Demo](https://tinyurl-spd.vercel.app).
2. Paste a long URL into the input field.
3. Click **Shorten URL**.
4. Copy the generated short link.
5. Open the short link to verify that it redirects to the original destination.

Example input:

```text
https://example.com/very/long/nested/path?id=123
```

### 2. Run the Project Locally

Follow the installation instructions in the [Getting Started Locally](#-getting-started-locally) section.

---

## 📌 Key Features

- ⚡ **URL Shortening:** Generates compact codes for long URLs.
- 🔄 **HTTP Redirection:** Redirects short links to their original destinations.
- 📱 **Responsive Interface:** Provides a simple, user-friendly web interface.
- 🧩 **Modular Codebase:** Separates frontend assets and backend application logic.
- ☁️ **Vercel Deployment:** Supports serverless deployment.
- 🛠️ **Extensible Foundation:** Can be extended with databases, caching, expiration, and click analytics.

---

## 📂 Project Structure

```text
TinyURL-SPD-LLD-0.1/
├── public/
│   ├── index.html       # Web interface
│   ├── style.css        # Frontend styling
│   └── script.js        # Frontend interactions
├── main.py              # Python application and API routes
├── requirements.txt     # Python dependencies
├── structure.txt        # Architecture specification
├── vercel.json          # Vercel deployment configuration, if present
├── LICENSE              # MIT License
└── README.md            # Project documentation
```

*Note: The frontend filenames and deployment configuration should match the actual files in your repository.*

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Backend | Python 3.x |
| Frontend | HTML5, CSS3, JavaScript |
| Hosting | Vercel |
| Deployment Model | Serverless Functions |
| Version Control | Git and GitHub |

---

## ⚙️ Getting Started Locally

### Prerequisites

Install the following tools before starting:

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### 1. Clone the Repository

```bash
git clone https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1.git
cd TinyURL-SPD-LLD-0.1
```

### 2. Create a Virtual Environment

**Windows — Command Prompt**

```bash
python -m venv venv
venv\Scripts\activate
```

**Windows — PowerShell**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

If your application uses MongoDB or other external services, configure the required environment variables before starting it.

For example, a MongoDB-backed deployment may require:

```env
MONGODB_URI=your_mongodb_connection_string
```

**Important:** Replace the example value with your own connection string. Never commit credentials, API keys, or production secrets to GitHub.

If the application does not use MongoDB, skip this step.

### 5. Start the Application

```bash
python main.py
```

Run this command only if `main.py` includes a local development entry point. Otherwise, follow the framework-specific startup instructions configured in the project.

### 6. Open the Application

Visit the local address printed in your terminal, commonly:

```text
http://localhost:5000
```

The actual port depends on your application configuration.

---

## ☁️ Deployment

TinyURL is deployed using [Vercel](https://vercel.com/).

To deploy your own version:

1. Push the project to GitHub.
2. Import the repository into Vercel.
3. Configure the appropriate Python runtime and deployment settings.
4. Add the required environment variables in **Vercel → Project Settings → Environment Variables**.
5. Deploy the project.
6. Test URL shortening and redirection using the deployed domain.

**Live Application:** [tinyurl-spd.vercel.app](https://tinyurl-spd.vercel.app)

---

## 🧠 Low-Level Design Concepts

This project provides a practical starting point for understanding the following design concepts.

| Concept | Purpose |
|---|---|
| URL Validation | Checks whether the submitted URL is valid |
| Short Code Generation | Generates a compact identifier for a URL |
| URL Mapping | Associates a short code with its destination URL |
| Redirection Service | Resolves a code and redirects the user |
| Separation of Concerns | Keeps application responsibilities organized |
| Persistent Storage | Allows URL mappings to survive application restarts |
| Error Handling | Handles invalid input and unknown short codes |

### Potential Improvements

The project can be extended with:

- Persistent database storage.
- Collision-resistant short code generation.
- Custom short aliases.
- URL expiration and deletion.
- Click analytics and usage statistics.
- Rate limiting and abuse prevention.
- Redis caching for frequently accessed links.
- Unit tests and API integration tests.
- Improved logging and monitoring.

These are possible extensions and should not be interpreted as existing features unless they have been implemented.

---

## 🚀 Future Roadmap

- [ ] Add comprehensive unit and integration tests.
- [ ] Improve URL validation and error handling.
- [ ] Add URL expiration support.
- [ ] Introduce click analytics.
- [ ] Add Redis caching.
- [ ] Improve rate limiting and abuse protection.
- [ ] Document API endpoints and system design decisions.

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add AmazingFeature"
   ```

4. Push your branch:

   ```bash
   git push origin feature/AmazingFeature
   ```

5. Open a Pull Request describing your changes.

For significant changes, consider opening an issue first to discuss the proposed implementation.

---

## 📄 License

This project is distributed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Spandan Das**

- GitHub: [@Spandan2106](https://github.com/Spandan2106)
- Project Repository: [TinyURL-SPD-LLD-0.1](https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1)
- Live Demo: [tinyurl-spd.vercel.app](https://tinyurl-spd.vercel.app)

---

<div align="center">

**⭐ If you find this project useful, consider giving it a star!**

Built with ❤️ using Python.

</div>
