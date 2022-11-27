import axios from 'axios'

async function uploadRequest(formData) {
    let res = await axios.post('http://127.0.0.1:8000/upload/model', formData, {
        headers: {
            "X-CSRFToken": getCSRFToken(),
            'Content-Type': 'multipart/form-data'
        }
    });
    let data = res.data
    console.log(data)
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

async function getCSRFToken() {
    let res = await axios.get('http://127.0.0.1:8000/admin')
    let cookie = res.headers.get('Set-Cookie').get('csrftoken')
    return cookie
}

export default uploadRequest