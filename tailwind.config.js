/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./webstore/templates/**/*.html', "./node_modules/flowbite/**/*.js"],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin'),
    require('@tailwindcss/forms'),
  ],
};

