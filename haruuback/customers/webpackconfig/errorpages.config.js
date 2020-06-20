const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  entry: { app: "../../static/js/app.js" },
  output: {
    path: path.resolve(__dirname, "/dist"),
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
      {
        test: /\.(jpg|png|gif)$/,
        use: [
          {
            loader: "file-loader",
            options: {
              name: "[name].[ext]",
              outputPath: "images/",
              publicPath: function (path) {
                return "../" + path;
              },
            },
          },
        ],
      },
      {
        test: /\.html$/i,
        loader: "html-loader",
        options: {
          minimize: false,
        },
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "../../templates/customers/error.html",
    }),
    new MiniCssExtractPlugin({
      filename: "../css/[name]-[hash].css",
    }),
  ],
};
