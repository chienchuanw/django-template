const path = require('path');

module.exports = {
  mode: 'development',
  entry: './src/scripts/input.js',
  output: {
    filename: 'output.js',
    path: path.resolve(__dirname, 'static/scripts'),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
    ],
  },
  optimization: {
    usedExports: true,
  },
  experiments: {
    outputModule: true,
  }
};
