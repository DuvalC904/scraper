class AccessControl:
    def __init__(self):
        # Initialize role-based access control with default users and their roles
        self.roles = {'admin': [], 'analyst': [], 'viewer': []}
        self.permissions = {
            'admin': ['read', 'write', 'execute'],
            'analyst': ['read', 'write'],
            'viewer': ['read']
        }

    def add_user(self, username, role):
        if role in self.roles:
            self.roles[role].append(username)
        else:
            raise ValueError('Invalid role')

    def remove_user(self, username):
        for role in self.roles:
            if username in self.roles[role]:
                self.roles[role].remove(username)
                return
        raise ValueError('User not found')

    def check_permission(self, username, action):
        for role, users in self.roles.items():
            if username in users:
                if action in self.permissions[role]:
                    return True
        return False

# Example Usage:
# access_control = AccessControl()
# access_control.add_user('john_doe', 'analyst')
# has_access = access_control.check_permission('john_doe', 'write')
# print(has_access)  # Should print True if the user has permission
