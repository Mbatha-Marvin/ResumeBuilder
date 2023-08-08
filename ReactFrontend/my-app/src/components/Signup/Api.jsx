import { useState, useEffect } from 'react';
import axios from 'axios';

const Api = () => {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        try {
            const response = await axios.get('http://localhost:5000/users');
            setUsers(response.data);
        } catch (error) {
            console.error('Error fetching users:', error.message);
        }
    };

    return (
<div>
            <h2>User List</h2>
            <ul>
                {users.map((user) => (
                    <li key="{user.id}">
                        Username: {user.username}, Email: {user.email}, Password: {user.password}
                    </li>
                ))}
            </ul>
        </div>
    );
};


export default Api;