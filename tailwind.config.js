/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./webstore/templates/**/*.html', "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
],
}

