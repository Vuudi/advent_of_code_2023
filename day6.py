if __name__ == '__main__':
    times = [48876981]
    distances = [255128811171623]
    product = 1
    for time, distance in zip(times, distances):
        waysToWin = 0
        for velocity in range(time):
            traveled = velocity * (time - velocity)
            if traveled > distance:
                waysToWin += 1
        product *= waysToWin
    print(product)
