# Temp Django

## Project to demonstrate some Django features

Currently only demonstrates GitHub OAuth with [drf-social-oauth2](https://github.com/wagnerdelima/drf-social-oauth2/)

### Setup

```bash
pip install -r requirements.txt
```

* Setup [New application](https://drf-social-oauth2.readthedocs.io/en/latest/application.html)
* Register [GitHub Integration](https://drf-social-oauth2.readthedocs.io/en/latest/integration.html#github-integration)
* Export key/secret as `SOCIAL_AUTH_GITHUB_KEY/SOCIAL_AUTH_GITHUB_SECRET`

### Run

* Go to `http://localhost:8000/auth/login/github/`
* Copy `code` from `/auth/complete/github` endpoint

```bash
curl -X POST -d "grant_type=convert_token&client_id=<client_id>&client_secret=<client_secret>&backend=github&token=<code>" http://localhost:8000/auth/convert-token
```
