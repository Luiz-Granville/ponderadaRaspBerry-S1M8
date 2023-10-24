import machine  

class MCP3008:

    def __init__(self, spi, cs, ref_volt=3.3):
        """Cria uma instância do MCP3008."""

        self.cs = cs
        self.cs.value(1)  # ncs on
        self._spi = spi
        self._out_buffer = bytearray(3)
        self._out_buffer[0] = 0x01
        self._in_buffer = bytearray(3)
        self._ref_volt = ref_volt

    def tensao_referencia(self) -> float:
        """Retorna a tensão de referência do MCP3008 como um valor float."""
        return self._ref_volt

    def ler(self, pino, e_diferencial=False):
        """Lê uma voltagem ou diferença de voltagem usando o MCP3008."""

        self.cs.value(0)  # select
        self._out_buffer[1] = ((not e_diferencial) << 7) | (pino << 4)
        self._spi.write_readinto(self._out_buffer, self._in_buffer)
        self.cs.value(1)  # turn off
        return ((self._in_buffer[1] & 0x03) << 8) | self._in_buffer[2]
