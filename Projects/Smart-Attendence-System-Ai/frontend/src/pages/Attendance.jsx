import React, { useEffect, useState } from 'react';
import { getAttendance } from '../services/api';

const Attendance = () => {
    const [records, setRecords] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState('');

    useEffect(() => {
        getAttendance()
            .then(res => {
                if (res.data.status === 'success') {
                    // Reverse to show latest first
                    setRecords(res.data.data.reverse());
                }
            })
            .catch(err => console.error(err))
            .finally(() => setLoading(false));
    }, []);

    const filteredRecords = records.filter(record => 
        record.Name?.toLowerCase().includes(searchTerm.toLowerCase()) || 
        record.Date?.includes(searchTerm)
    );

    return (
        <div>
            <div className="page-header" style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
                <div>
                    <h1 className="page-title">Attendance History</h1>
                    <p>Complete logs of all marked attendances.</p>
                </div>
                <div>
                    <input 
                        type="text" 
                        placeholder="Search name or date..." 
                        style={{padding: '10px 16px', borderRadius: '4px', border: '1px solid #ccc', minWidth: '250px'}}
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                    />
                </div>
            </div>

            {loading ? (
                <div className="loading">Loading records...</div>
            ) : (
                <div className="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Date</th>
                                <th>Time</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filteredRecords.length > 0 ? (
                                filteredRecords.map((r, i) => (
                                    <tr key={i}>
                                        <td><strong>{r.Name}</strong></td>
                                        <td>{r.Date}</td>
                                        <td>{r.Time}</td>
                                        <td><span className="badge present">{r.Status}</span></td>
                                    </tr>
                                ))
                            ) : (
                                <tr>
                                    <td colSpan="4" style={{textAlign: 'center', color: '#666'}}>
                                        No records found.
                                    </td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
};

export default Attendance;
