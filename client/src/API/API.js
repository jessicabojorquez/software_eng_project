import axios from 'axios'

async function uploadFile() {
    let payload = { name: 'John Doe', occupation: 'gardener' };

    let res = await axios.post('http://127.0.0.1:8000', payload, {headers: {"X-CSRFToken": "CSRFToken"}});

    let data = res.data;
    console.log(data);
}

export default uploadFile