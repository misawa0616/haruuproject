var path = require("path");
var MiniCssExtractPlugin = require("mini-css-extract-plugin");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  entry: { email_change: "../../static/js/email_change.js" },
  output: {
    path: path.resolve(__dirname, "../../static/webpack/"),
    filename: "[name]-[hash].js",
  },
  module: {
    rules: [
      {
        test: /\.js/,
        exclude: "/node_modules",
        use: [
          "babel-loader",
          {
            loader: "eslint-loader",
            options: {
              configFile: "./.eslintrc",
            },
          },
        ],
      },
      {
        test: /\.css/,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          {
            loader: "postcss-loader",
            options: {
              config: {
                path: "./",
              },
            },
          },
        ],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name]-[hash].css",
    }),
    new BundleTracker({
      filename: "./webpack-stats.json",
    }),
  ],
};
