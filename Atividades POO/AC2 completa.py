# implementação de uma classe que modela uma conta em um banco.

class Conta:

	def __init__(self, titular, agencia, numero, saldo_inicial):
		self.__titular = titular
		self.__agencia = agencia
		self.__numero = numero
		self.__saldo = saldo_inicial
		self.__ativa = False
		self.__operacoes = [('saldo inicial', saldo_inicial)]


	@property
	def titular(self):
		return self.__titular


	@property
	def agencia(self):
		return self.__agencia


	@property
	def numero(self):
		return self.__numero


	@property
	def saldo(self):
		return self.__saldo


	@property
	def ativa(self):
		return self.__ativa


	@ativa.setter
	def ativa(self, situacao):
		if isinstance(situacao, bool):
			self.__ativa = situacao


	def depositar(self, valor):
		if self.__ativa == True and valor > 0:
			self.__saldo += valor
			self.__operacoes += [('deposito', valor)]


	def sacar(self, valor):
		if self.__ativa == True and valor > 0 and self.__saldo >= valor:
			self.__saldo -= valor
			self.__operacoes += [('saque', valor)]


	def transferir(self, conta_destino, valor):
		if conta_destino.ativa == True and self.__ativa == True and valor > 0 and self.__saldo >= valor:
			self.__saldo -= valor
			conta_destino.__saldo += valor
			self.__operacoes += [('transferencia', valor)]


	def tirar_extrato(self):
		return self.__operacoes