from logger_base import log
from cursor_del_pool import CursorDelPool
from usuario import Usuario

class UsuarioDAO:
    """
    DAO (Data Access Object)
    CRUD (CREATE, READ, UPDATE, DELETE)
    """
    _SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuarios (username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuarios SET username = %s, password = %s WHERE id_usuario = %s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario creado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    # usuario1 = Usuario(username="matias225", password="1234")
    # usuarios_insertados = UsuarioDAO.insertar(usuario1)
    # log.debug(f'Usuarios insertados: {usuarios_insertados}')

    # Actualizar un registro
    # usuario1 = Usuario(5, 'matias22', '123456')
    # usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
    # log.debug(f'Usuarios actualizados: {usuarios_actualizados}')

    # Eliminar un registro
    # usuario1 = Usuario(id_usuario=5)
    # usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
    # log.debug(f'Usuarios eliminados: {usuarios_eliminados}')

    # Mostrar todos los registros
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
