from backend.database import conectar


def realiza_login(email, senha_hash):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT u.id, u.nome, u.preferencia_contato, u.id_tipo_usuario
        FROM usuarios u
        JOIN dados_usuarios d ON u.id = d.id_usuario
        WHERE d.email = %s AND u.senha_hash = %s
        """, (email, senha_hash))

        resultado = cursor.fetchone()
        return resultado
    
    except Exception as e:
        print(f"Erro ao realizar login: {e}")
        return e

    finally:
        cursor.close()
        connection.close()


def verifica_email_existente(email):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT COUNT(*)
        FROM dados_usuarios
        WHERE email = %s
        """, (email,))

        resultado = cursor.fetchone()[0]
        return resultado > 0
    
    except Exception as e:
        print(f"Erro ao verificar email existente: {e}")
        return e

    finally:
        cursor.close()
        connection.close()


        