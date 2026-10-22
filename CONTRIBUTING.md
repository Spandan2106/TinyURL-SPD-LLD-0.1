
<div align="center">

# 🤝 Contributing to TinyURL (LLD)

<p align="center">
  Thank you for investing your time in contributing to our project! All contributions—whether fixing bugs, improving documentation, or proposing design enhancements—are welcome.
</p>

<p align="center">
  <a href="https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1/issues">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge" alt="PRs Welcome"/>
  </a>
  <img src="https://img.shields.io/badge/Contributions-Welcome-blue.svg?style=for-the-badge" alt="Contributions Welcome"/>
  <img src="https://img.shields.io/badge/Community-Driven-purple.svg?style=for-the-badge" alt="Community Driven"/>
</p>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=2500&pause=1000&color=22C55E&center=true&vCenter=true&width=500&lines=Read+the+guidelines;Fork+and+create+a+branch;Submit+your+Pull+Request!" alt="Typing Animation"/>

<p align="center">
  <a href="https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1">
    <img src="https://img.shields.io/badge/Repository-TinyURL-181717?style=flat&logo=github&logoColor=white" alt="GitHub Repository"/>
  </a>
  <a href="https://tinyurl-spd.vercel.app">
    <img src="https://img.shields.io/badge/Live-Demo-0070F3?style=flat&logo=vercel&logoColor=white" alt="Live Demo"/>
  </a>
</p>

</div>

---

## 🧭 Code of Conduct

By participating in this project, you agree to maintain a respectful, inclusive, and harassment-free environment for everyone.

Please be considerate, constructive, and collaborative in discussions, issue reports, and code reviews.

---

## 🛠️ How to Contribute

### 🐛 1. Reporting Bugs

Found a bug? Help us improve TinyURL!

- Check the [Issues tab](https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1/issues) to see whether the issue has already been reported.
- Open a new issue with a clear and descriptive title.
- Include steps to reproduce the problem.
- Describe the expected behavior and the actual behavior.
- Attach relevant terminal logs, error messages, or screenshots when applicable.

### 💡 2. Suggesting Enhancements

Have an idea for improving TinyURL?

- Open an issue describing your proposed enhancement.
- Explain the problem your idea solves and why it would be useful.
- Include implementation suggestions or architectural considerations where appropriate.
- Discuss significant changes before submitting a large implementation.

Potential areas for improvement include URL validation, short-code generation, persistent storage, caching, analytics, testing, and security.

### 🔧 3. Submitting Code Changes

Follow these steps to contribute code through a Pull Request (PR).

#### Step 1: Fork the Repository

Visit the [TinyURL repository](https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1) and click the **Fork** button.

#### Step 2: Clone Your Fork

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/TinyURL-SPD-LLD-0.1.git
cd TinyURL-SPD-LLD-0.1
```

#### Step 3: Create a Feature Branch

Create a separate branch for your changes.

```bash
# For new features
git checkout -b feature/your-feature-name

# For bug fixes
git checkout -b fix/issue-description
```

#### Step 4: Set Up a Virtual Environment

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

#### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 6: Make and Test Your Changes

- Write clean, readable, and maintainable code.
- Follow the existing project architecture.
- Keep modules focused on their intended responsibilities.
- Validate your changes locally before submitting a PR.
- Add or update tests when appropriate.
- Avoid introducing unnecessary dependencies.

If `main.py` supports local execution, run:

```bash
python main.py
```

Verify the application using the local address and port configured by the project.

#### Step 7: Commit Your Changes

Use clear, descriptive commit messages.

```bash
git add .
git commit -m "feat: add rate limiting support"
```

Examples of commit message prefixes:

| Prefix | Purpose |
|---|---|
| `feat:` | Add a feature |
| `fix:` | Fix a bug |
| `docs:` | Update documentation |
| `refactor:` | Improve code structure |
| `test:` | Add or update tests |
| `chore:` | Perform maintenance tasks |

#### Step 8: Push Your Branch

```bash
git push origin feature/your-feature-name
```

Replace the branch name with the one you created.

#### Step 9: Open a Pull Request

- Navigate to your fork on GitHub.
- Select **Compare & pull request**.
- Set the original repository as the base repository.
- Describe your changes and their purpose.
- Link any related issues, for example, `Fixes #12`.
- Submit your Pull Request for review.

---

## 📋 Development & Style Guidelines

### 🐍 Python Code

- Follow [PEP 8](https://peps.python.org/pep-0008/) conventions.
- Use descriptive variable and function names.
- Keep functions focused and avoid unnecessary complexity.
- Handle errors explicitly and provide useful error messages.
- Keep dependencies minimal and document new requirements.

### 🎨 Frontend Assets

- Keep static assets organized in the `public/` directory, where applicable.
- Use semantic HTML and maintainable CSS.
- Write clear, modular JavaScript.
- Ensure the interface remains usable on mobile and desktop screens.
- Avoid unrelated UI changes in backend-focused Pull Requests.

### 🏗️ Low-Level Design Principles

- Follow the existing architectural conventions.
- Keep responsibilities separated and modules loosely coupled.
- Apply SOLID principles where appropriate.
- Avoid unnecessary abstractions and overengineering.
- Keep URL validation, code generation, storage, and redirection responsibilities logically separated when the architecture supports it.

### 🧪 Testing & Reliability

- Test both successful operations and failure cases.
- Verify that valid URLs are shortened correctly.
- Verify that generated short links redirect to their intended destinations.
- Test invalid input and unknown short codes.
- Never include real credentials, private connection strings, or sensitive production data in tests or commits.

---

## ✅ Pull Request Checklist

Before submitting your Pull Request, make sure that:

- [ ] The changes solve the intended problem.
- [ ] The code follows the project's existing style.
- [ ] Relevant tests have been added or updated.
- [ ] The application has been tested locally where possible.
- [ ] Documentation has been updated if necessary.
- [ ] No secrets, credentials, or unrelated files have been committed.
- [ ] The Pull Request description clearly explains the changes.

---

## ❓ Need Help?

If you have questions, encounter blockers, or want to discuss an architectural decision, open an issue in the repository.

<p align="center">
  <a href="https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1/issues">
    <img src="https://img.shields.io/badge/Open_an_Issue-181717?style=for-the-badge&logo=github&logoColor=white" alt="Open an Issue"/>
  </a>
  <a href="https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1">
    <img src="https://img.shields.io/badge/Explore_Repository-0070F3?style=for-the-badge&logo=github&logoColor=white" alt="Explore Repository"/>
  </a>
</p>

---

<div align="center">

### 🌟 Every Contribution Matters

Thank you for helping make TinyURL better!

**Built with ❤️ using Python.**

[⬆ Back to Repository](https://github.com/Spandan2106/TinyURL-SPD-LLD-0.1)

</div>
