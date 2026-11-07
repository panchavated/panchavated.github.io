# Modern Developer Portfolio 🚀

A high-performance, responsive developer portfolio built with modern HTML5, CSS3, and Vanilla JavaScript. Ready for instant deployment on **GitHub Pages**.

## ✨ Features
- **Modern Glassmorphic UI**: Sleek dark and light mode toggle with state saved in localStorage.
- **Dynamic Typing Animation**: Interactive hero section highlighting your skills and roles.
- **Filterable Projects**: Categorized project showcase (Full Stack, Frontend, Backend / DevTools).
- **Interactive Experience & Education Timeline**: Clean vertical timeline displaying your journey.
- **Working Contact Section**: Direct email copy with toast notification and pre-filled email client opener.
- **Zero Dependencies / No Build Tools**: Works right out of the box in any browser.
- **GitHub Pages CI/CD Included**: Ready `.github/workflows/pages.yml` for automatic deployment on git push.

## 📁 Project Structure
```text
Portfolio/
├── index.html                  # Main portfolio website
├── styles.css                  # Modern styling & design system (CSS variables)
├── script.js                   # Interactive behaviors & theme switching
├── assets/
│   └── images/
│       └── avatar.svg          # Profile picture / avatar
└── .github/
    └── workflows/
        └── pages.yml           # Automated GitHub Pages deployment
```

## 🛠️ Customization Guide
1. **Your Information**: Open `index.html` and search for `Your Name` to customize your name, bio, social links, and contact information.
2. **Projects**: In `index.html`, edit the `<article class="project-card">` elements to showcase your own projects, links, and screenshots.
3. **Avatar**: Replace `assets/images/avatar.svg` with your own photo (e.g. `assets/images/avatar.jpg` or `.png`).
4. **Skills**: Add or adjust the skill badges under `#skills` in `index.html`.

## 🌐 Deploy to GitHub Pages
1. Authenticate with GitHub CLI:
   ```bash
   gh auth login
   ```
2. Initialize repository and commit:
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio release"
   ```
3. Create a public repository and push:
   ```bash
   gh repo create <your-username>.github.io --public --source=. --remote=origin --push
   ```
4. In your GitHub repository:
   - Go to **Settings** → **Pages**
   - Under **Build and deployment > Source**, select **GitHub Actions**
   - Your site will be live at `https://<your-username>.github.io/`!
