import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

async function uploadRequest(formData) {
    let res = await axios.post('http://127.0.0.1:8000/upload/request', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        },
    });
    return res.data
}

/*
async function uploadPictures(formData) {
    let res = await axios.post('http://127.0.0.1:8000/upload/image', formData, {
        headers: {
            "X-CSRFToken": "CSRFToken",
            'Content-Type': 'multipart/form-data'
        }
    })
    let data = res.data
    console.log(data)
}
*/

/*
async function getCSRFToken() {
    let res = await axios.get('http://127.0.0.1:8000/admin', {
        headers: {
            'Access-Control-Allow-Credentials': 'true',
            "Access-Control-Allow-Headers": "Authorization, access-control-allow-credentials",
        },
    })
    console.log(res.headers['set-cookie'])
}
*/
export default uploadRequest