# Local Development Guide

## Quick Start

Your development environment is now set up! The server is running at:
**http://127.0.0.1:8000/** (note: HTTP, not HTTPS)

## Environment Configuration

### Local Development (.env file)

The `.env` file has been created with these settings:

- `DEBUG=True` - Shows detailed error pages
- `SECRET_KEY` - Development-only key (not secure for production)
- `ALLOWED_HOSTS` - Localhost only
- `EMAIL_BACKEND` - Emails print to console (no real emails sent)

### What This Means:

✅ HTTPS enforcement is **disabled** (you can use http://127.0.0.1:8000)  
✅ Security headers are **relaxed** for development  
✅ Detailed error messages are **enabled**  
✅ Contact form emails will **print to console** (not sent via email)

## Testing Your Changes

### 1. Run the Development Server

```bash
python manage.py runserver
```

### 2. Access Your Site

Open your browser and go to: **http://127.0.0.1:8000**

### 3. Test All Pages

- Home: http://127.0.0.1:8000/
- About: http://127.0.0.1:8000/about/
- Services: http://127.0.0.1:8000/services/
- Careers: http://127.0.0.1:8000/careers/
- Contact: http://127.0.0.1:8000/contact/
- Admin: http://127.0.0.1:8000/admin/

### 4. Test Contact Form

When you submit the contact form:

- Check the **terminal/console** for the email output
- You should see both emails (to company and confirmation to user)
- No actual emails will be sent (they just print to console)

## Making Changes

### Code Changes

- HTML templates: `main/templates/main/*.html`
- Views: `main/views.py`
- URLs: `main/urls.py`
- Static files: `main/static/`

The development server **auto-reloads** when you save changes!

### Database Changes

If you modify models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Static Files

For local development, static files are served automatically.
No need to run `collectstatic`.

## Common Issues & Solutions

### Issue: Port already in use

**Error:** "That port is already in use"  
**Solution:**

```bash
# Use a different port
python manage.py runserver 8080
```

### Issue: Module not found

**Solution:**

```bash
pip install -r requirements.txt
```

### Issue: Database errors

**Solution:**

```bash
python manage.py migrate
```

### Issue: Static files not loading

**Solution:**

- Make sure DEBUG=True in .env
- Clear browser cache
- Hard refresh (Ctrl + Shift + R)

## Switching Between Development and Production

### Development Mode (Current)

```env
# .env file
DEBUG=True
```

- HTTP works fine
- Detailed errors shown
- Emails to console
- Less secure (OK for local testing)

### Production Mode (When Deploying)

```env
# Set on hosting platform
DEBUG=False
SECRET_KEY=<strong-random-key>
ALLOWED_HOSTS=yourdomain.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

- HTTPS required
- Generic error pages
- Real emails sent
- Full security enabled

## Development Workflow

1. **Make changes** to your code
2. **Save the file** (server auto-reloads)
3. **Refresh browser** to see changes
4. **Check console** for any errors
5. **Repeat** until satisfied

## Before Deployment

### Pre-Deployment Checklist:

- [ ] Test all pages locally
- [ ] Test contact form (emails appear in console)
- [ ] Test admin panel (create superuser if needed)
- [ ] Test on mobile view (responsive design)
- [ ] Fix any console errors
- [ ] Review all content and images

### Create Superuser (for Admin Access)

```bash
python manage.py createsuperuser
```

Then access admin at: http://127.0.0.1:8000/admin/

### When Ready to Deploy

1. Commit all changes: `git add . && git commit -m "Final changes"`
2. Push to GitHub: `git push origin main`
3. Follow `DEPLOYMENT.md` guide
4. Set production environment variables
5. Deploy!

## Getting Help

- **Django errors:** Check the terminal output for detailed error messages
- **Static files issues:** Make sure DEBUG=True
- **Database issues:** Try `python manage.py migrate`
- **Import errors:** Run `pip install -r requirements.txt`

## Important Files

- `.env` - Local environment variables (DO NOT COMMIT)
- `.env.example` - Template for production variables
- `DEPLOYMENT.md` - Production deployment guide
- `SECURITY_REPORT.md` - Security audit results
- `requirements.txt` - Python dependencies

---

**Happy Coding! 🚀**

Your development server is ready at: http://127.0.0.1:8000/
