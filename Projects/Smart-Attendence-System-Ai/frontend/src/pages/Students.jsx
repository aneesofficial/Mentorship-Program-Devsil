import React, { useEffect, useState } from 'react';
import { getStudents } from '../services/api';

const Students = () => {
    const [students, setStudents] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        getStudents()
            .then(res => {
                if (res.data.status === 'success') {
                    setStudents(res.data.data);
                }
            })
            .catch(err => console.error(err))
            .finally(() => setLoading(false));
    }, []);

    if (loading) return <div className="loading">Loading students...</div>;

    return (
        <div>
            <div className="page-header">
                <h1 className="page-title">Registered Students</h1>
                <p>List of all students known to the face recognition model.</p>
            </div>

            <div className="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Student ID</th>
                            <th>Name</th>
                            <th>Total Present Days</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {students.length > 0 ? (
                            students.map((student, idx) => (
                                <tr key={idx}>
                                    <td>{student.id}</td>
                                    <td>{student.name}</td>
                                    <td>{student.present_days}</td>
                                    <td><span className="badge present">Active</span></td>
                                </tr>
                            ))
                        ) : (
                            <tr>
                                <td colSpan="4" style={{textAlign: 'center', color: '#666'}}>
                                    No students found. Check your model encodings.
                                </td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default Students;
