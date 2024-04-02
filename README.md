# NTP-server
NTP Client to Server.

*Para configurar um computador com Windows 10 como um servidor NTP, você pode seguir estas etapas:*

Configurar o Serviço de Hora do Windows:

O Windows possui um serviço embutido para sincronização de hora chamado "Windows Time Service" (W32Time). Vamos configurá-lo para agir como um servidor NTP.
Editar o Registro do Windows:
Abra o Editor de Registro do Windows. Pressione Win + R, digite regedit e pressione Enter.
Navegue até a seguinte chave do registro:
sql
Copy code
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config
Localize a entrada AnnounceFlags e defina seu valor como 5 para indicar que este servidor é um servidor NTP.
Se a entrada AnnounceFlags não existir, você pode criá-la clicando com o botão direito em um espaço vazio no lado direito da janela do Editor de Registro, selecionando "Novo" -> "Valor DWORD (32 bits)" e nomeando-o como AnnounceFlags.
Reiniciar o Serviço de Hora do Windows:
Abra o Prompt de Comando como administrador. Pressione Win + X e escolha "Prompt de Comando (Admin)".
Execute os seguintes comandos para parar e reiniciar o serviço W32Time:
arduino
Copy code
net stop w32time
net start w32time
Abrir a Porta no Firewall (opcional):
Se você estiver executando um firewall no computador, precisará abrir a porta UDP 123 para permitir que outros dispositivos na rede sincronizem com o servidor NTP do Windows 10. Você pode fazer isso nas configurações do firewall do Windows.
Verificar a Configuração:
Para verificar se o serviço está em execução e configurado corretamente, você pode usar o seguinte comando no Prompt de Comando:
bash
Copy code
w32tm /query /status
Após seguir essas etapas, seu computador com Windows 10 estará configurado como um servidor NTP e estará pronto para fornecer a hora para outros dispositivos na rede. Certifique-se de testar a configuração para garantir que esteja funcionando corretamente.
