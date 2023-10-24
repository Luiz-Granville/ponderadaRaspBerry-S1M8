import machine

# Configuração do barramento SPI e pino de chip select
spi = machine.SPI(0)
cs = machine.Pin(15, machine.Pin.OUT)

# Cria uma instância da classe MCP3008
adc = MCP3008(spi, cs)

# Lê a voltagem do pino 0 do MCP3008
valor_analogico = adc.ler(0)

print(f"Valor analógico lido: {valor_analogico}")
