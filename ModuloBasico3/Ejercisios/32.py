class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

class Cita:
    def __init__(self, paciente, doctor, fecha):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha

paciente = Paciente("Ana")
doctor = Doctor("Dr. Pérez", "Cardiólogo")
cita = Cita(paciente, doctor, "2025-09-25")
print(f"{cita.paciente.nombre} tiene cita con {cita.doctor.nombre} ({cita.doctor.especialidad}) el {cita.fecha}")