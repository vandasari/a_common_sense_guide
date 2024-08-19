"""
Dijkstra's Algorithm for The Shortest (Cheapest) Path Problem

Algorithm: page 377--379
Time complexity: O(v^2)

Use Dijkstra's algorithm with array to find the cheapest path in a city flights example.
"""


class City:
    def __init__(self, name):
        self.name = name
        self.routes = {}

    def add_route(self, city, price):
        self.routes[city] = price

    def dijkstra_shortest_path(self, starting_city, final_destination):
        cheapest_prices = {}
        cheapest_previous_stopover_city = {}

        unvisited_cities = []

        visited_cities = {}

        cheapest_prices[starting_city.name] = 0

        current_city = starting_city

        # Run the loop as long as we can visit a city that we haven't visited yet:
        while current_city:

            visited_cities[current_city.name] = True

            if unvisited_cities != []:
                unvisited_cities.remove(current_city)

            for adjacent_city, price in current_city.routes.items():
                if adjacent_city.name not in visited_cities:
                    visited_cities[adjacent_city.name] = True
                    unvisited_cities.append(adjacent_city)

                price_through_current_city = cheapest_prices[current_city.name] + price

                if (
                    adjacent_city.name not in cheapest_prices
                    or price_through_current_city < cheapest_prices[adjacent_city.name]
                ):
                    cheapest_prices[adjacent_city.name] = price_through_current_city
                    cheapest_previous_stopover_city[adjacent_city.name] = (
                        current_city.name
                    )

            if len(unvisited_cities) > 0:
                current_city = unvisited_cities[min(cheapest_prices.values())]
            else:
                break

        shortest_path = []

        current_city_name = final_destination.name

        while current_city_name != starting_city.name:
            shortest_path.append(current_city_name)
            current_city_name = cheapest_previous_stopover_city[current_city_name]

        shortest_path.append(starting_city.name)

        return shortest_path[::-1]

    def dijkstra_shortest_path_steps(self, starting_city, final_destination):
        print(f"starting_city = {starting_city.name}")
        cheapest_prices = {}
        cheapest_previous_stopover_city = {}

        unvisited_cities = []

        visited_cities = {}

        cheapest_prices[starting_city.name] = 0
        print(f"cheapest_prices = {cheapest_prices}")

        current_city = starting_city
        print(f"current_city = {current_city.name}")

        # Run the loop as long as we can visit a city that we haven't visited yet:
        while current_city:

            visited_cities[current_city.name] = True
            print(f"visited_cities = {visited_cities}")

            if unvisited_cities != []:
                unvisited_cities.remove(current_city)
            print(f"unvisited_cities = {[i.name for i in unvisited_cities]}")

            print(f"current_city.routes = {[i.name for i in current_city.routes]}")

            for adjacent_city, price in current_city.routes.items():
                print(f"adjacent_city = {adjacent_city.name}, price = {price}")
                if adjacent_city.name not in visited_cities:
                    print(f"{adjacent_city.name} is not in visited_cities")
                    visited_cities[adjacent_city.name] = True
                    unvisited_cities.append(adjacent_city)
                    print(f"visited_cities = {visited_cities}")
                    print(f"unvisited_cities = {[i.name for i in unvisited_cities]}")

                price_through_current_city = cheapest_prices[current_city.name] + price
                print(f"price_through_current_city = {price_through_current_city}")

                if (
                    adjacent_city.name not in cheapest_prices
                    or price_through_current_city < cheapest_prices[adjacent_city.name]
                ):
                    cheapest_prices[adjacent_city.name] = price_through_current_city
                    cheapest_previous_stopover_city[adjacent_city.name] = (
                        current_city.name
                    )

                print(f"cheapest_prices = {cheapest_prices}")
                print(
                    f"cheapest_previous_stopover_city = {cheapest_previous_stopover_city}"
                )

            if len(unvisited_cities) > 0:
                current_city = unvisited_cities[min(cheapest_prices.values())]
                print(f"current_city = {current_city.name}")
            else:
                break

        shortest_path = []

        current_city_name = final_destination.name
        print(f"current_city_name = {current_city_name} - before looping")

        while current_city_name != starting_city.name:
            print(
                f"{current_city_name} != {starting_city.name} = {current_city_name != starting_city.name}"
            )
            shortest_path.append(current_city_name)
            print(f"shortest_path = {shortest_path}")
            current_city_name = cheapest_previous_stopover_city[current_city_name]
            print(f"current_city_name = {current_city_name}")

        shortest_path.append(starting_city.name)

        print(f"final shortest_path = {shortest_path[::-1]}")

        return shortest_path[::-1]


if __name__ == "__main__":
    atlanta = City("Atlanta")
    boston = City("Boston")
    chicago = City("Chicago")
    denver = City("Denver")
    el_paso = City("El Paso")

    atlanta.add_route(boston, 100)
    atlanta.add_route(denver, 160)
    boston.add_route(chicago, 120)
    boston.add_route(denver, 180)
    chicago.add_route(el_paso, 80)
    denver.add_route(chicago, 40)
    denver.add_route(el_paso, 140)
    el_paso.add_route(boston, 100)

    # --- To show only the result ---#
    res = atlanta.dijkstra_shortest_path(atlanta, el_paso)
    print(res)

    # --- To print/display step-by-step search process: ---#
    # atlanta.dijkstra_shortest_path_steps(atlanta, el_paso)

"""
Returns:
    
['Atlanta', 'Denver', 'Chicago', 'El Paso']
"""
