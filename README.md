# Denaro

## How to get started!

### Requirements

> Latest version is okay

- PHP
- Composer
- Python

> ! This does not include any frontend packages yet, so if it goes further, will have to update accordingly.

### Instruction

1. Initialize git into current directory
2. Run `git remote add origin "https://github.com/Denaro-Project/Denaro.git"`
3. Run `git pull origin main`
4. Change directory to denaro-webapp: `cd denaro-webapp`.
5. Run `composer install` (helps install all PHP dependencies from `composer.lock`)
6. Run `cp .env.example .env` (helps match run the machine)
7. Run `php artisan key:generate` (Generates missing APP_KEY in .env)
8. Run `php artisan migrate` (Runs installation of database + tables)

### Update (17/10/25)

1. Ensure that `php artisan storage:link` is run on the machine to link the `storage/app/public` is linked with `public/storage`.
