import random


def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength


def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours


def getBestNeighbour(tsp, neighbours):
    bestRouteLength = routeLength(tsp, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength


def hillClimbing(tsp):
    cities = list(range(len(tsp)))
    random.shuffle(cities)
    currentSolution = cities
    currentRouteLength = routeLength(tsp, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    return currentSolution, currentRouteLength


def main():
    # n = int(input('Enter number of cities: '))
    # adj = []
    # print('Enter costs of travelling: ')
    # for i in range(n):
    #     m = list(map(int, input().strip().split()))
    #     adj.append(m)

    # adj = [
    #     [0, 400, 500, 300],
    #     [400, 0, 300, 500],
    #     [500, 300, 0, 400],
    #     [300, 500, 400, 0]
    # ]
    adj = [[0, 7, 9, 6, 1],
            [7, 0, 3, 4, 9],
            [9, 3, 0, 2, 5],
            [6, 4, 2, 0, 3],
            [1, 9, 5, 3, 0]]
    bestPath, bestCost = hillClimbing(adj)
    print("Best path : ", end="")
    for i in bestPath:
        print(i+1, end=" -> ")
    print(bestPath[0]+1)
    print("Cost : ", bestCost)


if __name__ == "__main__":
    main()
