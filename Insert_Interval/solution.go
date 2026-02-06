package main

import "fmt"

func insert(intervals [][]int, newInterval []int) [][]int {
    res := [][]int{}

	// add all intervals that end before the new interval starts (i.e the left side of the new interval)
    i := 0
    for i < len(intervals) && newInterval[0] > intervals[i][1] {
        res = append(res, intervals[i])
        i++
    }

	// if we passed all the intervals, it means that the newInterval is in the end
	if i == len(intervals) {
		res = append(res, newInterval)
		return res
	}

	// update the newInterval[0] to be the minimum of the newInterval[0] and the current interval's start, because they overlap
	if intervals[i][0] < newInterval[0] {
	    newInterval[0] = intervals[i][0]
    }

	// continue the loop to find the end of the newInterval 
    for i < len(intervals) && newInterval[1] >= intervals[i][0] {
	    if intervals[i][1] > newInterval[1] {
		    newInterval[1] = intervals[i][1]
		}
	    i++
    }
	
    res = append(res, newInterval)

	// add all the remaining intervals (i.e the right side of the new interval)
    for i < len(intervals) {
	    res = append(res, intervals[i])
		i++
    }

    return res
}


func main() {
	intervals := [][]int{{4,5},{6,7},{8,10},{14,16}}
	newInterval := []int{12,13}
	fmt.Println(insert(intervals, newInterval))	
}
