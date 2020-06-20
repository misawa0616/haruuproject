var path = require("path");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  entry: { app: "../../static/js/app.js" },
  output: {
    path: path.resolve(__dirname, "../../static/webpack/"),
    filename: "[name]-[hash].js",
  },
  module: {
    rules: [
      {
        test: /\.js/,
        exclude: "/node_modules",
        use: ["babel-loader"],
      },
      {
        test: /\.css/,
        use: [
          "style-loader",
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
  plugins: [new BundleTracker({ filename: "./webpack-stats.json" })],
};
