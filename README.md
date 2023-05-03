# E Commerce Django
This is an E-Commerce website project in Django which is currently in-progress. Stay tuned for more updates :)

# To Run the project
* Step 1:
  ```
  py manage.py migrate
  ```
* Step 2:
  ```
  python manage.py runserver
  ```

# TailwindCss CLI

* Add Tailwindcss Postcss 

```
  npm install -D tailwindcss postcss autoprefixer
  npx tailwindcss init 
```

* Add Flowbite and Tailwindcss Forms

```
  npm install fowbite
  npm install @tailwindcss/forms
  npm install @tailwindcss/aspect-ratio
```
* Run this in terminal
```
npx tailwindcss -i ./tailwind.css -o ./webstore/static/output.css --watch
```