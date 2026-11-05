# CLAUDE.md — Project context for Claude

## Project
Syncora: a real-time chat and collaboration app built day by day with the owner, who wants to understand every step and how data flows.

## Stack
Django, Django Channels (ASGI), WebSockets, Redis (channel layer), HTML/CSS/JavaScript, GSAP, WebRTC. Windows dev machine.

## Requirements
- Rooms, private messages, online status, notifications
- Notification whenever a user receives a message: in-app (toast, badge, sound) and browser push notifications when the tab is closed
- Login with either phone number or email (OTP verification for phone; in development the OTP is printed to the console, SMS provider chosen at deployment)
- Works on mobile and laptop (responsive, PWA later)
- Cool, attractive UI/UX, dark/light mode switch, GSAP animations
- End-to-end encrypted chats (Web Crypto in the browser; server stores ciphertext only)
- Voice call, video call, 1-to-1 and group, screen sharing
- Unique features: self-destructing messages, call whiteboard and screen-share annotations, safety number verification, voice notes with auto-transcript

## Working rules
- One day at a time; the owner finishes Day N, then asks for Day N+1.
- Explain how each step works and flows.
- At the end of each day: update README.md (day log, structure, stack) and this file's progress section, and give the owner the full updated README.md.
- Owner pushes to GitHub daily.

## Progress
- Day 1: project setup, apps registered, first page (home) working. Daphne is installed but not yet in INSTALLED_APPS; Day 4 adds it with ASGI_APPLICATION.
- Day 2: custom User (email and/or phone, unique, nullable), EmailOrPhoneBackend (only backend), phone OTP (PhoneOTP model, printed to console), register/login/logout/verify views, login-protected /app/ dashboard. AUTH_USER_MODEL = 'accounts.User'.
- Current day: 3 next (UI shell, dark/light theme, GSAP)

## Project structure
config/ (settings, urls, asgi); accounts/ (models.py User+PhoneOTP, backends.py, forms.py, views.py, urls.py, admin.py); chat/ (urls.py, views.py: home, dashboard); templates/ (base.html, home.html, dashboard.html, accounts/register.html, login.html, verify_otp.html); static/css, static/js; requirements.txt; README.md; ROADMAP.md; CLAUDE.md; .gitignore