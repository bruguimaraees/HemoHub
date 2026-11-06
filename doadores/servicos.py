from django.db import transaction

from usuarios.models import Usuario

from .models import Doador


def criar_doador(dados):
    with transaction.atomic():
        usuario = Usuario.objects.create_user(
            username=dados['username'],
            email=dados['email'],
            password=dados['password1'],
            tipo_usuario=Usuario.TipoUsuario.DOADOR,
        )
        doador = Doador.objects.create(
            usuario=usuario,
            nome_completo=dados['nome_completo'],
            cpf=dados['cpf'],
            data_nascimento=dados['data_nascimento'],
            sexo=dados['sexo'],
            tipo_sanguineo=dados['tipo_sanguineo'],
            telefone=dados['telefone'],
            logradouro=dados['logradouro'],
            numero=dados['numero'],
            bairro=dados['bairro'],
            cidade=dados['cidade'],
            estado=dados['estado'],
            cep=dados['cep'],
        )
    return doador
