class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = [(p, s) for p, s in zip(position, speed)]
        paired.sort(reverse = True)

        fleets = 1
        prevCar = (target - paired[0][0]) / paired[0][1]
        for i in range(1, len(paired)):
            currCar = (target - paired[i][0]) / paired[i][1]
            if currCar > prevCar:
                fleets += 1
                prevCar = currCar
        return fleets