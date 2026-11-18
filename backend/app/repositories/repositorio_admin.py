from database import conectar

def cadastra_admin(id, nome, email, telefone, senha_hash, preferencias):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    id_tipo = 1  # Tipo de usuário para admin
    try:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO usuarios (id, nome, senha_hash, preferencia_contato, id_tipo_usuario)
        VALUES (%s, %s, %s, %s, %s)
        """, (id, nome, senha_hash, preferencias, id_tipo))

        id_usuario = cursor.fetchone()[0]

        cursor.execute("""
        INSERT INTO dados_usuarios (id_usuario, email, telefone)
        VALUES (%s, %s, %s)
        """, (id_usuario, email, telefone))

        connection.commit()
        return id_usuario
    except Exception as e:
        print(f"Erro ao cadastrar admin: {e}")
        connection.rollback()
        return e

    finally:
        cursor.close()
        connection.close()


def atualiza_admin(id, nome, email, preferencias, telefone):
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
        print(f"Erro ao atualizar admin: {e}")
        connection.rollback()
        return e

    finally:
        cursor.close()
        connection.close()


def deleta_admin(id):
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
        print(f"Erro ao deletar admin: {e}")
        connection.rollback()
        return e

    finally:
        cursor.close()
        connection.close()


def lista_admins():
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT u.id, u.nome, d.email, d.telefone, u.preferencia_contato
        FROM usuarios u
        JOIN dados_usuarios d ON u.id = d.id_usuario
        WHERE u.id_tipo_usuario = 1
        """)

        resultado = cursor.fetchall()
        return resultado
    
    except Exception as e:
        print(f"Erro ao listar admins: {e}")
        return e

    finally:
        cursor.close()
        connection.close()


def lista_interessados():
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM interessados
        """)

        resultado = cursor.fetchall()
        return resultado
    
    except Exception as e:
        print(f"Erro ao listar interessados: {e}")
        return e

    finally:
        cursor.close()
        connection.close()


def lista_atendimentos():
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM atendimento
        """)

        resultado = cursor.fetchall()
        return resultado
    
    except Exception as e:
        print(f"Erro ao listar atendimentos: {e}")
        return e

    finally:
        cursor.close()
        connection.close()


def atualiza_interesse(id, id_interessado, id_usuario, status_atendimento, resultado):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO atendimento (id, id_adm, id_interessado, status_atendimento, resultado)
        VALUES (%s, %s, %s, %s, %s)
        """, (id, id_usuario, id_interessado, status_atendimento, resultado))

        id_atendimento = cursor.fetchone()[0]

        connection.commit()
        return id_atendimento
    
    except Exception as e:
        print(f"Erro ao atualizar interesse: {e}")
        connection.rollback()
        return e

    finally:
        cursor.close()
        connection.close()


def busca_interesse_por_nome(nome):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM interessados
        WHERE nome = %s
        """, (nome,))

        resultado = cursor.fetchall()
        return resultado
    
    except Exception as e:
        print(f"Erro ao buscar interessado por nome: {e}")
        return e

    finally:
        cursor.close()
        connection.close()


def busca_interessados_por_id(id_usuario):
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

        resultado = cursor.fetchone()
        return resultado
    
    except Exception as e:
        print(f"Erro ao buscar interessado: {e}")
        return e

    finally:
        cursor.close()
        connection.close()


def busca_atendimentos_por_status(status):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM atendimento
        WHERE status_atendimento = %s
        """, (status,))

        resultado = cursor.fetchall()
        return resultado
    
    except Exception as e:
        print(f"Erro ao buscar atendimentos por status: {e}")
        return e

    finally:
        cursor.close()
        connection.close()


def busca_atendimentos_por_id_e_status(id_usuario, status):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM atendimento   
        WHERE id_usuario = %s AND status = %s
        """, (id_usuario, status))

        resultado = cursor.fetchall()
        return resultado
    
    except Exception as e:
        print(f"Erro ao buscar atendimentos por id e status: {e}")
        return e

    finally:
        cursor.close()
        connection.close()


def busca_atendimentos_idAdm(id_adm):
    connection = conectar()

    if connection is None:
        return None

    cursor = None
    try:
        cursor = connection.cursor()
        cursor.execute("""
        SELECT * FROM atendimento
        WHERE id_adm = %s
        """, (id_adm,))

        resultado = cursor.fetchall()
        return resultado
    
    except Exception as e:
        print(f"Erro ao buscar atendimentos por id do admin: {e}")
        return e

    finally:
        cursor.close()
        connection.close()