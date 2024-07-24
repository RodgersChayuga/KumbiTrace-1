/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // "./kumbitraceweb/templates/**/*.html",
    "./kumbitraceweb/**/*.{html,py}",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
