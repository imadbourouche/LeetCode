var memo map[int]int
var N int

func recv(current int) int{
    val, ok := memo[current]

    if ok {
        return val
    } else {
        if current == N {
            return 1
        }

        if current > N {
            return 0
        }
        res := recv(current + 1) + recv(current + 2)
        memo[current] = res
        return res
    }
}

func climbStairs(n int) int {
    memo = make(map[int]int)
    N = n
    return recv(0)
}
