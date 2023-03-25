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
        reachable = set()
        unreachable = set()

        for ip_addr in hosts:
            if isinstance(ip_addr, (str, bytes, bytearray)):
                ip_addr = self.translate(ip_addr)
            response = os.system(f"ping -n 1 {ip_addr} > ping.log")
            if response == 0:
                reachable.add(ip_addr)
            else:
                unreachable.add(ip_addr)

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
        hosts = [ip_addr + i for i in range(stop - start)]
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
    hosts = ['192.168.1.1', '192.168.1.3', 'yandex.ru', 'google.com']
    ping = Ping()
    ping.host_ping(hosts)
    ping.host_range_ping('5.255.255.70', '5.255.255.73')
    ping.host_range_ping_tab('5.255.255.70', '5.255.255.73')
