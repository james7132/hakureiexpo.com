# hakureiexpo.com
Hakurei Expo, a global annual event for doujin creators to share their works with the community

## Local Development Setup

Prerequsites:

 * Python 3: This project is Python 3.5.x+ only.
 * PostgreSQL: A local installation of Postgres is required. Along with a role
   capable of creating databases.
 * (Optional but recommended) virtualenv: for isolating project setup from
   global python setup.

```bash
# Clone git repo
git clone https://github.com/james7132/hakureiexpo.com.git
cd hakureiexpo.com

# (Optional) Create virtualenv for project
virtualenv -P python3 venv
source venv/bin/activate

# Install required pip packages
pip install -r requirements.txt

# Migrate the database
python hakureiexpo/manage.py migrate

# Run tests
python hakureiexpo/manage.py test

# Start development server
python hakureiexpo/manage.py runserver
```
