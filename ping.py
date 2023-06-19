import os
from ipaddress import ip_address
from socket import gethostbyname

from tabulate import tabulate


class Ping:
    def translate(self, host):
        return ip_address(gethostbyname(host))

    def host_ping(self, hosts, output=True):
        """
        Метод, в котором с помощью утилиты ping проверяется доступность сетевых узлов.
        Аргументом метода является список, в котором каждый сетевой узел должен быть
        представлен именем хоста или ip-адресом. В методе перебираются ip-адреса
        и проверяется их доступность с выводом соответствующего сообщения
        («Узел доступен», «Узел недоступен»).

        При этом ip-адрес сетевого узлa создаваться с помощью функции ip_address()
        """
        reachable = []
        unreachable = []

        for ip_addr in hosts:
            if isinstance(ip_addr, (str, bytes, bytearray)):
                ip_addr = self.translate(ip_addr)
            response = os.system(f"ping -n 1 {ip_addr} > ping.log")
            if response == 0:
                reachable.append(ip_addr)
            else:
                unreachable.append(ip_addr)

        if output:
            for addr in reachable:
                print(f"{addr} Узел доступен")
            for addr in unreachable:
                print(f"{addr} Узел недоступен")

        return {'reachable': reachable, 'unreachable': unreachable}

    def host_range_ping(self, start_ip, stop_ip, output=True):
        """
        Метод для перебора ip-адресов из заданного диапазона. Меняться может только
        последний октет каждого адреса. По результатам проверки должно выводиться
        соответствующее сообщение.

        """
        start, stop = map(lambda x: int(
            self.translate(x)), (start_ip, stop_ip))

        if (stop - start) + start % 256 > 255:
            print('Меняется только последний октет')
            return

        ip_addr = self.translate(start_ip)
        hosts = [ip_addr + i for i in range(stop - start + 1)]
        return self.host_ping(hosts, output=output)

    def host_range_ping_tab(self, start_ip, stop_ip):
        """
        Результат выполнения host_range_ping() представляет в табличном формате.
        Таблица состоит из двух Reachable, Unreachable:
        """
        print(tabulate(
            self.host_range_ping(start_ip, stop_ip, output=False),
            headers='keys',
            tablefmt="pipe",
            stralign="center",
        ))


if __name__ == '__main__':
    hosts = ['192.168.1.1', '192.168.0.3', 'yandex.ru', 'google.com']
    ping = Ping()

    # Задача 1
    ping.host_ping(hosts)
    """
    192.168.1.1 Узел доступен
    192.168.0.3 Узел недоступен
    5.255.255.70 Узел доступен
    216.58.207.206 Узел доступен
    """

    # Задача 2
    ping.host_range_ping('5.255.255.70', '5.255.255.80')
    """
    5.255.255.70 Узел доступен
    5.255.255.77 Узел доступен
    5.255.255.80 Узел доступен
    5.255.255.71 Узел недоступен
    5.255.255.72 Узел недоступен
    5.255.255.73 Узел недоступен
    5.255.255.74 Узел недоступен
    5.255.255.75 Узел недоступен
    5.255.255.76 Узел недоступен
    5.255.255.78 Узел недоступен
    5.255.255.79 Узел недоступен
    """

    # Задача 3
    ping.host_range_ping_tab('5.255.255.70', '5.255.255.80')
    """
    |  reachable   |  unreachable  |
    |:------------:|:-------------:|
    | 5.255.255.70 | 5.255.255.71  |
    | 5.255.255.77 | 5.255.255.72  |
    | 5.255.255.80 | 5.255.255.73  |
    |              | 5.255.255.74  |
    |              | 5.255.255.75  |
    |              | 5.255.255.76  |
    |              | 5.255.255.78  |
    |              | 5.255.255.79  |
    """
