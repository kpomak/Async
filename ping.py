"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
Reachable
10.0.0.1
10.0.0.2

Unreachable
10.0.0.3
10.0.0.4
"""
from ipaddress import ip_address
import os
from socket import gethostbyname


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
            response = os.system(f"ping -n 1 {ip_addr} > null")
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
        self.host_ping(hosts, output=output)


if __name__ == '__main__':
    hosts = ['192.168.1.1', '192.168.1.3', 'yandex.ru', 'google.com']
    ping = Ping()
    # ping.host_ping(hosts)
    # ping.host_range_ping('192.168.1.1', '192.168.1.3')
    # ipv4 = ip_address('192.168.1.2')
    # print(ipv4.is_loopback)
    # print(ipv4.is_multicast)
    # print(ipv4.is_reserved)
    # print(ipv4.is_private)
