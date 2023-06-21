/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./webstore/templates/**/*.html', './static/**/*.svg', "./node_modules/flowbite/**/*.js"],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
};

