import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
    baseURL: API_URL,
});

export const getDashboardStats = () => api.get('/dashboard');
export const getStudents = () => api.get('/students');
export const getStudentDetails = (id) => api.get(`/students/${id}`);
export const getAttendance = () => api.get('/attendance');
export const getTodayAttendance = () => api.get('/attendance/today');
export const getStudentAttendance = (name) => api.get(`/attendance/student/${name}`);
export const getSystemStatus = () => api.get('/system/status');

export const recognizeAndMark = async (imageBlob) => {
    const formData = new FormData();
    formData.append('image', imageBlob, 'capture.jpg');
    
    return api.post('/recognition', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });
};

export default api;
