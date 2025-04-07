from django.shortcuts import render,redirect
from django.db import connection
from django.shortcuts import HttpResponse



def insert_user(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        with connection.cursor() as cursor:
            cursor.callproc('InsertUser', [name, email])
        return redirect('user_list')
    return render(request, 'insert_user.html')


def user_list(request):
    with connection.cursor() as cursor:
        cursor.callproc('GetUsers')
        users = cursor.fetchall()  
    return render(request, 'user_list.html', {'users': users})



def update_user(request, user_id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        with connection.cursor() as cursor:
            cursor.callproc('UpdateUser', [user_id, name, email])
        return redirect('user_list')
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", [user_id])
        user = cursor.fetchone()

    return render(request, 'update_user.html', {'user': user})



def delete_user(request, user_id):
    with connection.cursor() as cursor:
        cursor.callproc('DeleteUser', [user_id])
    return redirect('user_list')
