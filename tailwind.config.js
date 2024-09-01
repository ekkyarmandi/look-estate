/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,vue}"],
  theme: {
    extend: {
      colors: {
        primary: {
          500: "#3FBA84",
        },
        secondary: {
          500: "#30485E",
        },
      },
    },
  },
  plugins: [],
};
