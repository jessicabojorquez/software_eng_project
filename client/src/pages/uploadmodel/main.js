import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')



const form = document.getElementById('form');
const formData = new FormData(form);
const output = document.getElementById('output');

for (const [key, value] of formData) {
    output.textContent += `${key}: ${value}\n`;
}

//According to this: https://stackoverflow.com/questions/65413569/how-to-upload-an-image-to-a-local-folder-in-vuejs
//You need an app on the server to save the image I don't think it is possible to 
//save it in the front app, You can temporarily save it in base 64 in localsotrage



// source: https://masteringjs.io/tutorials/vue/file-upload
// const app = new Vue({
//     data: () => ({images: null}),
//     template: `
//       <div>
//         <input type="file" @change="uploadFile" ref="file">
//         <button @click="submitFile">Upload!</button>
//       </div>
//     `,
//     methods: {
//       uploadFile() {
//         this.Images = this.$refs.file.files[0];
//       },
//       submitFile() {
//         const formData = new FormData();
//         formData.append('file', this.Images);
//         const headers = { 'Content-Type': 'multipart/form-data' };
//         axios.post('https://httpbin.org/post', formData, { headers }).then((res) => {
//           res.data.files; // binary representation of the file
//           res.status; // HTTP status
//         });
//       }
//     }
//   });
//   app.$mount("#content");