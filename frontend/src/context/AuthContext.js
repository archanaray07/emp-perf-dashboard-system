import React, { createContext, useState, useEffect } from "react";
import API from '../api/axiosConfig';
import { jwtDecode } from 'jwt-decode';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const token = localStorage.getItem('access_token');

        if(token){
            try {
                const decodedUser = jwtDecode(token);
                setUser(decodedUser);
            } catch (error) {
                logout();
            }
        }

        setLoading(false);
    }, []);

    const login = async(username, password) => {
        const response = await API.post('accounts/login/', {
            username,
            password,
        });

        const { access, refresh } = response.data;

        localStorage.setItem('access_token', access);
        localStorage.setItem('refresh_token', refresh);

        const decodedUser = jwtDecode(access);
        setUser(decodedUser);

        return decodedUser;
    };

    const register = async(formdata) => {
        return await API.post('accounts/register/', formdata);
    };

    const logout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        setUser(null);
    };

    const isAuthenticated = () => {
        return !!localStorage.getItem('access_token');
    };

    const getUserRole = () => {
        return user?.role || null;
    };

    return(
        <AuthContext.Provider
            value={{
                user,
                login,
                register,
                logout,
                isAuthenticated,
                getUserRole,
            }}
        >
            {!loading && children}
        </AuthContext.Provider>
    );

};