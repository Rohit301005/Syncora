# Syncora

Syncora is a real-time chat and collaboration app. It is a Django Channels app with email or phone-number login, rooms, private messages, online status, notifications, end-to-end encryption, voice/video/group calls, screen sharing, and a call whiteboard.

## Tech stack
Django, Django Channels, WebSockets, Redis, HTML/CSS/JavaScript, GSAP, WebRTC

## Day log
### Day 0 — Planning
- Defined scope, roadmap (24 days) and project context files.
- Added: login with email or phone number, and notifications on every received message.

### Day 1 — Project setup
- Created a virtual environment and installed django, channels, daphne, channels-redis.
- Created the `config` project and the `accounts` and `chat` apps.
- Registered the apps, set up `templates/` and `static/` folders, and set the time zone.
- Built the first page: URL -> view -> template.
- Set up Git with a .gitignore and pushed to GitHub.
- Learned: how a normal HTTP request flows through Django (urls.py -> view -> template -> response).

### Day 2 — Authentication (email or phone login)
- Built a custom `User` model: `full_name`, optional unique `email`, optional unique `phone`, plus `is_phone_verified`.
- Wrote a custom authentication backend so a user can log in with either email or phone number.
- Added register, login, logout and OTP-verification pages. Phone accounts must verify a 6-digit OTP (printed in the terminal during development; a real SMS provider comes on Day 24).
- Added a login-protected dashboard at `/app/` and registered the user model in the admin.
- Learned: why the custom user model must exist before the first migration, how Django's authentication backends and sessions work.

## Project structure
```
syncora/
├── config/            # settings, root urls, asgi/wsgi entry points
├── accounts/          # users and login
│   ├── models.py      # User, PhoneOTP
│   ├── backends.py    # login with email or phone
│   ├── forms.py       # register, login, OTP forms
│   ├── views.py       # register, login, logout, verify OTP
│   ├── urls.py
│   └── admin.py
├── chat/              # rooms, messages, consumers (from Day 4)
│   ├── urls.py
│   └── views.py       # home, dashboard
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── dashboard.html
│   └── accounts/
│       ├── register.html
│       ├── login.html
│       └── verify_otp.html
├── static/
│   ├── css/
│   └── js/
├── manage.py
├── requirements.txt
├── README.md
├── ROADMAP.md
├── CLAUDE.md
└── .gitignore
```


