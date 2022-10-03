
class LogMixes:
    @staticmethod
    def escrever_log(msg):
        with open('modulo_4/heranca_multipla/log.log', 'a+') as file:
            file.write(msg)
            file.write('\n')
            
    def log_error(self, msg):
        self.escrever_log(f'ERROR: {msg}')
    
    def log_info(self, msg):
        self.escrever_log(f'INFO: {msg}')