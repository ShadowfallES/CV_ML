var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    entry: "./dist/main.js",
    output: {
        path: path.resolve(__dirname, "static/webpack_bundles/"),
        publicPath: "auto", // necessary for CDNs/S3/blob storages
        filename: "[name]-[contenthash].js",
    },
    plugins: [
        new BundleTracker({ path: __dirname, filename: "webpack-stats.json" }),
    ],
};