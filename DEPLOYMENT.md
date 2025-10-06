# Deployment Guide for Zuhayrān Oil & Gas Website

## Pre-Deployment Checklist ✅

### Security Configuration

- [x] All credentials moved to environment variables
- [x] DEBUG set to False by default
- [x] HTTPS/SSL redirect enabled in production
- [x] Secure cookies (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE)
- [x] HSTS headers configured (1 year)
- [x] Security headers added (X-Frame-Options, Content-Type-Nosniff)
- [x] Whitenoise configured for static files
- [ ] Generate strong SECRET_KEY (see instructions below)

### Required Environment Variables

You MUST set these environment variables on your deployment platform:

```bash
SECRET_KEY=<generate-strong-secret-key-min-50-chars>
DEBUG=False
ALLOWED_HOSTS=<your-domain.com,www.your-domain.com>
EMAIL_HOST_USER=<your-email@gmail.com>
EMAIL_HOST_PASSWORD=<your-gmail-app-password>
```

Optional (use DATABASE_URL for PostgreSQL in production):

```bash
DATABASE_URL=postgresql://user:password@host:port/dbname
```

### Generate a Strong SECRET_KEY

Run this command to generate a secure secret key:

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and set it as your SECRET_KEY environment variable.

## Deployment Steps

### For Render.com:

1. **Push your code to GitHub**

   ```bash
   git add .
   git commit -m "Prepare for production deployment with security fixes"
   git push origin main
   ```

2. **Create a new Web Service on Render**

   - Connect your GitHub repository
   - Select Python environment
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn oilandgas.wsgi`

3. **Set Environment Variables** (in Render Dashboard)

   - Go to Environment → Add Environment Variables
   - Add all required variables listed above
   - **IMPORTANT:** Set `DEBUG=False`

4. **Deploy**
   - Render will automatically deploy
   - Monitor logs for any errors

### For Railway:

1. **Push code to GitHub** (same as above)

2. **Create new project on Railway**

   - Connect GitHub repository
   - Railway auto-detects Django

3. **Set Environment Variables**

   - Go to Variables tab
   - Add all required environment variables
   - Railway provides DATABASE_URL automatically if you add PostgreSQL

4. **Deploy**
   - Railway deploys automatically

### For Other Platforms (Heroku, DigitalOcean, etc.):

Follow similar steps:

1. Push code to repository
2. Connect platform to your repo
3. Set environment variables
4. Configure build/start commands:
   - Build: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - Start: `gunicorn oilandgas.wsgi`

## Post-Deployment Tasks

1. **Run migrations** (if deploying to new database):

   ```bash
   python manage.py migrate
   ```

2. **Create superuser** (for admin access):

   ```bash
   python manage.py createsuperuser
   ```

3. **Test your deployment:**

   - Visit your site URL
   - Test contact form
   - Check all pages load correctly
   - Verify static files are served
   - Try accessing /admin

4. **Security verification:**
   - Test HTTPS is working
   - Check SSL certificate
   - Verify all pages redirect to HTTPS
   - Test security headers: https://securityheaders.com

## Database Recommendations

### Development:

- SQLite (current setup) - OK for testing

### Production:

- **PostgreSQL** (recommended for production)
- More reliable and scalable than SQLite
- Better concurrency handling
- Supported by all major hosting platforms

To switch to PostgreSQL, set the DATABASE_URL environment variable:

```
DATABASE_URL=postgresql://username:password@hostname:5432/database_name
```

The app will automatically use it (already configured with dj-database-url).

## Monitoring & Maintenance

1. **Monitor error logs** on your hosting platform
2. **Set up email notifications** for errors
3. **Regular backups** of your database
4. **Keep dependencies updated** (security patches)
5. **Monitor SSL certificate expiration**

## Security Best Practices

- Never commit `.env` file to Git (it's in .gitignore)
- Rotate SECRET_KEY periodically
- Keep Django and all dependencies updated
- Monitor Django security advisories
- Use strong passwords for admin accounts
- Enable 2FA on hosting platform

## Scaling Considerations

Current setup supports:

- Up to ~1000 concurrent users with gunicorn
- Static files served efficiently via Whitenoise
- Database connection pooling enabled

For higher traffic:

- Add more gunicorn workers
- Upgrade to larger database instance
- Consider CDN for static files
- Add Redis for caching
- Implement rate limiting

## Troubleshooting

### Static files not loading:

```bash
python manage.py collectstatic --clear
```

### Database errors:

- Check DATABASE_URL is set correctly
- Run migrations: `python manage.py migrate`

### Email not sending:

- Verify EMAIL_HOST_USER and EMAIL_HOST_PASSWORD
- Check Gmail app password is correct
- Ensure 2FA is enabled on Gmail account

### 500 errors:

- Check DEBUG=False is set
- Review application logs
- Verify all environment variables are set
- Check ALLOWED_HOSTS includes your domain

## Support

For issues or questions:

- Check application logs first
- Review Django documentation: https://docs.djangoproject.com
- Check hosting platform docs
- Review this deployment guide

---

**Last Updated:** October 6, 2025
**Django Version:** 5.2.3
**Python Version:** 3.13+
