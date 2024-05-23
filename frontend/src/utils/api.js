import axios from "axios";

export const analysisApi = 'http://127.0.0.1:14400/upload?type=analysis';
export const sovitsApi = 'http://127.0.0.1:14400/upload?type=conversion';

export default {
    methods: {
        update(file, url, sampleRate) {
            const formData = new FormData();
            formData.append('sample', file);
            formData.append('sampleRate', sampleRate);
            return axios.post(url, formData, { responseType: 'blob' })
                .then(response => {
                    console.log("Response:", response);
                    return response;
                })
                .catch(error => {
                    console.error("Error:", error);
                    throw error;
                });
        }
    }
}

