from usuario import Usuario
from usuario_dao import UsuarioDAO

opcion = None

while opcion != 5:
    print('''----- Opciones -----
1. Listar usuarios
2. Agregar usuario
3. Editar usuario
4. Eliminar usuario
5. Salir''')
    opcion = int(input('Escribe tu opción (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        print('\nUsuarios:')
        for usuario in usuarios:
            print(usuario)
        print()
    elif opcion == 2:
        nombre = input('Ingrese el nombre de usuario: ')
        password = input('Ingrese el password: ')
        usuario = Usuario(username=nombre, password=password)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        print(f'Usuarios insertados: {usuarios_insertados}\n')
    elif opcion == 3:
        id_usuario_var = int(input('Ingrese el id del usuario a modificar: '))
        nombre = input('Ingrese el nuevo nombre de usuario: ')
        password = input('Ingrese el nuevo password: ')
        usuario = Usuario(id_usuario_var,nombre, password)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        print(f'Usuarios actualizados: {usuarios_actualizados}\n')
    elif opcion == 4:
        id_usuario_var = int(input('Ingrese el id del usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        print(f'Usuarios eliminados: {usuarios_eliminados}\n')
else:
    print('Saliendo de la aplicación...')
