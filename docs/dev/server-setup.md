# Server setup

Some useful guides if self-hosting (e.g. on Digital Ocean):

- https://www.digitalocean.com/community/tutorials/how-to-set-up-an-ubuntu-server-on-a-digitalocean-droplet
- https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu
- https://hostadvice.com/how-to/web-hosting/ubuntu/how-to-harden-your-ubuntu-18-04-server/
- https://www.digitalocean.com/community/tutorials/ubuntu-and-debian-package-management-essentials
- https://www.digitalocean.com/community/tutorials/how-to-keep-ubuntu-22-04-servers-updated
- https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu
- https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-22-04
- https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-22-04
- https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04
- https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-with-http-2-support-on-ubuntu-22-04
- https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-22-04-quickstart
- https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-22-04


---

## If cloning a private GitHub repo

- Create an ssh key on the server:

```
ssh-keygen
```

- Follow the steps. It may be worth changing the default key path so that you can create a unique ssh key for different repos

- Once this is complete, create a config file: `~/.ssh/config`:

```
Host          hostname
HostName      github.com
User          git
IdentityFile  ~/.ssh/id_rsa
```

- Next, copy the public key from ~/.ssh/id_rsa_backend.pub and add this to the GitHub repository as a deploy key

This will allow you to clone this private repo on the server, using the config name.

- Clone this repo onto the server:

```
git clone hostname:user/repo.git
```

---

## Installation

- Create and enter a virtualenv

- Install the project dependencies:

  ```
  pip install -r requirements.txt
  ```

- Manually create an `.env` file in the root of the project directory, based on the sample `.env.example` file:

  ```
  cp .env.example .env
  nano .env
  ```

- [Generate](https://djecrety.ir/) a new Django secret key

- Update the `.env` details

- Add the website's URL to the list of `ALLOWED_HOSTS`

- Add relevant API keys to the file

- Move into the repo directory

- Run the database migrations:

  ```
  python manage.py migrate
  ```

- Gather static assets:

  ```
  python manage.py collectstatic
  ```

- Create an admin superuser:

  ```
  python manage.py createsuperuser
  ```

- Follow the instructions above to set up gunicorn

- Set up a new nginx site:

  ```
  server {
    server_name sitename.com;
    location /static/ {
      alias /path/to/sitename/static/;
    }
    location /media/ {
      alias /path/to/sitename/media/;
    }
    location / {
      include proxy_params;
      proxy_pass http://unix:/run/gunicorn.sock;
    }
  }
  ```

- Follow the instructions above to use certbot to set up a free SSL certificate.

