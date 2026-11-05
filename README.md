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

## Project structure
```
syncora/
├── config/            # project settings, root urls, asgi/wsgi entry points
├── accounts/          # users and login (built from Day 2)
├── chat/              # rooms, messages, consumers (built from Day 4)
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html      # shared layout all pages extend
│   └── home.html
├── static/
│   ├── css/
│   └── js/
├── manage.py
├── requirements.txt
└── .gitignore
```

## Roadmap
See ROADMAP.md
