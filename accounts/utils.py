
def detectUser(user):
    if user.role == 1:
        redirect_url = 'vendor-dashboard'
    elif user.role == 2:
        redirect_url = 'cust-dashboard'
    elif user.role == None and user.is_superadmin:
        redirect_url = 'admin:index'
    return redirect_url