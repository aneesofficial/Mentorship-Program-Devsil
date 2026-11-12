import React, { useEffect, useState } from 'react';
import { getDashboardStats } from '../services/api';

const Dashboard = () => {
    const [stats, setStats] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        getDashboardStats()
            .then(res => {
                if(res.data.status === 'success') {
                    setStats(res.data.data);
                } else {
                    setError('Failed to load stats');
                }
            })
            .catch(err => setError(err.message))
            .finally(() => setLoading(false));
    }, []);

    if (loading) return <div className="loading">Loading dashboard...</div>;
    if (error) return <div className="loading" style={{color: 'red'}}>Error: {error}</div>;

    return (
        <div>
            <div className="page-header">
                <h1 className="page-title">Dashboard</h1>
                <p>Welcome back! Here is today's overview.</p>
            </div>

            <div className="dashboard-grid">
                <div className="stat-card">
                    <span className="stat-title">Registered Students</span>
                    <span className="stat-value">{stats?.registered_students_estimate || 0}</span>
                </div>
                <div className="stat-card">
                    <span className="stat-title">Present Today</span>
                    <span className="stat-value">{stats?.present_today || 0}</span>
                </div>
                <div className="stat-card">
                    <span className="stat-title">Today's Attendance %</span>
                    <span className="stat-value">{stats?.today_percentage || 0}%</span>
                </div>
                <div className="stat-card">
                    <span className="stat-title">Total Records</span>
                    <span className="stat-value">{stats?.total_attendance_records || 0}</span>
                </div>
            </div>

            <div className="table-container">
                <div style={{padding: '24px', borderBottom: '1px solid #eee', fontWeight: 'bold'}}>
                    Recent System Activity
                </div>
                <div style={{padding: '24px', color: '#666'}}>
                    Navigate to the Attendance tab to view detailed history.
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
