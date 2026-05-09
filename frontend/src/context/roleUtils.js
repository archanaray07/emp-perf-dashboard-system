export const roleRedirect = (role) => {
    switch(role) {
        case 'hr':
            return '/hr-dashboard';
        case 'manager':
            return '/manager-dashboard';
        case 'employee':
            return '/employee-dashboard';
        default:
            return '/login';
    }
};