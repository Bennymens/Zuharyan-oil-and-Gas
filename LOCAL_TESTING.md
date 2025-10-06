# 🚨 IMPORTANT: Use HTTP (not HTTPS) for Local Development

## ✅ Correct URL for Local Development:

http://127.0.0.1:8000/

## ❌ WRONG URLs (These will NOT work):

~~https://127.0.0.1:8000/~~ ← Don't use HTTPS
~~https://localhost:8000/~~ ← Don't use HTTPS

## Why?

The Django development server only supports HTTP.
HTTPS security features are automatically disabled when DEBUG=True.

## Your Development Server is Running

Open your browser and navigate to:

**http://127.0.0.1:8000/**

(Copy and paste this exact URL into your browser)

---

## All Your Local Pages:

- Home: http://127.0.0.1:8000/
- About: http://127.0.0.1:8000/about/
- Services: http://127.0.0.1:8000/services/
- Careers: http://127.0.0.1:8000/careers/
- Contact: http://127.0.0.1:8000/contact/
- Admin: http://127.0.0.1:8000/admin/

## Browser Security Warning?

If your browser tries to force HTTPS:

1. Make sure you type "http://" explicitly (not "https://")
2. Clear your browser cache
3. Try incognito/private browsing mode
4. Use a different browser

## Production vs Development

### Development (Now):

- URL: http://127.0.0.1:8000/
- No SSL/HTTPS required
- DEBUG=True

### Production (After Deployment):

- URL: https://yourdomain.com/
- HTTPS required and enforced
- DEBUG=False
