const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  devServer: {
    proxy: {
      "^/properties": {
        target: "http://localhost:8000",
        changeOrigin: true,
        pathRewrite: { "^/properties": "/properties" },
      },
      "^/property": {
        target: "http://localhost:8000",
        changeOrigin: true,
        pathRewrite: { "^/property": "/property" },
      },
    },
  },
});
