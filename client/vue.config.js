/*
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})
*/
const path = require('path');

module.exports = {
  pages: {
    about: 'src/pages/about/main.js',
    howitworks: 'src/pages/howitworks/main.js',
    index: 'src/pages/index/main.js',
    library: 'src/pages/library/main.js',
    output: 'src/pages/output/main.js',
    uploadmodel: 'src/pages/uploadmodel/main.js',
  },
  publicPath: '/static/src/vue/dist/', // Should be STATIC_URL + path/to/build
  outputDir: path.resolve(__dirname, '../server/static/src/vue/dist/'), // Output to a directory in STATICFILES_DIRS
  filenameHashing: false, // Django will hash file names, not webpack
  runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
  devServer: {
    devMiddleware: {
      writeToDisk: true,
    }
  },
};