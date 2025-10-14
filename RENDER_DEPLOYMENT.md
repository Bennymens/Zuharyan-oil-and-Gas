# Render Deployment Configuration

## Environment Variables to Set in Render Dashboard

After deploying to Render, you need to manually add these environment variables in the Render dashboard:

### Required Variables:

```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

### Optional (if using PostgreSQL):

```
DATABASE_URL=postgresql://user:password@host:port/dbname
```

## Deployment Steps:

1. **Push your code to GitHub**

   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Create Web Service on Render**

   - Go to https://render.com
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `Bennymens/Zuharyan-oil-and-Gas`
   - Render will auto-detect the `render.yaml` configuration

3. **Add Email Environment Variables**

   - Go to your service's "Environment" tab
   - Add the required variables listed above
   - Click "Save Changes"

4. **Deploy**

   - Render will automatically trigger a deployment
   - Monitor the logs for any errors
   - Wait for the build to complete

5. **Verify Deployment**
   - Visit your Render URL: `https://zuhayran-oil-and-gas.onrender.com`
   - Test all pages
   - Test the contact form
   - Check that static files load correctly

## Build Command Explanation:

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

- `pip install -r requirements.txt` - Installs all Python dependencies
- `python manage.py collectstatic --noinput` - Collects all static files for Whitenoise
- `python manage.py migrate` - Runs database migrations

## Start Command:

```bash
gunicorn oilandgas.wsgi --log-file -
```

- Starts Gunicorn web server
- `--log-file -` sends logs to stdout for Render to capture

## Static Files:

Static files are served by Whitenoise (configured in settings.py):

- Compressed and cached automatically
- No separate static file server needed
- Production-ready performance

## Database:

- Default: SQLite (included in build)
- Recommended for production: PostgreSQL
- To add PostgreSQL:
  1. In Render, add a PostgreSQL database
  2. Copy the "Internal Database URL"
  3. Set as `DATABASE_URL` environment variable

## Troubleshooting:

### Build fails:

- Check that all dependencies are in `requirements.txt`
- Verify Python version compatibility (3.13.0)
- Check build logs for specific errors

### Static files not loading:

- Ensure `collectstatic` ran successfully in build command
- Check that Whitenoise is in MIDDLEWARE (settings.py)
- Verify STATIC_ROOT is set correctly

### Site won't load:

- Check `ALLOWED_HOSTS` includes your Render domain
- Verify `DEBUG=False` is set
- Check application logs for errors

### Contact form not working:

- Verify email environment variables are set
- Check Gmail app password is correct
- Ensure 2FA is enabled on Gmail account

## Monitoring:

- **Logs**: View real-time logs in Render dashboard
- **Metrics**: Check CPU, memory usage in Render dashboard
- **Alerts**: Set up email notifications for deploy failures

## Updating Your Site:

After making changes locally:

1. Test locally with `python manage.py runserver`
2. Commit changes: `git add . && git commit -m "Your message"`
3. Push to GitHub: `git push origin main`
4. Render auto-deploys on push (if enabled)
5. Or manually trigger deploy in Render dashboard

## Security Checklist:

- [x] DEBUG=False in production
- [x] Strong SECRET_KEY generated
- [x] ALLOWED_HOSTS restricted to your domain
- [x] Email credentials in environment variables
- [x] HTTPS enforced (automatic on Render)
- [x] Security headers configured
- [x] Static files compressed

## Performance Tips:

- Render free tier may sleep after 15 min of inactivity
- First request after sleep takes ~30 seconds to wake up
- Consider upgrading to paid plan for always-on service
- Use PostgreSQL for better database performance

---

**Your site is ready for Render deployment!** 🚀
