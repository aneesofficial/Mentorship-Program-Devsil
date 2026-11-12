import React, { useEffect, useState } from 'react';
import { getSystemStatus } from '../services/api';

const Settings = () => {
    const [status, setStatus] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        getSystemStatus()
            .then(res => {
                if (res.data.status === 'success') {
                    setStatus(res.data.data);
                }
            })
            .catch(err => console.error(err))
            .finally(() => setLoading(false));
    }, []);

    if (loading) return <div className="loading">Checking system status...</div>;

    return (
        <div>
            <div className="page-header">
                <h1 className="page-title">System Settings & Status</h1>
                <p>Diagnostic information about the backend and model connectivity.</p>
            </div>

            <div className="table-container" style={{maxWidth: '800px'}}>
                <div style={{padding: '24px', borderBottom: '1px solid #eee'}}>
                    <h3 style={{marginBottom: '16px', color: '#1a237e'}}>Connection Status</h3>
                    
                    <div style={{display: 'flex', justifyContent: 'space-between', marginBottom: '12px'}}>
                        <span>Backend API</span>
                        <span className="badge present">{status?.backend || 'Offline'}</span>
                    </div>
                    
                    <div style={{display: 'flex', justifyContent: 'space-between', marginBottom: '12px'}}>
                        <span>Model File Found</span>
                        <span className={status?.model_file_found ? "badge present" : "badge"} style={!status?.model_file_found ? {background: '#fee2e2', color: '#991b1b'} : {}}>
                            {status?.model_file_found ? 'Yes' : 'No'}
                        </span>
                    </div>

                    <div style={{display: 'flex', justifyContent: 'space-between', marginBottom: '12px'}}>
                        <span>Model Loaded in Memory</span>
                        <span className={status?.model_loaded_in_memory ? "badge present" : "badge"} style={!status?.model_loaded_in_memory ? {background: '#fee2e2', color: '#991b1b'} : {}}>
                            {status?.model_loaded_in_memory ? 'Yes' : 'No'}
                        </span>
                    </div>
                    
                    <div style={{display: 'flex', justifyContent: 'space-between', marginBottom: '12px'}}>
                        <span>Attendance CSV File</span>
                        <span className={status?.attendance_file_found ? "badge present" : "badge"} style={!status?.attendance_file_found ? {background: '#fee2e2', color: '#991b1b'} : {}}>
                            {status?.attendance_file_found ? 'Yes' : 'No'}
                        </span>
                    </div>
                </div>

                <div style={{padding: '24px', background: '#f8fafc'}}>
                    <h3 style={{marginBottom: '16px', color: '#1a237e'}}>Configured Paths</h3>
                    <div style={{marginBottom: '12px'}}>
                        <strong>Model Path:</strong> <code style={{background: '#eee', padding: '2px 6px', borderRadius: '4px'}}>{status?.model_path}</code>
                    </div>
                    <div>
                        <strong>Attendance Data:</strong> <code style={{background: '#eee', padding: '2px 6px', borderRadius: '4px'}}>{status?.attendance_path}</code>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Settings;
