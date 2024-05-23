import axios from "axios";

export const analysis_api = 'http://localhost:14400/upload?type=analysis';
export const sovits_api = 'http://localhost:14400/upload?type=conversion';

export default {
    methods: {
        update(file, url, sampleRate) {
            const formData = new FormData();
            formData.append('sample', file)
            formData.append('sampleRate', sampleRate)
            return axios.post(url, formData, { responseType: 'blob' })
        }
    }
}
