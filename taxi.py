import json
import sys
import argparse


class BDError(Exception):
    pass


class BD:
    def __init__(self, file='taxi.json'):
        self.file = file
        if not self.get():
            self.push({'orders': {}, 'drivers': {}})

    def push(self, d):
        try:
            with open(self.file, 'w') as f:
                d = json.dumps(d, indent=2)
                f.write(d)
        except FileNotFoundError:
            assert BDError()

    def get(self):
        try:
            with open(self.file, 'r') as f:
                d = json.loads(f.read())
            return d
        except FileNotFoundError:
            return


class Taxi:
    def __init__(self):
        self.bd = BD()

    def add_driver(self, args):
        if args.speed > 0:
            taxi = self.bd.get()
            if taxi['drivers']:
                id_ = max(map(int, taxi['drivers'].keys())) + 1
            else:
                id_ = 0
            taxi['drivers'].setdefault(id_, {'name': args.name,
                                             'pos': args.pos,
                                             'car': args.car,
                                             'speed': args.speed,
                                             'occupied': 0})
            self.bd.push(taxi)
        else:
            print('speed mush be positive')

    def new_order(self, args):
        from_pos = args.from_pos
        to = args.to

        def get_driver(from_pos):
            drivers = self.bd.get()['drivers']
            time = lambda driver, from_pos: abs(from_pos - driver['pos']) / driver['speed']
            drivers_times = {time(driver, from_pos): id
                             for id, driver in drivers.items() if not driver['occupied']}
            if drivers_times:
                id_ = drivers_times[min(drivers_times.keys())]
            else:
                return None, None, None
            return id_, time(drivers[id_], from_pos), drivers[id_]

        taxi = self.bd.get()
        if taxi['orders']:
            id_ = max(map(int, taxi['orders'].keys())) + 1
        else:
            id_ = 0

        driver_id, time, driver = get_driver(args.from_pos)

        if driver_id:
            driver_name = taxi['drivers'].get(driver_id)['name']
            taxi['orders'].setdefault(id_, {'from': from_pos,
                                            'to': to,
                                            'driver': driver_id,
                                            'status': 'in_progress'})

            taxi['drivers'][driver_id]['occupied'] = 1
            print(f'Driver {driver_name} will come in {round(time, 2)} hours (order-id: {id_})')
        else:
            taxi['orders'].setdefault(id_, {'from': from_pos,
                                            'to': to,
                                            'driver': None,
                                            'status': 'declined'})

            print('All drivers are occupied')

        self.bd.push(taxi)

    def finish(self, args):
        order_id = str(args.order_id)
        taxi = self.bd.get()
        order = taxi['orders'].get(str(order_id))
        if order:
            driver_id = order['driver']
            if order['status'] == 'in_progress':
                order['status'] = 'finished'
                driver = taxi['drivers'][driver_id]
                driver['pos'] = order['to']
                driver['occupied'] = 0
                distance = abs(order['from'] - order['to'])
                time = distance / driver['speed']
                price = (300 * time) + (5 * distance)

                print(f'price : {price}')

            else:
                print('this order will be declined or finished')
        else:
            print('order not exist')
        self.bd.push(taxi)


def main(args):
    taxi = Taxi()
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()
    add_driver = subparser.add_parser('add-driver')
    add_driver.add_argument('name')
    add_driver.add_argument('pos', type=int)
    add_driver.add_argument('car')
    add_driver.add_argument('speed', type=int)
    add_driver.set_defaults(func=taxi.add_driver)

    order = subparser.add_parser('order')
    order.add_argument('from_pos', type=int)
    order.add_argument('to', type=int)
    order.set_defaults(func=taxi.new_order)

    finish = subparser.add_parser('finish')
    finish.add_argument('order_id', type=int)
    finish.set_defaults(func=taxi.finish)

    cmd = parser.parse_args(args)
    if cmd:
        cmd.func(cmd)


if __name__ == '__main__':
    main(sys.argv[1:])
