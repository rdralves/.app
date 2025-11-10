from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app import db
from app.models.veiculos import Veiculo
from app.models.alerta import Alerta


def verificar_alertas(app):
    with app.app_context():  # 👈 Aqui garantimos o contexto Flask
        print("[Scheduler] Verificando alertas...")
        hoje = datetime.utcnow().date()

        veiculos = Veiculo.query.all()
        for v in veiculos:
            if v.kilometragem > 10000 and not v.status == "EM MANUTENÇÃO":
                existe = Alerta.query.filter_by(
                    titulo=f"Revisão de {v.placa}", resolvido=False
                ).first()

                if not existe:
                    alerta = Alerta(
                        titulo=f"Revisão de {v.placa}",
                        descricao=f"O veículo {v.modelo} ({v.placa}) atingiu {v.kilometragem} km. Agendar revisão.",
                        tipo="MANUTENÇÃO"
                    )
                    db.session.add(alerta)
                    print(f"✅ Alerta criado: {alerta.titulo}")

        db.session.commit()
        print("[Scheduler] Verificação concluída!\n")


def iniciar_scheduler(app):
    scheduler = BackgroundScheduler()
    # 👇 Passa o app como argumento para o job
    scheduler.add_job(func=lambda: verificar_alertas(app),
                      trigger="interval", minutes=1)
    scheduler.start()
    print("✅ Scheduler de alertas iniciado!")
