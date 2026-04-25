# .gitignore Configuration Guide

## What We're Ignoring and Why

### 🔴 CRITICAL - Security Sensitive Files

**Environment Variables:**
- `.env` - Contains API keys and passwords
- `docker/.env` - Docker-specific secrets
- Never commit these to git!

**Credentials:**
- `*.key`, `*.pem`, `*.pfx` - Private keys and certificates
- `secrets/` - Any secret files

**Why:** If exposed, your API keys can be abused, databases compromised, and infrastructure breached.

---

### 🟠 HIGH PRIORITY - Generated Files

**Database:**
- `postgres/data/` - Database files (generated fresh each run)
- Large files that shouldn't be in version control

**Python:**
- `__pycache__/` - Python bytecode cache
- `.venv/`, `venv/` - Virtual environments
- `*.egg-info/` - Package metadata

**dbt:**
- `dbt/target/` - Compiled dbt models
- `dbt/logs/` - dbt execution logs

**Airflow:**
- `airflow/logs/` - Airflow execution logs
- `*.log` - All log files

**Why:** These are generated during execution and can be large. They bloat the repository and aren't needed for collaboration.

---

### 🟡 MEDIUM PRIORITY - Development Files

**IDE & Editor:**
- `.vscode/` - VS Code settings (personal to you)
- `.idea/` - JetBrains IDE settings (personal to you)
- `*.swp`, `*.swo` - Vim swap files

**Operating System:**
- `.DS_Store` - macOS system files
- `Thumbs.db` - Windows thumbnail cache

**Testing:**
- `.pytest_cache/` - Pytest cache
- `.coverage` - Code coverage files

**Why:** These are specific to your development environment and not needed for others.

---

## File Structure

```
weather-etl-pipeline/
├── .gitignore          ← Excludes files from git
├── docker/
│   ├── .env           ← NEVER COMMIT (actual secrets)
│   └── .env.example   ← DO COMMIT (template only)
├── postgres/
│   └── data/          ← NEVER COMMIT (generated DB files)
└── ... other files
```

---

## Workflow

### 1. Create your .env files (NEVER commit)
```bash
cp docker/.env.example docker/.env
# Edit docker/.env with your actual API keys
```

### 2. .gitignore automatically excludes them
```bash
git status
# .env files won't show up (they're ignored)
```

### 3. Share template with team
```bash
# Commit .env.example (no secrets)
# Others will copy and fill in their values
git add docker/.env.example
git commit -m "Add .env template"
```

---

## Quick Checklist

Before committing to GitHub:
- [ ] `docker/.env` is NOT in git (has real secrets)
- [ ] `docker/.env.example` IS in git (template only)
- [ ] `.gitignore` is in place
- [ ] No `postgres/data/` folder in git
- [ ] No `.vscode/` or `.idea/` in git

---

## If You Accidentally Committed Secrets

If you accidentally committed a `.env` file with API keys:

1. **Remove from git history** (but keep locally):
   ```bash
   git rm --cached docker/.env
   git commit -m "Remove .env from git history"
   ```

2. **Rotate your API keys** on the provider's website

3. **Push to GitHub** to remove from history

---

## Reference: What Each Section Does

| File/Folder | Reason | Impact |
|---|---|---|
| `.env` | Secrets | 🔴 HIGH |
| `postgres/data/` | Generated | 🟠 MEDIUM |
| `__pycache__/` | Generated | 🟡 LOW |
| `.vscode/` | Personal | 🟡 LOW |
| `*.log` | Generated | 🟡 LOW |

---

Happy committing! 🚀
