from backend.database import conectar

def cria_cliente(id, nome, email, telefone, senha_hash, preferencias, id_tipo ):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    id_tipo = 2 
    try:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO usuarios (id, nome, senha_hash, preferencia_contato, id_tipo_usuario)
        VALUES (%s, %s, %s, %s, %s)
        """,(id, nome, senha_hash, preferencias, id_tipo))

        id_usuario = cursor.fetchone()[0]

        cursor.execute("""
        INSERT INTO dados_usuarios (id_usuario, email, telefone)
        VALUES (%s, %s, %s)
        """,(id_usuario, email, telefone))

        connection.commit()
        return id_usuario
    except Exception as e:
        print(f"Erro ao criar cliente: {e}")
        connection.rollback()
        return e

    finally:
        cursor.close()
        connection.close()


def atualiza_cliente(id, nome, email, preferencias, telefone):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        UPDATE usuarios
        SET nome = %s, preferencia_contato = %s
        WHERE id = %s
        """, (nome, preferencias, id))

        cursor.execute("""
        UPDATE dados_usuarios
        SET email = %s, telefone = %s
        WHERE id_usuario = %s
        """, (email, telefone, id))

        connection.commit()
        return True
    
    except Exception as e:
        print(f"Erro ao atualizar cliente: {e}")
        connection.rollback()
        return e

    finally:
        cursor.close()
        connection.close()


def deleta_usuario(id):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        DELETE FROM dados_usuarios
        WHERE id_usuario = %s
        """, (id,))

        cursor.execute("""
        DELETE FROM usuarios
        WHERE id = %s
        """, (id,))

        connection.commit()
        return True
    
    except Exception as e:
        print(f"Erro ao deletar cliente: {e}")
        connection.rollback()
        return e

    finally:
        cursor.close()
        connection.close()


def envia_interesse( id_interessado,id_usuario, descricao, status):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO interessados (id, id_usuario, descricao, status)
        VALUES (%s, %s, %s, %s)
        """, (id_interessado, id_usuario, descricao, status))

        connection.commit()
        return True
    
    except Exception as e:
        print(f"Erro ao adicionar interessado: {e}")
        connection.rollback()
        return e

    finally:
        cursor.close()
        connection.close()


def deleta_interesse(id_interessado):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        DELETE FROM interessados
        WHERE id = %s
        """, (id_interessado,))

        connection.commit()
        return True
    
    except Exception as e:
        print(f"Erro ao deletar interessado: {e}")
        connection.rollback()
        return e

    finally:
        cursor.close()
        connection.close()


def checa_interesse(id_interessado):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM interessados
        WHERE id = %s
        """, (id_interessado,))

        resultado = cursor.fetchone()
        return resultado is not None
    
    except Exception as e:
        print(f"Erro ao checar interessado: {e}")
        return e

    finally:
        cursor.close()
        connection.close()


def lista_interesses(id_usuario):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM interessados
        WHERE id_usuario = %s
        """, (id_usuario,))

        resultado = cursor.fetchall()
        return resultado
    
    except Exception as e:
        print(f"Erro ao listar interesses: {e}")
        return e

    finally:
        cursor.close()
        connection.close()