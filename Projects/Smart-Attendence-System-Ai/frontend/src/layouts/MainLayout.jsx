import React from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import { LayoutDashboard, Users, CalendarCheck, Camera, BarChart3, Settings } from 'lucide-react';

const MainLayout = () => {
    return (
        <div className="app-container">
            <aside className="sidebar">
                <div className="sidebar-header">
                    Smart Attendance
                </div>
                <nav className="sidebar-nav">
                    <NavLink to="/" className={({isActive}) => isActive ? "nav-link active" : "nav-link"} end>
                        <LayoutDashboard size={20} /> Dashboard
                    </NavLink>
                    <NavLink to="/students" className={({isActive}) => isActive ? "nav-link active" : "nav-link"}>
                        <Users size={20} /> Students
                    </NavLink>
                    <NavLink to="/attendance" className={({isActive}) => isActive ? "nav-link active" : "nav-link"}>
                        <CalendarCheck size={20} /> Attendance
                    </NavLink>
                    <NavLink to="/recognition" className={({isActive}) => isActive ? "nav-link active" : "nav-link"}>
                        <Camera size={20} /> Face Recognition
                    </NavLink>
                    <NavLink to="/analytics" className={({isActive}) => isActive ? "nav-link active" : "nav-link"}>
                        <BarChart3 size={20} /> Analytics
                    </NavLink>
                    <NavLink to="/settings" className={({isActive}) => isActive ? "nav-link active" : "nav-link"}>
                        <Settings size={20} /> Settings
                    </NavLink>
                </nav>
            </aside>
            <main className="main-content">
                <Outlet />
            </main>
        </div>
    );
};

export default MainLayout;
